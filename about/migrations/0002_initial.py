# Generated by Django 4.1.1 on 2022-10-16 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncomment',
            name='question_comment_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='question_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
