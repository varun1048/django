from django.forms import ModelForm 
from .models import Enquirys

class Enquiry_Form(ModelForm):
    class Meta:
        model = Enquirys
        fields = '__all__'
        