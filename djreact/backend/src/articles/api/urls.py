from rest_framework import routers
from django.urls import path
from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, base_name='articles')
urlpatterns = router.urls


# """ from .views import (
#     ArticleDetailView,
#     ArticleListView,
#     ArticleCreateView,
#     ArticleUpdateView,
#     ArticleDeleteView
# )


# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('<pk>', ArticleDetailView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('<pk>/update/', ArticleUpdateView.as_view()),
#     path('<pk>/delete/', ArticleDeleteView.as_view()),
# ] """
