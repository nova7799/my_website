<<<<<<< HEAD
# from app.routes import app
from app import app
if __name__ == '__main__':
    app.run(debug=True)
    # In run.py (when project.env is in same directory)
load_dotenv('project.env')
=======

# from app import app
# if __name__ == '__main__':
#     app.run(debug=True)
#     # In run.py (when project.env is in same directory)
# load_dotenv('project.env')
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 9a5e7ae3bf8d5382f1a7c4ff1d5c230cbb09ec86


# from flask import Flask, render_template, request, redirect, flash
# import smtplib
# from email.message import EmailMessage

# app = Flask(__name__)
# app.secret_key = 'pzih sgrn xfxk dveq'

# @app.route("/help")
# def help_page():
#     return render_template("help.html")

# @app.route("/ask_question", methods=["POST"])
# def ask_question():
#     name = request.form["name"]
#     email = request.form["email"]
#     question = request.form["question"]

#     msg = EmailMessage()
#     msg.set_content(f"New question from {name} ({email}):\n\n{question}")
#     msg["Subject"] = "New Customer Question - Curtains For You"
#     msg["From"] = "yourcompany@example.com"
#     msg["To"] = "velfanova143@gmail.com"  # Your real email

#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#             smtp.login("yourcompany@example.com", "pzih sgrn xfxk dveq")
#             smtp.send_message(msg)
#         flash("Your question has been submitted successfully!", "success")
#     except Exception as e:
#         flash("Error sending your message. Please try again later.", "danger")
#         print("Email error:", e)

#     return redirect("/help")

# if __name__ == "__main__":
#     app.run(debug=True)

