# Generated by Django 4.1.3 on 2022-12-06 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_dogwalker_remove_person_data_remove_person_hora_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogwalker',
            old_name='nome',
            new_name='nome_dog',
        ),
    ]
