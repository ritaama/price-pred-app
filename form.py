from flask_wtf import FlaskForm
from wtforms import IntegerField,DecimalField,SubmitField
from wtforms.validators import DataRequired


class prediction(FlaskForm):
    bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    sqft_living = DecimalField('sqft_living',validators=[DataRequired()])
    sqft_lot = DecimalField('sqft_lot',validators=[DataRequired()]) 
    floors = IntegerField('Floor',validators=[DataRequired()])
    sqft_above = DecimalField('sqft_above',validators=[DataRequired()])
    sqft_lot15 = DecimalField('sqft_lot15',validators=[DataRequired()])
    yr_built = IntegerField('yr_built',validators=[DataRequired()])
    condition = IntegerField('condition',validators=[DataRequired()])
    zipcode = IntegerField('zipcode',validators=[DataRequired()])
    submit = SubmitField('Submit')
