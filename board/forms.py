from django import forms
from .models import Comments


class CommentFrom(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('author', 'content')