from django import forms

from .models import Book1


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    Roll_no = forms.IntegerField(help_text='Enter 6 digit Roll no')
    password = forms.CharField(widget=forms.PasswordInput())

class Book1Form(forms.ModelForm):
    is_published = forms.BooleanField()
    upload_book = forms.FileField()
    class Meta:
        model = Book1
        fields = "__all__"

class AddressForm(forms.Form):
    STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
    )
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField(max_length=100)
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
