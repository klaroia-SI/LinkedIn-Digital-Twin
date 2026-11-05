# Digital Twin

A chatbot that represents you on a website. It answers questions about your career using your LinkedIn profile and a short personal summary, and it can notify you via Pushover when a visitor leaves their email or asks something it can't answer. Built with OpenAI and Gradio.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in your keys
```

- `OPENAI_API_KEY`: from platform.openai.com
- `PUSHOVER_USER` / `PUSHOVER_TOKEN`: from pushover.net (optional but needed for notifications)

## Make it yours

1. Copy `summary.example.txt` to `summary.txt` and write about yourself.
2. Export your LinkedIn profile as a PDF and save it as `linkedin.pdf`.

Both files are gitignored so your personal data stays out of the repo. Without them the app falls back to the sample files, which describe a fictional person.

## Run

```bash
python app.py
```

Then open the local URL Gradio prints.

## Files

- `app.py`: chat loop with tool calling and the Gradio UI
- `context.py`: builds the system prompt from your summary and LinkedIn data
- `tools.py`: Pushover notification tools
- `styles.py`: theme, CSS and example prompts
