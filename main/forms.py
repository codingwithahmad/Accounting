from django import forms
from .models import Sabt
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class SabtForm(forms.ModelForm):


    class Meta:
        model = Sabt
        fields = ['title', 'income', 'spending', 'date']
        widgets= {
            'date': DateTimePickerInput(),
        }
