from django.shortcuts import render
from django.views.generic import ListView, DetailView
from project_task.models import ProductDetail, Brand, Category
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProductList(ListView):
    model = ProductDetail
    paginate_by = 20
    template_name = 'project_task/product_list.html'
    context_object_name = 'product_list'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brand'] = Brand.objects.all()
        print(context)
        return context


class ProductFilterByCategory(ProductList, ListView):
    model = ProductDetail
    template_name = 'project_task/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self, *args, **kwargs):
        query_set = super(ProductFilterByCategory, self).get_queryset(*args, **kwargs)

        pk = self.request.resolver_match.kwargs.get('pk')
        url = self.request.resolver_match.url_name
        if pk:
            if url == 'product_filter_brand':
                query_set = query_set.filter(product__brand__id=pk)
            elif url == 'product_filter_category':
                query_set = query_set.filter(product__category__id=pk)
            else:
                return query_set
        return query_set
