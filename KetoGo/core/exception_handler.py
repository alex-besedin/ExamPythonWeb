from django.http import JsonResponse
from django.shortcuts import render


# def my_custom_page_not_found(request, exception):
#     return JsonResponse({
#         "error": "Sorry, bro, there's nothing here for ya...",
#         "status": 404,
#     })


def my500_custom_error_view(request):
    return render(request, '500.html')


def my404_custom_page_not_found_view(request, *args):
    return render(request, '404.html')


def my400_custom_bad_request_view(request, *args):
    return render(request, '400.html')
