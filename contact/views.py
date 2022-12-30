from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ContactUsModelForm, ProfileForm
from .models import ContactUs, UserProfile
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView


# Create your views here.

# class base view
# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         context = {'contact_form': contact_form}
#         return render(request, 'contact/contact-us.html', context)
#
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home')
#
#         context = {'contact_form': contact_form}
#         return render(request, 'contact/contact-us.html', context)

# form view
# when form view is in use, contact_form kw in contact/contact-us.html should change to form kw
class ContactUsView(FormView):
    template_name = 'contact/contact-us.html'
    form_class = ContactUsModelForm
    # success url
    success_url = '/contact-us/'

    # if form is valid
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# class ContactUsView(FormView, CreateView):
#     template_name = 'contact/contact-us.html'
#     model = ContactUs
#     form_class = ContactUsModelForm
#     # success url
#     success_url = '/contact-us/'


# function base view
# contact us page
# def contact_us(request):
#     if request.method == 'POST':
#         contact_form = ContactUsForm(request.POST)
#         if contact_form.is_valid():
#             contact = ContactUs(
#                 subject=contact_form.cleaned_data.get('subject'),
#                 full_name=contact_form.cleaned_data.get('full_name'),
#                 email=contact_form.cleaned_data.get('email'),
#                 message=contact_form.cleaned_data.get('message'),
#             )
#
#             contact.save()
#             return redirect('home')
#     else:
#         contact_form = ContactUsForm()
#
#     context = {'contact_form': contact_form}
#     return render(request, 'contact/contact-us.html', context)

# store file method
def store_file(file):
    with open('temp/image.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        context = {'form': ProfileForm()}
        return render(request, 'contact/profile.html', context)

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # store_file(request.FILES['image'])
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return redirect('contact.profile')

        # else
        context = {'form': ProfileForm()}
        return render(request, 'contact/profile.html', context)
