from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            #send email
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail("Email from " + name, message, email_from,['sinzunza@sdgku.edu'])
        
            return redirect('about')
        
        else:
            print("Invalid form")   
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

