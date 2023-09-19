from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, SelectField,HiddenField
from wtforms.validators import DataRequired, EqualTo, Length,Email,Optional
from libraries.import_export_data_objects import import_export_data as Import_Export_Data
from libraries.data_objects import data_objects as do

# Set your classes here.

class state_county_selection_form(Form):
    mdo = do()
    state_list      = SelectField('state_list',choices=mdo.state_names_tuple())
    county_list     = SelectField('county_list')
    state           = HiddenField("state")
    county          = HiddenField("county")
    county_or_msa   = HiddenField("county_or_msa")
 

class monthly_allocation_form(Form):
    mdo = do()
    #monthly allocation, interest rate, downpayment
    #print(mdo.monthly_allocation_tuple())
    monthly_allocation = SelectField('monthly_allocation',choices=mdo.monthly_allocation_tuple())
    interest_rates = SelectField('interest_rates',choices=mdo.interest_rate_tuple())
    downpayment_amt = SelectField('downpayment_amt',choices=mdo.down_payment_tuple())
    loan_term  = SelectField('downpayment_amt',choices=mdo.loan_term_tuple())
    current_monthly_allocation = HiddenField("current_monthly_allocation")
    current_interest_rate = HiddenField("current_interest_rate")
    current_downpayent_amt = HiddenField("current_downpayent_amt")
    current_loan_term = HiddenField("current_loan_term")
    



class email_form(Form):

    first_name = TextField(
        'first_name', validators=[DataRequired(message="First name required"), Length(min=3, max=25)]
    )
    email_address = TextField(
        'email_address', validators=[Email(message="Please enter a valid email address"), Length(min=6, max=60),DataRequired()]
        # email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
        #email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    )
    message_text = TextField(
        'message_text', validators=[DataRequired(message="Please enter a text message."), Length(min=4, max=600)]
    )


# class CountryDetailVisualizationForm(Form):
#     my_data = Import_Export_Data()

#     source_country = SelectField('source_country',choices=my_data.get_distinct_country_tuples())
#     target_country = SelectField('target_country',choices=my_data.get_distinct_country_tuples())
#     current_source_country = HiddenField("current_source_country")
#     current_target_country = HiddenField("current_target_country")


# class CountryToWorldVisualizationForm(Form):
#     my_data = Import_Export_Data()

#     source_country = SelectField('source_country',choices=my_data.get_distinct_country_tuples())
#     current_source_country = HiddenField("current_source_country")

# class CountryToWorldVisualizationFormWithWorld(Form):
#     my_data = Import_Export_Data()

#     target_country = SelectField('target_country',choices=my_data.get_distinct_country_tuples(add_world=True))
#     source_country = HiddenField("source_country")
#     current_target_country = HiddenField("current_target_country")

# class CountryVisualizationFormWithDirection(Form):
#     my_data = Import_Export_Data()

#     target_country = SelectField('target_country',choices=my_data.get_distinct_country_tuples(add_world=True))
#     source_country = SelectField('source_country',choices=my_data.get_distinct_country_tuples(add_world=True))
#     direction = SelectField('direction')
#     current_source_country = HiddenField("current_source_country")
#     current_target_country = HiddenField("current_target_country")
#     current_direction = SelectField('current_direction')


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )

class sign_up_form(Form):

    first_name = TextField(
        'first_name', validators=[DataRequired(message="First name requrired"), Length(min=6, max=25)]
    )
    last_name = TextField(
        'last_name', validators=[DataRequired(message="Last name required"), Length(min=6, max=25)]
    )
    email_address = TextField(
        'email_address', validators=[Email(message="Please enter a valid email address"), Length(min=6, max=60)]
    )
    address_1 = TextField(
        'address_1', validators=[DataRequired(message="Please enter an address"), Length(min=6, max=60)]
    )
    address_2 = TextField(
        'address_2', validators=[Optional(), Length(min=6, max=60)]
    )
    address_3 = TextField(
        'address_3', validators=[Optional(), Length(min=6, max=60)]
    )
    city = TextField(
        'city', validators=[DataRequired(message="Please enter a valid City."), Length(min=6, max=60)]
    )
    state = TextField(
        'state', validators=[DataRequired(message="Please enter a valid State."), Length(min=6, max=60)]
    )
    country = TextField(
        'country', validators=[DataRequired(message="Please enter a valid country"), Length(min=6, max=60)]
    )
    postal_code = TextField(
        'postal_code', validators=[DataRequired(message="Please enter a valid postal code"), Length(min=6, max=60)]
    )
    recaptcha = RecaptchaField()


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
