# Generated by Django 4.1.2 on 2022-10-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardgameAge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='min_age_of_player',
            field=models.CharField(max_length=2),
        ),
    ]
