# coding=utf-8
from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(error_messages={'required': '请填写您的邮箱地址:', 'invalid': '请填写正确的邮箱格式:'})
    subject = forms.CharField(max_length=100, error_messages={'required': '请填写邮件主题:', 'max_length':'邮件主题不得超过100个字'})
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':'10'}), error_messages={'required':'请填写邮件正文:'})
    cc_myself = forms.BooleanField(required=False)

