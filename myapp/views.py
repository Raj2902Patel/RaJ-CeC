from django.shortcuts import render
from .models import raj
# Create your views here.

def index(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')

        ent = raj(name=name,email=email)
        ent.save()

        msg = "               Hello Developer!" "\n\nName is :- " + name + "\n\nEmail is :- " + email

        from django.core.mail import send_mail

        send_mail(
            'New Enquiry',
            msg,
            'rajpatel.imscit20@gmail.com',
            ['raj2902patel@gmail.com'],
            fail_silently=False,
        )

    else:
        pass

    return render(requests,'index.html')