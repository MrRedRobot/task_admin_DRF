# Generated by Django 4.1.4 on 2022-12-06 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('state', models.CharField(choices=[('BACKLOG', 'Backlog'), ('TO DO', 'To Do'), ('DOING', 'Doing'), ('TEST', 'Test'), ('DONE', 'Done')], max_length=10)),
                ('priority', models.CharField(choices=[('ALTA', 'Alta'), ('MEDIA', 'Media'), ('BAJA', 'Baja')], max_length=5)),
                ('delivery_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentary_text', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
