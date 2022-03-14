from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """

        Return 'True' if request method is one of safe methods
        or Sabt.author is equals to request.user
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
