from dataclasses import field
from xml.etree.ElementInclude import include
from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host', 'participants']
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']