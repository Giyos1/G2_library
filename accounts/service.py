from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
import threading

from config import settings


def send_email_with_file_html():
    email = EmailMultiAlternatives(
        subject='test',
        body='test',
        from_email=settings.EMAIL_HOST_USER,
        to=['giyosoripov4@gmail.com']
    )
    email.attach_alternative('<p>test</p>', 'text/html')
    email.attach_file('D:\\Ustudy\\G2_django\\project1\\media\\books\\drawSQL-image-export-2025-02-02.png')
    email.send()


def send_email_with_file():
    email = EmailMessage(
        subject='test',
        body='test',
        from_email=settings.EMAIL_HOST_USER,
        to=['giyosoripov4@gmail.com']
    )
    email.attach_file('D:\\Ustudy\\G2_django\\project1\\media\\books\\drawSQL-image-export-2025-02-02.png')
    email.send()


def send_email_with_file_thread():
    t = threading.Thread(target=send_email_with_file)
    t.start()


def send_email(subject,
               message,
               to_email='jaloliddinkholmatov47@gmail.com'):
    send_mail(
        subject=subject,
        message=None,
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True
    )


def send_email_thread(subject,
                      message,
                      to_email='jaloliddinkholmatov47@gmail.com'):
    thread = threading.Thread(target=send_email,
                              args=(subject,
                                    message,
                                    to_email))
    thread.start()
