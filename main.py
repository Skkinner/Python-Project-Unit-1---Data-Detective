# ============================================================
# Data Detective
# Main Game Engine / CLI Integration
# Developed by: Fahad
#
# Responsibility:
# - Connect the dataset with the game logic
# - Handle player interaction
# - Manage actions, score, streak, mistakes, and inspections
# - Generate the final game result
# ============================================================


import copy

# Import all level settings and datasets
from data import case_settings

# Import calculation functions
from game_logic import (
    average,
    calculate_median,
    give_hint,
    calculate_accuracy,
    calculate_stars
)

# Import scoring functions
from scoring import (
    calculate_score,
    update_streak,
    unresolved_penalty
)


# ============================================================
# 1. GAME SETUP
# ============================================================

# For the CLI version, we start with the Beginner level
level = "Beginner"

# Create a copy of the selected level records.
# deepcopy is used so the original dataset in data.py is not changed.
records = copy.deepcopy(
    case_settings[level]["records"]
)

# Correct reference dataset used at the end of the game
correct_records = case_settings[level]["correct"]

# Initial game values
score = 0
streak = 0
mistakes = 0

# Get the number of available inspections from the level settings
inspections = case_settings[level]["inspections"]

# Controls the main game loop
game_running = True

# Save the original average before the player changes anything
original_average = average(records)


# ============================================================
# 2. DISPLAY EMPLOYEE RECORDS
# ============================================================

def display_records(records):
    """
    Display all employee records that have not been reviewed yet.
    """

    print("\n" + "=" * 70)
    print("DATA DETECTIVE - EMPLOYEE RECORDS")
    print("=" * 70)

    for record in records:

        # Only show records that still need a decision
        if not record["reviewed"]:

            salary = record["salary"]

            # Display missing salary clearly instead of showing None
            if salary is None:
                salary_display = "Missing"

            else:
                salary_display = f"{salary:,.2f}"

            print(
                f'ID: {record["id"]} | '
                f'Name: {record["name"]} | '
                f'Job: {record["job"]} | '
                f'Salary: {salary_display}'
            )

    print("=" * 70)


# ============================================================
# 3. FIND EMPLOYEE RECORD
# ============================================================

def find_record(records, employee_id):
    """
    Search for an employee using their ID.
    Return the employee record if found.
    """

    for record in records:

        if record["id"] == employee_id:
            return record

    return None


# ============================================================
# 4. MAIN GAME LOOP
# ============================================================

while game_running:

    # Display the current employee records
    display_records(records)

    # Display current game information
    print("\nLevel:", level)
    print("Score:", score)
    print("Streak:", streak)
    print("Mistakes:", mistakes)
    print("Inspections remaining:", inspections)

    print("\nChoose an option:")
    print("1. Select employee")
    print("2. Submit report")

    main_choice = input("Enter your choice: ")


    # ========================================================
    # OPTION 1: SELECT EMPLOYEE
    # ========================================================

    if main_choice == "1":

        # Prevent the game from crashing if the user enters text
        try:
            employee_id = int(
                input("Enter employee ID: ")
            )

        except ValueError:
            print("Invalid ID. Please enter a number.")
            continue


        # Find the selected employee
        selected_record = find_record(
            records,
            employee_id
        )


        # Check if the employee exists
        if selected_record is None:
            print("Employee not found.")
            continue


        # Prevent changing a final decision
        if selected_record["reviewed"]:
            print("This record has already been reviewed.")
            continue


        # Display selected employee information
        print(
            f'\nSelected: '
            f'{selected_record["name"]} - '
            f'{selected_record["job"]}'
        )


        # Display player actions
        print("\nChoose an action:")
        print("1. Inspect")
        print("2. Delete")
        print("3. Replace with Median")
        print("4. Mark as Valid")

        action = input("Enter action: ")


        # ====================================================
        # ACTION 1: INSPECT
        # ====================================================

        if action == "1":

            # Check if the player still has inspections available
            if inspections > 0:

                # Calculate the current median
                median = calculate_median(records)

                # Generate a clue without directly revealing the answer
                hint = give_hint(
                    selected_record,
                    median,
                    records
                )

                print("\nHint:")
                print(hint)

                # Reduce the available inspection count
                inspections -= 1

            else:
                print("No inspections remaining.")


        # ====================================================
        # ACTION 2: DELETE
        # ====================================================

        elif action == "2":

            # Calculate the score for this action
            points, correct = calculate_score(
                "delete",
                selected_record,
                streak
            )

            # Update total score
            score += points

            # Count mistakes
            if correct is False:
                mistakes += 1

            # Update the current streak
            streak = update_streak(
                streak,
                correct,
                selected_record
            )

            # Mark the record as deleted and reviewed
            selected_record["deleted"] = True
            selected_record["reviewed"] = True

            print("Record deleted.")
            print("Points:", points)


        # ====================================================
        # ACTION 3: REPLACE WITH MEDIAN
        # ====================================================

        elif action == "3":

            # Calculate the median before replacing the salary
            median = calculate_median(records)

            # Calculate points for this action
            points, correct = calculate_score(
                "replace",
                selected_record,
                streak
            )

            # Update total score
            score += points

            # Count mistakes
            if correct is False:
                mistakes += 1

            # Update streak
            streak = update_streak(
                streak,
                correct,
                selected_record
            )

            # Replace the salary with the company median
            selected_record["salary"] = median

            # Lock the record
            selected_record["reviewed"] = True

            print(
                f"Salary replaced with median: {median:,.2f}"
            )

            print("Points:", points)


        # ====================================================
        # ACTION 4: MARK AS VALID
        # ====================================================

        elif action == "4":

            # Calculate the score for accepting the record
            points, correct = calculate_score(
                "valid",
                selected_record,
                streak
            )

            # Update total score
            score += points

            # Count mistakes
            if correct is False:
                mistakes += 1

            # Update streak
            streak = update_streak(
                streak,
                correct,
                selected_record
            )

            # Mark the record as reviewed
            selected_record["reviewed"] = True

            print("Record marked as valid.")
            print("Points:", points)


        # Invalid action
        else:
            print("Invalid action.")


    # ========================================================
    # OPTION 2: SUBMIT REPORT
    # ========================================================

    elif main_choice == "2":

        # Stop the main game loop
        game_running = False


    # Invalid main menu input
    else:
        print("Invalid choice.")


# ============================================================
# 5. FINAL GAME CALCULATIONS
# ============================================================

# Apply penalty for errors that were never reviewed
score += unresolved_penalty(records)

# Calculate the player's final salary average
final_average = average(records)

# Calculate the correct reference average
correct_average = average(
    correct_records
)

# Compare the player's result with the correct result
accuracy = calculate_accuracy(
    final_average,
    correct_average
)

# Calculate the final star rating
stars = calculate_stars(
    accuracy,
    mistakes
)


# ============================================================
# 6. FINAL RESULT SCREEN
# ============================================================

print("\n" + "=" * 45)
print("CASE COMPLETE")
print("=" * 45)

print(f"Original Average: {original_average:,.2f} SAR")
print(f"Your Final Average: {final_average:,.2f} SAR")
print(f"Correct Average: {correct_average:,.2f} SAR")

print(f"\nAccuracy: {accuracy:.2f}%")

print("Final Score:", score)
print("Mistakes:", mistakes)
print("Final Streak:", streak)

# Display stars
if stars > 0:
    print("Rating:", "⭐" * stars)

else:
    print("Rating: No stars")


print("\nThank you for playing Data Detective.")