# Generated by Django 2.1.3 on 2018-11-23 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketon', '0003_auto_20181123_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.IntegerField()),
                ('available', models.BooleanField()),
                ('cinema_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketon.Cinema')),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketon.Movie')),
            ],
        ),
    ]