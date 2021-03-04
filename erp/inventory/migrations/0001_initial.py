# Generated by Django 3.1.6 on 2021-02-24 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('project', models.ForeignKey(blank=True, limit_choices_to=models.Q(_negated=True, project_status=2), null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.projects', verbose_name="Projects's Name")),
                ('user', models.ForeignKey(on_delete=models.SET(inventory.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tools',
                'db_table': 'Tools',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RawMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('project', models.ForeignKey(blank=True, limit_choices_to=models.Q(_negated=True, project_status=2), null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.projects', verbose_name="Projects's Name")),
                ('user', models.ForeignKey(on_delete=models.SET(inventory.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'RawMaterials',
                'db_table': 'RawMaterials',
                'ordering': ['id'],
            },
        ),
    ]