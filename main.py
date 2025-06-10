from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
from forms import ContactForm
from flask_bootstrap import Bootstrap5
import smtplib
import os
from email.message import EmailMessage
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
bootstrap = Bootstrap5(app)

# Def the send email function, which will send emails lol (GOES WITH CONTACT FORM)
def send_email(name, email, message):
    my_email = os.environ.get('MY_EMAIL_FOR_USER')
    my_pass = os.environ.get('MY_PASS_FOR_USER')
    users_name = name
    users_email = email
    users_message = message

    # MAKE EMAIL MESSAGE OBJECT!
    msg = EmailMessage()
    msg["Subject"] = f"You've received a contact form message from {users_name}!"
    msg["From"] = my_email
    msg["To"] = my_email
    msg["Reply-To"] = users_email # REPLIES GO TO THEM, NOT ME!

    # Make body
    body = f"""\
Name: {users_name}
Email: {users_email}
Location: Portfolio Website

Message: {users_message}
"""
    msg.set_content(body, charset='utf-8')

    # Let's try sending the email, if it doesn't work then ye lol
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.send_message(msg=msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact-me', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    email_sent = None
    if form.validate_on_submit(): # IF A POST REQUEST IS MADE
        user_name = form.name.data
        user_email = form.email.data
        user_msg = form.message.data
        email_sent = send_email(user_name, user_email, user_msg)
        if email_sent:
            flash("Your email was sent successfully! ✅")
        else:
            flash("Oops! Something went wrong while sending your message. 😿")
        return redirect(url_for('contact', email_sent=email_sent))

    # Capture the email sent parameter
    email_sent_param = request.args.get('email_sent')
    if email_sent_param == 'True':
        email_sent = True
    elif email_sent_param == 'False':
        email_sent = False

    return render_template('contact.html', form=form, email_sent=email_sent)

@app.route('/elisha-portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port)
