from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.conf import settings
from projects.models import Projects


def get_sentinel_user():
    return get_user_model().objects.get(id=1)


class Inventory (models.Model):
    name = models.CharField('Name', max_length=100, unique=True)
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING, null=True, blank=True, limit_choices_to=~Q(project_status=2), verbose_name='Projects\'s Name')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))

    class Meta:
        abstract = True

    def __str__(self):
        try:
            i = int(self.project.project_status)
            status = Projects.status[i][1]
        except AttributeError:
            status = 'available'

        if status == 'available':
            return '{} is available'.format(str(self.name))
        else:
            return '{} is being used in {}'.format(str(self.name), self.project.project_name)

    # This function is used to split the project_name in the template
    def split(self):
        return self.project.project_name.split('is')


class RawMaterials(Inventory):
    class Meta:
        db_table = 'RawMaterials'
        verbose_name_plural = 'RawMaterials'
        ordering = ['id']


class Tools(Inventory):
    class Meta:
        db_table = 'Tools'
        verbose_name_plural = 'Tools'
        ordering = ['id']
