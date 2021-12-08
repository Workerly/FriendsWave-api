# Generated by Django 3.2.9 on 2021-12-02 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postModule', '0001_initial'),
        ('commentModule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postModule_comment_related', related_query_name='postModule_comments', to='postModule.post'),
        ),
    ]
