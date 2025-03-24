from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from pessoa.models import License

class SimpleMiddleware:
    def __init__(self, get_response):
        print("Passei pelo construtor: ") 
        self.get_response = get_response
        

    def __call__(self, request):
        print("Passei pelo call: ")
        if request.user.is_authenticated:
            print("Usuário autenticado")
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        print("Passei pelo process_template_response")
        return response

class LicenseCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                license = License.objects.get(user=request.user)
                if not license.is_valid():
                    return redirect('license_invalid')  
            except License.DoesNotExist:
                return redirect('license_missing')  
        return None