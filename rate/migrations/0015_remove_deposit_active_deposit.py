# Generated by Django 5.1.2 on 2024-11-02 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0014_alter_alert_alert_alter_alert1_alert_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='active_deposit',
        ),
    ]