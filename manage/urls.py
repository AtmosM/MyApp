"""manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path, include
from django.conf import settings
from django.views.static import serve
from django.urls import path
from system.views import EntitiesListView, DocumentCreate, LoginUser, ViewFiles, FileUpdate, FileCreate, FilesToCategories, SearchFiles, AddEntities, DocumentsToFiles, ViewDocument, SearchDocs, Search, Practice, Practice1,SysBuy, PracticeENG
from system.views import category_detail, entities_form, files_form, logout_user, UserRegister, DeleteCategory, delete_cat, change_password
from django.contrib.auth import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EntitiesListView.as_view(), name='category-list'),
    path(r'cms/', include('cms.urls')),
    path('category/<my_id>/', category_detail, name='category-detail'),
    path('form/', AddEntities.as_view(), name='entities-form'),
    path('add-document/', DocumentCreate.as_view(), name='document-form'),
    path('add-file/', FileCreate.as_view(), name='file-form'),
    path('register/', UserRegister, name='register' ),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name = 'logout'),
    path('files/', ViewFiles.as_view(), name = 'files'),
    path('file-update/<slug:slug>', FileUpdate.as_view(), name = 'file-update'),
    path('files-cat/', FilesToCategories.as_view(), name = 'cat-files'),
    path('search-file/', SearchFiles.as_view(), name = 'search'),
    path('category/<new_id>/delete', delete_cat, name= "delete"),
    path('password-change/', change_password, name='password_change'),
    path('doc-file/', DocumentsToFiles.as_view(), name = 'doc-files'),
    path('documents/', ViewDocument.as_view(), name = 'docs'),
    path('search-docs/', SearchDocs.as_view(), name = 'search-docs'),
    path('search/', Search.as_view(), name = 'search'),
    path('pract/', Practice.as_view(), name = 'pract'),
    path('pract1/', Practice1.as_view(), name = 'pract1'),
    path('buy/', SysBuy.as_view(), name = 'buy'),
    path('AboutCompany/', PracticeENG.as_view(), name = 'eng'),
    #path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
   # path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

    ]
