from django.shortcuts import render
from django.db.models import Q

from app.models import win

def index(request):
    return render(request, "index.html")

def search(request):
    q = request.GET.get('q')

    print(q)

    if q:
        results = win.objects.filter(Q(ItemNumber__icontains=q) | Q(WiseItemNumber__icontains=q) | Q(WinItemName__icontains=q)) \
        .order_by("WinItemName")[0:100]
    else:
        results = []

    return render(request, "partials/results.html", {"results": results})