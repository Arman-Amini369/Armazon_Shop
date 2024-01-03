from django import forms
from django.forms import Select
from .models import Cart, Comment

class AddCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ("quantities",)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body", "score")
        widgets = {
            'score' : forms.TextInput(attrs={"placeholder" : "0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%"}),
        }   
