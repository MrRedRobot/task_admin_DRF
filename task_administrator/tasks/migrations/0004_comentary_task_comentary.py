# Generated by Django 4.1.4 on 2022-12-13 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentary_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='comentary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.comentary', verbose_name='Comentario'),
        ),
    ]
