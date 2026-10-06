# game_logic.py - calculations and game rules (no Streamlit and no input/print in here)
import copy
from scoring import calculate_score


# ---------- Calculations ----------

def average(records):
    """Average salary. Ignores deleted records and None. Returns a float."""
    total = 0
    count = 0
    for r in records:
        if r["salary"] is not None and not r["deleted"]:
            total = total + r["salary"]
            count = count + 1
    if count == 0:
        return 0.0
    return total / count


def calculate_median(records):
    """Median of usable salaries only (no None, zero, negative or deleted)."""
    salaries = []
    for r in records:
        if r["salary"] is not None and r["salary"] > 0 and not r["deleted"]:
            salaries.append(r["salary"])
    salaries.sort()
    n = len(salaries)
    if n == 0:
        return 0
    if n % 2 == 1:
        return salaries[n // 2]
    return (salaries[n // 2 - 1] + salaries[n // 2]) / 2


# Suspicious does NOT mean incorrect
is_suspicious = lambda record: record["salary"] is None or record["salary"] <= 0 or record["salary"] > 40000


def give_hint(record, median):
    """A clue that never says directly that the record is wrong."""
    salary = record["salary"]
    if salary is None:
        return "This record contains no salary value."
    if salary < 0:
        return "This salary is a negative number."
    if salary == 0:
        return "This salary is zero."
    if median == 0:
        return "There is not enough data to compare this salary."
    ratio = salary / median
    if ratio >= 3:
        return "This salary is " + str(round(ratio, 1)) + " times the company median. Compare it with the job title."
    if ratio <= 0.4:
        return "This salary is " + str(round(median / salary, 1)) + " times lower than the company median. Compare it with the job title."
    return "This salary is close to the company median."


def calculate_accuracy(player_average, correct_average):
    """100 minus the percentage error, kept between 0 and 100."""
    if correct_average == 0:
        return 0
    difference = abs(player_average - correct_average)
    error_percentage = (difference / correct_average) * 100
    accuracy = 100 - error_percentage
    if accuracy < 0:
        accuracy = 0
    if accuracy > 100:
        accuracy = 100
    return accuracy


def calculate_stars(accuracy, mistakes):
    """Stars depend on accuracy AND on the number of mistakes (wrong decisions + missed errors),
    because wrong decisions can cancel each other out in the average."""
    if accuracy >= 95 and mistakes <= 1:
        return 3
    if accuracy >= 85 and mistakes <= 3:
        return 2
    if accuracy >= 70 and mistakes <= 6:
        return 1
    return 0


# ---------- Game engine (used by main.py and app.py) ----------

def new_game(level_name, case_settings):
    """Create a fresh game (a dictionary) for one level."""
    setting = case_settings[level_name]
    records = copy.deepcopy(setting["records"])       # copy, so the original data never changes
    return {
        "level": level_name,
        "records": records,
        "correct": setting["correct"],
        "median": calculate_median(records),          # company median, calculated once
        "original_average": average(records),
        "score": 0,
        "streak": 0,
        "mistakes": 0,
        "right": 0,
        "inspections": setting["inspections"],
        "notes": [],
        "weak": {},
    }


def find_record(game, record_id):
    for r in game["records"]:
        if r["id"] == record_id:
            return r
    return None


def inspect_record(game, record):
    """Use one inspection. Returns the clue, or None if no inspections are left."""
    if game["inspections"] <= 0:
        return None
    game["inspections"] = game["inspections"] - 1
    for other in game["records"]:
        if other["id"] != record["id"] and other["name"] == record["name"] and other["job"] == record["job"]:
            return "This employee appears twice: same name and job as record #" + str(other["id"]) + "."
    return give_hint(record, game["median"])


def explain_fix(record):
    if record["expected_action"] == "delete":
        return "it was a duplicate and should have been deleted."
    return "the salary should be replaced (correct value: " + format(record["correct_salary"], ",") + ")."


def take_action(game, record, action):
    """Apply delete / replace / valid to a record. Returns (points, message)."""
    if record["reviewed"] or record["deleted"]:
        return 0, "This record is already reviewed."

    points, correct = calculate_score(action, record, game["streak"])

    if action == "delete":
        record["deleted"] = True
        message = "Record deleted."
    elif action == "replace":
        record["salary"] = game["median"]
        message = "Salary replaced with the company median."
    else:
        message = "Marked as valid."
    record["reviewed"] = True

    game["score"] = game["score"] + points
    if points > 0:
        game["streak"] = game["streak"] + 1
        game["right"] = game["right"] + 1
    elif not correct:
        game["streak"] = 0
        game["mistakes"] = game["mistakes"] + 1
        if record["is_error"]:
            game["notes"].append(record["name"] + " (" + record["job"] + "): this record was an error, " + explain_fix(record))
            kind = record["error_type"]
        else:
            game["notes"].append(record["name"] + " (" + record["job"] + "): this record was valid. Unusual is not the same as wrong.")
            kind = "valid record changed"
        game["weak"][kind] = game["weak"].get(kind, 0) + 1
    return points, message


def finish_game(game):
    """Penalty for undiscovered errors, then the final report."""
    missed = 0
    for r in game["records"]:
        if r["is_error"] and not r["reviewed"]:
            missed = missed + 1
            game["score"] = game["score"] - 50
            game["notes"].append(r["name"] + " (" + r["job"] + "): you missed this error, " + explain_fix(r))
            game["weak"][r["error_type"]] = game["weak"].get(r["error_type"], 0) + 1

    final_average = average(game["records"])
    correct_average = average(game["correct"])
    accuracy = calculate_accuracy(final_average, correct_average)
    stars = calculate_stars(accuracy, game["mistakes"] + missed)

    return {
        "level": game["level"],
        "original_average": game["original_average"],
        "final_average": final_average,
        "correct_average": correct_average,
        "accuracy": accuracy,
        "score": game["score"],
        "mistakes": game["mistakes"],
        "missed": missed,
        "right": game["right"],
        "stars": stars,
        "notes": game["notes"],
        "weak": game["weak"],
    }
