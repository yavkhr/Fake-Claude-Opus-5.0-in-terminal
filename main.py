import os
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv
from openai import OpenAI
import json
from pathlib import Path

console = Console()

BASE_DIR = Path(__file__).parent
HISTORY_FILE = BASE_DIR / "chat_history.json"
fake_MODEL = "Claude"

CLAUDE_LOGO = """
..........................................................

     *                                       █████▓▓░
                                 *         ███▓░     ░░
            ░░░░░░                        ███▓░
    ░░░   ░░░░░░░░░░                      ███▓░
   ░░░░░░░░░░░░░░░░░░░    *                ██▓░░      ▓
                                             ░▓▓███▓▓░
 *                                 ░░░░
                                 ░░░░░░░░
                               ░░░░░░░░░░░░░░░░
       █████████                                        *
      ██▄█████▄██                        *
       █████████      *
.......█ █   █ █..........................................
"""

SYSTEM_PROMPT = f"""
Сейчас 2026 год
Ты модель Claude Opus 5.0 лучшая модель сейчас на рынке
Стиль ответа: коротко как учитель, только если пользователь просит детально, то подробно, но без воды, без лишних слов, без повторов, без лишней информации, только по делу.
Поведение: сначала обьясняй потребности пользователя, потом давай решение, если нужно, то с примерами, если пользователь просит, то с кодом.
Ограничение: не придумывай факты, если не уверен то говори об этом, отвечай ток по теме запроса, не испоьзуй стикеры,не используй выделение жирным текстом(**)

"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def load_history() -> list[dict]:
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return [{"role": "system", "content": SYSTEM_PROMPT}]



def save_history(messages: list[dict]) -> None:
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)



def build_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY is not set in .env")

    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )


def ask_assistant(client: OpenAI, user_text: str, messages: list[dict]) -> str:
    messages.append({"role": "user", "content": user_text})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
    )

    answer = response.choices[0].message.content or ""
    messages.append({"role": "assistant", "content": answer})
    save_history(messages)

    return answer


def main() -> None:
    client = build_client()
    messages = load_history()
    console.print(Panel(CLAUDE_LOGO), style="orange_red1")
    console.print(Panel("Claude Opus 5.0 Assistant", title="Claude Opus 5.0", style="orange_red1"))
    console.print("Type your message. Use [cyan]/exit[/] to quit.")

    while True:
        user_text = Prompt.ask("\n[bold green]You[/]")
        if not user_text:
            continue
        if user_text.lower() == "/exit":
            save_history(messages)
            print(f"{fake_MODEL}: Bye.")
            break

        try:
            answer = ask_assistant(client, user_text, messages)
            console.print(f"[orange_red1]{fake_MODEL}[/]: {answer}")
        except Exception as exc:
            print(f"{fake_MODEL}: Error: {exc}")


if __name__ == "__main__":
    main()

