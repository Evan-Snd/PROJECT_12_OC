from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from accounts.models import CustomUser
from core.models import Client, Contract, Event


class Command(BaseCommand):
    help = "Add permission to specifique groupe"
    perms_map =  [
        {'add': '%(app_label)s.add_%(model_name)s'},
        {'view': '%(app_label)s.view_%(model_name)s'},
        {'change': '%(app_label)s.change_%(model_name)s'},
        {'delete': '%(app_label)s.delete_%(model_name)s'}
    ]
    
    def add_arguments(self, parser):
        parser.add_argument('--create', help="Add permission to specifique groupe")
        
    def handle(self, *args, **options):
        comercial_gp, created = Group.objects.get_or_create(name="commercial")
        gestion_gp, created = Group.objects.get_or_create(name="gestion")
        support_gp, created = Group.objects.get_or_create(name="support")
        
        client_ct = ContentType.objects.get_for_model(Client)
        contrat_ct = ContentType.objects.get_for_model(Contract)
        event_ct = ContentType.objects.get_for_model(Event)
        user_ct = ContentType.objects.get_for_model(CustomUser)
        
        client_perm = Permission.objects.filter(content_type=client_ct)
        contrat_perm = Permission.objects.filter(content_type=contrat_ct)
        event_perm = Permission.objects.filter(content_type=event_ct)
        user_perm = Permission.objects.filter(content_type=user_ct)
        
        for perm in client_perm:
            comercial_gp.permissions.add(perm)
        
        for perm in user_perm:
            gestion_gp.permissions.add(perm)
        
        for perm in event_perm:
            gestion_gp.permissions.add(perm)
            if perm.codename == 'add_event':
                comercial_gp.permissions.add(perm)
            if perm.codename == 'change_event':
                support_gp.permissions.add(perm)
            if perm.codename == 'view_event':
                support_gp.permissions.add(perm)
        
        for perm in contrat_perm:
            gestion_gp.permissions.add(perm)
            if perm.codename == 'view_contract':
                comercial_gp.permissions.add(perm)
            
            
            
                