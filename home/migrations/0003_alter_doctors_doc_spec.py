# Generated by Django 4.2.2 on 2023-07-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors_doc_spec_alter_doctors_doc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_spec',
            field=models.CharField(max_length=290),
        ),
    ]
