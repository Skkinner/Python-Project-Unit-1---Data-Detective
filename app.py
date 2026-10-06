# app.py - the Streamlit version of Data Detective
# Run:  streamlit run app.py
import time
import streamlit as st
from data import case_settings
from game_logic import average, new_game, find_record, inspect_record, take_action, finish_game

st.set_page_config(page_title="Data Detective", page_icon="🕵️", layout="wide")

# ---------- Session state (created once) ----------
if "page" not in st.session_state:
    st.session_state.page = "home"          # home -> levels -> game
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "level" not in st.session_state:
    st.session_state.level = "Beginner"
if "game_finished" not in st.session_state:
    st.session_state.game_finished = False
if "message" not in st.session_state:
    st.session_state.message = ("info", "Use the buttons next to an employee to inspect or decide.")


# ---------- Button actions (callbacks run once per click) ----------
def go_to_levels():
    name = st.session_state.name_input.strip()
    if name == "":
        st.session_state.name_warning = True
    else:
        st.session_state.name_warning = False
        st.session_state.player_name = name
        st.session_state.page = "levels"


def start_case():
    level = st.session_state.level_choice
    st.session_state.level = level
    st.session_state.game = new_game(level, case_settings)     # a fresh copy of the records
    st.session_state.end_time = time.time() + case_settings[level]["time_limit"]
    st.session_state.game_finished = False
    st.session_state.message = ("info", "Use the buttons next to an employee to inspect or decide.")
    st.session_state.page = "game"


def do_inspect(record_id):
    game = st.session_state.game
    record = find_record(game, record_id)
    hint = inspect_record(game, record)
    if hint is None:
        st.session_state.message = ("error", "No inspections left.")
    else:
        st.session_state.message = ("info", "Hint for " + record["name"] + ": " + hint)


def do_action(action, record_id):
    game = st.session_state.game
    record = find_record(game, record_id)
    points, message = take_action(game, record, action)
    if points > 0:
        st.session_state.message = ("success", message + " +" + str(points) + " points")
    elif points < 0:
        st.session_state.message = ("error", message + " " + str(points) + " points. That was the wrong decision.")
    else:
        st.session_state.message = ("info", message)


def submit_report():
    st.session_state.report = finish_game(st.session_state.game)
    st.session_state.game_finished = True


def return_to_beginning():
    st.session_state.clear()


# ---------- Interface 1: Welcome ----------
def show_home_page():
    st.title("🕵️ Data Detective")
    st.subheader("Bad Data → Wrong Analysis → Wrong Decisions")
    st.write("You are a junior analyst. An employee salary report is about to reach management, "
             "and it hides errors. Find them before it goes out.")
    st.text_input("Enter your name", key="name_input", value=st.session_state.player_name)
    if st.session_state.get("name_warning"):
        st.warning("Please enter your name to start.")
    st.button("START", on_click=go_to_levels, type="primary")


