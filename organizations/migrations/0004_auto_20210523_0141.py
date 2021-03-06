# Generated by Django 2.2.15 on 2021-05-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20210522_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportmeasures',
            name='is_sofinance',
            field=models.BooleanField(default=False, verbose_name='Необходимость софинансирования проекта'),
        ),
        migrations.AddField(
            model_name='supportmeasures',
            name='regularity_select',
            field=models.CharField(choices=[('regular', 'На регулярной основе'), ('every_year', 'Ежегодно'), ('one_time', 'Единоразово'), ('every_month', 'Ежемесячно'), ('not_more_two_times', 'Не более 2 раз в год'), ('every_kvartal', 'Ежеквартально'), ('two_times_per_year_2_4_kvartal', '2 раза в год (во 2 и 4 квартале)'), ('two_times_per_year_1_3_kvartal', '2 раза в год (во 1 и 3 квартале)')], default='regular', max_length=30, verbose_name='Регуляронсть оказания мер поддержки'),
        ),
        migrations.AddField(
            model_name='supportmeasures',
            name='type_format_support',
            field=models.CharField(choices=[('not_defined', 'Не определено'), ('credit', 'Возвратная (займ, кредит)'), ('consultation', 'Консультации'), ('grant', 'Грант'), ('subsidian', 'Субсидиарная'), ('guarantee', 'Гарантии (поручительства)'), ('regulator', 'Регуляторная'), ('property_support', 'Имущественная поддержка'), ('education_help', 'Образовательная поддержка')], default='not_defined', max_length=20, verbose_name='Формат предоставления поддержки'),
        ),
    ]
