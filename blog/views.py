from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import *


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        deta = query.filter(is_active=True)
        category = self.kwargs.get('categorys')
        if category is not None:
            deta = query.filter(category__url_title__iexact=category)
            return deta
        return deta


def blog_categris(request):
    blog_categoriss = BlogCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'blog_categoriss': blog_categoriss,
    }
    return render(request, 'blog/blog_category.html', context)


class BlogDeteliView(DetailView):
    model = Blog
    template_name = 'blog/blog_deteil.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDeteliView, self).get_context_data()
        blog = kwargs.get('object')
        context['comment'] = BlogComment.objects.filter(is_delete=False, blog_id=blog.id,
                                                        parent=None).order_by('-create_date').prefetch_related(
            'blogcomment_set')
        return context


def send_comment(request: HttpRequest):
    if request.user.is_authenticated:
        blog_id = request.GET.get('blog_id')
        blog_comment = request.GET.get('blog_comment')
        parent_id = request.GET.get('parent_id')
        comment = BlogComment(blog_id=blog_id, comment_text=blog_comment, user_id=request.user.id, parent_id=parent_id)
        comment.save()
        comments = BlogComment.objects.filter(is_delete=False, blog_id=blog_id, parent=None).order_by(
            '-create_date').all()
        context = {
            'commentss': comments,
            'comment_count': BlogComment.objects.filter(blog_id=blog_id).count()
        }
        return render(request, 'blog/blog_comment_component.html', context)
