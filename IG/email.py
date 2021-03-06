from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    subject = 'Boychild welcomes you to Instagram Community'
    sender = 'jackotienokey@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"name": name})
    html_content = render_to_string('email/welcome.html',{"name": name})
    print('Sending......')
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    print('Send')
    