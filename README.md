# AI-Driven Credential Harvesting Bot

This project demonstrates how AI could potentially be used in credential harvesting and phishing attacks. It is designed for educational purposes in a network security class context.

## Project Components

1. Web Scraper: Extracts data from a mock forum website
2. AI Credential Extractor: Uses DistilBERT to identify credentials
3. Phishing Generator: Uses GPT-2 to generate targeted phishing messages

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `forum.html`: Mock forum website for demonstration
- `scraper.py`: Web scraping module
- `extractor.py`: Credential extraction using DistilBERT
- `generator.py`: Phishing message generation using GPT-2
- `bot.py`: Main script combining all components

## Usage

Run the main script:
```bash
python bot.py
```

## Note

This project is for educational purposes only to demonstrate potential security vulnerabilities. Do not use for malicious purposes. 