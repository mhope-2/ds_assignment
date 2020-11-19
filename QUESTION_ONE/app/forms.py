from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label= 'name')
    file = forms.FileField(required=True, label='file')

    class Meta:
        model = Contact
        fields = ('name', 'file')

        def save(self, commit=True):
            contact_obj = super(ContactForm, self).save(commit=False)
            contact_obj.file = self.cleaned_data["file"]
            contact_obj.name = self.cleaned_data['name']

            if commit:
                contact_obj.save()
            return contact_obj