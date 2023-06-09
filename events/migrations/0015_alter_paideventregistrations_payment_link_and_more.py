# Generated by Django 4.2.1 on 2023-05-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0014_alter_paidevents_invitation_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paideventregistrations",
            name="payment_link",
            field=models.URLField(
                blank=True, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AlterField(
            model_name="paideventregistrations",
            name="payment_status",
            field=models.TextField(
                blank=True,
                choices=[
                    ("CREATED", "Платеж создан"),
                    ("WAITING", "Платёж в обработке / ожидает оплаты"),
                    ("PAID", "Платёж оплачен"),
                    ("EXPIRED", "Время жизни счета истекло. Счет не оплачен."),
                    ("REJECTED", "Платёж отклонен"),
                ],
                default="CREATED",
                null=True,
                verbose_name="Статус оплаты",
            ),
        ),
    ]
