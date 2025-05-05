from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from accounts.models import User
from accounts.service import send_email_thread


@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    if created:
        send_email_thread(
            subject='User created',
            message=f"""
    
            <p>Username: {instance.username}</p>
            <p>First name: {instance.first_name}</p>
            <p>Last name: {instance.last_name}</p>
            <p>Email: {instance.email}</p>
            <p>Balance: {instance.balance}</p>
            
            link: <a href="http://127.0.0.1:8000/accounts/login/">login</a> 
            """,
            to_email='giyosoripov4@gmail.com'
        )


@receiver(pre_save, sender=User)
def user_auto_line_name(sender, instance, **kwargs):
    if not instance.first_name:
        instance.first_name = 'UNKNOWN'
    if not instance.last_name:
        instance.last_name = 'UNKNOWN'


@receiver(post_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    print(f'{instance.username} deleted boldi.')
