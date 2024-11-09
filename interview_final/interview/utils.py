from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_round_assignment_email(receiver_email, round_type, round_number):
    subject = f"Assignment for {round_type} - Round {round_number}"
    
    html_message = render_to_string('interview/email_template.html', {
        'round_type': round_type,
        'round_number': round_number
    })
    
    try:
        send_mail(
            subject=subject,
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receiver_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False