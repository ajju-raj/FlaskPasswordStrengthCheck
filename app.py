from flask import Flask, render_template, request, jsonify
import re
import zxcvbn
import json
from decimal import Decimal
from datetime import timedelta

app = Flask(__name__)

# Function to handle non-serializable types
def json_frmtting(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, timedelta):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")


# Function to check password strength
def pass_strg(password):
    score = 0

    # Check if password is in common password list
    with open("D:\\Projects On the Go\\flask-password-strength-checker\\Common Pass 10M.txt", "r") as file:
        for line in file:
            if password == line.strip():
                return {"status": "error", "message": "Password is in the common list, change to another."}

    score += 1

    # Password length check
    if len(password) < 8:
        return {"status": "weak", "message": "Password is too short, less than 8 characters."}
    elif 8 <= len(password) < 12:
        score += 1
    elif len(password) >= 16:
        score += 2

    # Character variety check
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[$#@]', password):
        score += 1

    # Determine strength
    if score < 3:
        return {"status": "weak", "score": score, "message": "Password is weak"}, {"score": score}
    elif score < 5:
        return {"status": "medium", "score": score, "message": "Password is medium"}, {"score": score}
    else:
        return {"status": "strong", "score": score, "message": "Password is strong"}, {"score": score}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check-password', methods=['POST'])
def check_password():
    password = request.form['password']

    # Using zxcvbn to analyze password
    result = zxcvbn.zxcvbn(password)
    result_str = json.dumps(result, default=json_frmtting)
    results = json.loads(result_str)

    feedback = results["feedback"]["warning"] or "No warnings"
    suggests = results["feedback"]["suggestions"] or ["No suggestions"]
    exploit_time = results["crack_times_display"]["online_throttling_100_per_hour"]

    password_strength = pass_strg(password)
    
    return jsonify({
        "feedback": feedback,
        "suggestions": suggests,
        "time_to_crack": exploit_time,
        "strength": password_strength
    })

    del password

if __name__ == '__main__':
    app.run(debug=True)
