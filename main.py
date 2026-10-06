# main.py - the text (CLI) version of Data Detective
# Run:  python main.py
import time
from data import case_settings
from game_logic import new_game, find_record, inspect_record, take_action, finish_game

print("DATA DETECTIVE")
print("Bad Data -> Wrong Analysis -> Wrong Decisions")
print()
level_names = list(case_settings.keys())
for i in range(len(level_names)):
    print(str(i + 1) + ".", level_names[i], "-", case_settings[level_names[i]]["description"])

level_number = input("Choose a level (1-3): ")
if level_number not in ["1", "2", "3"]:
    level_number = "1"
level_name = level_names[int(level_number) - 1]

game = new_game(level_name, case_settings)
end_time = time.time() + case_settings[level_name]["time_limit"]

while True:
    seconds_left = int(end_time - time.time())
    if seconds_left <= 0:
        print("TIME IS UP!")
        break

    print()
    for r in game["records"]:
        shown = "None" if r["salary"] is None else r["salary"]
        status = ""
        if r["deleted"]:
            status = "  [deleted]"
        elif r["reviewed"]:
            status = "  [reviewed]"
        print("ID:", r["id"], "|", r["name"], "|", r["job"], "|", shown, status)
    print()
    print("Score:", game["score"], "| Inspections:", game["inspections"], "| Streak:", game["streak"], "| Time left:", seconds_left, "s")

    choice = input("Choose employee ID (0 to submit): ")
    if not choice.isdigit():
        print("Please type a number.")
        continue
    choice = int(choice)
    if choice == 0:
        break

    selected = find_record(game, choice)
    if selected is None:
        print("No employee with this ID.")
        continue
    if selected["reviewed"] or selected["deleted"]:
        print("You already decided on this record.")
        continue

    print("1. Inspect  2. Delete  3. Replace  4. Valid")
    action_number = input("Action: ")
    if action_number == "1":
        hint = inspect_record(game, selected)
        if hint is None:
            print("No inspections left.")
        else:
            print("Hint:", hint)
            print("Inspections:", game["inspections"])
    elif action_number in ["2", "3", "4"]:
        action = {"2": "delete", "3": "replace", "4": "valid"}[action_number]
        points, message = take_action(game, selected, action)
        print(message)
        print(("+" if points > 0 else "") + str(points), "points")
    else:
        print("Please choose 1, 2, 3 or 4.")

report = finish_game(game)
print()
print("=" * 40)
print("CASE COMPLETE")
print("=" * 40)
print()
print("Original Average:", format(report["original_average"], ",.2f"), "SAR")
print("Final Average:", format(report["final_average"], ",.2f"), "SAR")
print("Correct Average:", format(report["correct_average"], ",.2f"), "SAR")
print()
print("Accuracy:", format(report["accuracy"], ".2f") + "%")
print("Score:", report["score"])
print("Mistakes:", report["mistakes"], "| Missed errors:", report["missed"])
print("Rating:", "★" * report["stars"] + "☆" * (3 - report["stars"]))
print()
if len(report["notes"]) == 0:
    print("No mistakes. Great work!")
else:
    print("What to improve:")
    for note in report["notes"]:
        print("-", note)
