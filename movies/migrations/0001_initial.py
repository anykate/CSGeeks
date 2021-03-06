# Generated by Django 2.0.1 on 2018-01-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=255)),
                ('actor', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=255)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='movies.Movie')),
            ],
        ),
    ]
