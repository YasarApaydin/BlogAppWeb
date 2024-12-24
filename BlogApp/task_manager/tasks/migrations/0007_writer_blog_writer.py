# Generated by Django 5.1.4 on 2024-12-15 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_blog_blogcontent_alter_blog_blogimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WriterName', models.CharField(max_length=50)),
                ('WriterAbout', models.CharField(max_length=200)),
                ('WriterImage', models.ImageField(upload_to='blogs')),
                ('WriterMail', models.EmailField(max_length=200)),
                ('WriterPassword', models.CharField(max_length=128)),
                ('WriterStatus', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.writer'),
        ),
    ]
