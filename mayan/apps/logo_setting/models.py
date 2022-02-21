from django.db import models
from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from django.utils.encoding import force_text
from django.urls import reverse
from mayan.apps.events.classes import EventManagerSave
from mayan.apps.appearance.events import event_theme_created, event_theme_edited
from django.utils.translation import ugettext_lazy as _
import bleach
from mayan.apps.events.decorators import method_event

class LogoName(ExtraDataModelMixin, models.Model):
    logoName = models.CharField(
        db_index=True, help_text=_('text LogoName.'),
        max_length=128, unique=True, verbose_name=_('LogoName')
    )

    class Meta:
        verbose_name = _('LogoName')
        verbose_name_plural = _('LogoName')

    def __str__(self):
        return force_text(s=self.label)

    def get_absolute_url(self):
        return reverse(
            viewname='appearance:theme_edit', kwargs={
                'theme_id': self.pk
            }
        )

    @method_event(
        event_manager_class=EventManagerSave,
        created={
            'event': event_theme_created,
            'target': 'self',
        },
        edited={
            'event': event_theme_edited,
            'target': 'self',
        }
    )
    def save(self, *args, **kwargs):
        self.stylesheet = bleach.clean(
            text=self.stylesheet, tags=('style',)
        )
        super().save(*args, **kwargs)