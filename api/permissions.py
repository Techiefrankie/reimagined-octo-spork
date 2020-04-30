from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Read-only permissions are allowed for any request
            return True
        # Write permissions are only allowed to the creator of a meeting schedule
        return obj.created_by == request.user