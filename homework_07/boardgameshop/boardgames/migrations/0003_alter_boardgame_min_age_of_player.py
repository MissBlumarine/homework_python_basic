# Generated by Django 4.1.2 on 2022-10-14 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0002_boardgameage_alter_boardgame_min_age_of_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='min_age_of_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boardgame', to='boardgames.boardgameage'),
        ),
    ]
