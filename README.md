# Fake News Detection Using NLP and Machine Learning

## Overview
A simple Fake News Detection system built using NLP and Machine Learning.
The model classifies news text as Fake or Real and exposes predictions via a REST API.

## Tech Stack
- Python
- NLP (TF-IDF)
- Machine Learning (Logistic Regression)
- Flask
- Git & GitHub

## How It Works
- Text data is vectorized using TF-IDF
- A Logistic Regression model is trained
- Flask API exposes a /predict endpoint

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python app.py

3. Test API:
   POST /predict
   {
     "news": "Your news text here"
   }
