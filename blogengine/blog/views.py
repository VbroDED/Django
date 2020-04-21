# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts' : posts})

#def post_detail(request, slug):
#    post = Post.objects.get(slug__iexact=slug)
#    return render(request, 'blog/post_detail.html', context={'post' : post})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
#    def get(self, request, slug):
#        post = Post.objects.get(slug__iexact=slug)
#        post = get_object_or_404(Post, slug__iexact=slug)
#        return render(request, 'blog/post_detail.html', context={'post' : post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags' : tags})

class TagDetail(ObjectDetailMixin, View):
        model = Tag
        template = 'blog/tag_detail.html'

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form':form})

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Someone',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.3,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Student:
    pass


class Statistics:
    # student_id, [Scores]
    pass

class Subject:
    pass

class Score:
    # Subject, Student, value
    pass



#    def get(self, request, slug):
#       tag = Tag.objects.get(slug__iexact=slug)
#        tag = get_object_or_404(Tag, slug__iexact=slug)
#        return render(request, 'blog/tag_detail.html', context={'tag' : tag })

#def tag_detail(request, slug):
#    tag = Tag.objects.get(slug__iexact=slug)
#    return render(request, 'blog/tag_detail.html', context={'tag' : tag })
