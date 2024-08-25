from django.core.mail import send_mail
from django.conf import settings
import random
import string
from .models import Account

def sending_email(email, Message):
    account = Account.objects.get(email = email)
    subject = '''To Activate Your Account'''
    
    message = Message
    
    from_email = settings.EMAIL_HOST_USER
    
    send_mail(subject, message, from_email, [email])
    
def random_code():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return random_string