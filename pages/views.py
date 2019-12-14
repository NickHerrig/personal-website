from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class LoginPageView(TemplateView):
    template_name = 'pages/login.html'
