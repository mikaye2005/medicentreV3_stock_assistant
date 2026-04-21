# MedicentreV3 Stock Assistant

A Django-based AI assistant for the **stock module** of MedicentreV3, powered by **Ollama** and a pretrained **Llama model**.  
The system is designed to answer stock-related questions using:

- investigated stock schema knowledge
- live stock summaries from the restored PostgreSQL database
- controlled stock facts from the real database
- a clean dashboard-style user interface

---

## Project Overview

This project focuses on the **stock section** of the MedicentreV3 hospital management system.

The main goal is to build a **ChatGPT-like assistant** that helps users understand the stock module by answering questions in natural language.

Instead of training a model from scratch, the project uses a **pretrained language model** through **Ollama** and connects it to a Django application. The assistant is guided using:

1. manually interpreted stock schema context  
2. live summaries from the actual restored PostgreSQL database  
3. verified stock facts selected according to the user’s question  

This makes the assistant more relevant, more controlled, and more useful for the MedicentreV3 stock workflow.

---

## Main Objective

To design and develop a stock-focused AI assistant that can answer questions about the MedicentreV3 stock module using a pretrained language model, Django, and a restored PostgreSQL database schema.

---

## Current Scope

The current version focuses on:

- stock item definitions
- branch-linked stock items
- stock storage records
- stock movement history
- stock take sessions
- conversation logging
- dashboard presentation
- admin review of saved logs

The system is currently **read-only** with respect to the MedicentreV3 PostgreSQL database.

---

## Key Features

- AI assistant for stock-related questions
- Uses **Ollama** with a local Llama model
- Django web interface
- PostgreSQL connection to restored MedicentreV3 database
- Live stock-aware prompts
- Controlled stock facts based on question type
- Dashboard with stock summary cards
- Low stock alerts
- Recent stock activity
- Saved conversation history
- Django Admin integration for conversation logs

---

## Technologies Used

### Backend
- Python
- Django
- PostgreSQL
- psycopg

### AI Layer
- Ollama
- Llama model

### Frontend
- Django Templates
- HTML
- CSS

### Development Tools
- VS Code
- pgAdmin 4
- Git
- GitHub

---

## Why Django Was Used

Django was chosen because it provides:

- a fast and organized web framework
- URL routing
- template rendering
- model-based database interaction
- migration support
- a built-in admin panel

This made it easier to build both the assistant interface and the backend management tools.

---

## Project Structure

```text
medicentre_stock_assistant/
│
├── assistant/
│   ├── migrations/
│   ├── services/
│   │   ├── answer_parser.py
│   │   ├── db_context.py
│   │   ├── fact_builder.py
│   │   ├── ollama_client.py
│   │   ├── prompt_builder.py
│   │   └── stock_context.py
│   ├── templates/
│   │   └── assistant/
│   │       ├── base.html
│   │       ├── history.html
│   │       └── test_ollama.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── legacydb/
│   ├── models.py
│   └── ...
│
├── stock_ai/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md