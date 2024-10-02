# Flask Password Strength Checker

This project is a **Password Strength Checker** built using the **Flask** web framework. It evaluates password strength using the **zxcvbn** library and provides feedback, warnings, and suggestions to improve the entered password's security.

---

## Features

- **Password Strength Evaluation**: Analyzes the password's strength based on various criteria such as length, variety of characters, and common passwords.
- **zxcvbn Integration**: Leverages the zxcvbn library to provide advanced feedback on password security.
- **Feedback and Suggestions**: Offers detailed feedback to users, including warnings and suggestions to improve password strength.
- **Flask Framework**: Built using the Flask framework to make the project scalable and easier to manage.

---

## Requirements

- Python 3.8+
- Flask
- `zxcvbn-python` library

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/flask-password-strength-checker.git
   cd flask-password-strength-checker
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the `zxcvbn-python` library**:
   - If not in the `requirements.txt`, install it:
   ```bash
   pip install zxcvbn-python
   ```

5. **Prepare the common password list**:
   - Ensure that you have the `Common Pass 10M.txt` file in the project directory to check against common passwords.

---

## Running the Application

1. **Run the Flask development server**:
   ```bash
   flask run
   ```

2. **Access the application**:
   - Open your browser and go to: `http://127.0.0.1:5000`

---

## Project Structure

```
flask-password-strength-checker/
├── app/
│   ├── __init__.py          # Flask application initialization
│   ├── routes.py            # Application routes and logic
│   └── templates/
│       └── index.html       # HTML for password input and display
├── static/
│   └── styles.css           # CSS for styling
├── Common Pass 10M.txt       # Common password list
├── requirements.txt          # Python dependencies
├── run.py                    # Entry point for the application
└── README.md                 # Project readme
```

---

## Usage

1. **Enter a Password**: Users enter a password on the home page to check its strength.
2. **Check Strength**: The server processes the password using the `zxcvbn` library and returns feedback.
3. **Feedback**: The feedback will include warnings, suggestions, and the estimated time it would take to crack the password.

---

## Example Output

- **Feedback**: Password is too common, consider using a unique one.
- **Suggestions**: Add more characters, symbols, or numbers.
- **Time to Crack**: 20 years (depending on password complexity).

---

## Future Updates

### Next.js Integration

In the future, the frontend of this project will be migrated to **Next.js** for a modern, single-page experience.

- **Why Next.js?**
  - **Improved UI/UX**: With React, users will get real-time password strength updates without needing to reload the page.
  - **SSG and SSR**: Next.js will provide a fast and SEO-friendly application.

- **Planned Features**:
  - Full React-based UI.
  - Real-time password feedback with Next.js components.

---

## Contributing

Feel free to contribute! If you find any bugs or want to add features, open an issue or submit a pull request.

---

## License

This project is licensed under the **MIT License**.

---

## Notes

- **Current version**: Flask-based Password Strength Checker.
- **Upcoming updates**: Next.js version for better user experience and performance.

---
