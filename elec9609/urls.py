"""elec9609 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  p
    ath('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
import xadmin
from elec9609.settings import  MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewset
from users.views import UserViewset

router = DefaultRouter()

#configure url for goods
router.register(r'goods', GoodsListViewSet, base_name="goods-list")

#configure url for category
router.register(r'categorys', CategoryViewset, base_name="category-list")

router.register(r'users', UserViewset, base_name="users")



from goods.views import GoodsListViewSet

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    re_path(r'^ api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^',include(router.urls)),
    #doc
    re_path(r'docs/',include_docs_urls(title="Neptune")),

    #drf token auth
    re_path(r'^api-token-auth/', views.obtain_auth_token),

    #jwt auth
    re_path(r'^login/', obtain_jwt_token),
]
