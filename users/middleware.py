# middleware.py

from django.http import HttpResponseRedirect

class RedirectToHomePageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:  # Check if the response is a 404 error
            return HttpResponseRedirect('/')  # Redirect to the home page
        
        return response