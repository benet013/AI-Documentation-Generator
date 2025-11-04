from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from .serializers import ReadmeSerializer
from groq import Groq
import zipfile, io, os


class ReadMeGeneratorView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def post(self, request):
        
        def generateResult(data):
            api_key = os.getenv("documentation_generation_api_key")
            client = Groq(api_key=api_key)
            name_completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Give me a short, single-word name for this repository: {data}.\n\n"
                            "Output only the name itself — no explanations, no punctuation, and no extra words. "
                            "Do not include phrases like 'Here is a possible name' or 'I suggest'. "
                            "Return just one clean word suitable for a README file name."
                        ),
                    }
                ],
                temperature=1,
                stream=False,
            )
            
            readme_completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Generate a professional and complete `README.md` file for this repository: {data}.\n\n"
                            "Output *only* the raw Markdown content. Do not include any introductory text like "
                            "'Here is a possible README' or 'Generated README content'. "
                            "Start your response directly with the first Markdown header (e.g. '# Project Name'). "
                            "Do not wrap the Markdown in code fences."
                        ),
                    }
                    ,
                ],
                temperature=1,
                max_tokens=1024,
                stream=False,
            )

            nameFile = name_completion.choices[0].message.content
            readmeFile  = readme_completion.choices[0].message.content
            print("Generated README content:", nameFile)
            print("___________________________________________")
            print("Generated README content:", readmeFile)

            filepath = f"./readmeFiles/{nameFile}README.md"
            with open(filepath, "w") as f:
                f.write(readmeFile)
            f.close()
        
        print(request.data)
        
        url = request.data['data']
        if url:
            try:
                generateResult(url)
                return Response({'message': 'ALl GOOD'}, status=status.HTTP_200_OK)
            except Exception as exc:
                import logging
                logging.exception("Error generating from URL")
                return Response({"error": "internal error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        else:
            serializer = ReadmeSerializer(data=request.data)
            if serializer.is_valid():
                zip_file = serializer.validated_data['zip_file']
                with zipfile.ZipFile(zip_file, 'r') as z:
                    file_list = z.namelist()
                    print("Received ZIP file with contents:", file_list)
                    selected_files = []
                    for name in file_list:
                        if any(name.lower().endswith(ext) for ext in (".png", ".jpg", ".gif", ".pdf", ".exe", ".dll", ".zip")):
                            continue
                        if name.endswith('/'):
                            continue
                        
                        data = z.read(name)
                        
                        if len(data) > 200_000:
                            continue
                        
                        try:
                            text = data.decode('utf-8')
                        except UnicodeDecodeError:
                            continue
                        
                        selected_files.append((name, text))
                
                def clip(s, max_chars=4000):
                    return s[:max_chars]
                
                filesForPrompt = []
                for name, text in selected_files:
                    filesForPrompt.append(f"\n---\nFILE: {name}\n{clip(text, 8000)}")
                
                codeCorpus = "".join(filesForPrompt)
                
                generateResult(codeCorpus[:12000])
                
                return Response({'message': 'ALl GOOD'}, status=status.HTTP_200_OK)
            
            else:
                return Response(serializer.errors, status=400)
        