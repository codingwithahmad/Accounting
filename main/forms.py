from django import forms
from .models import Sabt, Category
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class SabtForm(forms.ModelForm):
    cats = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = Sabt
        fields = ['title', 'income', 'spending', 'date', 'cats']
        widgets= {
            'date': DateTimePickerInput(),
        }
