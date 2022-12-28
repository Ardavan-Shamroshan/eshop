from django import forms
from .models import ContactUs


# Every form that uses this field will have these methods run before anything else can be done with the field’s data.
# This is cleaning that is specific to this type of field, regardless of how it is subsequently used.
class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی', max_length=50,
        error_messages={
            'required': 'نام و نام خانوادگی را خالی رها نکنید',
            'max_length': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کاراکتر باشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': "required",
            'placeholder': "نام و نام خانوادگی",
        }),
    )
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'required': "required",
        'placeholder': "ایمیل",
    }))
    subject = forms.CharField(label='موضوع', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': "required",
        'placeholder': "موضوع پیام",
    }))
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={
        'id': "message",
        'required': "",
        'class': "form-control",
        'rows': "8",
        'placeholder': "پیغـام شمـا",
    }))


# If you’re building a database-driven app, chances are you’ll have forms that map closely to Django models.
# For instance, you might have a BlogComment model, and you want to create a form that lets people submit comments.
# In this case, it would be redundant to define the field types in your form,
# because you’ve already defined the fields in your model.
class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message']
        # fields = '__all__'

        # Set the exclude attribute of the ModelForm’s inner Meta class to a list of fields to be excluded from the form.
        # exclude = ['response']

        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'subject': 'موضوع پیام',
            'message': 'پیغام شما',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "نام و نام خانوادگی",
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "ایمیل",
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "موضوع پیام",

            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'id': 'message',
                'placeholder': "پیغـام شمـا",
            })
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی را خالی رها نکنید',
            }
        }
