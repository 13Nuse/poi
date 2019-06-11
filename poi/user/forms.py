from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import InventoryProfile, EmployeeProfile, ForcastedSalesProfile

# user


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

# Inventory


class EditInventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryProfile
        fields = (
            'category',
            'serving_yield',
            'serving_size',
            'unit',

        )


# Employee

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = (
            'first',
            'last',
            'email',
            'employee_number',
            'pay',
            'phone',
            'active',
        )


# Sales

class EditForcastForm(forms.ModelForm):
    class Meta:
        model = ForcastedSalesProfile
        fields = (
            'date_start',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        )
