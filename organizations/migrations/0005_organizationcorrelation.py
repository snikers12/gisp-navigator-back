# Generated by Django 2.2.15 on 2021-05-23 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20210523_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationCorrelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlation', models.FloatField(default=0, verbose_name='Коэффициент')),
                ('org_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='correlation_1', to='organizations.Organization')),
                ('org_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='correlation_2', to='organizations.Organization')),
            ],
            options={
                'verbose_name': 'Близость организации',
                'verbose_name_plural': 'Близости Организаций',
                'unique_together': {('org_1', 'org_2')},
            },
        ),
    ]
