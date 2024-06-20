from django import forms
# from datetime import datetime
from .models import Form

class Formapi(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    # comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    url = forms.URLField(label="Your website", required=False)
   
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))

    value = forms.DecimalField()
    message = forms.CharField(max_length = 10)
    email_address = forms.EmailField( 
    label="Please enter your email address")
    first_name = forms.CharField(initial='Your name')
    # agree = forms.BooleanField(initial=True)
    # day = forms.DateField(initial=forms.datetime.date.today)
    
    CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    
    colors = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple)

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)


    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 



class ModelForm(forms.ModelForm):
    class Meta:
        model  = Form
        fields = '__all__'