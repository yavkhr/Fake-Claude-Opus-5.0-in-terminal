
# MyDeepSeekChat

MyDeepSeekChat is a simple terminal AI assistant made with Python.

It lets you talk with DeepSeek in the terminal.

## Features

- Chat in terminal
- Use DeepSeek API
- Save chat history in `chat_history.json`
- Load history when the app starts
- Nice terminal interface with `rich`
- `/exit` command to close the app

## Requirements

- Python 3.10 or newer
- DeepSeek API key

## Install

1. Open the project folder.
2. Install the packages:

```bash
pip install -r requirements.txt
```

## Setup

Create a file named `.env` in the project folder.

Add your API key:

```env
DEEPSEEK_API_KEY=your_api_key_here
```

You can also use `.env.example` as a sample file.

## Run

```bash
python main.py
```

## How it works

1. The app loads `chat_history.json` when it starts.
2. If the file does not exist, the app creates a new chat history.
3. Every user message and AI answer is saved in JSON.
4. Next time you open the app, the history is loaded again.

## Project files

```text
MyDeepSeekChat/
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── chat_history.json
```

## Commands

- `/exit` - close the app

## License

This project is for learning and personal use.
```