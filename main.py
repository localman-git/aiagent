import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args: argparse.Namespace = parser.parse_args()

    load_dotenv()
    api_key: str | None = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("could not retrieve api key, please check .env file")

    client: OpenAI = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = api_key
    )
    messages: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": args.user_prompt},
    ]
    response: ChatCompletion = client.chat.completions.create(
        model = "openrouter/free",
        messages = messages
    )

    if args.verbose:
        if not response.usage:
            raise RuntimeError("no usage information recieved")
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response:\n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
