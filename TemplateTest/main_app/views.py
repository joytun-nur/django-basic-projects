from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Joytun'
        context['country'] = 'Bangladesh'
   
        context['list'] = [1,2,3,4,5]

        return context

class AboutView(TemplateView):
    template_name = "about.html"

# Create your views here.
