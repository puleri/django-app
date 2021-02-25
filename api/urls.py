from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.project_views import Projects, ProjectDetail
from .views.task_views import Tasks, TaskDetail

urlpatterns = [
  	# Restful routing
    # path('mangos/', Mangos.as_view(), name='mangos'),
    # path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('projects/', Projects.as_view(), name='projects'),
    path('projects/<int:pk>/tasks/', ProjectDetail.as_view(), name='project_detail'),
    path('projects/<int:pk>/tasks/', Tasks.as_view(), name='tasks'),
    # path('projects/<int:pk>/tasks/<int:pk>', TaskDetail.as_view(), name='tasks'),
]
