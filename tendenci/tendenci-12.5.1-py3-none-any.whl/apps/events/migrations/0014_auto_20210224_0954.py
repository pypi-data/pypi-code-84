# Generated by Django 2.2.18 on 2021-02-24 09:54
import os
from django.db import migrations


def remove_urlize_filter(apps, schema_editor):
    """
    The urlize filter breaks the links in the description generated with wysiwyg editor.
    The issue has been fixed in core.
    
    This migration is to fix for the event template pulled down to the site.
    """
    from tendenci.apps.theme.utils import get_theme_root
    dir_path = get_theme_root()
    file_path = f'{dir_path}/templates/events/view.html'
    if os.path.isfile(file_path):
        updated = False
        with open(file_path, 'r') as f:
            content = f.read()
            if content.find('|urlize') >= 0:
                content = content.replace('speaker.description|safe|urlize|linebreaks',
                                          'speaker.description|safe|linebreaks')
                content = content.replace('organizer.description|safe|urlize|linebreaks',
                                          'organizer.description|safe|linebreaks')
                content = content.replace('sponsor.description|safe|urlize',
                                          'sponsor.description|safe')
                updated = True

        if updated:
            with open(file_path, 'w') as f:
                f.write(content)


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20200902_1545'),
    ]

    operations = [
        migrations.RunPython(remove_urlize_filter),
    ]
