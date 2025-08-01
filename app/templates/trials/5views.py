# app/views.py

from django.shortcuts import render
from django.db.models import Q
from app.models import win # Make sure your model is imported

def index(request):
    """
    This new view renders the main homepage.
    """
    return render(request, "index.html")

def search(request):
    """
    Handles a single query 'q' from the search bar and searches across
    multiple relevant fields.
    """
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        # Create a complex lookup Q object to search across multiple fields
        # This makes the single search bar powerful.
        filters = Q(ItemNumber__icontains=query) | \
                  Q(WiseItemNumber__icontains=query) | \
                  Q(WinItemName__icontains=query) | \
                  Q(ManufacturerName__icontains=query) | \
                  Q(ProductNumber__icontains=query)
        
        results = win.objects.filter(filters).distinct()[:100]

    return render(request, "partials/results.html", {"results": results})