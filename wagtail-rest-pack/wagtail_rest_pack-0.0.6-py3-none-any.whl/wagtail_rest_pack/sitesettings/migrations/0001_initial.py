# Generated by Django 3.1.8 on 2021-04-30 06:37

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields
from wagtail.images import get_image_model_string


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSliderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', wagtail.core.fields.RichTextField(default='', help_text='Text zobrazený přes obrázek.', max_length=200)),
                ('image', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=get_image_model_string())),
            ],
            options={
                'verbose_name': 'Carousel Item',
                'verbose_name_plural': 'Carousel Items',
            },
        ),
        migrations.CreateModel(
            name='SiteSettingsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carouselitems', to='wagtailcore.page')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sitesettings.imageslideritem')),
            ],
            options={
                'verbose_name': 'Carousel Item',
                'verbose_name_plural': 'Carousel Items',
            },
        ),
    ]
