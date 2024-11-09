# Generated by Django 4.2.16 on 2024-11-09 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.cafedra')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.cafedra')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeday', models.CharField(choices=[('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thu', 'Thu'), ('Fri', 'Fri'), ('Sat', 'Sat')], max_length=50)),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.clas')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.teacher')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.time')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.clas')),
            ],
        ),
        migrations.AddField(
            model_name='clas',
            name='headteacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maktab.teacher'),
        ),
    ]
