
# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import win # Make sure you are importing your model correctly

def index(request):
    # Get the search query from the URL's GET parameters.
    # It will be None if the user hasn't searched for anything yet.
    q = request.GET.get('q') 
    
    results = []  # Default to an empty list
    if q:
        # If a query exists, filter the database just like before.
        print(f"Searching for: '{q}'") # For debugging
        results = win.objects.filter(
            Q(ItemNumber__icontains=q) | 
            Q(WiseItemNumber__icontains=q) | 
            Q(WinItemName__icontains=q)
        ).order_by("WinItemName","-SimilarityScore")[:100]

    # The context dictionary now passes the results to index.html
    context = {
        'results': results,
        'query': q  # Optional: pass the query back to pre-fill the search box
    }
    
    # Render the main index.html file with the results
    return render(request, "index.html", context)

# The 'search' view is no longer needed and should be deleted.













# # from django.shortcuts import render
# # from django.db.models import Q

# # from app.models import win


# from django.shortcuts import render
# from django.db.models import Q
# from app.models import win

# def index(request):
#     return render(request, "index.html")

# def search(request):
#     q = request.GET.get('q')
#     results = []  # Initialize results as an empty list

#     # Print the received query to the terminal for debugging
#     print(f"Search query received: '{q}'")

#     if q:
#         # If a query is present, filter the win objects
#         results = win.objects.filter(
#             Q(ItemNumber__icontains=q) | 
#             Q(WiseItemNumber__icontains=q) | 
#             Q(WinItemName__icontains=q)
#         ).order_by("WinItemName")[:100]
    
#     # No need for an else block, 'results' will remain an empty list if q is empty
#     # Pass the 'results' queryset directly to the template
#     # return render(request, "partials/results.html", {"results": results})
#     return render(request, "index.html", {"results": results})





# # def index(request):
# #     return render(request, "index.html")

# # def search(request):
# #     q = request.GET.get('q')
# #     results_list=[]

# #     print(q)

# #     if q:
# #         results = win.objects.filter(Q(ItemNumber__icontains=q) | Q(WiseItemNumber__icontains=q) | Q(WinItemName__icontains=q)) \
# #         .order_by("WinItemName")[0:100]
# #         # results_list = list(results.values_list(...)) 
# #         # results = win.objects.filter(Q(ItemNumber__icontains=q) | Q(WiseItemNumber__icontains=q) | Q(WinItemName__icontains=q) | Q(MainframeDescription__icontains=q)) \
# #         # .order_by("WinItemName", "-MainframeDescription")[0:100]
# #     else:
# #         results = []

# #     return render(request, "partials/results.html", {"results": results_list})