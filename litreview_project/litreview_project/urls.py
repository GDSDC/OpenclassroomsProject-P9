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
from feed import views as feed_views
from follows import views as subscriptions_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # PAGES
    path('auth/', auth_views.SignInForm.as_view(), name='authentication'),
    path('auth/sign_up/', auth_views.SignUpForm.as_view(), name='sign_up'),
    path('ticket/create/', ticket_views.CreateTicket.as_view(), name='create_ticket'),
    path('review/create/', review_views.CreateReviewTicket.as_view(), name='create_review_ticket'),
    path('posts/', posts_views.PostsPage.as_view(), name='posts'),
    path('subscriptions/', subscriptions_views.Subscriptions.as_view(), name='subscriptions'),
    path('feed/', feed_views.FeedPage.as_view(), name='feed'),

    # END POINTS
    path('', auth_views.HomePage.as_view(), name='home'),
    path('auth/logout/', include("django.contrib.auth.urls")),
    path('ticket/<int:id>/delete/', ticket_views.DeleteTicket.as_view(), name='delete_ticket'),
    path('ticket/<int:id>/edit/', ticket_views.EditTicket.as_view(), name='edit_ticket'),
    path('review/ticket_id_<int:ticket_id>/create/', review_views.CreateReviewFromTicket.as_view(), name='create_review_from_ticket'),
    path('review/<int:id>/delete/', review_views.DeleteReview.as_view(), name='delete_review'),
    path('review/<int:id>/edit/', review_views.EditReview.as_view(), name='edit_review'),
    path('subscriptions/followed_user_id_<int:followed_user_id>/delete/', subscriptions_views.DeleteSubscription.as_view(), name='delete_subscription'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
