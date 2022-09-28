from rest_framework import permissions


class IsPartOfOrganisation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.organisation.org_members


class IsPartOfProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.members
