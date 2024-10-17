import ast
import sys
import threading
import time
import openai
import json
from openai import OpenAI

class OpenAIFormatter:
    def __init__(self, api_key, dev_view=False):
        self.client = OpenAI(api_key=api_key)
        self.dev_view = dev_view
        self.stop_event = threading.Event()

    def get_format_from_model(self, prompt, model):
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that formats responses in specific ways."},
                {"role": "user", "content": prompt}
            ],
        )
        response = completion.choices[0].message.content
        total_completion_tokens = completion.usage.total_tokens
        if self.dev_view:
            print("\n======================================")
            print(f"{total_completion_tokens} tokens ")
        return response

    def parse_response(self, response):
        # Strip code block delimiters if present
        if "```" in response:
            response = response.split("```")[1].strip()
            if response.startswith("python") or response.startswith("json"):
                response = response[response.index('\n') + 1:].strip()

        # Check if the response is a JSON-like object or Python literal (including tuples)
        if response.startswith("{") or response.startswith("[") or response.startswith("("):
            try:
                # Try to parse as JSON (won't work for tuples)
                return json.loads(response)
            except json.JSONDecodeError:
                pass

            try:
                # Try to parse as a Python literal (which includes tuples)
                return ast.literal_eval(response)
            except Exception as e:
                return f"Error parsing as Python: {e}", "error"

        # Return the raw response if it's neither JSON nor Python tuple-like
        return response

    def animate(self):
        while not self.stop_event.is_set():
            for char in "|/-\\":
                sys.stdout.write(f"\rCalculating {char}")
                sys.stdout.flush()
                time.sleep(0.2)
            sys.stdout.write("\r")

    def process_prompt(self, prompt, model="gpt-4o-mini", code_output=False):
        animation_thread = threading.Thread(target=self.animate)
        animation_thread.start()

        response = self.get_format_from_model(prompt, model)

        if self.dev_view:
            print("Generated Response:")
            print(response)

        data = self.parse_response(response)
        if self.dev_view:
            print("\nParsed Data:")
            print(data)
            print("\n======================================")

        self.stop_event.set()
        animation_thread.join()
        print("Processing complete!")

        if code_output:
            return data
        else:
            return response

# Example usage:
if __name__ == "__main__":
   pass
