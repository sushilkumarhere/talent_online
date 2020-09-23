from django import forms
from .models import SiteSetting, Course, services


# DataFlair
class sitecreate(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = '__all__'


class course_create(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class service_create(forms.ModelForm):
    class Meta:
        model = services
        fields = '__all__'
