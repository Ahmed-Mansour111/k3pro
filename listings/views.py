from django.shortcuts import render
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from .models import Listing
from django.shortcuts import get_object_or_404 , render
from .choices import category_choices

# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            listings = listings.filter(category__category_name__iexact=category)


    context = {
        'category_choices': category_choices,
        'listings':paged_listings,
        'values': request.GET
        }
    return render(request,'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__category_name__iexact=category)

    context={
        'category_choices':category_choices,
        'listings':queryset_list,
        'values':request.GET
    }
    return render(request,'listings/search.html',context)