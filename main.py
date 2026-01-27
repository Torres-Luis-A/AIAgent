import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
#gittest

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="Generate content using Gemini API.")
    parser.add_argument('user_prompt', type=str, help="user prompt")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")
    args = parser.parse_args()
    messages=[types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(model='gemini-2.5-flash',
                                            contents=messages,
                                            config=types.GenerateContentConfig(system_instruction=system_prompt,temperature=0,tools=[available_functions]))
    if args.verbose:
        if response.usage_metadata == None:
            raise RuntimeError("Usage metadata is None.")
        else:
            print(f"User prompt:{args.user_prompt}")
            print(f"Prompt tokens:{response.usage_metadata.prompt_token_count}")
            print(f"Response tokens:{response.usage_metadata.candidates_token_count}")
            print(response.text)
    else:
        for function_call in response.function_calls:
            if function_call.name != "":
                print(f"Calling function: {function_call.name}({function_call.args})")
            else:
                print(response.text)
if __name__ == "__main__":
    main()
