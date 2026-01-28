# Memory-consolidator

Memory Consolidator – AI Chat Application
📌 Overview

Memory Consolidator is a FastAPI-based web application that provides a chat interface backed by an AI model (OpenAI GPT).
Users can log in, chat with the AI, and explicitly end a conversation, triggering backend logic that condenses the conversation into long-term memories and an identity stack, which are then stored in a database.

The project is designed with clear architectural and design patterns in mind (Service Layer, Data Mapper, Separated Presentation, Range/TimePoint, etc.) and serves both as a functional prototype and a learning-oriented architecture example.

🧱 Architecture at a Glance

Frontend

HTML + CSS + Vanilla JS

Client-side session state (messages, theme) stored in localStorage

Explicit “End Chat” action triggers memory consolidation

Backend

FastAPI (stateless API)

Service Layer for business logic

SQLAlchemy ORM for persistence

OpenAI GPT API used via a gateway client

Database

Lightweight SQL database (e.g. SQLite)

Stores:

Users (login + password hash)

Long-term memory objects

Identity stack entries

Temporal metadata (time ranges)

INSTALATION

git clone https://github.com/wojtek777/Memory-consolidator
cd Memory-consolidator

pip3 install -r requirements.txt

RUNNING THE APP

uvicorn app.main:app --reload
