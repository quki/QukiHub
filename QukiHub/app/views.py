"""
Definition of views.
MVC pattern
Controller: Controll 함!
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Post, Category
# from django.contrib.auth.decorators import permission_required
# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.views import generic
from . import models, category_config
from django.utils import timezone

...


class BlogIndex(generic.ListView):
    template_name = 'app/post.html'
    layout_index = 0
    view_name = 'home'
    config = category_config.POST_CATEGORIES
    choice = category_config.POST_MAIN_CHOICES
    choice_name = category_config.CATEGORY_NAME_PAIR

    def get_queryset(self):
        self.category = get_object_or_404(Category, main=self.kwargs['main'], sub=self.kwargs['sub'])
        obj = Post.objects.published().filter(category=self.category)
        print(obj)
        return obj


class PostsList(generic.ListView):
    queryset = Post.objects.published()  # ?????
    template_name = 'app/index.html'
    # paginate_by = 2
    view_name = 'home'
    config = category_config.POST_CATEGORIES
    choice = category_config.POST_MAIN_CHOICES
    choice_name = category_config.CATEGORY_NAME_PAIR
    layout_index = 0  # layout_index = [picture-left-layout, picture-top-layout]


class PostItem(generic.DetailView):
    model = models.Post
    template_name = 'app/post_item.html'
    layout_index = 1
    view_name = 'post-item'
    config = category_config.POST_CATEGORIES
    choice = category_config.POST_MAIN_CHOICES
    choice_name = category_config.CATEGORY_NAME_PAIR


class Contact(generic.TemplateView):
    template_name = 'app/contact.html'
    layout_index = 0
    view_name = 'contact'
    config = category_config.POST_CATEGORIES
    choice = category_config.POST_MAIN_CHOICES
    choice_name = category_config.CATEGORY_NAME_PAIR


class About(generic.TemplateView):
    template_name = 'app/about.html'
    layout_index = 0
    view_name = 'about'
    config = category_config.POST_CATEGORIES
    choice = category_config.POST_MAIN_CHOICES
    choice_name = category_config.CATEGORY_NAME_PAIR


@user_passes_test(lambda u: u.is_superuser)
def only_admin(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/onlyadmin.html',
        {
            'layout_index': 'auth',
        }
    )
