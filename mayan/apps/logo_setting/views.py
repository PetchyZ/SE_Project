from mayan.apps.views.generics import SimpleView,SingleObjectCreateView
from django.urls import reverse_lazy

from .forms import ThemeForm
from mayan.apps.appearance.permissions import permission_theme_create


class ThemeCreateView(SingleObjectCreateView):
    extra_context = {'title': ('Create new theme')}
    form_class = ThemeForm
    post_action_redirect = reverse_lazy(
        viewname='appearance:theme_list'
    )
    view_permission = permission_theme_create

    def get_instance_extra_data(self):
        return {'_event_actor': self.request.user}