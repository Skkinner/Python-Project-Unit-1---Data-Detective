# ============================================================
# Data Detective
# Streamlit Web Application
#
# This file connects:
# - data.py
# - game_logic.py
# - scoring.py
#
# Application Flow:
# Phase 1 -> Home Page
# Phase 2 -> Level Selection
# Phase 3 -> Game
# Phase 4 -> Results
# Phase 5 -> Restart / Final Integration
# ============================================================


import copy
import time
import streamlit as st


# ============================================================
# IMPORT PROJECT FILES
# ============================================================

from data import case_settings

from game_logic import (
    average,
    calculate_median,
    give_hint,
    calculate_accuracy,
    calculate_stars
)

from scoring import (
    calculate_score,
    update_streak,
    unresolved_penalty
)


# ============================================================
# STREAMLIT PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Data Detective",
    page_icon="🕵️",
    layout="wide"
)


# ============================================================
# PHASE 1
# SESSION STATE INITIALIZATION
# ============================================================

def initialize_session_state():
    """
    Create all session-state variables required by the application.
    """

    default_values = {
        "page": "home",
        "player_name": "",
        "level": None,
        "records": [],
        "correct_records": [],
        "score": 0,
        "streak": 0,
        "best_streak": 0,
        "mistakes": 0,
        "inspections": 0,
        "original_average": 0.0,
        "game_finished": False,
        "penalty_applied": False,
        "start_time": None,
        "time_limit": 0,
        "finish_reason": "submitted",
        "message": None,
        "message_type": None
    }

    for key, value in default_values.items():

        if key not in st.session_state:
            st.session_state[key] = value


initialize_session_state()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def reset_game():
    """
    Return the application to the beginning.
    """

    st.session_state.page = "home"
    st.session_state.player_name = ""
    st.session_state.level = None

    st.session_state.records = []
    st.session_state.correct_records = []

    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.mistakes = 0
    st.session_state.inspections = 0

    st.session_state.original_average = 0.0

    st.session_state.game_finished = False
    st.session_state.penalty_applied = False

    st.session_state.start_time = None
    st.session_state.time_limit = 0

    st.session_state.finish_reason = "submitted"

    st.session_state.message = None
    st.session_state.message_type = None


def start_game(level):
    """
    Load the selected difficulty and initialize a new game.
    """

    settings = case_settings[level]

    # Deep copy prevents changes to the original data.py dataset.
    st.session_state.records = copy.deepcopy(
        settings["records"]
    )

    st.session_state.correct_records = copy.deepcopy(
        settings["correct"]
    )

    st.session_state.level = level

    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0
    st.session_state.mistakes = 0

    st.session_state.inspections = settings["inspections"]

    st.session_state.original_average = average(
        st.session_state.records
    )

    st.session_state.time_limit = settings["time_limit"]
    st.session_state.start_time = time.time()

    st.session_state.game_finished = False
    st.session_state.penalty_applied = False

    st.session_state.finish_reason = "submitted"

    st.session_state.message = None
    st.session_state.message_type = None

    st.session_state.page = "game"


def find_record(employee_id):
    """
    Find an employee inside the active game.
    """

    for record in st.session_state.records:

        if record["id"] == employee_id:
            return record

    return None


def get_remaining_time():
    """
    Calculate how much time remains in the current case.
    """

    if st.session_state.start_time is None:
        return st.session_state.time_limit

    elapsed = int(
        time.time() - st.session_state.start_time
    )

    remaining = (
        st.session_state.time_limit
        - elapsed
    )

    return max(0, remaining)


def format_time(seconds):
    """
    Convert seconds to MM:SS.
    """

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes:02d}:{seconds:02d}"


def set_message(message, message_type="info"):
    """
    Store feedback so it survives Streamlit reruns.
    """

    st.session_state.message = message
    st.session_state.message_type = message_type


def show_message():
    """
    Display the latest action feedback.
    """

    if st.session_state.message is None:
        return

    if st.session_state.message_type == "success":
        st.success(st.session_state.message)

    elif st.session_state.message_type == "error":
        st.error(st.session_state.message)

    elif st.session_state.message_type == "warning":
        st.warning(st.session_state.message)

    else:
        st.info(st.session_state.message)


def finish_game(reason="submitted"):
    """
    Finish the case and apply unresolved-error penalty once.
    """

    if not st.session_state.penalty_applied:

        penalty = unresolved_penalty(
            st.session_state.records
        )

        st.session_state.score += penalty
        st.session_state.penalty_applied = True

    st.session_state.finish_reason = reason
    st.session_state.game_finished = True


# ============================================================
# PHASE 1
# HOME PAGE
# ============================================================

