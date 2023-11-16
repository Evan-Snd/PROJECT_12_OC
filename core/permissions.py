from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission


class IsAuthUser(BasePermission):
    def __init__(self, groups=None) -> None:
        super().__init__()
        self.groups: str = groups

    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            return _has_group_permissions(request.user, self.groups)
        return False


def _is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permissions(user, groups):
    return any([_is_in_group(user, group_name) for group_name in groups])


class IsCommercial(IsAuthUser):
    def __init__(self) -> None:
        super().__init__(['commercial'])

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permissions(
            request.user,
            self.groups)
        print(has_group_permission)
        if not has_group_permission or not obj.commercial_contact == request.user:
            return False
        return True


class IsSupport(IsAuthUser):
    def __init__(self) -> None:
        super().__init__(['support'])

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permissions(request.user, self.groups)
        print(has_group_permission)
        if not has_group_permission or not obj.support == request.user:
            return False
        return True


class IsGestion(IsAuthUser):
    def __init__(self) -> None:
        super().__init__(['gestion'])

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permissions(request.user, self.groups)
        print(has_group_permission)
        if not has_group_permission:
            return False
        return True