from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs


# Create your views here.

# contact us page
def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)

            contact = ContactUs(
                subject=contact_form.cleaned_data.get('subject'),
                full_name=contact_form.cleaned_data.get('full_name'),
                email=contact_form.cleaned_data.get('email'),
                message=contact_form.cleaned_data.get('message'),
            )
            contact.save()
            return redirect('home')
    else:
        contact_form = ContactUsForm()

    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact/contact-us.html', context)
