# AI Documentation Generator

A full-stack application that automatically generates professional `README.md` files from uploaded project source code.  
It uses **Django REST Framework** on the backend and **React (Vite)** on the frontend, providing a clean UI for users to upload `.zip` files and receive ready-to-use documentation.

---

## Overview

**AI Documentation Generator** streamlines the process of writing documentation by analyzing your project’s structure, dependencies, and key files — automatically generating a Markdown README for developers.  

Upload your project’s `.zip` file, click **Generate**, and instantly download a structured, styled `README.md`.

---

## Features

- Upload `.zip` project files directly from the UI  
- AI-powered README generation using backend logic  
- Full-stack setup: Django (API) + React (frontend)  
- Modern Glassmorphism UI  
- Automatically detects dependencies and core project info  
- One-click README download  
- Modular code structure for scalability  

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React (Vite), HTML5, CSS3 |
| **Backend** | Django, Django REST Framework |
| **Build Tools** | Vite, NPM |
| **API Communication** | Axios |
| **Hosting** | Render (Frontend + Backend) |
| **Environment** | Free-tier deployment (Render auto-sleep enabled) |

---

## Project Structure

``` bash
AI-Documentation-Generator-main/
│
├── backend/
│   └── readme_generator/
│       ├── api/
│       │   ├── views.py
│       │   ├── models.py
│       │   ├── serializers.py
│       │   └── urls.py
│       ├── settings.py
│       ├── deployment_settings.py
│       ├── urls.py
│       ├── wsgi.py
│       ├── asgi.py
│       └── readmeFiles/
│
├── frontend/
│   └── client_readmegenerator/
│       ├── src/
│       │   ├── App.jsx
│       │   ├── api.js
│       │   ├── pages/
│       │   │   └── home.jsx
│       │   └── components/
│       │       └── form.jsx
│       ├── package.json
│       ├── vite.config.js
│       └── index.html
│
└── README.md 
```

## Setup Instruction 

### 1. Clone the Repository
``` bash
git clone https://github.com/benet013/AI-Documentation-Generator
cd AI-Documentation-Generator
```

### 2. Backend Setup (Django)

#### a. Navigate to backend folder
``` bash
cd backend/readme_generator
```
#### b. Create and activate a virtual environment
``` bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```
#### c. Install dependencies
``` bash
pip install -r requirements.txt
```
#### d. Run migrations and start the server
``` bash
python manage.py migrate
python manage.py runserver
```

Backend starts on http://127.0.0.1:8000/

### Frontend Setup (React)

#### a. Navigate to frontend folder
``` bash
cd frontend/client_readmegenerator
```
#### b. Install dependencies
``` bash
npm install
```
#### c. Run development server
``` bash
npm run dev
```
Frontend starts on http://localhost:5173/

## Deployment (Render)

Both the **frontend and backend** of this project are fully deployed on **Render**.

### Deployment Summary
| Component | Platform | URL | Notes |
|------------|-----------|-----|------|
| **Frontend** | Render Static Site | https://ai-documentation-generator-client.onrender.com | React app built with Vite |
| **Backend** | Render Web Service | https://ai-documentation-generator-server.onrender.com | Django REST API endpoint |

> ⚠️ **Note:**  
> This project is hosted on Render’s **free tier**, which automatically puts the services to sleep when idle.  
> It may take **30–60 seconds** for the app to start up after inactivity — please be patient while the server wakes up.

---

## How It Works

1. The user uploads their project’s `.zip` file through the **React frontend**.  
2. The file is sent to the **Django REST API** backend.  
3. The backend extracts, analyzes, and identifies project details such as dependencies, structure, and code files.  
4. The system generates a well-formatted `README.md` file based on that analysis.  
5. The frontend then provides a **Download** button for the user to retrieve the generated README instantly.

---

## Future Enhancements

- Integrate GPT for intelligent, context-aware README generation  
- Add user authentication and project history tracking  
- Markdown preview mode before downloading  
- Add light/dark theme switcher  
- Support for `.tar` and `.rar` archive uploads  

---

## Example Generated READMEs

Auto-generated examples are saved under:
``` bash
backend/readme_generator/readmeFiles/
│
├── TaskAPIREADME.md
└── TodoHubREADME.md
```

These files demonstrate how the backend analyzes and creates complete documentation automatically.

---

## Author

**Developed by [benet013](https://github.com/benet013)**  
Full Stack Developer (Backend Focused)  
_Seeking opportunities in software development and open-source collaboration._

---

## Example Workflow

1. Visit the live deployed application on Render.  
2. Upload your project’s `.zip` file from the UI.  
3. Click **Generate** and wait for the backend to process your files.  
4. Once complete, click **Download** to get your generated `README.md`.  
5. Customize or use it directly for your project repository.

---

## Support

If you find this project useful, please consider giving it a **⭐ star** on GitHub.  
Your support helps others discover this project and encourages continued improvements!

---
