from django.forms import ModelForm, CharField
from posts.models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    tags = CharField(label="Tagi")
