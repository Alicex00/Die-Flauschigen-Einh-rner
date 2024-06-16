from flask_wtf import FlaskForm #automatically transforms python code to an html form
from flask_wtf.file import FileField, FileAllowed #allows forms with file upload
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from chat.models import User, Reaction

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

#form for user registration
class SignUpForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)]) #DataRequired means it can't be empty
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    confirm_password = PasswordField('Passwort wiederholen', validators=[DataRequired(), EqualTo('password')]) #equal_to doesn't work?
    submit = SubmitField('Sign-Up')

    #custom validators so username and email being unique is checked on validation
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Benutzername bereits vergeben, bitte einen anderen wählen.')
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('E-Mail bereits vergeben. Passwort vergessen?')

#form for user login
class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Einloggen')

#form for profile update
class UpdateProfileForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)]) #DataRequired means it can't be empty
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    picture = FileField('Profilbild anpassen', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Speichern')

    #custom validators so username and email being unique is checked on validation
    def validate_username(self, username):
        if username.data != current_user.username: #if username wasn't changed it doesn't need to be validated
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Benutzername bereits vergeben, bitte einen anderen wählen.')
            
    def validate_email(self, email):
        if email.data != current_user.email: #if email wasn't changed it doesn't need to be validated
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('E-Mail bereits vergeben. Passwort vergessen?')

#form for password reset request
class RequestResetForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Passwort zurücksetzen')
     
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first() #if email exists in our db user will get reset email, for security reasons we don't tell the user if the email is registered

#form for resetting password  
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Passwort', validators=[DataRequired()])
    confirm_password = PasswordField('Passwort wiederholen', validators=[DataRequired(), EqualTo('password')]) #equal_to doesn't work?
    submit = SubmitField('Zurücksetzen')

#form for searching
class SearchForm(FlaskForm):
  search = StringField('Seite durchsuchen', validators=[DataRequired()])
  submit = SubmitField('Suchen')

#form for posting
class PostForm(FlaskForm):
    title = StringField('Titel', validators=[DataRequired()])
    content = TextAreaField('Inhalt', validators=[DataRequired()])
    submit = SubmitField('Speichern')

#form for bewertung (stern)
class ReactionForm(FlaskForm):
    user_reaction = SelectField('Bewerten:', validators=[InputRequired()])
