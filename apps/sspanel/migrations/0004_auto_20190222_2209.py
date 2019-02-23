# Generated by Django 2.0 on 2019-02-22 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0003_auto_20181009_0909")]

    operations = [
        migrations.CreateModel(
            name="UserOrder",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "created"), (1, "paid"), (2, "finished")],
                        db_index=True,
                        verbose_name="订单状态",
                    ),
                ),
                (
                    "out_trade_no",
                    models.CharField(
                        db_index=True, max_length=64, unique=True, verbose_name="流水号"
                    ),
                ),
                (
                    "qrcode_url",
                    models.CharField(max_length=64, null=True, verbose_name="支付连接"),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="金额"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="时间"
                    ),
                ),
                (
                    "expired_at",
                    models.DateTimeField(db_index=True, verbose_name="过期时间"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={"verbose_name_plural": "用户订单"},
        ),
        migrations.AlterIndexTogether(
            name="userorder", index_together={("user", "status")}
        ),
    ]
