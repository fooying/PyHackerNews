#!/usr/bin/env python


from django import forms

from pyhn.news.models import Post


class CommentForm(forms.Form):

    content = forms.CharField(widget=forms.Textarea)

    def save(self, user, post):
        pass