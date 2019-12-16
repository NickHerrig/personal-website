from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/books.html'


class LoginPageView(TemplateView):
    template_name = 'pages/login.html'
