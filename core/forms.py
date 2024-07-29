from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from core.models import CustomUser, Car


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CarPricePredictionForm(ModelForm):

    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'version', 'year', 'mileage', 'displacement', 'power', 'fuel_type',
            'gearbox', 'propulsion', 'color', 'is_accident_free', 'condition',
        ]

