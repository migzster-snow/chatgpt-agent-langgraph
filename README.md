# chatgpt-agent-langgraph

A simple example using **LangGraph** and **OpenAI's GPT-4o** model to build an interactive ChatGPT-style agent.

## Overview

* Loads API keys from `.env`.
* Uses **LangChain** and **LangGraph** to connect with OpenAI’s GPT-4o.
* Accepts user input from the terminal.
* Prints the model’s response to the console.

## Files

* `main.py` — main code for the agent
* `requirements.txt` — dependencies
* `.env` — environment variables (e.g., OpenAI API key)
* `LICENSE` — MIT License

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your OpenAI API key in the `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Run the script:

```bash
python main.py
```

Example:

```
Prompt: What is computer science?
gpt-4o: Computer science is the study of computers and computational systems...
```

## License

This project is licensed under the MIT License.
