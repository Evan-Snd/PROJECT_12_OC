from django.contrib import admin

from core.models import Client, Contract, Event


admin.site.register([Client, Event, Contract])