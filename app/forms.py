from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class City_Form(FlaskForm):
    city_form = StringField( 'City' , validators=[DataRequired()])
    submit_form = SubmitField('Search')

