from django.shortcuts import render,redirect
from emailapp.models import *
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Index View
def index(request):   
    
    
    return render(request, 'index.html')

# Email page
def email_page(request):   
    
    
    return render(request, 'invitationmailv3.html')




# Invitation Email Sending View


def send_invitation_email(user_email):
    print("in email function")
    # Render the HTML email content
    context = {}
    html_content = render_to_string('invitationmailv3.html', context)

    # Create the email
    subject = 'Climate Change Conference!'
    from_email = 'ashraf.uzair01@gmail.com'  
    to_email = [user_email]

    email = EmailMultiAlternatives(subject, "", from_email, to_email)
    email.attach_alternative(html_content, "text/html")

     # Send the email
    try:
        email.send()
        print("Email Sent Successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")





def email_form_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  
        print("email",email)
        send_invitation_email(email)
        
        print("email sent successfully")
        
        return redirect('index')
    return render(request, 'index.html')