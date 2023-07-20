from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from shop.forms import SearchForm
from shop.models import *
from utilities.http_service import get_user_ip


class ProductListView(ListView):
    model = ProductList
    template_name = 'shop/product_list.html'

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        deta = query.filter(is_active=True, is_delete=False)
        category = self.kwargs.get('category')
        if category is not None:
            deta = query.filter(category__url_title__iexact=category)
            return deta
        brand_name = self.kwargs.get('br')
        if brand_name is not None:
            deta = query.filter(brand__url_tital__iexact=brand_name)
            return deta
        return deta


def product_categris(request):
    product_categoriss = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'product_categoriss': product_categoriss,
    }
    return render(request, 'shop/category.html', context)


class ProductDeteilView(DetailView):
    model = ProductList
    template_name = 'shop/product_deteil.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDeteilView, self).get_context_data()
        my_product = kwargs.get('object')
        context['comment'] = ProductComment.objects.filter(is_delete=False, product_id=my_product.id,
                                                           parent=None).order_by('-create_date').prefetch_related(
            'productcomment_set')
        gallerise = list(Gallery.objects.filter(product_id=my_product.id).all())
        gallerise.insert(0, my_product)
        context['gallery'] = gallerise
        context['related_product'] = ProductList.objects.filter(brand_id=my_product.brand_id).all()[:10]
        product = self.object
        user_ip = get_user_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            viewed: bool = SeenProduct.objects.filter(viewer_ip__iexact=user_ip, product=product).exists()
            if not viewed:
                new_view = SeenProduct(
                    viewer_ip=user_ip,
                    user_id=user_id,
                    product_id=product.id,
                )
                new_view.save()
        return context


def send_comment_product(request: HttpRequest):
    if request.user.is_authenticated:
        product_id = request.GET.get('product_id')
        product_comment = request.GET.get('product_comment')
        parent_id = request.GET.get('parent_id')
        comment = ProductComment(product_id=product_id, comment_text=product_comment, user_id=request.user.id,
                                 parent_id=parent_id)
        comment.save()


def product_brand(request: HttpRequest):
    product_brand = ProductBrand.objects.annotate(brand_count=Count('productlist')).filter(is_active=True,
                                                                                           is_delete=False)
    context = {
        'brand': product_brand
    }
    return render(request, 'shop/brand.html', context)


def product_dislike(request, id):
    product = get_object_or_404(ProductList, id=id)
    if request.user.is_authenticated:
        if request.user in product.like.all():
            product.like.remove(request.user)
            product.dislike.add(request.user)
        elif request.user in product.dislike.all():
            product.dislike.remove(request.user)
        else:
            product.dislike.add(request.user)
    else:
        # url = request.META.get('HTTP_REFERER')
        # request.session['last_url'] = url
        # return redirect('RefererLogin')
        return redirect(reverse('product_list'))


def product_like(request, id):
    product = get_object_or_404(ProductList, id=id)
    if request.user.is_authenticated:
        if request.user in product.dislike.all():
            product.dislike.remove(request.user)
            product.like.add(request.user)
        elif request.user in product.like.all():
            product.like.remove(request.user)
        else:
            product.like.add(request.user)
    else:
        # url = request.META.get('HTTP_REFERER')
        # request.session['last_url'] = url
        # return redirect('RefererLogin')
        return redirect(reverse('product_list'))


def search(request):
    product = ProductList.objects.all()
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            product = product.filter(title__icontains=cd)
    return render(request, 'shop/product_list.html', {'form': form, 'object_list': product})
