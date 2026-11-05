import os
from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES, THEME
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False, scale=1, elem_classes="twin-chatbot"),
        textbox=gr.Textbox(
            placeholder="Type your message here...",
            show_label=False,
            elem_classes="twin-input",
            lines=1,
            max_lines=6,
        ),
        fill_height=True,
    ).launch(css=CSS, js=JS, theme=THEME, share=False)
