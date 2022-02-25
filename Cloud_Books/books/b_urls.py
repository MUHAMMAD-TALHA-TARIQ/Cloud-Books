from django.urls import path
from . import views


# Books Application Url Extensions
urlpatterns = [
    path('', views.home, name='home'),

    # Sub-Sections
    path('sub/<section>/', views.sub_sections, name='sub_sections'),

    # Create Sections
    path('create_section/', views.create_section, name='create_section'),

    # Update Sections
    path('update_section/', views.update_section, name='update_section'),

    # Update Sections
    path('drf_creation/', views.create_section_module.as_view(), name='drf_creation'),

    # Json Response
    path('json_tree/', views.json_tree, name='json_tree'),
]
