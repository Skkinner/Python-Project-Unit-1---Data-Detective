# Data Detective 🕵️

**Bad Data → Wrong Analysis → Wrong Decisions**

A data-cleaning game built with Python and Streamlit.

## Project Overview

You are a junior analyst. An employee salary report is about to reach management, and it hides errors.
Your job is to find them and fix them before the report goes out. But be careful: some salaries look strange
and are still correct (a CEO with a high salary, an intern with a low one). Treating them as errors is a mistake too.

## Core Concept

A wrong salary changes the company average, and a wrong average leads to wrong decisions.
The game teaches that data cleaning needs judgment, not just rules: an outlier is a reason to check, not a reason to delete.

## How the Game Works

1. Enter your name and choose a difficulty level.
2. Every employee row has four actions:
   - 🔍 **Inspect**: get a clue (limited number of inspections, the clue never says "this is wrong")
   - 🗑️ **Delete**: remove the record (correct only for duplicate employees)
   - 🔧 **Replace**: replace the salary with the company median (correct for wrong salaries)
   - ✅ **Valid**: keep the record as it is
3. A decision is locked once it is made (the row shows "Reviewed ✅").
4. Press **Submit Report** (or run out of time) to see the final results.

**Scoring**

| Event | Points |
|---|---|
| Correct fix of an error | +100 |
| Keeping a valid but unusual record | +60 |
| Changing a valid record | −150 |
| Wrong action on an error (for example marking it valid) | −80 |
| Undiscovered error at submission | −50 each |

A streak multiplier (×1 to ×4) applies to positive points and resets after a mistake.

**Accuracy** = 100 − |your average − correct average| / correct average × 100, kept between 0 and 100.

**Stars**: 3 stars (accuracy 95%+ and at most 1 mistake), 2 stars (85%+ and at most 3 mistakes),
1 star (70%+ and at most 6 mistakes), otherwise 0. Mistakes count wrong decisions and missed errors.

After every game the results page lists each mistake and the weak areas (which error types cost points).

## Difficulty Levels

| Level | Records | Errors | Valid traps | Inspections | Time |
|---|---|---|---|---|---|
| Beginner | 10 | 4 | 2 | 3 | 3:00 |
| Medium | 15 | 6 (2 duplicates) | 2 | 3 | 2:30 |
| Advanced | 20 | 8 (2 duplicates) | 3 | 3 | 2:00 |

- **Beginner**: missing, negative, zero and ×10 salaries.
- **Medium**: adds duplicate employees (the only case where Delete is right).
- **Advanced**: adds a salary 10 times too small, more outliers and disguised errors
  (the same salary can be wrong for an intern and correct for a director).

Only the data and the settings change between levels. The game logic is the same.

## Python Concepts Used

- **Data types**: integers, floats, strings, booleans, `None`
- **Collections**: lists of dictionaries (records), dictionaries (settings, game state)
- **Conditions**: `if / elif / else` for scoring, hints and stars
- **Loops**: `for` and `while` (average, median, game loop in the CLI version)
- **Functions with return values**: `average`, `calculate_median`, `give_hint`, `calculate_score`, `calculate_accuracy`, `calculate_stars`
- **Lambda**: `is_valid_trap` (scoring.py) and `is_suspicious` (game_logic.py)
- **Input / print**: the text version in `main.py`
- **Modules and imports**: logic is split into `data.py`, `game_logic.py` and `scoring.py` and reused by both versions
- **Streamlit**: `st.session_state`, columns, metrics, buttons with callbacks, and a live timer (`st.fragment`)

## Project Structure

```
data-detective/
├── app.py          # Streamlit app: Welcome, Instructions + Levels, Game + Results
├── main.py         # Text (CLI) version of the game
├── data.py         # Datasets, correct reference datasets and level settings
├── game_logic.py   # Average, median, hints, accuracy, stars and the game engine
├── scoring.py      # Points for each action
├── requirements.txt
└── README.md
```

Every record uses the same keys:
`id, name, job, salary, correct_salary, is_error, error_type, expected_action, reviewed, deleted`

## How to Run Locally

```
pip install -r requirements.txt
streamlit run app.py
```

Text version:

```
python main.py
```

## Streamlit Deployment

The app is deployed from this GitHub repository with the entry file `app.py`.

Public link: **[add the Streamlit Cloud link here]**

## Team Members

| Member | Contribution |
|---|---|
| Fahad | Main game flow, integration, navigation and game state, GitHub repository |
| Norah | Datasets, correct reference datasets, hidden errors, expected actions, difficulty levels and validation |
| Raghad | Calculation and scoring functions (average, median, hints, score, accuracy, stars) |
| Rawan | Streamlit interface and visual layout, UX testing |

## Reflection

**Fahad:** Working on Data Detective helped me understand how Python concepts can be combined into a complete application. My main role was integrating the game logic, data, and scoring system. I also improved my understanding of data cleaning, testing, teamwork, GitHub, and Streamlit. The project taught me that unusual data is not always incorrect and that context is important when making data-cleaning decisions.

**Norah:** I worked on the datasets, the hidden errors, the expected actions and the level settings, The most important thing I learned is that unusual data is not always wrong: a CEO or intern salary looks strange but is valid, so a good analyst has to check before deleting. The hardest part was making the scoring and the accuracy fair, so that keeping a valid record is rewarded and changing it is penalized. I solved it by testing each level many times with perfect and bad runs until the results made sense. I made sure I understood and tested every part of the code.

**Raghad:** I worked on `game_logic.py` and `scoring.py`, which have the calculations and the rules of the game. It was fun to write the code and set the game rules myself. Usually I'm the one playing a game and following its rules, not creating them, so this was a very cool and educational experience. I loved seeing that the simple Python concepts we learned in class could turn into a real game. The most useful Python concept was Functions. I wrote calculations: (average, median, hints, score, accuracy, stars) and tested it. If we have more time for improvements, i would add more levels and different kinds of data, such as exam scores or temperatures, and make the game look more polished.

**Rawan:** I worked mainly on the Streamlit user interface and the overall player experience of Data Detective. My role included designing the welcome page, instructions and level selection, game layout, employee records, action buttons, and final results screen. I also tested the application from the player’s perspective to make sure the interface was clear and easy to use. The most useful thing I learned was how Python and Streamlit can turn backend code into an interactive web application. 
