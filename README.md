# Data Detective 🕵️

Data Detective is an interactive Python and Streamlit game that teaches the importance of data cleaning.

The player acts as a junior data analyst responsible for reviewing a salary dataset that contains hidden data-quality problems.

The main idea is:

**Bad Data → Wrong Analysis → Wrong Decisions**

## Project Objective

The player must inspect employee records, identify incorrect data, clean the dataset, and improve the final salary report.

The game also teaches an important lesson:

An unusual value is not always incorrect.

For example, a CEO may legitimately have a much higher salary than other employees, while an intern may have a lower salary.

## Features

- Interactive Streamlit interface
- Three difficulty levels:
  - Beginner
  - Medium
  - Advanced
- Employee salary datasets with hidden errors
- Data inspection hints
- Delete duplicate records
- Replace incorrect salaries with the median
- Mark valid records
- Score system
- Streak multiplier
- Mistake tracking
- Limited inspections
- Time limits for each level
- Accuracy calculation
- Star rating system
- Final salary report comparison

## Error Types

The game includes several data-quality problems:

- Missing values
- Negative salaries
- Zero salaries
- Salary multiplied by 10
- Salary divided by 10
- Duplicate records

The game also contains valid unusual values to test whether the player can distinguish between an outlier and an actual error.

## Difficulty Levels

### Beginner

- 10 records
- 3 inspections
- 180 seconds
- Basic salary errors

### Medium

- 15 records
- 3 inspections
- 150 seconds
- Includes duplicate records

### Advanced

- 20 records
- 3 inspections
- 120 seconds
- More records and more complex error patterns

## Project Structure

```text
Data Detective/
│
├── app.py
├── main.py
├── data.py
├── game_logic.py
├── scoring.py
├── test_logic.py
├── requirements.txt
└── README.md