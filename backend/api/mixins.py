from .Permissions import IsStaffPermission


class IsStaffPermissionMixin():
    permission_classes = [IsStaffPermission]