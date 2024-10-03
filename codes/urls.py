from django.urls import path
from . import views

app_name = 'codes'

urlpatterns =[
    path('', views.codes_list,name='codes-list'),
    path('code/<slug:code_slug>/',views.code_detail,name='code-detail'),
    path('codes/<str:category_name>/',views.codes_per_category,name='category-codes'),
    path('results/codes/',views.search_code,name='search'),
    path('create-code/',views.create_code,name='create-code'),
    path('update-code/<int:code_pk>/',views.update_code,name='update-code'),
    path('faqs/',views.faqs,name='faqs')
]