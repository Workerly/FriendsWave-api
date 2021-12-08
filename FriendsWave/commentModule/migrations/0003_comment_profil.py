# Generated by Django 3.2.9 on 2021-12-02 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social', '0001_initial'),
        ('commentModule', '0002_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials_content', related_query_name='socials_contents', to='social.profil'),
        ),
    ]
