from rest_framework.permissions import BasePermission

class IsCEO(BasePermission):
    """
    Allows access only to CEOs.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'CEO'

class IsStoreManager(BasePermission):
    """
    Allows access only to Store Managers.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'STORE_MANAGER'
