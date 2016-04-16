#blog2 form
from django import forms
from .models import Entry, Comment


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['title', 'body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']