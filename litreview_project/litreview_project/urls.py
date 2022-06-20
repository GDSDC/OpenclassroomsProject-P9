"""litreview_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views as auth_views
from ticket import views as ticket_views
from review import views as review_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # PAGES
    path('auth/', auth_views.sign_in_form.as_view()),
    path('auth/sign_up/', auth_views.sign_up_form.as_view(), name='sign_up'),
    path('ticket/create/', ticket_views.create_ticket.as_view(), name='create_ticket'),
    path('review/create/', review_views.create_review_ticket.as_view(), name='create_review_ticket'),
    path('posts/', posts_views.posts_page.as_view(), name='posts'),

    # END POINTS
    path('', auth_views.homepage.as_view(), name='home'),
    path('auth/logout/', include("django.contrib.auth.urls")),
    path('ticket/<int:id>/delete/', ticket_views.delete_ticket.as_view(), name='delete_ticket'),
    path('ticket/<int:id>/edit/', ticket_views.edit_ticket.as_view(), name='edit_ticket'),
    path('review/ticket_id_<int:ticket_id>/create/', review_views.create_review_from_ticket.as_view(), name='create_review_from_ticket'),
    path('review/<int:id>/delete/', review_views.delete_review.as_view(), name='delete_review'),
    path('review/<int:id>/edit/', review_views.edit_review.as_view(), name='edit_review'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
