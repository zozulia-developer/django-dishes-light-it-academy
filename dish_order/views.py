from django.shortcuts import redirect


def redirect_dishes(request):
    return redirect ('dishes:index', permanent=True)