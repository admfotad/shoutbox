from django.views.generic import FormView
from django.shortcuts import render
from django.urls import reverse_lazy

from posts.models import Post, Tag
from posts.forms import AddPostForm


def list_posts(request, tagname=None):
    context = {}
    if tagname is not None:
        tag = Tag.objects.get(name=tagname)
        posts = tag.post_set.all()
    else:
        posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'posts/list_posts.html', context)


class AddPost(FormView):
    form_class = AddPostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('list_posts')

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags').split(',')
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()

        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return super(AddPost, self).form_valid(form)
