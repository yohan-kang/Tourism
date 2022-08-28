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
    # def has_permission(self, request, view, obj):
    #   # user = request.user
    # print(user.get_all_permissions())
    #   if not request.user.is_staff:
    #     return False
    #   # if user.has_perm("board.view_board"):
    #   #   return False
    #   return super().has_permission(request, view)()


class IsTechnicianPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    def has_permission(self, request, view):
      user = request.user
      queryset = user.groups.all()
      lst_groups = [g.name for g in queryset] 
      print("-------------------------------------------")
      print(lst_groups)
      print(lst_groups.index('technician'))
      if lst_groups.index('technician') == -1:
        return False

      return super().has_permission(request, view)


class IsReviewerEditorPermission(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
      user = request.user
      # print("===========user.groups.all()==========")
      # print(user.groups.all())
      # print("===========request.user==========")
      # print(request.user)
      # print("===========user.get_all_permissions()==========")
      # print(user.get_all_permissions())

      userGroup = user.groups.all()
      print("-----------userGroup--------")
      print(userGroup.values('name'))
      if user.is_staff:
        return True
      # ↓ This part is not being applied
      if user.has_perm("board.view_board"):
        print("why??")
        return False

    #   return super().has_permission(request, view)()
