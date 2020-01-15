from rest_framework import permissions


class IsStaffOrAdminWriteOnly(permissions.BasePermission):
    """Custom permission for certain REST endpoints

    So if you are certain user or anon - you could only fulfill GET request to marked endpoints; if you are staff or
    admin - you could fulfill all types of requests.
    """

    def has_permission(self, request, view):
        """ Check your user's type to allow access to write operations."""
        if request.user.is_staff == True or request.user.is_superuser == True:
            return True
        elif (request.method == 'GET') and ((
                                                    request.user.is_staff == False and request.user.is_superuser == False) or request.user.is_anonymous == True):
            return True
        else:
            return False
