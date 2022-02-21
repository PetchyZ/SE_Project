from django.conf.urls import url

from .views import ThemeCreateView

urlpatterns = [
    url(regex=r'^logo/$', name='logo_view', view=ThemeCreateView.as_view()),
]
