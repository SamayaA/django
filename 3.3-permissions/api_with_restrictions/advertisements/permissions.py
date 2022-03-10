from rest_framework.permissions import BasePermission

class AdvertisementPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        #Is not DRAFT
        if request.method == 'GET' and \
            (obj.status != 'DRAFT' or request.user == obj.creator):
            return True
        # is user creator or admin
        return request.user == obj.creator or request.user.is_staff
             