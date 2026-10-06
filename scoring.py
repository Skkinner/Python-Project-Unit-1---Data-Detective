# phase 3: Raghad
"""
scoring.py  --  Data Detective: scoring rules (Raghad)

The score judges the ACTION the player chose, using the record's
expected_action (valid / replace / delete) that Norah added to the data.
"""

# Points (change the numbers here, not inside the functions)
POINTS_ERROR_FIXED = 100         # right action on an error (x streak)
POINTS_VALID_TRAP_KEPT = 60      # kept a valid record that only LOOKS wrong
PENALTY_VALID_CHANGED = -150     # deleted/replaced a valid record
PENALTY_WRONG_ACTION = -80       # wrong action on an error (for example "valid")
PENALTY_UNRESOLVED_ERROR = -50   # error never reviewed before submitting
MAX_MULTIPLIER = 4

# A valid record with a salary outside this range is a "valid trap"
# (for example the CEO or an intern). Same rule Norah uses in her table.
TRAP_LOW_SALARY = 4000
TRAP_HIGH_SALARY = 40000


def is_valid_trap(record):
    """True for a correct record whose salary only looks unusual."""
    if record["is_error"]:
        return False
    salary = record["salary"]
    return salary > TRAP_HIGH_SALARY or salary < TRAP_LOW_SALARY


def calculate_score(action, record, streak):
    """
    Returns (points, correct).
    correct is True / False for delete, replace and valid.
    "inspect" is not a final decision, so it returns (0, None).
    """
    if action not in ("delete", "replace", "valid"):
        return 0, None

    if action == record["expected_action"]:
        if record["is_error"]:
            multiplier = min(streak + 1, MAX_MULTIPLIER)
            return POINTS_ERROR_FIXED * multiplier, True
        if is_valid_trap(record):
            return POINTS_VALID_TRAP_KEPT, True
        return 0, True              # normal valid record: nothing happens

    if not record["is_error"]:
        return PENALTY_VALID_CHANGED, False
    return PENALTY_WRONG_ACTION, False


def update_streak(streak, correct, record):
    """
    Streak = correct error fixes in a row (as in the game sample).
    A mistake resets it. Keeping a valid record does not change it.
    """
    if correct is None:
        return streak
    if not correct:
        return 0
    if record["is_error"]:
        return streak + 1
    return streak


def unresolved_penalty(records):
    """-50 for every error the player never reviewed (use when submitting)."""
    count = 0
    for record in records:
        if record["is_error"] and not record.get("reviewed", False):
            count += 1
    return count * PENALTY_UNRESOLVED_ERROR