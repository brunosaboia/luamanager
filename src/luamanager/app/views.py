"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse
from app.services.facebook import FacebookFeed
from django.conf import settings
import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    fb_profile, fb_posts = FacebookFeed.get_fb_data(
        user=settings.SOCIAL_AUTH_FACEBOOK_PROFILE)

    return render(
        request,
        'app/index.html',
        {
            'title':'Início',
            'year':datetime.now().year,
            'fb_posts': FacebookFeed.parse_posts(fb_posts['data'], fb_profile),
            'fb_profile': fb_profile,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contato',
            'message':'Fale conosco!',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Sobre',
            'message':'Informações sobre o sistema',
            'year':datetime.now().year,
        }
    )