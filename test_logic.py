# Previous phases test: Raghad
"""
test_logic.py  --  Phase 5 edge-case tests for game_logic.py and scoring.py (Raghad)

Run: python test_logic.py
In Colab, paste this as a cell AFTER the data, game_logic and scoring cells
(the names already exist there, so the imports below are skipped).
"""
import copy

try:
    from data import case_settings
    from game_logic import (average, calculate_median, give_hint,
                            calculate_accuracy, calculate_stars, is_suspicious)
    from scoring import (calculate_score, update_streak, unresolved_penalty,
                         is_valid_trap)
except ImportError:
    pass  # Colab: everything is already defined in earlier cells


def play_case(level, choose_action, stop_after=None):
    """Play a whole case the way main.py / app.py will, and return the results."""
    setting = case_settings[level]
    records = copy.deepcopy(setting["records"])      # never touch the original data
    original_average = average(records)
    score, streak, best_streak, mistakes = 0, 0, 0, 0

    for number, record in enumerate(records):
        if stop_after is not None and number >= stop_after:
            break                                    # submit early
        action = choose_action(record)
        median = calculate_median(records)
        points, correct = calculate_score(action, record, streak)

        if action == "replace":
            record["salary"] = median
        elif action == "delete":
            record["deleted"] = True
        record["reviewed"] = True

        score += points
        if correct is False:
            mistakes += 1
        streak = update_streak(streak, correct, record)
        best_streak = max(best_streak, streak)

    score += unresolved_penalty(records)
    final_average = average(records)
    correct_average = average(setting["correct"])
    accuracy = calculate_accuracy(final_average, correct_average)
    return {"score": score, "mistakes": mistakes, "best_streak": best_streak,
            "original": original_average, "final": final_average,
            "correct": correct_average, "accuracy": accuracy,
            "stars": calculate_stars(accuracy, mistakes)}


def right_action(record):
    return record["expected_action"]


def wrong_action(record):
    # always pick an action that is NOT the expected one
    return "replace" if record["expected_action"] == "valid" else "valid"


def find(level, name):
    for record in case_settings[level]["records"]:
        if record["name"] == name:
            return record


passed = 0
def check(description, condition):
    global passed
    assert condition, "FAILED: " + description
    passed += 1
    print("PASS:", description)


# ---------- Bad values in the basic functions ----------
print("--- Bad values ---")
none_row = {"id": 1, "name": "A", "job": "J", "salary": None, "deleted": False}
zero_row = dict(none_row, salary=0)
neg_row = dict(none_row, salary=-500)
check("None salary: hint works", "No salary value" in give_hint(none_row, 9000))
check("Zero salary: hint works", "0 SAR" in give_hint(zero_row, 9000))
check("Negative salary: hint works", "below zero" in give_hint(neg_row, 9000))
check("Hints never say 'wrong' or 'error'",
      all(word not in give_hint(r, 9000).lower()
          for r in (none_row, zero_row, neg_row) for word in ("wrong", "error", "incorrect")))
check("Median 0 does not crash the hint", "not enough data" in give_hint(dict(none_row, salary=100), 0))
check("is_suspicious: None, zero, negative, very high",
      is_suspicious(none_row) and is_suspicious(zero_row) and is_suspicious(neg_row)
      and is_suspicious(dict(none_row, salary=45000)))
check("is_suspicious: normal salary is not suspicious", not is_suspicious(dict(none_row, salary=9000)))

check("average of an empty list is 0.0", average([]) == 0.0)
check("median of an empty list is 0.0", calculate_median([]) == 0.0)
check("average ignores None and deleted",
      average([dict(none_row, salary=100), none_row, dict(none_row, salary=900, deleted=True)]) == 100)
check("median ignores None, zero, negative",
      calculate_median([none_row, zero_row, neg_row, dict(none_row, salary=10), dict(none_row, salary=20)]) == 15)

# ---------- Accuracy and stars ----------
print("--- Accuracy and stars ---")
check("accuracy never above 100", calculate_accuracy(12000, 12000) == 100 and calculate_accuracy(5, 5) <= 100)
check("accuracy never below 0", calculate_accuracy(1000000, 12000) == 0)
check("correct average of 0 does not divide by zero", calculate_accuracy(500, 0) == 0.0)
check("stars thresholds",
      [calculate_stars(a, 0) for a in (96, 90, 75, 50)] == [3, 2, 1, 0])
check("many mistakes lower the stars",
      calculate_stars(99, 2) == 2 and calculate_stars(99, 4) == 1 and calculate_stars(99, 6) == 0)

