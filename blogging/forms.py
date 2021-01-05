from django.forms import ModelForm
from blogging.models import Post


class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            # 'created_date',
            # 'modifed_date',
            #'published_date',
        ]