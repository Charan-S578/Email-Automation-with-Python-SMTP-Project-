# Email Automation with Python (SMTP Project)

This Python project demonstrates how to send emails automatically using the `smtplib` library. It includes basic email sending and a scheduled motivational email system that sends random quotes based on the day of the week using the `datetime` module.

---

## 📌 Features

- Send emails using Gmail SMTP server
- Secure login using app passwords
- Send custom subject and message
- Automated motivational email system
- Random quote selection from file
- Day-based scheduling using datetime

---

## 🛠 Technologies Used

- Python 3
- smtplib
- datetime module
- random module

---

## 📂 Project Structure

```text
Project/
│
├── main.py
├── quotes.txt
└── README.md


▶️ How It Works
Connects to Gmail SMTP server.
Logs in using email credentials.
Sends a test email or motivational quote.
On a specific weekday, selects a random quote.
Sends the quote as an email automatically.


⚠️ Security Note
Use App Passwords instead of real Gmail passwords.
Do NOT hardcode sensitive credentials in production.


🚀 How to Run
python main.py
