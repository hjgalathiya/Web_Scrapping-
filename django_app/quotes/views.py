from django.shortcuts import render
from .models import Quote

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, "quotes.html", {"quotes": quotes})
