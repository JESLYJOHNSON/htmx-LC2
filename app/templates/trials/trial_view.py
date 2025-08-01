# # views.py

# from django.shortcuts import render
# from django.db.models import Q
# from .models import win

# # View 1: Renders the main page structure ONE TIME.
# def index(request):
#     # This view no longer handles searching. It just displays the main page.
#     return render(request, "index.html")

# # View 2: Handles HTMX search requests and returns ONLY the table rows.
# def search(request):
#     q = request.GET.get('q') 
    
#     results = []
#     if q:
#         # The search logic is the same as before.
#         results = win.objects.filter(
#             Q(ItemNumber__icontains=q) | 
#             Q(WiseItemNumber__icontains=q) | 
#             Q(WinItemName__icontains=q)
#         ).order_by("WinItemName")[:100]

#     # This view now renders a NEW "partial" template.
#     # It only returns the <tr> table rows, not the whole page.
#     return render(request, "partials/results_partial.html", {'results': results})