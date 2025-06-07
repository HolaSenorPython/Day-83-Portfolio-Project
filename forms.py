from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

# Contact Me Form!
class ContactForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    name = StringField(label="Your Name!", validators=[DataRequired()])
    message = StringField(label="Your Message!", validators=[DataRequired()])
    send_msg = SubmitField("Send Message!😁")