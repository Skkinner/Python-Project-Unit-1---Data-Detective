# main.py - CLI version of Data Detective
# Run the program using: python main.py

import time

# Import game settings and game functions
from data import case_settings
from game_logic import new_game, find_record, inspect_record, take_action, finish_game


# --------------------------------------------------
# Game Introduction
# --------------------------------------------------

print("DATA DETECTIVE")
print("Bad Data -> Wrong Analysis -> Wrong Decisions")
print()


# --------------------------------------------------
# Display Available Difficulty Levels
# --------------------------------------------------

# Get all level names from case_settings
level_names = list(case_settings.keys())

# Show each level with its description
for i in range(len(level_names)):
    print(
        str(i + 1) + ".",
        level_names[i],
        "-",
        case_settings[level_names[i]]["description"]
    )


# --------------------------------------------------
# Level Selection
# --------------------------------------------------

level_number = input("Choose a level (1-3): ")

# If the user enters an invalid option,
# automatically select level 1
if level_number not in ["1", "2", "3"]:
    level_number = "1"

# Convert the selected number into the level name
level_name = level_names[int(level_number) - 1]


# --------------------------------------------------
# Start a New Game
# --------------------------------------------------

# Create the game using the selected difficulty level
game = new_game(level_name, case_settings)

# Calculate when the game timer should end
end_time = time.time() + case_settings[level_name]["time_limit"]


# --------------------------------------------------
# Main Game Loop
# --------------------------------------------------

while True:

    # Calculate remaining time
    seconds_left = int(end_time - time.time())

    # End the game if time runs out
    if seconds_left <= 0:
        print("TIME IS UP!")
        break


    # --------------------------------------------------
    # Display Employee Records
    # --------------------------------------------------

    print()

    for r in game["records"]:

        # Show "None" if the salary value is missing
        shown = "None" if r["salary"] is None else r["salary"]

        # Show the current status of the record
        status = ""

        if r["deleted"]:
            status = "  [deleted]"

        elif r["reviewed"]:
            status = "  [reviewed]"

        # Display employee information
        print(
            "ID:", r["id"],
            "|", r["name"],
            "|", r["job"],
            "|", shown,
            status
        )


    # --------------------------------------------------
    # Display Current Game Statistics
    # --------------------------------------------------

    print()

    print(
        "Score:", game["score"],
        "| Inspections:", game["inspections"],
        "| Streak:", game["streak"],
        "| Time left:", seconds_left, "s"
    )


    # --------------------------------------------------
    # Employee Selection
    # --------------------------------------------------

    choice = input("Choose employee ID (0 to submit): ")

    # Check that the input contains only numbers
    if not choice.isdigit():
        print("Please type a number.")
        continue

    choice = int(choice)

    # Entering 0 submits the case
    if choice == 0:
        break


    # Find the selected employee record
    selected = find_record(game, choice)

    # Check if the employee ID exists
    if selected is None:
        print("No employee with this ID.")
        continue

    # Prevent the player from reviewing the same record again
    if selected["reviewed"] or selected["deleted"]:
        print("You already decided on this record.")
        continue


    # --------------------------------------------------
    # Choose an Action
    # --------------------------------------------------

    print("1. Inspect  2. Delete  3. Replace  4. Valid")

    action_number = input("Action: ")


    # --------------------------------------------------
    # Inspect Record
    # --------------------------------------------------

    if action_number == "1":

        # Inspect the selected record and receive a hint
        hint = inspect_record(game, selected)

        # The player may have a limited number of inspections
        if hint is None:
            print("No inspections left.")

        else:
            print("Hint:", hint)
            print("Inspections:", game["inspections"])


    # --------------------------------------------------
    # Delete, Replace, or Mark as Valid
    # --------------------------------------------------

    elif action_number in ["2", "3", "4"]:

        # Convert menu numbers into action names
        action = {
            "2": "delete",
            "3": "replace",
            "4": "valid"
        }[action_number]

        # Perform the selected action
        points, message = take_action(game, selected, action)

        # Display action result
        print(message)

        # Add "+" before positive points
        print(
            ("+" if points > 0 else "") + str(points),
            "points"
        )


    # Invalid action input
    else:
        print("Please choose 1, 2, 3 or 4.")


# --------------------------------------------------
# Finish the Game and Generate the Final Report
# --------------------------------------------------

report = finish_game(game)


# --------------------------------------------------
# Display Final Results
# --------------------------------------------------

print()
print("=" * 40)
print("CASE COMPLETE")
print("=" * 40)
print()

# Compare the dataset averages
print(
    "Original Average:",
    format(report["original_average"], ",.2f"),
    "SAR"
)

print(
    "Final Average:",
    format(report["final_average"], ",.2f"),
    "SAR"
)

print(
    "Correct Average:",
    format(report["correct_average"], ",.2f"),
    "SAR"
)

print()

# Display player performance
print(
    "Accuracy:",
    format(report["accuracy"], ".2f") + "%"
)

print("Score:", report["score"])

print(
    "Mistakes:", report["mistakes"],
    "| Missed errors:", report["missed"]
)

# Display rating using stars
print(
    "Rating:",
    "★" * report["stars"]
    + "☆" * (3 - report["stars"])
)

print()


# --------------------------------------------------
# Feedback
# --------------------------------------------------

# Show a success message if no mistakes were made
if len(report["notes"]) == 0:
    print("No mistakes. Great work!")

# Otherwise, display suggestions for improvement
else:
    print("What to improve:")

    for note in report["notes"]:
        print("-", note)
