from django import forms
from django.contrib.auth.models import User
from lite_app.models import UserProfile

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=16)
    
    class Meta:
        model = User
        fields= ('first_name','last_name', 'username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('phone_number', 'picture', 'birthday')
