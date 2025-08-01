# app/views.py

import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Case, When, Value
from .models import win

def index(request):
    # This view remains the same
    context = {
        'results': [], 'sort_by': None,
        'direction': 'asc', 'next_direction': 'asc',
    }
    return render(request, "index.html", context)


def search(request):
    """
    Handles both general search/sort and the new commodity-specific search.
    """
    # Check for the new commodity-specific search parameter
    commodity_query = request.GET.get('commodity_search')

    if commodity_query:
        # --- NEW LOGIC: If a commodity search is triggered ---
        print(f"Performing new search for all items in commodity: {commodity_query}")
        filters = Q(ComodityNumber__iexact=commodity_query)
        results = win.objects.filter(filters).order_by('WinItemName')

        # Set default context for the commodity results page
        context = {
            "results": results[:100],
            "sort_by": 'WinItemName', # Default sort
            "next_direction": "desc",
        }

    else:
        # --- EXISTING LOGIC: For general search and sorting ---
        query = request.GET.get('q', '').strip()
        sort_by = request.GET.get('sort')
        direction = request.GET.get('direction', 'asc')
        
        results = win.objects.all()

        if query:
            filters = Q(VENDOR_ITEM_NUMBER__icontains=query) | \
                      Q(WiseItemNumber__icontains=query) | \
                      Q(WinItemName__icontains=query) | \
                      Q(ManufacturerName__icontains=query) | \
                      Q(MainframeDescription__icontains=query) | \
                      Q(UPC__icontains=query) | \
                      Q(CatalogNnumber__icontains=query) | \
                      Q(VENDOR_NUMBER__icontains=query) | \
                      Q(ProductNumber__icontains=query)
            results = results.filter(filters).distinct()

        if sort_by:
            if sort_by == 'ItemStatus':
                custom_order = Case(
                    When(ItemStatus='A', then=Value(1)), When(ItemStatus='D', then=Value(2)),
                    When(ItemStatus='O', then=Value(3)), default=Value(4)
                )
                results = results.order_by(custom_order.desc() if direction == 'desc' else custom_order.asc())
            else:
                order_field = f"-{sort_by}" if direction == 'desc' else sort_by
                results = results.order_by(order_field)

        context = {
            "results": results[:100],
            "sort_by": sort_by,
            "next_direction": "asc" if direction == "desc" else "desc",
        }
    
    return render(request, "partials/results_and_headers.html", context)

def export_csv(request):
    """
    Performs a search using the 'q' parameter from the URL and returns the
    full result set as a downloadable CSV file.
    """
    query = request.GET.get('q', '').strip()
    results = win.objects.all() # Start with all results

    if query:
        # Use the same filter logic as the main search view
        filters = Q(VENDOR_ITEM_NUMBER__icontains=query) | Q(WiseItemNumber__icontains=query) | \
                  Q(WinItemName__icontains=query) | Q(ManufacturerName__icontains=query) | \
                  Q(MainframeDescription__icontains=query) | Q(UPC__icontains=query) | \
                  Q(CatalogNnumber__icontains=query) | Q(VENDOR_NUMBER__icontains=query) | \
                  Q(ProductNumber__icontains=query)
        results = results.filter(filters).distinct()
    
    # Set up the HTTP response for a CSV file
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vendor_part_numbers.csv"'

    writer = csv.writer(response)
    # Write the header row for the CSV
    writer.writerow([
        'WiseItemNumber', 'ManufacturerName', 'WinItemName', 'MainframeDescription',
        'VENDOR_NUMBER', 'VENDOR_ITEM_NUMBER', 'CatalogNnumber', 'UPC', 'ItemStatus'
    ])

    # Write the data rows
    for item in results:
        writer.writerow([
            item.WiseItemNumber, item.ManufacturerName, item.WinItemName,
            item.MainframeDescription, item.VENDOR_NUMBER, item.VENDOR_ITEM_NUMBER,
            item.CatalogNnumber, item.UPC, item.ItemStatus
        ])

    return response