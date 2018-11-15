from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    #fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your full name","id":form_full_name}))
    email = forms.EmailField()

    # Gives us nested namespace for configurations in one place
    # The model that will be affected is the User model.. form.save() will be saved to this User model

    class Meta:
        model = User
        # What fields to show and in which order
        fields = ['username', 'email', 'password1', 'password2']

# Model forms

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
