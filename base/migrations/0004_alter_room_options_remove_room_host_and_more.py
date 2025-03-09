# Generated by Django 4.2.11 on 2025-03-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_message_options_alter_room_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='reservation',
            name='participants_emails',
            field=models.TextField(blank=True, help_text='Enter email addresses separated by commas', null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reminder_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
