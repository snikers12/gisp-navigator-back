# Generated by Django 2.2.15 on 2021-05-22 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000, verbose_name='Код')),
                ('name', models.CharField(max_length=5000, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000, verbose_name='Код')),
                ('name', models.CharField(max_length=5000, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменты',
            },
        ),
        migrations.CreateModel(
            name='Okved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000, verbose_name='Код')),
                ('name', models.CharField(max_length=5000, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'ОКВЭД',
                'verbose_name_plural': 'ОКВЭД',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активна?')),
                ('ogrn', models.CharField(blank=True, max_length=255, null=True, verbose_name='ОРГН')),
                ('inn', models.CharField(blank=True, max_length=255, null=True, verbose_name='ИНН')),
                ('found_date', models.DateField(verbose_name='Дата основания')),
                ('branch', models.ManyToManyField(blank=True, to='organizations.Branch', verbose_name='Отрасль')),
                ('okveds', models.ManyToManyField(blank=True, to='organizations.Okved', verbose_name='ОКВЭДы')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='OrganizationSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер организаций',
                'verbose_name_plural': 'Размеры организаций',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=255, verbose_name='Назване региона')),
                ('region_code', models.CharField(max_length=255, verbose_name='Код региона')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Tass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000, verbose_name='Код')),
                ('name', models.CharField(max_length=5000, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'ТАСС',
                'verbose_name_plural': 'ТАСС',
            },
        ),
        migrations.CreateModel(
            name='SupportMeasures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kbk', models.CharField(blank=True, max_length=255, null=True, verbose_name='КБК')),
                ('name', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Название')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активна?')),
                ('is_federal', models.BooleanField(default=True, verbose_name='Федеральный бюджет?')),
                ('support_type', models.CharField(choices=[('fin', 'Финансовая поддержка'), ('prop', 'Имущественная поддержка'), ('cons', 'Консультационная (информационная) поддержка'), ('edu', 'Образовательная поддержка'), ('sup', 'Поддержка внешнеэкономической деятельности'), ('reg', 'Регуляторная поддержка (налоговые, таможенные, инвестиционные льготы и т.д.)')], default='fin', max_length=4, verbose_name='Тип поддержки')),
                ('branch', models.ManyToManyField(blank=True, to='organizations.Branch', verbose_name='Отрасль')),
                ('departments', models.ManyToManyField(blank=True, to='organizations.Department', verbose_name='Департаменты')),
                ('okveds', models.ManyToManyField(blank=True, to='organizations.Okved', verbose_name='ОКВЭДЫ')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='support_measures', to='organizations.Region', verbose_name='Регион')),
                ('sizes', models.ManyToManyField(blank=True, to='organizations.OrganizationSize', verbose_name='Размеры организаций')),
            ],
        ),
        migrations.CreateModel(
            name='Subsidies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(blank=True, null=True, verbose_name='Сумма')),
                ('date_received', models.DateField(blank=True, null=True, verbose_name='Дата получения')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subsidies', to='organizations.Organization', verbose_name='Организация')),
                ('support_measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subsidies', to='organizations.SupportMeasures', verbose_name='Тип поддержки')),
            ],
            options={
                'verbose_name': 'Субсидия',
                'verbose_name_plural': 'Субсидии',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations', to='organizations.Region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='organization',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizations', to='organizations.OrganizationSize', verbose_name='Размер организации'),
        ),
        migrations.AddField(
            model_name='organization',
            name='tasses',
            field=models.ManyToManyField(blank=True, to='organizations.Tass', verbose_name='ТАСС'),
        ),
    ]