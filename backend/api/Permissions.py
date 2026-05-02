from rest_framework import permissions

class IsStaffPermission(permissions.DjangoModelPermissions):

    # override the default perms_map to include view permissions for GET requests
    perms_map = {
        'GET':    ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD':   [],
        'POST':   ['%(app_label)s.add_%(model_name)s'],
        'PUT':    ['%(app_label)s.change_%(model_name)s'],
        'PATCH':  ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    

    def has_permission(self, request, view):
        user = request.user
        
        if not user or not user.is_authenticated or not user.is_staff:
            return False
        
        return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     user = request.user
        
    #     if not user or not user.is_authenticated or not user.is_staff:
    #         return False
        
    #     required_perm = self.method_perm_map.get(request.method)
        
    #     print(required_perm)
    #     print(user.has_perm(required_perm))
    #     if required_perm is None:
    #         return False
        
    #     return user.has_perm(required_perm)
    

    
    # def __init__(self):
    #     self.perms_map = super().perms_map.copy()
    #     self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s'] # Add view permission for GET requests
    
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user and user.is_authenticated and user.is_staff:
    #         if user.has_perm('products.view_product'):
    #             return True
    #         return False
    #     return False
