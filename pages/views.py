from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from rep.models import Rep
from listings.choices import usb_choices , output_choices , usb_Type_choices , handsfree_Type_choices , category_choices
# Create your views here.

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'usb_choices':usb_choices,
        'output_choices':output_choices,
        'usb_Type_choices':usb_Type_choices,
        'handsfree_Type_choices':handsfree_Type_choices,
        'category_choices':category_choices

    }
    return render(request, 'pages/index.html', context)


def about(request):
    rep = Rep.objects.all()

    mvp_rep = Rep.objects.all().filter(is_mvp=True)

    context = {
        'rep':rep,
        'mvp_rep': mvp_rep
    }
    return render(request, 'pages/about.html' , context)
