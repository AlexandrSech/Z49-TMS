from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=25)
    password = forms.CharField(max_length=255)


class MessageForm(forms.Form):
    m_text = forms.CharField(max_length=256)
    user_name = forms.CharField(max_length=256)
