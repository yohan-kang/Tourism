from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    def has_object_permission(self, request, view, obj):
      # user = request.user
      if not request.user.is_staff:
        return False
      # if user.has_perm("board.view_board"):
      #   return False
      return super().has_permission(request, view)()


    # def has_object_permission(self, request, view, obj):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if request.user.is_staff:
    #       if user.has_perm("board.add_board"):
    #         return True
    #       if user.has_perm("board.delete_board"):
    #         return True
    #       if user.has_perm("board.change_board"):
    #         return True
    #       if user.has_perm("board.view_board"):
    #         return False
    #     return False
        # return super().has_object_permission(request, view, obj)()

