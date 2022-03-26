# Generated by Django 4.0.3 on 2022-03-26 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchannelgroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='userchannelgroup',
            name='user_channel_group.user',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='message',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='chat.user',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='chat',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.DeleteModel(
            name='ChannelGroup',
        ),
        migrations.DeleteModel(
            name='UserChannelGroup',
        ),
    ]
