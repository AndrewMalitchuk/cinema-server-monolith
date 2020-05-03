from rest_framework import permissions


class IsStaffOrAdminWriteOnly(permissions.BasePermission):
    """
    Custom permission for certain REST endpoints

    So if you are certain user or anon - you could only fulfill GET request to marked endpoints; if you are staff or
    admin - you could fulfill all types of requests
    """

    def has_permission(self, request, view):
        """
        Check your user's type to allow access to write operations

        :return True if permission is granted
        """

        if request.user.is_staff is True or request.user.is_superuser is True:
            return True
        elif (request.method == 'GET') and ((request.user.is_staff is False and request.user.is_superuser is False) or request.user.is_anonymous is True):
            return True
        else:
            return False
