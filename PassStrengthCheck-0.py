# One of the basic password strength checker as 0th project in cybersecurity path
# Used most advanced password strength checker library zxcvbn

import re
import getpass
import zxcvbn
import json
from decimal import Decimal
from datetime import timedelta

def pass_strg(password):
    score = 0

    # check iff password in common password list
    with open("Common Pass 10M.txt", "r") as file:
        for line in file:
            if password == line.strip():
                print("Password is in Common list, Please choose another password for your account.")
                exit()

        score += 1

    # password length check 
    if len(password) < 8:
        score += 0
        print("Password is weak")
        exit()
    elif (len(password) < 12 and len(password) >= 8):
        score += 1
    elif (len(password) >= 14):
        score += 2
    
    # password character check
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[$#@]', password):
        score += 1

    # password strength check
    if score < 3:
        print("Password is weak", score, "/7") 
    elif score < 5:
        print("Password is medium", score, "/7")
    else:
        print("Password is strong", score, "/7")


def json_frmtting(obj):
    if isinstance(obj, Decimal):
        return float(obj)  
    if isinstance(obj, timedelta):
        return str(obj)  
    raise TypeError(f"Type {type(obj)} not serializable")


password = getpass.getpass("Enter your password: ")
result = zxcvbn.zxcvbn(password)
result_str = json.dumps(result, default=json_frmtting)
results = json.loads(result_str)
feedback = results["feedback"]["warning"] or "No warnings"
suggests = results["feedback"]["suggestions"] or ["No suggestions"]
exploit_time = results["crack_times_display"]["online_throttling_100_per_hour"]
form_output = f"{{feedback: {feedback}, suggestions: {', '.join(suggests)}, time_to_crack: {exploit_time}}}"
print(form_output, "\n")
print("Password strength score:", results['score'],"(Out of 4)",'\n')
pass_strg(password)
del password

# Output:
# Enter your password:
# {feedback: No warnings, suggestions: No suggestions, time_to_crack: centuries}
# Password strength score: 4 (Out of 4)


# Currently working on the project to make it more user-friendly and interactive
# Also working on the project to make it more secure and efficient
# Also will add an ML model to check password related to the user's data or not and then rate the password
# Also will add a feature to check the password strength in real-time
# Also will add a feature to check the password strength in the background

