# Generated by Django 3.2.10 on 2021-12-10 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topicModule', '0001_initial'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='topics_of_interest',
            field=models.ManyToManyField(related_name='topicModule_profil_related', related_query_name='topicModule_profils', through='topicModule.ProfilTopic', to='topicModule.Topic'),
        ),
        migrations.AddField(
            model_name='profil',
            name='usedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_profil_related', related_query_name='social_profils', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friend',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_friend', related_query_name='socials_friends', to='social.profil'),
        ),
        migrations.AddField(
            model_name='friend',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='social_friend_related', related_query_name='social_friends', to='social.profil'),
        ),
    ]
