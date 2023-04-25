from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserCreation(UserCreationForm):
    ROLE_CHOICES = [
        ('mentee', 'Mentee'),
        ('mentor', 'Mentor'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        if role == 'mentee':
            user.is_mentee = True
        elif role == 'mentor':
            user.is_mentor = True
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)