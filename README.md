# ⚠️ AIAgent - Educational/Portfolio Project

**WARNING:** This project is for **educational and portfolio use only**. It should not be used in production environments without significant improvements to security, error handling, and validation. Use at your own risk.

---

## Overview

AIAgent is an AI-powered coding assistant that leverages the **Google Gemini 2.5 Flash API** to interact with the file system and execute Python code. The agent can understand user requests and autonomously perform file operations, code execution, and analysis.

## Features

- 🤖 **AI-Powered Assistant**: Uses Google Gemini API for intelligent task planning and execution
- 📁 **File Operations**: List files, read file contents, and write/overwrite files
- 🐍 **Python Execution**: Execute Python scripts with optional arguments
- 🔄 **Multi-turn Conversations**: Maintains context across multiple function calls
- 📊 **Token Usage Tracking**: Monitor API usage with verbose output
- 🎯 **Agentic Loop**: Automatically iterates up to 20 times to complete tasks

## Project Structure

```
AIAgent/
├── main.py                 # Main entry point and agentic loop
├── config.py              # Configuration (max chars, working directory)
├── prompts.py             # System prompt for the AI agent
├── call_function.py       # Function dispatcher and tool definitions
├── functions/
│   ├── get_file_content.py    # Read file contents
│   ├── get_files_info.py      # List files and directories
│   ├── run_python_file.py     # Execute Python scripts
│   └── write_file.py          # Write/overwrite files
├── calculator/            # Example working directory with test scripts
└── pyproject.toml         # Project dependencies and metadata
```

## Requirements

- **Python 3.12+**
- **google-genai** (version 1.12.1)
- **python-dotenv** (version 1.1.0)
- **Google Gemini API Key**

## Installation

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   pip install google-genai==1.12.1 python-dotenv==1.1.0
   ```

4. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the agent with a user prompt:

```bash
python main.py "Your prompt here"
```

### Examples

```bash
# List files in the working directory
python main.py "List all files in the working directory"

# Execute a Python script
python main.py "Run the main.py script in the calculator directory"

# Read a file
python main.py "Read the contents of calculator/README.md"

# Write a file
python main.py "Create a new file called 'test.py' with a simple hello world script"
```

### Verbose Output

For detailed token usage and function call information:

```bash
python main.py "Your prompt" --verbose
```

## Available Functions

The agent can call the following functions:

1. **get_files_info** - List files and directories in a specified path
2. **get_file_content** - Read the contents of a file (truncated at 10,000 characters)
3. **run_python_file** - Execute a Python file with optional arguments
4. **write_file** - Create or overwrite a file with specified content

## Security Considerations

⚠️ **THIS PROJECT HAS SECURITY ISSUES AND IS NOT PRODUCTION-READY:**

- **Path Traversal**: File operations check for directory escape, but this is a basic implementation
- **Code Execution**: Arbitrary Python code execution is enabled—use only with trusted inputs
- **API Key Exposure**: Store API keys securely; never commit `.env` files
- **No Input Validation**: Limited validation on user prompts and file operations
- **Agentic Loop**: The agent can execute up to 20 iterations, potentially leading to infinite loops or excessive API calls

## Configuration

Edit `config.py` to customize:

```python
max_chars = 10000        # Maximum characters to read from a file
WORKING_DIR = "./calculator"  # Default working directory for file operations
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| google-genai | 1.12.1 | Google Gemini API client |
| python-dotenv | 1.1.0 | Load environment variables from `.env` |

## License

This is an educational project. Use freely for learning and portfolio purposes.

## Disclaimer

This project is provided as-is for educational purposes. The authors are not responsible for any misuse, data loss, or security breaches. Do not use in production without thorough security review and hardening.

---

**Last Updated:** February 2, 2026