def show_home_page():

    st.title("🕵️ Data Detective")

    st.subheader(
        "Bad Data → Wrong Analysis → Wrong Decisions"
    )

    st.write(
        """
        You are a junior data analyst.

        Your company is preparing a salary report for management,
        but the dataset may contain hidden errors.

        Your mission is to inspect the employee records, identify
        incorrect data, clean the report, and produce a more
        accurate salary analysis.
        """
    )

    st.divider()

    player_name = st.text_input(
        "Enter your name",
        placeholder="Your name"
    )

    if st.button(
        "Start",
        type="primary",
        use_container_width=True
    ):

        if player_name.strip() == "":

            st.warning(
                "Please enter your name before starting."
            )

        else:

            st.session_state.player_name = (
                player_name.strip()
            )

            st.session_state.page = "levels"

            st.rerun()


# ============================================================
# PHASE 2
# LEVEL SELECTION PAGE
# ============================================================

def show_level_page():

    st.title(
        f"Welcome, {st.session_state.player_name} 👋"
    )

    st.write(
        """
        ### Your Mission

        Review the salary dataset and decide what should happen
        to each employee record.

        You may:

        - 🔍 **Inspect** a suspicious record for a hint.
        - 🗑️ **Delete** a record if it is a duplicate.
        - 🔄 **Replace with Median** when a salary value is incorrect.
        - ✅ **Mark as Valid** when the record is correct.

        Be careful: an unusual salary is not automatically wrong.
        A CEO can legitimately earn much more than an intern.
        """
    )

    st.divider()

    st.subheader("Choose Difficulty")

    level = st.radio(
        "Difficulty Level",
        ["Beginner", "Medium", "Advanced"],
        horizontal=True
    )

    settings = case_settings[level]

    record_count = len(settings["records"])

    error_count = sum(
        1
        for record in settings["records"]
        if record["is_error"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Records",
        record_count
    )

    col2.metric(
        "Inspections",
        settings["inspections"]
    )

    col3.metric(
        "Time",
        format_time(settings["time_limit"])
    )

    if level == "Beginner":

        st.info(
            f"""
            Beginner contains {record_count} employee records
            and {error_count} hidden errors.
            """
        )

    elif level == "Medium":

        st.info(
            f"""
            Medium contains {record_count} employee records,
            {error_count} hidden errors, and duplicate records.
            """
        )

    else:

        st.info(
            f"""
            Advanced contains {record_count} employee records
            with more difficult error patterns and less time.
            """
        )

    st.divider()

    col_back, col_start = st.columns(2)

    with col_back:

        if st.button(
            "← Back",
            use_container_width=True
        ):

            st.session_state.page = "home"
            st.rerun()

    with col_start:

        if st.button(
            "Start Case",
            type="primary",
            use_container_width=True
        ):

            start_game(level)
            st.rerun()


# ============================================================
# PHASE 3
# GAME ACTION FUNCTIONS
# ============================================================

def inspect_record(record):
    """
    Give the player a hint.
    Inspect does not finalize the record.
    """

    if st.session_state.inspections <= 0:

        set_message(
            "No inspections remaining.",
            "warning"
        )

        return

    median = calculate_median(
        st.session_state.records
    )

    hint = give_hint(
        record,
        median,
        st.session_state.records
    )

    st.session_state.inspections -= 1

    set_message(
        f"🔍 Hint for {record['name']}: {hint}",
        "info"
    )


def process_action(record, action):
    """
    Process Delete, Replace, or Mark Valid.
    """

    if record["reviewed"]:

        set_message(
            "This record has already been reviewed.",
            "warning"
        )

        return

    points, correct = calculate_score(
        action,
        record,
        st.session_state.streak
    )

    # Add points or penalties.
    st.session_state.score += points

    # Count wrong final decisions.
    if correct is False:
        st.session_state.mistakes += 1

    # Update streak.
    st.session_state.streak = update_streak(
        st.session_state.streak,
        correct,
        record
    )

    # Track highest streak reached.
    st.session_state.best_streak = max(
        st.session_state.best_streak,
        st.session_state.streak
    )

    # --------------------------------------------
    # DELETE
    # --------------------------------------------

    if action == "delete":

        record["deleted"] = True
        record["reviewed"] = True

        action_text = "Record deleted"

    # --------------------------------------------
    # REPLACE
    # --------------------------------------------

    elif action == "replace":

        median = calculate_median(
            st.session_state.records
        )

        record["salary"] = median
        record["reviewed"] = True

        action_text = (
            f"Salary replaced with median "
            f"({median:,.2f} SAR)"
        )

    # --------------------------------------------
    # MARK VALID
    # --------------------------------------------

    elif action == "valid":

        record["reviewed"] = True

        action_text = "Record marked as valid"

    else:
        return

    if points > 0:

        set_message(
            f"✅ {action_text}. Points: +{points}",
            "success"
        )

    elif points < 0:

        set_message(
            f"❌ {action_text}. Points: {points}",
            "error"
        )

    else:

        set_message(
            f"✅ {action_text}. Points: 0",
            "success"
        )


# ============================================================
# GAME RECORD TABLE
# ============================================================

def show_records_table():

    table_data = []

    for record in st.session_state.records:

        if record["salary"] is None:
            salary = "Missing"

        else:
            salary = f'{record["salary"]:,.2f} SAR'

        if record["deleted"]:
            status = "Deleted"

        elif record["reviewed"]:
            status = "Reviewed"

        else:
            status = "Pending"

        table_data.append(
            {
                "ID": record["id"],
                "Employee": record["name"],
                "Job": record["job"],
                "Salary": salary,
                "Status": status
            }
        )

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PHASE 3
# MAIN GAME PAGE
# ============================================================

def show_game_page():

    # --------------------------------------------
    # TIME CHECK
    # --------------------------------------------

    remaining_time = get_remaining_time()

    if (
        remaining_time <= 0
        and not st.session_state.game_finished
    ):

        finish_game("time")

    # If case finished, show result page.
    if st.session_state.game_finished:

        show_results_page()
        return

    # --------------------------------------------
    # HEADER
    # --------------------------------------------

    st.title("🕵️ Data Detective")

    st.write(
        f"Player: **{st.session_state.player_name}**"
    )

    st.write(
        f"Level: **{st.session_state.level}**"
    )

    # --------------------------------------------
    # GAME METRICS
    # --------------------------------------------

    metric1, metric2, metric3, metric4, metric5 = (
        st.columns(5)
    )

    metric1.metric(
        "Score",
        st.session_state.score
    )

    metric2.metric(
        "Streak",
        f"×{min(st.session_state.streak + 1, 4)}"
        if st.session_state.streak > 0
        else "×1"
    )

    metric3.metric(
        "Mistakes",
        st.session_state.mistakes
    )

    metric4.metric(
        "Inspections",
        st.session_state.inspections
    )

    metric5.metric(
        "Time Left",
        format_time(remaining_time)
    )

    current_average = average(
        st.session_state.records
    )

    st.caption(
        f"Current report average: "
        f"{current_average:,.2f} SAR"
    )

    st.divider()

    # Show latest feedback.
    show_message()

    # --------------------------------------------
    # EMPLOYEE TABLE
    # --------------------------------------------

    st.subheader("Employee Records")

    show_records_table()

    st.divider()

    # --------------------------------------------
    # PENDING RECORDS
    # --------------------------------------------

    pending_records = [
        record
        for record in st.session_state.records
        if not record["reviewed"]
    ]

    if len(pending_records) == 0:

        st.success(
            "All employee records have been reviewed."
        )

        if st.button(
            "Submit Report",
            type="primary",
            use_container_width=True
        ):

            finish_game("submitted")
            st.rerun()

        return

    # --------------------------------------------
    # EMPLOYEE SELECTION
    # --------------------------------------------

    employee_options = {
        (
            f'ID {record["id"]} — '
            f'{record["name"]} — '
            f'{record["job"]}'
        ): record["id"]
        for record in pending_records
    }

    selected_label = st.selectbox(
        "Select an employee",
        list(employee_options.keys())
    )

    selected_id = employee_options[
        selected_label
    ]

    selected_record = find_record(
        selected_id
    )

    # --------------------------------------------
    # SELECTED EMPLOYEE CARD
    # --------------------------------------------

    st.subheader("Selected Employee")

    col1, col2, col3 = st.columns(3)

    col1.write(
        f"**Name:** {selected_record['name']}"
    )

    col2.write(
        f"**Job:** {selected_record['job']}"
    )

    salary = selected_record["salary"]

    if salary is None:

        salary_display = "Missing"

    else:

        salary_display = f"{salary:,.2f} SAR"

    col3.write(
        f"**Salary:** {salary_display}"
    )

    st.write("### Choose an Action")

    action1, action2, action3, action4 = (
        st.columns(4)
    )

    # --------------------------------------------
    # INSPECT
    # --------------------------------------------

    with action1:

        if st.button(
            "🔍 Inspect",
            use_container_width=True,
            key=f"inspect_{selected_id}"
        ):

            inspect_record(
                selected_record
            )

            st.rerun()

    # --------------------------------------------
    # DELETE
    # --------------------------------------------

    with action2:

        if st.button(
            "🗑️ Delete",
            use_container_width=True,
            key=f"delete_{selected_id}"
        ):

            process_action(
                selected_record,
                "delete"
            )

            st.rerun()

    # --------------------------------------------
    # REPLACE
    # --------------------------------------------

    with action3:

        if st.button(
            "🔄 Replace with Median",
            use_container_width=True,
            key=f"replace_{selected_id}"
        ):

            process_action(
                selected_record,
                "replace"
            )

            st.rerun()

    # --------------------------------------------
    # VALID
    # --------------------------------------------

    with action4:

        if st.button(
            "✅ Mark as Valid",
            use_container_width=True,
            key=f"valid_{selected_id}"
        ):

            process_action(
                selected_record,
                "valid"
            )

            st.rerun()

    st.divider()

    # --------------------------------------------
    # SUBMIT EARLY
    # --------------------------------------------

    st.warning(
        """
        You can submit before reviewing every employee,
        but unresolved errors will reduce your score.
        """
    )

    if st.button(
        "Submit Report",
        type="primary",
        use_container_width=True
    ):

        finish_game("submitted")
        st.rerun()


# ============================================================
# PHASE 4
# RESULTS PAGE
# ============================================================

def show_results_page():

    records = st.session_state.records

    correct_records = (
        st.session_state.correct_records
    )

    final_average = average(
        records
    )

    correct_average = average(
        correct_records
    )

    accuracy = calculate_accuracy(
        final_average,
        correct_average
    )

    stars = calculate_stars(
        accuracy,
        st.session_state.mistakes
    )

    st.title("🏁 Case Complete")

    if st.session_state.finish_reason == "time":

        st.warning(
            "Time expired. The case was submitted automatically."
        )

    else:

        st.success(
            "Your salary report has been submitted."
        )

    st.write(
        f"Detective: **{st.session_state.player_name}**"
    )

    st.write(
        f"Difficulty: **{st.session_state.level}**"
    )

    st.divider()

    # --------------------------------------------
    # STAR RATING
    # --------------------------------------------

    if stars > 0:

        st.header(
            "⭐" * stars
        )

    else:

        st.header(
            "No Stars"
        )

    # --------------------------------------------
    # MAIN RESULTS
    # --------------------------------------------

    col1, col2, col3, col4 = (
        st.columns(4)
    )

    col1.metric(
        "Final Score",
        st.session_state.score
    )

    col2.metric(
        "Accuracy",
        f"{accuracy:.2f}%"
    )

    col3.metric(
        "Mistakes",
        st.session_state.mistakes
    )

    col4.metric(
        "Best Streak",
        st.session_state.best_streak
    )

    st.divider()

    # --------------------------------------------
    # AVERAGE COMPARISON
    # --------------------------------------------

    st.subheader("Salary Report")

    average1, average2, average3 = (
        st.columns(3)
    )

    average1.metric(
        "Original Average",
        f"{st.session_state.original_average:,.2f} SAR"
    )

    average2.metric(
        "Your Final Average",
        f"{final_average:,.2f} SAR"
    )

    average3.metric(
        "Correct Average",
        f"{correct_average:,.2f} SAR"
    )

    st.divider()

    # --------------------------------------------
    # EDUCATIONAL MESSAGE
    # --------------------------------------------

    if stars == 3:

        st.success(
            """
            Excellent investigation.

            You identified the important data-quality problems
            while protecting valid unusual values.
            """
        )

    elif stars == 2:

        st.info(
            """
            Good work.

            Your report was close to the correct result,
            but a few decisions could be improved.
            """
        )

    elif stars == 1:

        st.warning(
            """
            Case completed.

            Review how missing values, unusual salaries,
            duplicates, and incorrect values affect analysis.
            """
        )

    else:

        st.error(
            """
            The report still contains major data-quality problems.

            Remember:

            Bad Data → Wrong Analysis → Wrong Decisions
            """
        )

    # --------------------------------------------
    # FINAL RECORDS
    # --------------------------------------------

    with st.expander(
        "View Final Employee Records"
    ):

        show_records_table()

    st.divider()

    # --------------------------------------------
    # PLAY AGAIN
    # --------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Play Again",
            use_container_width=True
        ):

            player_name = (
                st.session_state.player_name
            )

            reset_game()

            st.session_state.player_name = (
                player_name
            )

            st.session_state.page = "levels"

            st.rerun()

    with col2:

        if st.button(
            "Return to Beginning",
            type="primary",
            use_container_width=True
        ):

            reset_game()
            st.rerun()


# ============================================================
# PHASE 5
# APPLICATION ROUTER
# ============================================================

if st.session_state.page == "home":

    show_home_page()


elif st.session_state.page == "levels":

    show_level_page()


elif st.session_state.page == "game":

    show_game_page()


else:

    # Safety fallback
    reset_game()
    st.rerun()