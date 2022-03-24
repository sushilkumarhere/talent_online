from django import forms
from .models import  Course, services, StuRegistrations


# DataFlair



class course_create(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class course_update(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class service_create(forms.ModelForm):
    class Meta:
        model = services
        fields = '__all__'



class Frm_StuRegistration(forms.ModelForm):
    class Meta:
        model = StuRegistrations
        fields = '__all__'
