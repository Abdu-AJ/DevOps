from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=10, required=False)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        
        

class CustomUserChangeForm(UserChangeForm):
    phone_number = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = '__all__'