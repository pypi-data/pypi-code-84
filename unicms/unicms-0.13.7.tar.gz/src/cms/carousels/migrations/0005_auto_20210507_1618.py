# Generated by Django 3.1.6 on 2021-05-07 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmsmedias', '0005_auto_20210507_1618'),
        ('cmscarousels', '0004_auto_20210401_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carousel_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carousel_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitem_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cmsmedias.media'),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitem_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitemlink',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitemlink_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitemlink',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitemlink_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitemlinklocalization',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitemlinklocalization_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitemlinklocalization',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitemlinklocalization_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitemlocalization',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitemlocalization_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carouselitemlocalization',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carouselitemlocalization_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
