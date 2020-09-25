'''
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CreateRecord(forms.Form):
    first_name = forms.CharField(max_length=20, help_text="Enter forname", required=True)
    last_name = forms.CharField(max_length=20, help_text="Enter surname", required=True)
    location = forms.CharField(max_length=20, help_text="Enter location", required=True)
    age = forms.IntegerField(help_text="Enter Age", required=True)
    shoe_size = forms.IntegerField(help_text="Enter Shoe Size", required=True)

    def clean_age(self):
        data = self.cleaned_data["age"]

        if age < 0:
            raise ValidationError(_("Invalid age - Age must be positive"))

        return data
'''

from django.forms import ModelForm
from users.models import UserModel

# Create the form class.
class CreateRecord(ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'age', 'location', 'shoe_size']