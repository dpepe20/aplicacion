from rest_framework.permissions import BasePermission, SAFE_METHODS
from restprofile.views import *



class IsOwnerOrReadOnly(BasePermission):
	message = "MAS NIVEL SEGURIDAD."
	my_safe_method = ['GET', 'PUT']
	def has_permisson(self, request, view):
		if request.method in self.my_safe_method:
			return True
		return False

	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.id == request.user.id
		