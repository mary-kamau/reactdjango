from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = []

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
