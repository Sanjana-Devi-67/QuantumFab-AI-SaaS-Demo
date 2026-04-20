# QuantumFab AI SaaS Demo

## Overview
QuantumFab is an AI-powered SaaS platform designed to assist with intelligent design generation and processing. It combines a frontend interface, backend services, and an AI engine to deliver automated solutions.

## Features
- AI-based design generation  
- FastAPI backend for handling requests  
- Interactive frontend interface  
- Scalable microservice architecture  
- Easy local setup and deployment  

## Tech Stack
- Frontend: React.js  
- Backend: FastAPI  
- AI Engine: Python (ML/AI models)  
- Server: Uvicorn  

## Setup Instructions

### 1. Clone the Repository
git clone <your-repo-url>
cd QuantumFab-AI-SaaS-Demo

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run AI Engine
cd ai_engine
python -m uvicorn main:app --port 8001 --reload

### 5. Run Backend
cd backend
python -m uvicorn main:app --port 8000 --reload

### 6. Run Frontend
cd frontend
npm install
npm start

## Usage
- Open browser at: http://localhost:3000
- Use the interface to generate AI-based designs
- Backend communicates with AI engine to process requests

## Notes
- Ensure all services are running simultaneously  
- Check CORS settings if facing issues  
- Use correct ports as specified  

## Future Improvements
- Model optimization  
- Cloud deployment  
- Enhanced UI/UX  
- Authentication system  
