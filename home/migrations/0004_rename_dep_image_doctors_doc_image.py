# Generated by Django 4.2.2 on 2023-07-29 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_doctors_doc_spec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='dep_image',
            new_name='doc_image',
        ),
    ]
