# ---------- Datasets for all 3 levels (Norah) ----------
# Same keys everywhere. expected_action is the best action: valid / replace / delete

beginner_case = [
    {"id": 1, "name": "Ahmed", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 2, "name": "Sara", "job": "Designer", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 3, "name": "Khalid", "job": "Manager", "salary": 15000, "correct_salary": 15000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 4, "name": "Nora", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 5, "name": "Fahad", "job": "Engineer", "salary": 95000, "correct_salary": 9500, "is_error": True, "error_type": 'x10', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 6, "name": "Maha", "job": "Analyst", "salary": None, "correct_salary": 8000, "is_error": True, "error_type": 'missing', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 7, "name": "Omar", "job": "Assistant", "salary": -7000, "correct_salary": 7000, "is_error": True, "error_type": 'negative', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 8, "name": "Ali", "job": "CEO", "salary": 45000, "correct_salary": 45000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 9, "name": "Reem", "job": "HR Specialist", "salary": 0, "correct_salary": 7000, "is_error": True, "error_type": 'zero', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 10, "name": "Turki", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
]

correct_beginner_case = [
    {"id": 1, "name": "Ahmed", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 2, "name": "Sara", "job": "Designer", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 3, "name": "Khalid", "job": "Manager", "salary": 15000, "correct_salary": 15000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 4, "name": "Nora", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 5, "name": "Fahad", "job": "Engineer", "salary": 9500, "correct_salary": 9500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 6, "name": "Maha", "job": "Analyst", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 7, "name": "Omar", "job": "Assistant", "salary": 7000, "correct_salary": 7000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 8, "name": "Ali", "job": "CEO", "salary": 45000, "correct_salary": 45000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 9, "name": "Reem", "job": "HR Specialist", "salary": 7000, "correct_salary": 7000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 10, "name": "Turki", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
]

medium_case = [
    {"id": 1, "name": "Layla", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 2, "name": "Yousef", "job": "Designer", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 3, "name": "Abeer", "job": "Engineer", "salary": 95000, "correct_salary": 9500, "is_error": True, "error_type": 'x10', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 4, "name": "Hessa", "job": "Data Analyst", "salary": 10500, "correct_salary": 10500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 5, "name": "Salma", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 6, "name": "Majed", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 7, "name": "Waleed", "job": "Analyst", "salary": None, "correct_salary": 9000, "is_error": True, "error_type": 'missing', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 8, "name": "Hamad", "job": "Director", "salary": 30000, "correct_salary": 30000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 9, "name": "Layla", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": True, "error_type": 'duplicate', "expected_action": "delete", "reviewed": False, "deleted": False},
    {"id": 10, "name": "Dalal", "job": "Project Manager", "salary": 12000, "correct_salary": 12000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 11, "name": "Joud", "job": "Assistant", "salary": -8000, "correct_salary": 8000, "is_error": True, "error_type": 'negative', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 12, "name": "Bandar", "job": "CEO", "salary": 45000, "correct_salary": 45000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 13, "name": "Hessa", "job": "Data Analyst", "salary": 10500, "correct_salary": 10500, "is_error": True, "error_type": 'duplicate', "expected_action": "delete", "reviewed": False, "deleted": False},
    {"id": 14, "name": "Rakan", "job": "Receptionist", "salary": 5000, "correct_salary": 5000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 15, "name": "Mishari", "job": "HR Specialist", "salary": 0, "correct_salary": 8000, "is_error": True, "error_type": 'zero', "expected_action": "replace", "reviewed": False, "deleted": False},
]

correct_medium_case = [
    {"id": 1, "name": "Layla", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 2, "name": "Yousef", "job": "Designer", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 3, "name": "Abeer", "job": "Engineer", "salary": 9500, "correct_salary": 9500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 4, "name": "Hessa", "job": "Data Analyst", "salary": 10500, "correct_salary": 10500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 5, "name": "Salma", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 6, "name": "Majed", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 7, "name": "Waleed", "job": "Analyst", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 8, "name": "Hamad", "job": "Director", "salary": 30000, "correct_salary": 30000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 10, "name": "Dalal", "job": "Project Manager", "salary": 12000, "correct_salary": 12000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 11, "name": "Joud", "job": "Assistant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 12, "name": "Bandar", "job": "CEO", "salary": 45000, "correct_salary": 45000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 14, "name": "Rakan", "job": "Receptionist", "salary": 5000, "correct_salary": 5000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 15, "name": "Mishari", "job": "HR Specialist", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
]

advanced_case = [
    {"id": 1, "name": "Noura", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 2, "name": "Yazeed", "job": "Intern", "salary": 30000, "correct_salary": 3000, "is_error": True, "error_type": 'x10', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 3, "name": "Faisal", "job": "Senior Developer", "salary": 12000, "correct_salary": 12000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 4, "name": "Sultan", "job": "CEO", "salary": 45000, "correct_salary": 45000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 5, "name": "Lina", "job": "Designer", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 6, "name": "Basma", "job": "Engineer", "salary": 950, "correct_salary": 9500, "is_error": True, "error_type": 'div10', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 7, "name": "Jawaher", "job": "Analyst", "salary": 105000, "correct_salary": 10500, "is_error": True, "error_type": 'x10', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 8, "name": "Saud", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 9, "name": "Rahaf", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 10, "name": "Rahaf", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": True, "error_type": 'duplicate', "expected_action": "delete", "reviewed": False, "deleted": False},
    {"id": 11, "name": "Hanan", "job": "Marketing Specialist", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 12, "name": "Osama", "job": "Engineer", "salary": None, "correct_salary": 8000, "is_error": True, "error_type": 'missing', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 13, "name": "Maram", "job": "Part-time Assistant", "salary": 2500, "correct_salary": 2500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 14, "name": "Talal", "job": "Data Analyst", "salary": 10500, "correct_salary": 10500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 15, "name": "Reema", "job": "Team Lead", "salary": -12000, "correct_salary": 12000, "is_error": True, "error_type": 'negative', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 16, "name": "Hanan", "job": "Marketing Specialist", "salary": 8500, "correct_salary": 8500, "is_error": True, "error_type": 'duplicate', "expected_action": "delete", "reviewed": False, "deleted": False},
    {"id": 17, "name": "Ghada", "job": "HR Specialist", "salary": 7000, "correct_salary": 7000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 18, "name": "Nasser", "job": "Director", "salary": 30000, "correct_salary": 30000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 19, "name": "Badr", "job": "Accountant", "salary": 0, "correct_salary": 8000, "is_error": True, "error_type": 'zero', "expected_action": "replace", "reviewed": False, "deleted": False},
    {"id": 20, "name": "Ziyad", "job": "Coordinator", "salary": 7500, "correct_salary": 7500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
]

correct_advanced_case = [
    {"id": 1, "name": "Noura", "job": "Developer", "salary": 9000, "correct_salary": 9000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 2, "name": "Yazeed", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 3, "name": "Faisal", "job": "Senior Developer", "salary": 12000, "correct_salary": 12000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 4, "name": "Sultan", "job": "CEO", "salary": 45000, "correct_salary": 45000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 5, "name": "Lina", "job": "Designer", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 6, "name": "Basma", "job": "Engineer", "salary": 9500, "correct_salary": 9500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 7, "name": "Jawaher", "job": "Analyst", "salary": 10500, "correct_salary": 10500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 8, "name": "Saud", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 9, "name": "Rahaf", "job": "Intern", "salary": 3000, "correct_salary": 3000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 11, "name": "Hanan", "job": "Marketing Specialist", "salary": 8500, "correct_salary": 8500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 12, "name": "Osama", "job": "Engineer", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 13, "name": "Maram", "job": "Part-time Assistant", "salary": 2500, "correct_salary": 2500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 14, "name": "Talal", "job": "Data Analyst", "salary": 10500, "correct_salary": 10500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 15, "name": "Reema", "job": "Team Lead", "salary": 12000, "correct_salary": 12000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 17, "name": "Ghada", "job": "HR Specialist", "salary": 7000, "correct_salary": 7000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 18, "name": "Nasser", "job": "Director", "salary": 30000, "correct_salary": 30000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 19, "name": "Badr", "job": "Accountant", "salary": 8000, "correct_salary": 8000, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
    {"id": 20, "name": "Ziyad", "job": "Coordinator", "salary": 7500, "correct_salary": 7500, "is_error": False, "error_type": None, "expected_action": "valid", "reviewed": False, "deleted": False},
]

# ---------- Settings for each difficulty ----------
case_settings = {
    "Beginner": {"inspections": 3, "time_limit": 180, "records": beginner_case, "correct": correct_beginner_case},
    "Medium":   {"inspections": 3, "time_limit": 150, "records": medium_case,   "correct": correct_medium_case},
    "Advanced": {"inspections": 3, "time_limit": 120, "records": advanced_case, "correct": correct_advanced_case},
}

# ---------- Validation for every level ----------
for level, setting in case_settings.items():
    records = setting["records"]
    correct = setting["correct"]
    print("=====", level, "=====")

    ids = [r["id"] for r in records]
    print("Records:", len(records), "| IDs unique:", len(ids) == len(set(ids)))

    all_have_action = True
    for r in records:
        if r["expected_action"] not in ["valid", "replace", "delete"]:
            all_have_action = False
    print("Every record has expected_action:", all_have_action)

    # errors must have an expected action that fixes them, valid records must be "valid"
    rules_ok = True
    for r in records:
        if r["is_error"] and r["expected_action"] == "valid":
            rules_ok = False
        if not r["is_error"] and r["expected_action"] != "valid":
            rules_ok = False
        if r["error_type"] == "duplicate" and r["expected_action"] != "delete":
            rules_ok = False
        if r["error_type"] not in [None, "duplicate"] and r["expected_action"] != "replace":
            rules_ok = False
    print("Expected actions match the errors:", rules_ok)

    # no accidental errors: salary differs from correct_salary only for real (non-duplicate) errors
    no_accident = True
    for r in records:
        differs = r["salary"] != r["correct_salary"]
        if r["error_type"] == "duplicate":
            differs = False
        if differs != (r["is_error"] and r["error_type"] != "duplicate"):
            no_accident = False
    print("No accidental errors:", no_accident)

    # correct average
    total = 0
    for r in correct:
        total = total + r["salary"]
    print("Correct average:", total / len(correct))

    # counts
    counts = {}
    for r in records:
        if r["is_error"]:
            counts[r["error_type"]] = counts.get(r["error_type"], 0) + 1
    print("Errors:", counts)
    print("Settings:", setting["inspections"], "inspections,", setting["time_limit"], "seconds")
    print()

# expected actions table for Beginner
print("ID | Employee | Problem | Expected action")
for r in beginner_case:
    problem = r["error_type"] if r["is_error"] else "none"
    print(r["id"], "|", r["name"], "|", problem, "|", r["expected_action"])

# ---------- Phase 3 (Norah): expected action + ground-truth tests ----------

# 1. The expected best action for every record (the ground-truth table)
expected = {
    1: "valid",    # Ahmed  - no problem
    2: "valid",    # Sara   - no problem
    3: "valid",    # Khalid - no problem
    4: "valid",    # Nora   - valid low salary (intern)
    5: "replace",  # Fahad  - x10 salary
    6: "replace",  # Maha   - missing salary
    7: "replace",  # Omar   - negative salary
    8: "valid",    # Ali    - valid high salary (CEO)
    9: "replace",  # Reem   - zero salary
    10: "valid",   # Turki  - no problem
}

# add the field "expected_action" to every record
for r in beginner_case:
    r["expected_action"] = expected[r["id"]]
for r in correct_beginner_case:
    r["expected_action"] = expected[r["id"]]

# 2. Print the table
print("ID | Employee | Problem | Expected action")
for r in beginner_case:
    problem = r["error_type"] if r["is_error"] else "none"
    print(r["id"], "|", r["name"], "|", problem, "|", r["expected_action"])

# 3. Validation checks
ok = True
for r in beginner_case:
    if r["expected_action"] not in ["valid", "replace", "delete"]:
        ok = False
print("Every record has an expected action:", ok)

rules_ok = True
for r in beginner_case:
    if r["is_error"] and r["expected_action"] != "replace":
        rules_ok = False
    if not r["is_error"] and r["expected_action"] != "valid":
        rules_ok = False
print("Expected actions match is_error:", rules_ok)

names = [r["name"] for r in beginner_case]
print("No duplicate records (Delete is always wrong):", len(names) == len(set(names)))

total = 0
for r in correct_beginner_case:
    total = total + r["salary"]
print("Correct average is 12,000:", total / len(correct_beginner_case) == 12000)


# ---------- 4. The four test scenarios ----------
def score_action(action, record, streak):
    # simple scoring based on expected_action (same rules as the team file)
    if action == record["expected_action"]:
        if record["is_error"]:
            return 100 * min(streak + 1, 4)
        if record["id"] in [4, 8]:       # valid traps: Nora and Ali
            return 60 * min(streak + 1, 4)
        return 0                         # a normal record, nothing happens
    if not record["is_error"]:
        return -150          # changed a valid record
    return -80               # wrong action on an error

def play(choices):
    # choices = {record id: action}. Records not in choices stay unresolved.
    score = 0
    streak = 0
    mistakes = 0
    for r in beginner_case:
        if r["id"] in choices:
            points = score_action(choices[r["id"]], r, streak)
            score = score + points
            if points > 0:
                streak = streak + 1
            elif points < 0:
                streak = 0
                mistakes = mistakes + 1
        elif r["is_error"]:
            score = score - 50   # unresolved error
    return score, mistakes

# Test A - perfect player
perfect = {}
for r in beginner_case:
    perfect[r["id"]] = r["expected_action"]
print("Test A perfect player:", play(perfect))

# Test B - deletes the CEO (Ali, id 8)
b = dict(perfect)
b[8] = "delete"
print("Test B deletes Ali:", play(b))

# Test C - marks Fahad's x10 salary as valid (id 5)
c = dict(perfect)
c[5] = "valid"
print("Test C keeps x10 salary:", play(c))

# Test D - submits early: only Ahmed (id 1) reviewed, 4 errors unresolved
print("Test D submit early:", play({1: "valid"}))

# ---------- Phase 5 (Norah): dataset and difficulty validation ----------
print("Level | Records | Errors | Traps | Error types | Correct average | Inspections | Seconds")
for level, setting in case_settings.items():
    records = setting["records"]
    correct = setting["correct"]

    errors = 0
    traps = 0
    types = []
    for r in records:
        if r["is_error"]:
            errors = errors + 1
            if r["error_type"] not in types:
                types.append(r["error_type"])
        elif r["salary"] > 40000 or r["salary"] < 4000:
            traps = traps + 1

    total = 0
    for r in correct:
        total = total + r["salary"]
    correct_average = total / len(correct)

    print(level, "|", len(records), "|", errors, "|", traps, "|", len(types), "|",
          round(correct_average), "|", setting["inspections"], "|", setting["time_limit"])

# ---------- Checks for every level ----------
print()
for level, setting in case_settings.items():
    records = setting["records"]
    correct = setting["correct"]
    ok = True

    ids = [r["id"] for r in records]
    if len(ids) != len(set(ids)):
        ok = False                                    # IDs must be unique

    for r in records:
        if r["is_error"] and r["correct_salary"] is None:
            ok = False                                # every error needs a correct value
        if not r["is_error"] and r["salary"] != r["correct_salary"]:
            ok = False                                # valid traps are not errors
        if r["correct_salary"] < 1000 or r["correct_salary"] > 60000:
            ok = False                                # no impossible correct salaries

    stay = []
    for r in records:
        if r["expected_action"] != "delete":
            stay.append(r["name"])
    names_correct = []
    for r in correct:
        names_correct.append(r["name"])
    if stay != names_correct:
        ok = False                                    # correct dataset = the employees who should stay

    print(level, "dataset is valid:", ok)

# ---------- Difficulty check ----------
levels = list(case_settings.keys())
harder = True
for i in range(1, len(levels)):
    before = case_settings[levels[i - 1]]
    now = case_settings[levels[i]]
    if len(now["records"]) <= len(before["records"]):
        harder = False
    if now["time_limit"] >= before["time_limit"]:
        harder = False
print("Each level has more records and less time than the one before:", harder)