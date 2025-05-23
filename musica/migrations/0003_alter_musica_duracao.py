# Generated by Django 5.2.1 on 2025-05-15 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musica", "0002_musica_id_externo"),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE musica_musica 
            ALTER COLUMN duracao 
            TYPE integer 
            USING EXTRACT(epoch FROM duracao);
            """
        ),
        migrations.AlterField(
            model_name="musica",
            name="duracao",
            field=models.IntegerField(),
        ),
    ]
