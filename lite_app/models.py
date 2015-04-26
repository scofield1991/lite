from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
# Create your models here.
class UserProfile(models.Model):

    user=models.OneToOneField(User)

    phone_regex= RegexValidator(regex=r'\b\d{3}-\d{7}\b', message="Phone number must be entered in the format: '000-0000000'.")
    phone_number= models.CharField(validators=[phone_regex], blank=True, max_length=11)
    picture= models.ImageField(upload_to='profile_images', blank=True)
    birthday= models.DateField()
    captcha= CaptchaField()
    
    def __str__(self):
        return self.user.username
    
    
