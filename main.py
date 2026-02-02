import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

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

    print(f"User prompt:{args.user_prompt}")
    for call in range(20):
        response = client.models.generate_content(model='gemini-2.5-flash',
                                            contents=messages,
                                            config=types.GenerateContentConfig(system_instruction=system_prompt,temperature=0,tools=[available_functions]))
        for candidate in response.candidates:
            messages.append(candidate.content)
        if args.verbose:
            if response.usage_metadata == None:
                raise RuntimeError("Usage metadata is None.")
        
        print(f"Prompt tokens:{response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:{response.usage_metadata.candidates_token_count}")
        if not response.function_calls:
            print(response.text)
            return
        else:
            tools_results = []
            for function_call in response.function_calls:
                tool_result = call_function(function_call, verbose=args.verbose)
                part = tool_result.parts[0]
                tools_results.append(part)
                fr= part.function_response
                data=fr.response
                if args.verbose:
                    print(f"calling function: {function_call.name}({function_call.args})")
                    print(f"-> {data['result']}")
                if part.function_response is None or part.function_response.response is None:
                    raise RuntimeError("Function response is None or empty.")
                if args.verbose:
                    print(f"-> {part.function_response.response}")
            messages.append(types.Content(role="user",parts=tools_results))
    raise RuntimeError("Exceeded maximum number of function call iterations.") 

if __name__ == "__main__":
    main()
