from flask import render_template, request, redirect, flash
import smtplib
import os
from email.message import EmailMessage

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/services')
    def services():
        return render_template('services.html')

    @app.route('/gallery')
    def gallery():
        return render_template('gallery.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/whatsapp')
    def whatsapp():
        return render_template('whatsapp.html')  # Make sure this file exists

    @app.route('/help')
    def help_page():
        return render_template('help.html')

    @app.route('/ask_question', methods=['POST'])
    def ask_question():
        name = request.form.get("name")
        email = request.form.get("email")
        question = request.form.get("question")

        try:
            # Explicitly get env variables
            email_user = os.environ.get("EMAIL_USER")
            email_pass = os.environ.get("EMAIL_PASS")

            if not all([email_user, email_pass]):
                raise ValueError("Missing email credentials")

            msg = EmailMessage()
            msg.set_content(
                f"Hello,\n\n"
                f"You've received a new question from your website:\n\n"
                f"From: {name} <{email}>\n\n"
                f"Question:\n{question}\n\n"
                "Regards,\nCurtains For You Website Bot"
            )

            # HTML version (better formatting for most email clients)
            msg.add_alternative(f"""
            <html>
            <body>
                <p>Hello,<br><br>
                You've received a new question from your website:<br><br>
                <strong>From:</strong> {name} &lt;{email}&gt;<br><br>
                <strong>Question:</strong><br>
                {question}<br><br>
                Regards,<br>
                <em>Curtains For You Website Bot</em>
                </p>
            </body>
            </html>
            """, subtype='html')

            # Email headers
            msg["Subject"] = f"Website Question from {name}"
            msg["From"] = email_user
            msg["To"] = "velfanova143@gmail.com"  # Replace with your email address


            # Try both common SMTP configurations
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as smtp:
                    smtp.login(email_user, email_pass)
                    smtp.send_message(msg)
            except:
                with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as smtp:
                    smtp.starttls()
                    smtp.login(email_user, email_pass)
                    smtp.send_message(msg)

            flash("Message sent successfully!", "success")

        except Exception as e:
            print(f"EMAIL ERROR DETAILS: {type(e).__name__}: {str(e)}")
            flash("Failed to send message. Please contact us directly.", "danger")

        return redirect("/help")


