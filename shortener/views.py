from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        url = URL(long_url=long_url)
        url.save()
        return render(request, 'shortener/home.html', {'short_url': request.build_absolute_uri('/') + url.short_url})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.long_url)
