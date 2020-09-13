from django.urls import path, include
from rest_framework import routers
from restapisexa.views import BookViewSet, AuthorViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Replica of Amazon')



app_name = 'restapisexa'

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', schema_view),
    path('apis/', include(router.urls))
]
