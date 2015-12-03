from django.views.generic.detail import DetailView
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


class HomeView(DetailView):
    model = Site
    template_name = 'home.html'

    def get_object(self):
        """HomeView should return current site object."""
        return get_current_site(self.request)