# ---------- Scoring rules ----------
print("--- Scoring ---")
ali = find("Beginner", "Ali")       # valid trap (CEO)
fahad = find("Beginner", "Fahad")   # x10 error
ahmed = find("Beginner", "Ahmed")   # normal valid record
check("Valid trap kept: +60", calculate_score("valid", ali, 0) == (60, True))
check("Normal valid kept: 0 points, still correct", calculate_score("valid", ahmed, 0) == (0, True))
check("Delete the CEO: -150", calculate_score("delete", ali, 0) == (-150, False))
check("x10 marked valid: -80", calculate_score("valid", fahad, 0) == (-80, False))
check("x10 deleted (should be replaced): -80", calculate_score("delete", fahad, 0) == (-80, False))
check("Inspect gives no points", calculate_score("inspect", fahad, 0) == (0, None))
check("Streak multiplier x1 x2 x3 x4 then stays x4",
      [calculate_score("replace", fahad, s)[0] for s in (0, 1, 2, 3, 4, 9)] == [100, 200, 300, 400, 400, 400])
check("Streak counts only error fixes",
      update_streak(2, True, fahad) == 3 and update_streak(2, True, ahmed) == 2)
check("Streak resets after a mistake", update_streak(3, False, fahad) == 0)
check("Inspect does not change the streak", update_streak(3, None, fahad) == 3)
check("Valid-trap rule matches Norah's table (2 traps in Beginner)",
      sum(is_valid_trap(r) for r in case_settings["Beginner"]["records"]) == 2)

# ---------- Full games on every level ----------
for level in case_settings:
    print("---", level, "---")
    perfect = play_case(level, right_action)
    check(level + " perfect run: 3 stars, 0 mistakes",
          perfect["stars"] == 3 and perfect["mistakes"] == 0)
    check(level + " perfect run: accuracy between 95 and 100", 95 <= perfect["accuracy"] <= 100)
    check(level + " perfect run reaches the x4 streak or has fewer than 4 errors",
          perfect["best_streak"] >= 4 or sum(r["is_error"] for r in case_settings[level]["records"]) < 4)

    bad = play_case(level, wrong_action)
    check(level + " all wrong: 0 stars, negative score, every record a mistake",
          bad["stars"] == 0 and bad["score"] < 0
          and bad["mistakes"] == len(case_settings[level]["records"]))

    everything_deleted = play_case(level, lambda r: "delete")
    check(level + " all records deleted: no crash, accuracy 0",
          everything_deleted["final"] == 0 and everything_deleted["accuracy"] == 0)

    nothing = play_case(level, right_action, stop_after=0)
    errors = sum(r["is_error"] for r in case_settings[level]["records"])
    check(level + " submit at once: -50 for each of the " + str(errors) + " errors",
          nothing["score"] == -50 * errors)

    early = play_case(level, right_action, stop_after=len(case_settings[level]["records"]) // 2)
    check(level + " submit early: no crash, penalty only for unreviewed errors",
          early["score"] > nothing["score"] and 0 <= early["accuracy"] <= 100)

    check(level + " original data is never changed by a game",
          all(r["reviewed"] is False and r["deleted"] is False for r in case_settings[level]["records"]))

# ---------- Specific story tests from the team plan ----------
print("--- Team plan tests (Beginner) ---")
delete_ceo = play_case("Beginner", lambda r: "delete" if r["name"] == "Ali" else r["expected_action"])
check("Test B: deleting the CEO costs a mistake and lowers the accuracy",
      delete_ceo["mistakes"] == 1 and delete_ceo["accuracy"] < play_case("Beginner", right_action)["accuracy"])
keep_x10 = play_case("Beginner", lambda r: "valid" if r["name"] == "Fahad" else r["expected_action"])
check("Test C: keeping the x10 salary gives a mistake and a worse average",
      keep_x10["mistakes"] == 1 and keep_x10["accuracy"] < play_case("Beginner", right_action)["accuracy"])

# ---------- Duplicate hints (Medium) ----------
print("--- Duplicate hints ---")
medium = case_settings["Medium"]["records"]
first_layla, repeat_layla = medium[0], medium[8]
check("Duplicate hint on the first copy", "later" in give_hint(first_layla, 9000, medium))
check("Duplicate hint on the repeat", "earlier" in give_hint(repeat_layla, 9000, medium))
check("Medium duplicate: deleting the repeat is correct",
      calculate_score("delete", repeat_layla, 0) == (100, True))
check("Medium duplicate: replacing the repeat is wrong",
      calculate_score("replace", repeat_layla, 0) == (-80, False))

print()
print("ALL", passed, "CHECKS PASSED")