from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate

# Create your forms here.

#user creation form
class UserCreation(UserCreationForm):
    username = forms.CharField(max_length=30, )
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    ROLE_CHOICES = [
        ('mentee', 'Mentee'),
        ('mentor', 'Mentor'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        #to check if password is not empty and passwords match each other
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        #to check if password is at least 8 characters
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        
        if password1 and password2.isdigit():
            raise forms.ValidationError("Password must contain at least one letter")
        
        #to check if password is too common
        common_passwords = ['password', '123456', '12345678', '12345', '123456789', 'qwerty', 'abc123', 'football', 'monkey', 'letmein', '111111', 'mustang', 'access', 'shadow', 'master', 'michael', 'superman', '696969', '123123', 'batman']
        if password1 in common_passwords:
            raise forms.ValidationError("Password is too common")
        
        #to check if password is too similar to other personal information
        user_inputs = [self.cleaned_data.get('username'), self.cleaned_data.get('first_name'), self.cleaned_data.get('last_name'), self.cleaned_data.get('email')]
        for user_input in user_inputs:
            if user_input and password1 in user_input:
                raise forms.ValidationError("Your password cannot be too similar to your other personal information.")
        return password2
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    # save def clean_username
    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        user.is_mentee = False
        user.is_mentor = False
        if role == 'mentee':
            user.is_mentee = True
        elif role == 'mentor':
            user.is_mentor = True
        if commit:
            user.save()
        return user
    

#login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid login")
            if not user.is_active:
                raise forms.ValidationError("Disabled account")

        return cleaned_data