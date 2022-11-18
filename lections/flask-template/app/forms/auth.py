from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo

from app.models import User


class LoginForm(FlaskForm):
    user_identifier = StringField("Username or Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired(), Length(6, 30)])
    password_confirmation = PasswordField(
        "Confirm Password", [DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(form, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This username is taken.")

    def validate_email(form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already registered.")


class ProfileForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    submit = SubmitField("Save")


class ForgotPasswordForm(FlaskForm):
    email = StringField("Email Address", [DataRequired(), Email()])
    submit = SubmitField("Reset password")

    def validate_email(form, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError("Not found registered user with this email.")


class PasswordResetForm(FlaskForm):
    password = PasswordField("Password", [DataRequired(), Length(6, 30)])
    password_confirmation = PasswordField(
        "Confirm Password", [DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Save")
