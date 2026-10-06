# data.py - datasets and difficulty settings for Data Detective
#
# Every record has exactly these keys:
#   id, name, job, salary, correct_salary, is_error, error_type, expected_action, reviewed, deleted
# error_type: "missing", "negative", "zero", "x10", "div10", "duplicate" or None
# expected_action: "valid", "replace" or "delete"
# A "duplicate" record must be deleted, so it is NOT in the correct reference dataset.
# The correct_*_case lists are the reference datasets. The player never sees them.

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
    "Beginner": {
        "inspections": 3,
        "time_limit": 180,
        "records": beginner_case,
        "correct": correct_beginner_case,
        "description": "10 employees. Clear errors: a missing salary, a negative salary, a zero salary and a salary ten times too big. Two unusual but valid salaries are there to test you.",
    },
    "Medium": {
        "inspections": 3,
        "time_limit": 150,
        "records": medium_case,
        "correct": correct_medium_case,
        "description": "15 employees. Duplicate records appear (the only time Delete is right) and some unusual salaries are valid.",
    },
    "Advanced": {
        "inspections": 3,
        "time_limit": 120,
        "records": advanced_case,
        "correct": correct_advanced_case,
        "description": "20 employees. Several error types, subtle outliers and more traps. The same salary can be wrong for one job and correct for another.",
    },
}
