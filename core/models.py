from django.db import models

from accounts.models import CustomUser


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    entreprise_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commercial_contact = models.ForeignKey(to=CustomUser,
                                           on_delete=models.PROTECT,
                                           related_name='client_commercial')

    def __str__(self) -> str:
        return self.full_name


class Contract(models.Model):
    PENDING = 'P'
    SIGNED = 'S'
    CONTRACT_STATUS = (
        (PENDING, 'Pending'),
        (SIGNED, 'signed'),
    )
    client_info = models.ForeignKey(to=Client,
                                    on_delete=models.CASCADE,
                                    related_name='contract_client')
    gestion_contact = models.ForeignKey(to=CustomUser,
                                        on_delete=models.CASCADE,
                                        related_name='contract_gestion')
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    rest_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    contrat_status = models.CharField(max_length=1,
                                      choices=CONTRACT_STATUS,
                                      default=PENDING)

    def __str__(self):
        return str(self.pk)


class Event(models.Model):
    contract = models.ForeignKey(to=Contract,
                                 on_delete=models.CASCADE,
                                 related_name='event_contract')
    client_name = models.ForeignKey(to=Client,
                                    on_delete=models.CASCADE,
                                    related_name='event_client')
    commercial = models.ForeignKey(to=CustomUser,
                                   on_delete=models.CASCADE,
                                   related_name='event_commercial')
    gestion = models.ForeignKey(to=CustomUser,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='event_gestion')
    support = models.ForeignKey(to=CustomUser,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='event_support')
    client_contact = models.TextField()
    event_date_start = models.DateTimeField()
    event_date_end = models.DateTimeField()
    location = models.CharField(max_length=255)
    attendees = models.IntegerField()
    notes = models.TextField()
