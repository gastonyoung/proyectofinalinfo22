# Generated by Django 4.0.6 on 2022-08-04 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarioevento',
            old_name='noticia',
            new_name='evento',
        ),
    ]
