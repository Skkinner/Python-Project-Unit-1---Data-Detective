# game_logic.py consists of calculations and game rules (no Streamlit and no input/print in here)
# This files has the calculations: average, median, hint, accuracy and stars. These are small
# functions that take data in and give a result back, so they are easy to test.
# Every employee is a dictionary with these keys: id, name, job, salary, correct_salary, is_error, error_type,
# expected_action ("valid", "replace" or "delete"), reviewed, deleted "salary" is what the player sees (it may be wrong), "correct_salary" is the true
# value that stays hidden, "reviewed" locks a record after a decision, and "deleted" hides a record from every calculation.
import copy
from scoring import calculate_score


# ---------- Calculations ----------

def average(records):
    """Average salary. Ignores deleted records and None. Returns a float."""
    # "total" adds up the salaries, "count" counts how many salaries were added.
    total = 0
    count = 0
    # Check every employee. A missing salary (None) or a deleted record is skipped so it can't change the average.
    for r in records:
        if r["salary"] is not None and not r["deleted"]:
            total = total + r["salary"]
            count = count + 1
    if count == 0: # If every salary was skipped there is nothing to divide by, so we return 0.0 instead of crashing with a division by zero.
        return 0.0
    return total / count


def calculate_median(records):
    """Median of usable salaries only (no None, zero, negative or deleted)."""
    # The median is the middle value of the sorted salaries. Unlike the average, it's not pulled away by one huge or tiny number
    # which makes it a safe replacement value for a broken salary.
    salaries = [] # Step 1: collect only usable salaries. Zero and negative values are excluded.
    for r in records:
        if r["salary"] is not None and r["salary"] > 0 and not r["deleted"]:
            salaries.append(r["salary"])
    # Step 2: sort from smallest to largest.
    salaries.sort()
    n = len(salaries)
    if n == 0: # No usable salaries at all: return 0 instead of crashing.
        return 0
    if n % 2 == 1: # Odd number of salaries: the median is the single middle one. (n//2 is the middle position, since positions start at 0.)
        return salaries[n // 2]
    return (salaries[n // 2 - 1] + salaries[n // 2]) / 2 # Even number of salaries: there are two middle ones, so take their average.


# Suspicious does NOT mean incorrect
# This lambda is a tiny one-line function. It says whether a record deserves a closer look: the salary is missing, zero or negative, or very high.
is_suspicious = lambda record: record["salary"] is None or record["salary"] <= 0 or record["salary"] > 40000


def give_hint(record, median):
    """A clue that never says directly that the record is wrong."""
    # The hints are checked from the most obvious problem to the least obvious one, and the first one that matches is returned.
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
    # Accuracy shows how close the player's cleaned average is to the true average.
    if correct_average == 0:
        return 0
    # Step 1: how far away is the player's average? abs() removes the minus sign, so being too high or too low counts the same.
    difference = abs(player_average - correct_average)
    # Step 2: turn that distance into a percentage of the correct average.
    error_percentage = (difference / correct_average) * 100
    # Step 3: accuracy is what is left after removing the error. 0% error = 100% accuracy.
    accuracy = 100 - error_percentage
    if accuracy < 0: # Keep the result between 0 and 100. A very bad average can give a negative number, and 100 is the highest possible.
        accuracy = 0
    if accuracy > 100:
        accuracy = 100
    return accuracy


def calculate_stars(accuracy, mistakes):
    """Stars depend on accuracy AND on the number of mistakes (wrong decisions + missed errors),
    because wrong decisions can cancel each other out in the average."""
    # Both conditions must be true for a star level. 
    if accuracy >= 95 and mistakes <= 1:
        return 3 # 3 stars: very accurate (95%+) with at most 1 mistake.
    if accuracy >= 85 and mistakes <= 3:
        return 2 # 2 stars: good accuracy (85%+) with at most 3 mistakes.
    if accuracy >= 70 and mistakes <= 6:
        return 1 # 1 star: acceptable accuracy (70%+) with at most 6 mistakes.
    return 0 # anything worse than that ... 0 stars


# ---------- Game engine (used by main.py and app.py) ----------

def new_game(level_name, case_settings):
    """Create a fresh game (a dictionary) for one level."""
    # All the information about one round is stored in a single dictionary. The player's decisions change this dictionary, never the original data.
    setting = case_settings[level_name]
    # deepcopy() makes a separate copy of the records. Without it, deleting or replacing a salary would change the original data.
    # and a restart would start with the old changes still there.
    records = copy.deepcopy(setting["records"])       
    return {
        "level": level_name, # Which level is being played.
        "records": records, # Editable records
        "correct": setting["correct"], # The correct dataset, used at the end to work out the true average.
        "median": calculate_median(records), # company median, calculated once, every "replace" later uses this same value, so the result does not change while the player is playing.
        "original_average": average(records), # The average before any cleaning
        # Counters that start from zero.
        "score": 0,
        "streak": 0,
        "mistakes": 0,
        "right": 0,
        "inspections": setting["inspections"], # How many inspections this level allows.
        "notes": [], # Feedback sentences for the final report.
        "weak": {}, # weak spots the player could improve
    }


def find_record(game, record_id): # Search the list for the employee with this id. Return None if there is no match
    for r in game["records"]:
        if r["id"] == record_id:
            return r
    return None


def inspect_record(game, record):
    """Use one inspection. Returns the clue, or None if no inspections are left."""
    if game["inspections"] <= 0:
        return None
    game["inspections"] = game["inspections"] - 1 # Using an inspection costs one point
    # First look for a duplicate, if found, that clue is more useful than a salary comparison.
    for other in game["records"]:
        if other["id"] != record["id"] and other["name"] == record["name"] and other["job"] == record["job"]:
            return "This employee appears twice: same name and job as record #" + str(other["id"]) + "."
    # Otherwise give the salary-based hint.
    return give_hint(record, game["median"])

# Builds the "what should have been done" sentence for the final report, using the expected action stored in the record.
def explain_fix(record):
    if record["expected_action"] == "delete":
        return "it was a duplicate and should have been deleted."
    return "the salary should be replaced (correct value: " + format(record["correct_salary"], ",") + ")."


def take_action(game, record, action):
    """Apply delete / replace / valid to a record. Returns (points, message)."""
    # Decisions are final. A record that was already reviewed or deleted cannot be changed again, so nothing happens and no points are given.
    if record["reviewed"] or record["deleted"]:
        return 0, "This record is already reviewed."

    # Asks scoring.py for the points BEFORE changing the record, because the score depends on the record as the player first saw it.
    # "correct" says if the decision was right (True) or wrong (False).
    points, correct = calculate_score(action, record, game["streak"])

    if action == "delete": # Deleted records are only hidden (flag), so they are ignored by average() and median.
        record["deleted"] = True
        message = "Record deleted."
    elif action == "replace": # Replace the bad salary with the company median calculated at the start.
        record["salary"] = game["median"]
        message = "Salary replaced with the company median."
    else:
        message = "Marked as valid." # Salary stays exactly as it is.
    record["reviewed"] = True # Lock the record so the player cannot decide on it again.

    game["score"] = game["score"] + points # Add the points (may be negative) to the total score.
    # Positive points mean: correct decision that earned a reward, the streak grows and "right decisions" counter goes up.
    if points > 0:
        game["streak"] = game["streak"] + 1
        game["right"] = game["right"] + 1
    # A wrong decision: break the streak and count a mistake.
    elif not correct:
        game["streak"] = 0
        game["mistakes"] = game["mistakes"] + 1
        if record["is_error"]:
            game["notes"].append(record["name"] + " (" + record["job"] + "): this record was an error, " + explain_fix(record))
            kind = record["error_type"] # Saves feedback sentence for the final report. "kind" names the type of mistake so the report show the player's weak areas.
        else:
            game["notes"].append(record["name"] + " (" + record["job"] + "): this record was valid. Unusual is not the same as wrong.")
            kind = "valid record changed"
        game["weak"][kind] = game["weak"].get(kind, 0) + 1
    return points, message


def finish_game(game):
    """Penalty for undiscovered errors, then the final report."""
    # Runs when the player submits (or when time runs out).
    # Step 1: find the real errors the player never reviewed. Each one costs 50 points, and it also gets a feedback note and a weak-area count.
    missed = 0
    for r in game["records"]:
        if r["is_error"] and not r["reviewed"]:
            missed = missed + 1
            game["score"] = game["score"] - 50
            game["notes"].append(r["name"] + " (" + r["job"] + "): you missed this error, " + explain_fix(r))
            game["weak"][r["error_type"]] = game["weak"].get(r["error_type"], 0) + 1

    # Step 2: compare the player's cleaned average with the true average of the correct dataset, and turn that into an accuracy percentage.
    final_average = average(game["records"])
    correct_average = average(game["correct"])
    accuracy = calculate_accuracy(final_average, correct_average)
    # Step 3: stars. Missed errors count as mistakes too, together with wrong decisions.
    stars = calculate_stars(accuracy, game["mistakes"] + missed)

    # Step 4: return everything the results screen needs in one dictionary.
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
