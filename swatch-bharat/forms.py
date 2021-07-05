from django import forms
from models import user,session,Post,like,comment
# Class for signup_form

class signup_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','name','email','password']
class login_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','password']
class post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','caption']
class like_form(forms.ModelForm):
    class Meta:
        model = like
        fields = ['post']
class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['post','comm_text']