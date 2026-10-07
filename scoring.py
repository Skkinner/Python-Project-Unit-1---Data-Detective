# scoring.py - points for one player action
# How Scoring work (general idea): every employee record has a hidden key called "expected_action". It stores the decision a perfect detective would make:
#       "valid"   -> keep the record as it is
#       "replace" -> the salary is an error, replace it with the company median
#       "delete"  -> the record is a duplicate, remove it
#   The player's action is simply compared with that expected action:
#       same action  -> the player is correct (earns points)
#       other action -> the player is wrong (loses points)
#   This file only DECIDES THE POINTS.

# A valid record that looks unusual (very high or very low salary)
# Examples: the CEO (45,000) or an intern (3,000). They look suspicious but are correct, so keeping them is rewarded and deleting/replacing them is punished.
is_valid_trap = lambda record: (not record["is_error"]) and (record["salary"] > 40000 or record["salary"] < 4000)


# Streak is how many correct decisions has the player got In A ROW 
def streak_multiplier(streak): 
    """1 correct -> x1, 2 -> x2, 3 -> x3, 4 or more -> x4."""
    return min(streak + 1, 4) # min() stops the multiplier from growing past 4.


def calculate_score(action, record, streak):
    """Return (points, correct) for one action.

    action: "inspect", "delete", "replace", "valid" or "submit"
    streak: how many correct decisions in a row the player already has
    """
    if action == "inspect" or action == "submit": # Since inspecting and submitting are not decisions about a record, they never earn or lose points.
        return 0, True # True means "this is not a mistake either".

    # The streak bonus is worked out once and used by the rewards below.
    multiplier = streak_multiplier(streak)

    # CASE 1: the player chose the expected action, so the decision is correct.
    if action == record["expected_action"]:
        if record["is_error"]: # Fixing a real error the right way is the main reward: 100 points x multiplier.
            return 100 * multiplier, True # fixed an error the right way
        # Keeping a valid but unusual record (the "trap") earns 60 points x multiplier.
        if is_valid_trap(record):
            return 60 * multiplier, True # kept a valid but unusual record
        return 0, True # a normal record, nothing happens

    # CASE 2: the player chose a different action, so the decision is wrong. The penalty depends on what the record really was.
    # Deleting or replacing a valid record damages good data, which is the worst mistake.
    if not record["is_error"]:
        return -150, False # changed a valid record
    # The record was a real error but the action was wrong (marked valid, or deleted when it should have been replaced, or the other way round): smaller penalty.
    return -80, False # wrong action on an error
