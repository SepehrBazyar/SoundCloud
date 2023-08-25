from rest_framework import permissions


class IsOwnerOrReadOnlyPermission(permissions.BasePermission):
    message = "Owner or read only permission of album"
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.artist == request.user
