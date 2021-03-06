# coding=utf-8

from django import forms
from django.contrib.comments.forms import CommentForm
from django.conf import settings
from django.utils.translation import ungettext, ugettext, ugettext_lazy as _

#from simple_comment.models import SimpleComment

COMMENT_MAX_LENGTH = getattr(settings,'COMMENT_MAX_LENGTH', 3000)

class SimpleCommentForm(CommentForm):
    # Set email attr 'required' to 'False' and use Chinese labels for name, email, url and comment
    name = forms.CharField(label="姓名", max_length=50, error_messages={'required': '请填写您的名字:', 'max_length': '名字长度不能超过50个字'})
    email = forms.EmailField(label="邮箱", required=False)
    url = forms.URLField(label="网址", required=False)
    comment = forms.CharField(label="评论", widget=forms.Textarea(attrs={'rows':'8','cols':'50'}), max_length=COMMENT_MAX_LENGTH, error_messages={'required': '请填写评论内容:', 'max_length':'评论长度不能超过3000个字'})

    #def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        #return SimpleComment

    #def get_comment_create_data(self):
        # Use the data of the superclass, and add in the title field
        #return super().get_comment_create_data()
