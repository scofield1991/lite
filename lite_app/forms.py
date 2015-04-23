from django import forms
from django.contrib.auth.models import User
from lite_app.models import UserProfile
from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=16)
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    class Meta:
        model = User
        fields= ('first_name','last_name', 'username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    birthday=forms.DateField(input_formats=['%Y-%m-%d'])
    captcha=CaptchaField()
    class Meta:
        model = UserProfile
        fields=('phone_number', 'picture', 'birthday')
        
class UserFormChange(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=16, required=False)
    email=forms.EmailField(required=False)
    first_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)
    class Meta:
        model = User
        fields= ('first_name','last_name', 'username', 'email', 'password')
        
class UserProfileFormChange(forms.ModelForm):
    birthday=forms.DateField(input_formats=['%Y-%m-%d'],required=False)
    captcha=CaptchaField(required=False)
    phone_number=CaptchaField(required=False)
    class Meta:
        model = UserProfile
        fields=('phone_number', 'picture', 'birthday')
