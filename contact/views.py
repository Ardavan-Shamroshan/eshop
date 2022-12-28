from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs


# Create your views here.

# class base view
class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsModelForm()
        context = {'contact_form': contact_form}
        return render(request, 'contact/contact-us.html', context)

    def post(self, request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home')

        context = {'contact_form': contact_form}
        return render(request, 'contact/contact-us.html', context)


# function base view
# contact us page
def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
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

    context = {'contact_form': contact_form}
    return render(request, 'contact/contact-us.html', context)
