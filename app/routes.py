from flask import Blueprint, render_template, request, redirect, flash
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Define the Blueprint
routes = Blueprint('routes', __name__)

# Email credentials
email_user = os.getenv('EMAIL_USER')
email_pass = os.getenv('EMAIL_PASS')

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/services')
def services():
    return render_template('services.html')

@routes.route('/gallery')
def gallery():
    return render_template('gallery.html')

@routes.route('/contact')
def contact():
    return render_template('contact.html')

@routes.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@routes.route('/help')
def help():
    return render_template('help.html')

@routes.route('/ask_question', methods=['POST'])
def ask_question():
    name = request.form.get('name')
    email = request.form.get('email')
    question = request.form.get('question')

    msg = EmailMessage()
    msg['Subject'] = f"Website Question from {name}"
    msg['From'] = email_user
    msg['To'] = 'velfanova143@gmail.com'

    msg.set_content(
        f"From: {name} <{email}>\n\nQuestion:\n{question}"
    )
    msg.add_alternative(f"""
        <html><body>
        <p><strong>From:</strong> {name} &lt;{email}&gt;<br>
        <strong>Question:</strong><br>{question}</p>
        </body></html>
    """, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as smtp:
            smtp.login(email_user, email_pass)
            smtp.send_message(msg)
        flash('Message sent successfully!', 'success')
    except Exception:
        try:
            with smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as smtp:
                smtp.starttls()
                smtp.login(email_user, email_pass)
                smtp.send_message(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(f"EMAIL ERROR DETAILS: {type(e).__name__}: {e}")
            flash('Failed to send message. Please contact us directly.', 'danger')

    return redirect('/help')
