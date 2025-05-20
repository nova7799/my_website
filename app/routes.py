from flask import render_template, request, redirect, flash
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()



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


        app = Flask(__name__)
    # Make sure you configure a secret key for session/flash messages
    app.config['SECRET_KEY'] = '777525551fc7ce2f9d2f49fd487830820aa4741884f090af502d37b1f3f32465'

    # Configure your email credentials (set these as environment variables in production!)
    email_user = 'curtainsforyouofficial@gmail.com'
    email_pass = 'vbmadmfidacrlpyu'

    @app.route('/help')
    def help_page():
        return render_template('help.html')

    @app.route('/ask_question', methods=['POST'])
    def ask_question():
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        question = request.form.get('question')

        # Compose the email
        msg = EmailMessage()
        msg['Subject'] = f"Website Question from {name}"
        msg['From'] = email_user
        msg['To'] = 'velfanova143@gmail.com'

        # Plain-text content
        msg.set_content(
            f"Hello,\n\n"
            f"You've received a new question from your website:\n\n"
            f"From: {name} <{email}>\n\n"
            f"Question:\n{question}\n\n"
            "Regards,\nCurtains For You Website Bot"
        )

        # HTML content
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

        # Send the email
        try:
            # Primary: SSL
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as smtp:
                smtp.login(email_user, email_pass)
                smtp.send_message(msg)
            flash('Message sent successfully!', 'success')
        except Exception:
            try:
                # Fallback: TLS
                with smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as smtp:
                    smtp.starttls()
                    smtp.login(email_user, email_pass)
                    smtp.send_message(msg)
                flash('Message sent successfully!', 'success')
            except Exception as e:
                print(f"EMAIL ERROR DETAILS: {type(e).__name__}: {e}")
                flash('Failed to send message. Please contact us directly.', 'danger')

        return redirect('/help')

    if __name__ == '__main__':
        app.run(debug=True)

