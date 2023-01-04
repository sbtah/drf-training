from rest_framework import permissions
from api.permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin:

    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if (
            user.is_staff
        ):  # Because staff user should have access to all products anyway.
            return qs
        return qs.filter(**lookup_data)
