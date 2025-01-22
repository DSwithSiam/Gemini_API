from django.urls import path
from .views import MultimodalLiveView, ResponseView

urlpatterns = [
    path('genai/', MultimodalLiveView.as_view(), name='multimodal-live'),
    path("responses_list/", ResponseView, name="response-view"),
]
