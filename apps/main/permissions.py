from rest_framework import permissions


class IsAuthenticatedAndOwnerOrReadOnly(permissions.BasePermission):
    """
    Проверка на собственника комментария при редактировании/удалении.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.author == request.user)