# ---------- Interface 2: Instructions + level selection ----------
def show_level_page():
    st.title("Welcome, " + st.session_state.player_name + " 👋")
    st.write("Inspect employee salaries and identify hidden data problems.")
    st.markdown("**Available actions**\n\n"
                "- 🔍 **Inspect**: get a clue about a record (limited number of inspections)\n"
                "- 🗑️ **Delete**: remove a record (only right for duplicates)\n"
                "- 🔧 **Replace**: replace the salary with the company median\n"
                "- ✅ **Valid**: keep the record as it is\n\n"
                "Careful: unusual salaries (a CEO, an intern) are not always errors.")

    st.subheader("Choose Difficulty")
    names = list(case_settings.keys())
    st.radio("Difficulty", names, key="level_choice", horizontal=True, label_visibility="collapsed",
             index=names.index(st.session_state.level))
    chosen = case_settings[st.session_state.level_choice]
    st.info(chosen["description"] + "\n\n"
            + str(len(chosen["records"])) + " records · " + str(chosen["inspections"]) + " inspections · "
            + str(chosen["time_limit"] // 60) + ":" + str(chosen["time_limit"] % 60).zfill(2) + " minutes")
    st.button("Start Case", on_click=start_case, type="primary")


# ---------- Interface 3: Game ----------
@st.fragment(run_every=1)
def show_timer():
    seconds_left = int(st.session_state.end_time - time.time())
    if seconds_left <= 0 and not st.session_state.game_finished:
        submit_report()
        st.rerun(scope="app")
    seconds_left = max(seconds_left, 0)
    st.metric("Time", str(seconds_left // 60).zfill(2) + ":" + str(seconds_left % 60).zfill(2))


def show_game_page():
    game = st.session_state.game
    left, right = st.columns([1, 3])

    with left:
        st.subheader("CASE " + game["level"].upper())
        st.caption("Detective " + st.session_state.player_name)
        show_timer()
        st.metric("Current Average", format(round(average(game["records"])), ",") + " SAR")
        st.metric("Score", game["score"])
        multiplier = min(game["streak"] + 1, 4)
        st.metric("Streak", "🔥 ×" + str(multiplier))
        st.metric("Inspections", game["inspections"])
        st.button("Submit Report", on_click=submit_report, type="primary")

    with right:
        kind, text = st.session_state.message
        if kind == "success":
            st.success(text)
        elif kind == "error":
            st.error(text)
        else:
            st.info(text)

        header = st.columns([2, 3, 2, 4])
        header[0].markdown("**Name**")
        header[1].markdown("**Job**")
        header[2].markdown("**Salary**")
        header[3].markdown("**Actions**")

        for r in game["records"]:
            row = st.columns([2, 3, 2, 1, 1, 1, 1])
            salary = "None" if r["salary"] is None else format(r["salary"], ",")
            if r["deleted"]:
                row[0].markdown("~~" + r["name"] + "~~")
                row[1].markdown("~~" + r["job"] + "~~")
                row[2].markdown("~~" + salary + "~~")
                row[3].write("Deleted ✅")
            elif r["reviewed"]:
                row[0].write(r["name"])
                row[1].write(r["job"])
                row[2].write(salary)
                row[3].write("Reviewed ✅")
            else:
                row[0].write(r["name"])
                row[1].write(r["job"])
                row[2].write(salary)
                key = str(r["id"])
                row[3].button("🔍", key="inspect_" + key, help="Inspect", on_click=do_inspect, args=(r["id"],),
                              disabled=game["inspections"] == 0)
                row[4].button("🗑️", key="delete_" + key, help="Delete", on_click=do_action, args=("delete", r["id"]))
                row[5].button("🔧", key="replace_" + key, help="Replace with median", on_click=do_action, args=("replace", r["id"]))
                row[6].button("✅", key="valid_" + key, help="Valid", on_click=do_action, args=("valid", r["id"]))


# ---------- Final results ----------
def show_results():
    report = st.session_state.report
    st.title("CASE COMPLETE 🎉")
    st.write("**Player:** " + st.session_state.player_name + "  ·  **Level:** " + report["level"])
    st.header("⭐" * report["stars"] + "☆" * (3 - report["stars"]))

    c1, c2, c3 = st.columns(3)
    c1.metric("Original Average", format(round(report["original_average"]), ",") + " SAR")
    c2.metric("Your Final Average", format(round(report["final_average"]), ",") + " SAR")
    c3.metric("Correct Average", format(round(report["correct_average"]), ",") + " SAR")

    c4, c5, c6 = st.columns(3)
    c4.metric("Accuracy", format(report["accuracy"], ".1f") + "%")
    c5.metric("Score", report["score"])
    c6.metric("Mistakes", report["mistakes"])
    st.write("Right decisions: " + str(report["right"]) + " · Missed errors: " + str(report["missed"]))

    st.subheader("What to improve")
    if len(report["notes"]) == 0:
        st.success("No mistakes. Great work! Try a harder level.")
    else:
        for note in report["notes"]:
            st.write("- " + note)
        weak = ", ".join(k + " (" + str(v) + ")" for k, v in report["weak"].items())
        st.write("**Weak areas:** " + weak)

    st.button("Return to Beginning", on_click=return_to_beginning, type="primary")


# ---------- Main navigation ----------
if st.session_state.game_finished:
    show_results()
elif st.session_state.page == "home":
    show_home_page()
elif st.session_state.page == "levels":
    show_level_page()
else:
    show_game_page()
