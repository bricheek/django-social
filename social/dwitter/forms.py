from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Dweet

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
    label=""
    )

    class Meta:
        model = Dweet
        exclude = ("user", )