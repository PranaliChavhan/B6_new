"""Library_proj URL Configuration

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
from book1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+ [
path('admin/', admin.site.urls), 
path('home/', views.homepage, name = "homepage"),
path('show-all-books/', views.show_all_books, name = "show_all_books"),
path('edit-data/<int:id>', views.edit_data, name = 'edit_data'),
path('delete-data/<int:id>', views.delete_data, name='delete_data'),
path('delete-all-data', views.delete_all_data, name="delete_all_data"),
path('soft-delete/<int:id>', views.soft_delete, name='soft_delete'),
path('recover-books/<int:id>', views.recover_books, name='recover_books'),
path('show-inactive-books', views.show_inactive_books, name = 'show_inactive_books'),
path('soft-delete-all/', views.soft_delete_all, name = "soft_delete_all"),
path('__debug__/', include('debug_toolbar.urls')),
path('form-home/', views.form_home, name ='form_home'),
path('book-data/', views.book_data, name='book_data'),
path('addr-form/', views.address_form, name='addr_form'),
path('users/', views.index, name='users')
]

urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]
