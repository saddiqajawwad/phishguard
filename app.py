from flask import Flask, render_template, request, redirect, url_for, session
from questions import QUESTIONS

app = Flask(__name__)


# Secret key is required for session (score + progress).

app.secret_key = "phishguard_secret_key_2026"


def reset_quiz():
    """Reset quiz progress in session."""
    session["current_index"] = 0
    session["score"] = 0


def get_current_question():
    """Return the current question based on session index."""
    index = session.get("current_index", 0)

    if index < 0:
        index = 0

    if index >= len(QUESTIONS):
        return None

    return QUESTIONS[index]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start():
    reset_quiz()
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    question = get_current_question()

    # If no question is left, go to result page
    if question is None:
        return redirect(url_for("result"))

    # If user submitted an answer
    if request.method == "POST":
        user_answer = request.form.get("answer")

        # Basic validation (prevents empty submission)
        if user_answer not in ["legit", "phishing"]:
            return redirect(url_for("quiz"))

        # Check correctness
        correct = (user_answer == question["correct_answer"])

        # Update score
        if correct:
            session["score"] = session.get("score", 0) + 1

        # Store feedback data in session
        session["last_feedback"] = {
            "question_type": question["type"],
            "scenario": question["scenario"],
            "extra": question["extra"],
            "user_answer": user_answer,
            "correct_answer": question["correct_answer"],
            "correct": correct,
            "explanation": question["explanation"],
            "red_flags": question["red_flags"]
        }

        # Move to next question
        session["current_index"] = session.get("current_index", 0) + 1

        return redirect(url_for("feedback"))

    # GET request (show question)
    current_index = session.get("current_index", 0)
    total_questions = len(QUESTIONS)

    return render_template(
        "quiz.html",
        question=question,
        current_index=current_index,
        total_questions=total_questions
    )


@app.route("/feedback")
def feedback():
    feedback_data = session.get("last_feedback")

    # If user directly opens feedback without playing
    if not feedback_data:
        return redirect(url_for("index"))

    current_index = session.get("current_index", 0)
    total_questions = len(QUESTIONS)

    return render_template(
        "feedback.html",
        feedback=feedback_data,
        current_index=current_index,
        total_questions=total_questions
    )


@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(QUESTIONS)

    percentage = int((score / total) * 100)

    # Safety level (simple and understandable)
    if percentage <= 40:
        level = "Beginner"
        message = "You need more practice. Phishing can easily trick you."
    elif percentage <= 75:
        level = "Safe User"
        message = "Good job! You can spot many scams, but stay alert."
    else:
        level = "Pro Defender"
        message = "Excellent! You are highly aware of phishing techniques."

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage,
        level=level,
        message=message
    )


@app.route("/restart")
def restart():
    reset_quiz()
    return redirect(url_for("quiz"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)