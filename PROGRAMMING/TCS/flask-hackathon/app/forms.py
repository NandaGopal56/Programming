from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField
from wtforms.validators import DataRequired,Length , ValidationError

class RegistrationForm(FlaskForm):

    name = StringField('name',validators=[DataRequired(),Length(min=3,max=25)])
    contact = StringField('contact',validators=[DataRequired()])
    number = StringField('number',validators=[DataRequired()])
    address = StringField('address',validators=[DataRequired()])
    bloodgroup = StringField('blood group',validators=[DataRequired()])
    dob = StringField('date of birth',validators=[DataRequired()])
    age = StringField('age',validators=[DataRequired()])
    ioe_name = StringField('ioe name',validators=[DataRequired()])
    ioe_contact = StringField('ioe contact',validators=[DataRequired()])
    ioe_number = StringField('ioe number',validators=[DataRequired()])
    ioe_relation = StringField('ioe relation',validators=[DataRequired()])
    password = PasswordField('password')

    submit = SubmitField('Submit')

    

class DetailsForm(FlaskForm):
    donor_name = StringField('donor name')
    location = StringField('location')
    contact = StringField('contact')
    blood_group = StringField('blood group')
    relation = StringField('relation')

class searchform(FlaskForm):
    bbid = StringField('enter bbid')
    bloodgroup = StringField('blood group')
    submit = SubmitField('Submit')