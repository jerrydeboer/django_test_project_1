from django.db import models


class EdosTemplate(models.Model):
    name = models.CharField(max_length=128, default="")
    dns_server_1 = models.CharField(max_length=128, default="8.8.8.8")
    dns_server_2 = models.CharField(max_length=128, default="")
    profile_rule_a = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
