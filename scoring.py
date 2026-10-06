# scoring.py - points for one player action

# A valid record that looks unusual (very high or very low salary)
is_valid_trap = lambda record: (not record["is_error"]) and (record["salary"] > 40000 or record["salary"] < 4000)


def streak_multiplier(streak):
    """1 correct -> x1, 2 -> x2, 3 -> x3, 4 or more -> x4."""
    return min(streak + 1, 4)


def calculate_score(action, record, streak):
    """Return (points, correct) for one action.

    action: "inspect", "delete", "replace", "valid" or "submit"
    streak: how many correct decisions in a row the player already has
    """
    if action == "inspect" or action == "submit":
        return 0, True

    multiplier = streak_multiplier(streak)

    if action == record["expected_action"]:
        if record["is_error"]:
            return 100 * multiplier, True      # fixed an error the right way
        if is_valid_trap(record):
            return 60 * multiplier, True       # kept a valid but unusual record
        return 0, True                         # a normal record, nothing happens

    if not record["is_error"]:
        return -150, False                     # changed a valid record
    return -80, False                          # wrong action on an error
