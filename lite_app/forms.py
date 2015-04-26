from django import forms
from django.contrib.auth.models import User
from lite_app.models import UserProfile
from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=16)
    email=forms.EmailField()
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField()
    class Meta:
        model = User
        fields= ('first_name','last_name', 'username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    birthday=forms.DateField(input_formats=['%Y-%m-%d'])
    captcha=CaptchaField()
    phone_number=forms.CharField( )
    class Meta:
        model = UserProfile
        fields=('phone_number', 'picture', 'birthday')
        
class UserFormChange(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=16, required=False)
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()

        
class UserProfileFormChange(forms.Form):
    birthday=forms.DateField(input_formats=['%Y-%m-%d'])
    phone_number=forms.CharField()
    picture=forms.ImageField(required=False)

