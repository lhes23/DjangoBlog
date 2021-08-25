from django.forms import ModelForm, fields
from .models import Post

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'