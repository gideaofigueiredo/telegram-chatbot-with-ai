# Telegram Chatbot with AI

A simple Telegram chatbot built with Python, `python-telegram-bot`, and Google Gemini AI.

## Features

- Responds to `/start`
- Uses Gemini AI to generate responses for incoming messages
- Loads sensitive keys from a `.env` file

<img width="370" height="488" alt="image" src="https://github.com/user-attachments/assets/f0c35182-df77-4d35-9b0a-de77d4ab6a28" />

## Requirements

- Python 3.11+
- `TOKEN` environment variable for the Telegram bot
- `GEMINI_API_KEY` environment variable for Google Gemini API

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   - Windows:
     ```bash
     .venv\Scripts\activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or use `pyproject.toml` with:

   ```bash
   pip install .
   ```

4. Create a `.env` file with:

   ```env
   TOKEN=your_telegram_token
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Run

```bash
python bot.py
```

## Notes

- Keep `.env` out of version control.
- The bot uses `gemini-3-flash-preview` by default.
