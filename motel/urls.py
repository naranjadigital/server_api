from django.urls import path

from motel.views import *

app_name = 'bo'

urlpatterns = [
    path('api/v1/distrito/', ApiDistritoList.as_view()),
    path('api/v1/distrito/<int:pk>', ApiDistritoEdit.as_view()),

    path('api/v1/motel/', ApiMotelList.as_view()),
    path('api/v1/motel/<int:pk>', ApiMotelEdit.as_view())
]