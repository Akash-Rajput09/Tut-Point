# Generated by Django 5.1.1 on 2024-10-21 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_course_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='courses.chapter')),
            ],
        ),
    ]
