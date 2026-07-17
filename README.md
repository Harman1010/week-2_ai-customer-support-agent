## Welcome to AI Customer Support Assistant

AI Customer Support Assistant is an LLM-powered FAQ assistant for a fictional e-commerce platform (ShopZone). It uses LangChain and Gemini 2.5 Flash to answer customer queries by grounding responses in a predefined FAQ knowledge base, enabling natural language understanding while avoiding unsupported answers.

## Architecture

```text
User Query
     │
     ▼
Frontend (HTML/CSS/JS)
     │
     ▼
FastAPI Backend
     │
     ▼
Prompt Template
     │
     ▼
FAQ Knowledge Base
     │
     ▼
Gemini 2.5 Flash
     │
     ▼
Generated Response
```

## Features

Modular project structure with clear separation of frontend, backend, AI service, and routing.
End-to-end pipeline connecting the frontend, FastAPI backend, and LLM.
Reusable prompt templates using LangChain.
FAQ-grounded responses to reduce hallucinations.
Supports both CLI and web interface.
Easily extendable to larger knowledge bases or RAG pipelines.

## Tech Stack

### Frontend:

HTML5
CSS
JavaScript

### Backend:

FastAPI
CORS

### AI:

LangChain
LLM API

Model used:

Gemini-2.5-Flash

## Installation

1. Clone the repository.

2. Create a `.env` file using the provided `.env.example`.

3. Install dependencies.

```powershell
pip install -r requirements.txt
```

4. Create a virtual environment.

```powershell
python -m venv venv
```

5. Activate it.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\Activate.ps1
```

## How to Run

### CLI

```powershell
python -m test
```

### Web Interface

Start the FastAPI server:

```powershell
uvicorn app:app --reload
```

Then open:

```text
frontend/index.html
```

using Live Server or the VS Code Integrated Browser.

## Examples

Query What is refund policy ?
Assistant : Products can be returned within 7 days of delivery if they are unused and in their original packaging.

Refunds are processed after inspection:
*   **UPI:** 2–3 days
*   **Card:** 5–7 days

Query  How can I contact customer support ?
Assistant : You can contact our customer support team via:

*   **Email:** support@shopzone.com
*   **Phone:** +91-1800-555-1234

Query When can I contact support ?
Assistant : Our customer support team is available Monday to Saturday from 9:00 AM to 8:00 PM IST.

Query I want to order
Assistant : I understand you want to place an order. The FAQs do not provide specific instructions on how to order.

Please contact our customer support team for assistance with placing an order:

Email: support@shopzone.com
Phone: +91-1800-555-1234

## Limitations

Uses the complete FAQ file as prompt context.
Best suited for small to medium-sized FAQ datasets.
Future enhancement: semantic retrieval (RAG) for large knowledge bases.