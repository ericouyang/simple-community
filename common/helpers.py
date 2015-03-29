from django.core.mail import EmailMultiAlternatives


def send_mail(to, subject, plain_text, html, tags=[], metadata={}):
    print to
    msg = EmailMultiAlternatives(
        subject=subject,
        body=plain_text,
        to=[to],
    )
    msg.attach_alternative(html, 'text/html')

    msg.tag = tags
    msg.metadata = {}

    msg.send()
