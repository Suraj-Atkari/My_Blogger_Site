from django import forms
from .models import Comment


class CommentFormView(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        label = {
            "user_name": "Your name",
            "email": "Your email",
            "text": "Your Message"

        }
