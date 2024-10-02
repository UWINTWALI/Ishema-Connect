from django.urls import path
from .views import follow_organization, unfollow_organization, manage_organization, organization_list

app_name='dashboard'
urlpatterns = [
    path('organizations/', organization_list, name='organization_list'),
    path('organizations/<int:organization_id>/follow/', follow_organization, name='follow_organization'),
    path('organizations/<int:organization_id>/unfollow/', unfollow_organization, name='unfollow_organization'),
    # path('organizations/create/',create_organization, name="create_organization" ),
    path('organizations/manage/',manage_organization, name="manage_organization" ),
]