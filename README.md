# PhishGuard – Cybersecurity Awareness Simulator

**PhishGuard** is an interactive web application built using **Python Flask** that helps users identify phishing emails and other online threats.  
It simulates real-life scenarios, allowing users to practice distinguishing between safe (legitimate) messages and phishing attempts, while providing immediate feedback to enhance cybersecurity awareness.  

## Features
- Interactive Quiz: Users answer multiple phishing scenarios one at a time.  
- Instant Feedback: Each question shows explanation and red flags after submission.  
- Scoring & Badge System: Tracks user score and awareness level.  
- Cybersecurity-themed UI: Engaging, user-friendly interface designed for learning.  
- Expandable Questions: Questions are stored in a separate Python file for easy editing.  

## Project Structure
PhishGuard/  
- **app.py** – Main Flask application file  
- **questions.py** – Stores all phishing scenarios and answers  
- **requirements.txt** – List of dependencies (Flask)  
- **templates/** – HTML templates for each page  
  - **index.html** – Home page  
  - **quiz.html** – Quiz page  
  - **feedback.html** – Feedback after each question  
  - **result.html** – Final result page  
- **static/** – CSS & JS files for UI  
  - **style.css** – Styles for cyber-themed UI  
  - **script.js** – Optional JS for button effects and interactivity  

## Tech Stack
- **Backend:** Python 3 + Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Session Handling:** Flask `session` stores score and progress  

## Installation & Running Locally

Step 1 – Clone the repository
Replace 'YourUsername' with your GitHub username:
git clone https://github.com/YourUsername/PhishGuard.git
cd PhishGuard

Step 2 – Install dependencies
pip install -r requirements.txt
(This will install Flask and any other required packages.)

Step 3 – Run the application
python app.py
(This starts the Flask server on default port 5000.)
You should see something like:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Step 4 – Open in browser
Open your browser and go to:
http://127.0.0.1:5000
This will show the home page.

Step 5 – Use the app
- Home Page: Click “Start Quiz”
- Quiz Page: Answer each question as Phishing or Legit
- Feedback Page: See explanation and red flags after each answer
- Result Page: View your total score and awareness badge

Notes:
- Questions are stored in questions.py – you can edit or add new scenarios.
- CSS and JS enhance user experience but all core logic runs on Flask backend.
- Designed for educational purposes and safe cybersecurity practice.
