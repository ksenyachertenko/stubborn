from django.urls import path, re_path

from apps import views

urlpatterns = [
    path('log/<uuid:log_id>/stub/', views.StubRequestView.as_view(), name='stub_it'),
    path('srv/export/<application_id>/', views.ExportToFile.as_view(), name='export'),
    path('srv/import/', views.ImportFromFile.as_view(), name='import'),
    path('srv/team/join/<team_id>/', views.JoinTeam.as_view(), name='join_team'),
    path('srv/team/leave/<team_id>/', views.LeaveTeam.as_view(), name='leave_team'),
    re_path(r'^srv/alive/?$', views.HealthCheckView.as_view(), name='alive'),
    re_path(r'^(?P<app_slug>[\w-]+)/?(?P<resource_slug>[\w-]+)?/?$',
            views.ResponseStubView.as_view(),
            name='stub-url'
    ),
    re_path(
        r'^(?P<app_slug>[\w-]+)/?(?P<resource_slug>[\w-]+)?/?(?P<tail>.+)$',
        views.ResponseStubView.as_view(),
        name='full-proxy-url',
    ),
]
