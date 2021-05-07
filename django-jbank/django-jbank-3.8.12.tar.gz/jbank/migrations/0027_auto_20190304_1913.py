# Generated by Django 2.1.7 on 2019-03-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0026_auto_20181205_0034"),
    ]

    operations = [
        migrations.AddField(
            model_name="referencepaymentrecord",
            name="manually_settled",
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name="manually settled"),
        ),
        migrations.AddField(
            model_name="statementrecord",
            name="manually_settled",
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name="manually settled"),
        ),
    ]
