from django.utils.deprecation import MiddlewareMixin


class ThemeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        theme = request.COOKIES.get('theme', 'light')
        request.theme = theme