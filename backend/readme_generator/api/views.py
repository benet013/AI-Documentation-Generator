from django.http import FileResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from .serializers import ReadmeSerializer
from groq import Groq
import zipfile, io, os


class ReadmeDownloadView(APIView):
    def get(self, request):
        file_name = request.GET.get('file')
        file_path = os.path.join("readmeFiles",file_name)
        
        if not os.path.exists(file_path):
            return Http404("File not found")
        
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)

class ReadMeGeneratorView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def post(self, request):
        
        def generateResult(data):
            api_key = os.getenv("documentation_generation_api_key")
            client = Groq(api_key=api_key)
            
            readme_completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": (
                                f"""
                                You are a professional technical writer and senior engineer.
                                Generate a complete, production-ready `README.md` file based on the provided input below.

                                The input may contain either:
                                1. Repository source files (between <<FILES_START>> and <<FILES_END>>), OR
                                2. A JSON-like object describing the project (e.g., {{ "appName": "TodoList", "techStacks": "Django, React" }}).

                                When generating the README:
                                - Output *only* the raw Markdown content — no preamble, explanations, or filler.
                                - Do NOT wrap the output in code fences.
                                - Start immediately with the first header (e.g., '# TodoList').
                                - If only metadata is provided (no files), infer the structure, usage, and setup instructions logically based on the tech stack.
                                - If repository files are provided, base the README entirely on their content.

                                FILES OR INPUT BELOW — do not add or remove these markers:

                                <<FILES_START>>
                                {data}
                                <<FILES_END>>
                                """
                        ),
                    }
                    ,
                ],
                temperature=1,
                max_tokens=1024,
                stream=False,
            )

            readmeFile  = readme_completion.choices[0].message.content
            print("___________________________________________")
            print("Generated README content:", readmeFile)

            filepath = f"./readmeFiles/README.md"
            with open(filepath, "w") as f:
                f.write(readmeFile)
            f.close()
            
            download_url = request.build_absolute_uri(f"/api/download/?file={'README.md'}")
            
            return download_url
        
        print(request.data)
        
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
            
            download_url = generateResult(codeCorpus[:12000])
            
            return Response({'message': 'All good', 'download_url': download_url}, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=400)
    