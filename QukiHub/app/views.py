"""
Definition of views.
MVC pattern
Controller: Controll 함!
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Post, CategoryPost
# from django.contrib.auth.decorators import permission_required
# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.views import generic
from . import models, category_config
from django.utils import timezone
from taggit.models import Tag

...


class TagMixin(object):
    def get_context_data(self):
        context = super(TagMixin, self).get_context_data()
        context['tags'] = Tag.objects.all()
        return context


class PostIndex(generic.ListView):
    model = Post
    template_name = 'app/index.html'
    layout_style = 'home_top'  # layout_style = {left: picture-left-layout, top: picture-top-layout}
    paginate_by = 5
    view_name = 'home'
    queryset = Post.objects.published()
    context_object_name = 'posts'


class Contact(generic.TemplateView):
    template_name = 'app/contact.html'
    layout_style = 'none'
    view_name = 'contact'


class About(generic.TemplateView):
    template_name = 'app/about.html'
    layout_style = 'none'
    view_name = 'about'


class PostItem(generic.DetailView):
    model = models.Post
    template_name = 'app/post_item.html'
    layout_style = 'none'
    view_name = 'post_item'


class ActivityList(generic.ListView):
    queryset = Post.objects.published()  # ?????
    template_name = 'app/index.html'
    layout_style = 'home_top'
    view_name = 'home'


class Portfolio(generic.TemplateView):
    template_name = 'app/portfolio_item.html'
    layout_style = 'home_top'
    view_name = 'portfolio'


class PostCategorizedList(generic.ListView):
    template_name = 'app/post_categorized_list.html'
    layout_style = 'none'
    view_name = 'home'

    def get_queryset(self):
        self.category = get_object_or_404(CategoryPost, parent=self.kwargs['parent'], child=self.kwargs['child'])
        obj = Post.objects.published().filter(category=self.category)
        print(obj)
        return obj


class TagIndexView(generic.ListView):
    template_name = 'app/post_categorized_list.html'
    layout_style = 'none'
    view_name = 'home'
    model = Post
    paginate_by = 5
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


@user_passes_test(lambda u: u.is_superuser)
def only_admin(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/onlyadmin.html',
        {
            'layout_style': 'none',
        }
    )
