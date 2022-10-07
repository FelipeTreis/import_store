from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from app.models import Product


def home(request):
    products = Product.objects.filter(is_published=True, ).order_by('-id')
    return render(request, 'app/pages/home.html', context={
        'products': products,
    })


def category(request, category_id):
    products = get_list_or_404(Product.objects.filter(category__id=category_id, is_published=True,).order_by('-id'))
    return render(request, 'app/pages/category.html', context={
        'products': products,
        'title': f'Category-{products[0].category.name}',
    })


def brand(request, brand_id):
    products = get_list_or_404(Product.objects.filter(brand__id=brand_id, is_published=True,).order_by('-id'))
    return render(request, 'app/pages/brand.html', context={
        'products': products,
        'title': f'Brand-{products[0].brand.name}',
    })


def item(request, id):
    product = get_object_or_404(Product, pk=id, is_published=True)
    return render(request, 'app/pages/product.html', context={
        'product': product,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    products = Product.objects.filter(
        Q(
            Q(name__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(slug__icontains=search_term),
        ), is_published=True
    ).order_by('-id')
    return render(request, 'app/pages/search.html', {
        'title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'products': products,
        'additional_url_query': f'&q={search_term}',
    })


def about(request):
    return render(request, 'app/pages/about.html', context={
        'title': 'About Us',
    })
