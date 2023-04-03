# Generated by Django 4.1.7 on 2023-04-02 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('baseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.baseclass')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            bases=('projects.baseclass',),
        ),
    ]
