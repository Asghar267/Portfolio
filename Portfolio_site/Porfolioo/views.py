from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'index.html')


def portfoliodet(request):
    return render(request, 'portfolio-details.html')


def contactMe(request):
    print("contact")

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        print(name)
        print(email)
        print(subject)
        print(message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        # Send email to the customer with order details
        # Name = f"Deart\n\n"
        emailresponse = "\nThank you for reaching out! \nI appreciate your interest. I will get back to you promptly regarding your inquiry. If you have any urgent matters, please feel free to reach me directly at the provided contact information. Looking forward to connecting with you soon!"

        send_mail(
            'Thank you for reaching out!',
            emailresponse,
            'asgharabbasi267@gmail.com',  # Replace with your email address
            [email],  # Send email to the customer's email address
            fail_silently=False,
        )
        send_mail(
            subject,
            message,
            'asgharabbasi267@gmail.com',  # Replace with your email address
            ['asgharabbasi267@gmail.com'],  # Send email to the customer's email address
            fail_silently=False,
        )

        return redirect('home')
