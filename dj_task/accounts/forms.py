from django import forms
from accounts.models import CustomUser
from django.forms.extras.widgets import SelectDateWidget


BASE_YEARS = range(1900,2100)


class AddUserForm(forms.ModelForm):

    class Meta:
        verbose_name = 'User'
        model = CustomUser
        fields = ('username', 'birthday',)
        widgets = {
            'birthday': SelectDateWidget(years=BASE_YEARS),
        }