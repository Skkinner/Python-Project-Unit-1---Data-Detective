# phase 1 & 2: Raghad
"""
game_logic.py  --  Data Detective: calculation functions

Every record follows the team's coding contract:
id, name, job, salary, correct_salary, is_error, error_type,
expected_action, reviewed, deleted
"""

# Lambda: marks a record that DESERVES investigation.
# Suspicious does not mean incorrect (a real CEO salary is suspicious too).
is_suspicious = lambda record: (
    record["salary"] is None
    or record["salary"] <= 0
    or record["salary"] > 40000
)

# Accuracy needed for each star (from the team plan) and the most
# mistakes allowed for it. Without the mistake limits, a player who
# gets everything wrong could still earn 2 stars on Medium and Advanced.
STARS_3_ACCURACY = 95
STARS_2_ACCURACY = 85
STARS_1_ACCURACY = 70
STARS_3_MAX_MISTAKES = 1   # "very few mistakes"
STARS_2_MAX_MISTAKES = 3
STARS_1_MAX_MISTAKES = 5


def _usable_salaries(records, positive_only=False):
    """Salaries of records that are not deleted and have a value."""
    salaries = []
    for record in records:
        salary = record["salary"]
        if salary is None or record.get("deleted", False):
            continue
        if positive_only and salary <= 0:
            continue
        salaries.append(salary)
    return salaries


def average(records):
    """Mean salary. Ignores deleted records and None. Returns a float."""
    salaries = _usable_salaries(records)
    if len(salaries) == 0:
        return 0.0
    return sum(salaries) / len(salaries)


def calculate_median(records):
    """Median of the usable salaries (no None, zero, negative or deleted)."""
    salaries = sorted(_usable_salaries(records, positive_only=True))
    n = len(salaries)
    if n == 0:
        return 0.0
    if n % 2 == 1:
        return float(salaries[n // 2])
    return (salaries[n // 2 - 1] + salaries[n // 2]) / 2


def _duplicate_hint(record, records):
    """Clue for repeated rows. Rule: keep the first copy, the later one is the repeat."""
    same = (record["name"], record["job"], record["salary"])
    found_itself = False
    seen_before = False
    seen_after = False

    for other in records:
        if other["id"] == record["id"]:
            found_itself = True
            continue
        if other.get("deleted", False):
            continue
        if (other["name"], other["job"], other["salary"]) == same:
            if found_itself:
                seen_after = True
            else:
                seen_before = True

    if seen_before:
        return "The same name, job, and salary already appear earlier in the list."
    if seen_after:
        return "The same name, job, and salary appear again later in the list."
    return None


def give_hint(record, median, records=None):
    """
    Return a clue about the salary. It never says 'this is wrong'.
    Pass records too (optional) so duplicate rows can be noticed.
    """
    salary = record["salary"]

    if salary is None:
        return ("No salary value is recorded for this employee. "
                "Consider how missing data should be handled.")

    if records is not None:
        duplicate_clue = _duplicate_hint(record, records)
        if duplicate_clue is not None:
            return duplicate_clue

    if salary < 0:
        return "This salary is below zero. Consider whether this is a valid salary value."
    if salary == 0:
        return ("This employee has a salary of 0 SAR. "
                "Consider whether this is reasonable for an active employee.")
    if median <= 0:
        return "There is not enough data to compare this salary."

    ratio = salary / median
    if ratio >= 2:
        return (f"This salary is {ratio:.1f} times the company median. "
                "Consider whether the employee's job role could explain the difference.")
    if ratio <= 0.5:
        return (f"This salary is only {ratio:.2f} times the company median. "
                "Consider whether the employee's job role could explain the difference.")
    return "This salary is close to the company median."


def calculate_accuracy(player_average, correct_average):
    """Accuracy % = 100 - error %. Always between 0 and 100."""
    if correct_average == 0:
        return 0.0
    difference = abs(player_average - correct_average)
    error_percentage = difference / correct_average * 100
    accuracy = 100 - error_percentage
    return round(max(0.0, min(100.0, accuracy)), 2)


def calculate_stars(accuracy, mistakes):
    """0 to 3 stars from the accuracy and the number of mistakes."""
    if accuracy >= STARS_3_ACCURACY and mistakes <= STARS_3_MAX_MISTAKES:
        return 3
    if accuracy >= STARS_2_ACCURACY and mistakes <= STARS_2_MAX_MISTAKES:
        return 2
    if accuracy >= STARS_1_ACCURACY and mistakes <= STARS_1_MAX_MISTAKES:
        return 1
    return 0