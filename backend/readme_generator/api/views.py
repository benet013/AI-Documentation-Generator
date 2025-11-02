from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import os
from .models import READMERequest
from .serializers import ReadmeSerializer
from groq import Groq

class ReadmeRequestViewset(ModelViewSet):
    queryset = READMERequest.objects.all()
    serializer_class = ReadmeSerializer
    
    def create(self, request):
        print("Received README generation request:", request.data)
        api_key = os.getenv("documentation_generation_api_key")

        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
            {
                "role": "user",
                "content": f"summarize this github/gitlab repository and generate me a full readme.md file for it: {request.data.get('url')}",
            }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )

        print("Groq API response:", completion.choices[0].message.content)


        
        # filepath = "./readmeFiles/readme.md"
        # with open(filepath, "w") as f:
        #     f.write("# Sample README\nThis is a sample README file generated for testing.\n")
        # f.close()
        return Response({"message": f"README generation request received. {request.data}"}, status=201)
        