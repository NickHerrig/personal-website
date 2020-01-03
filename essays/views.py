from django.views import generic

from .models import Essay

class IndexView(generic.ListView):
    template_name = 'essays/index.html'
    context_object_name = 'latest_essays_list'
    
    def get_queryset(self):
        """Return the 4 most recently published blogs."""
        return Essay.objects.order_by('-pub_date')[:4]

class DetailView(generic.DetailView):
    model = Essay
    template_name = 'essays/detail.html'

