# Generated by Django 2.2.20 on 2021-04-15 16:31

from django.db import migrations


def update_jquery_3_6_in_theme(apps, schema_editor):
    """
    Upgrade jquery from 3.4.1 to 3.6.0 for the base.html in theme's directory.
    """
    import os
    from tendenci.apps.theme.utils import get_theme_root
    
    theme_dir = get_theme_root()
    # Check base.html
    file_path = '{}/templates/base.html'.format(theme_dir)
    if os.path.isfile(file_path):
        file_changed = False
        with open(file_path, 'r') as f:
            content = f.read()
            str_find = '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'
            str_to_replace = '//ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'
            if content.find(str_find) != -1:
                content = content.replace(str_find, str_to_replace)
                
                str_find = 'https://code.jquery.com/jquery-migrate-3.1.0.min.js'
                str_to_replace = 'https://code.jquery.com/jquery-migrate-3.3.2.min.js'
                content = content.replace(str_find, str_to_replace)
                
                file_changed = True 

        if file_changed:
            with open(file_path, 'w') as f:
                f.write(content)


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20190913_1537'),
    ]

    operations = [
        migrations.RunPython(update_jquery_3_6_in_theme)
    ]
