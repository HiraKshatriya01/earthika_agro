from django.forms import forms

from choices import *
# class STATUS(forms.Form):
CHOICE_PRODUCT = (
    (1, 'TURMERIC'),
    (2, 'GINGER'),
    (2, 'COMPOST'),
)
CHOICE_ENQUIRY_STATUS = (
    (1, 'PENDING'),
    (2, 'CONTACTED'),
    (2, 'NO RESPONSE'),
)