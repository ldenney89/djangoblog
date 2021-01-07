from django.forms import ModelForm
from blogging.models import Post, Category


class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            # 'created_date',
            # 'modifed_date',
            # 'published_date',
        ]


class MyCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]
