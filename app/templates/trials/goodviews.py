from django.shortcuts import render
from django.db.models import Q
from app.models import win

def index(request):
    return render(request, "index.html")

def search(request):
    # Get and clean all inputs
    q = request.GET.get('q', '').strip()
    wise_item_str = request.GET.get('WiseItemNumber', '').strip()
    commodity_str = request.GET.get('ComodityNumber', '').strip()
    results = []

    print("\n--- STARTING SIMPLIFIED SEARCH ---")
    print(f"Received -> q: '{q}', WiseItemNumber: '{wise_item_str}', ComodityNumber: '{commodity_str}'")

    # Priority 1: If a commodity number is present, search ONLY by that.
    if commodity_str:
        print(f"--> Path 1: Searching ONLY for ComodityNumber: '{commodity_str}'")
        results = win.objects.filter(ComodityNumber__iexact=commodity_str).order_by("WinItemName")[:100]
        print(f"--> Database found {results.count()} items.")

    # Priority 2: If no commodity, but an item number is present, search ONLY by that.
    elif wise_item_str:
        print(f"--> Path 2: Searching ONLY for WiseItemNumber: '{wise_item_str}'")
        results = win.objects.filter(WiseItemNumber__iexact=wise_item_str).order_by("WinItemName")[:100]
        print(f"--> Database found {results.count()} items.")

    # Priority 3: If other fields are empty, do a global text search.
    elif q:
        print(f"--> Path 3: Searching ONLY for global term: '{q}'")
        filters = (Q(MainframeDescription__icontains=q) |
                   Q(WiseItemNumber__icontains=q) |
                   Q(WinItemName__icontains=q))
        results = win.objects.filter(filters).distinct().order_by("WinItemName")[:100]
        print(f"--> Database found {results.count()} items.")

    print(f"--- FINISHING. Sending {len(list(results))} items to template. ---")
    return render(request, "partials/results.html", {"results": results})