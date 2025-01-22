# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import google.generativeai as genai
# from multimodal_api import settings
# from .serializers import AIResponseSerializer
# from .models import AIResponse

# api_key = settings.GOOGLE_AI_API_KEY

# class MultimodalLiveView(APIView):
#     def post(self, request):

#         user_message = request.data.get("message", "")
#         if not user_message:
#             return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

#         genai.configure(api_key=api_key)
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(user_message)
#         print(response.text)
        
        
#         ai_response = AIResponse.objects.create(
#                 user_message=user_message,
#                 ai_response=response.text
#             )
#         return Response({"response": response.text}, status=status.HTTP_200_OK)
    

# def ResponseView(request):
#     if request.method == "GET":
#         data = AIResponse.objects.all
#         serializer = AIResponseSerializer(data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

