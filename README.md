<div align="center">

<img src="folio_logo.png" alt="FOLIO Logo" width="180">

# FOLIO

### AI Agent Orchestration Framework

Build intelligent workflows with **task splitting, dynamic tool matching, multi-agent execution, MCP tools, RAG, memory, and multi-model support.**

<p>
  <a href="https://github.com/parin0127-png/folio">
    <img src="https://img.shields.io/badge/GitHub-FOLIO-181717?logo=github" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/parin-prajapati-5b0579376/">
    <img src="https://img.shields.io/badge/LinkedIn-Parin%20Prajapati-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/MCP-1.9.4-6A5ACD" alt="MCP">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange" alt="Status">
</p>

</div>

---

## 🎥 FOLIO Demo

<p align="center">

<a href="media/FOLIO.mp4">
  ▶️ <strong>Watch the FOLIO Demo</strong>
</a>

</p>

---

## Overview

**FOLIO** is a Python-based AI agent orchestration framework that turns natural-language requests into executable workflows.

Instead of requiring users to manually select tools or decide how a task should be executed, FOLIO can:

- Normalize the user's request
- Split complex requests into smaller tasks
- Validate generated tasks
- Dynamically match tasks to available tools
- Select the appropriate agent
- Execute MCP tools
- Pass outputs between multiple steps
- Recover from tool failures
- Use RAG for document-based questions
- Support different models and customized agent behavior

### Core Workflow

```text
User Request
     │
     ▼
Normalizer
     │
     ▼
Task Splitter
     │
     ▼
Validator
     │
     ▼
Tool Matcher
     │
     ▼
Planner
     │
     ▼
Tool Selector
     │
     ▼
Agent Router
     │
     ├───────────────┬───────────────┐
     ▼               ▼               ▼
 Agent 1          Agent 2         Agent 3
     │               │               │
     └───────────────┴───────────────┘
                     │
                     ▼
                  Observer
                     │
                     ▼
               Result / Memory
```

---

# ✨ Features

## 🤖 Multi-Agent Architecture

FOLIO uses three agents with different responsibilities:

| Agent | Responsibility |
|---|---|
| **Agent 1** | Direct execution of deterministic/simple MCP tools |
| **Agent 2** | LLM-powered MCP tool execution using Mistral |
| **Agent 3** | Command/system-level execution |

The **Agent Router** dynamically selects an agent based on the selected tool.

---

## 🧩 Dynamic Task Splitting

FOLIO can turn one natural-language request into multiple executable tasks.

### Example

```text
Get information about Rohit Sharma, make a PDF from it,
and send the PDF to Slack.
```

FOLIO can split it into:

```text
1. Get information about Rohit Sharma
2. Make a PDF from that information
3. Send the PDF to Slack
```

The task splitter uses **spaCy dependency parsing** rather than relying entirely on an LLM.

---

## 🔎 Dynamic Tool Matching

FOLIO does not require the user to know the exact MCP tool name.

Tool matching combines:

- Sentence embeddings
- Cosine similarity
- RapidFuzz token similarity
- Tool descriptions
- Candidate ranking

For example:

```text
User:
send an email
```

Can resolve to:

```text
send_email
```

This allows users to interact with FOLIO naturally without knowing the internal tool names.

---

## 🧠 Brain & Planner

The FOLIO Brain converts the workflow into a compact execution plan.

Example:

```text
agent_2|wikipedia_search|job=get information|input=Rohit Sharma|out=wiki
agent_2|generate_pdf|job=make PDF|in=wiki|out=pdf
agent_2|send_message|job=send PDF|in=pdf|out=sent
```

The plan contains:

- Agent selection
- Tool selection
- Task description
- Input values
- Previous output references
- Output keys

This allows FOLIO to maintain dependencies between tasks.

---

## 🔗 Multi-Step Data Flow

Outputs from previous tasks can become inputs to later tasks.

```text
Wikipedia Search
       │
       ▼
      wiki
       │
       ▼
  Generate PDF
       │
       ▼
      pdf
       │
       ▼
Send / Upload
```

This allows FOLIO to build workflows instead of treating every request as an isolated tool call.

---

## 👁️ Observer & Recovery

FOLIO includes an Observer that monitors tool execution.

If a selected tool fails, the Observer can look for a suitable replacement tool.

```text
Selected Tool
      │
      ▼
  Execution
      │
      ▼
   ┌───────┐
   │ Error │
   └───────┘
      │
      ▼
   Observer
      │
      ▼
Find Substitute
      │
      ▼
Replacement Tool
      │
      ▼
   Continue
```

This helps workflows continue when a suitable fallback exists.

---

## 📚 RAG Pipeline

FOLIO includes a retrieval-augmented generation pipeline for working with user-provided documents.

The RAG pipeline includes:

- Document loading
- Chunking
- BM25 retrieval
- Vector retrieval
- Hybrid retrieval
- Embeddings
- Reranking
- Persistent storage

```text
Documents
    │
    ▼
  Loader
    │
    ▼
 Chunking
    │
    ├───────────────┐
    ▼               ▼
  BM25         Vector Search
    │               │
    └───────┬───────┘
            ▼
    Hybrid Retrieval
            │
            ▼
         Reranker
            │
            ▼
         Context
            │
            ▼
           LLM
```

---

## 🧠 Memory

FOLIO includes memory-related MCP tools for:

- Remembering information
- Recalling information
- Clearing memory
- Saving history

Execution memory is also used to pass outputs between workflow steps.

---

## 🛠️ MCP Tool Ecosystem

FOLIO includes MCP tools covering multiple categories.

### Web & Research

- Web search
- Web scraping
- Wikipedia
- News
- YouTube
- Trends
- arXiv
- Stack Overflow
- GitHub

### Productivity

- File writing
- Excel generation
- PDF generation
- File management
- Email
- Slack
- Reminders

### Information

- Weather
- Country information
- Medicine information
- Visa information
- Time zones
- IP lookup
- WHOIS
- Website status

### Finance

- Stocks
- Cryptocurrency
- Currency conversion

### Travel

- Flights
- Hotels

### Jobs

- Job search
- LinkedIn jobs
- Remote/EU jobs
- Startup search

### Utilities

- QR generation
- Password generation
- Math solving
- Package information
- Command execution
- Translation

---

# 📁 Project Structure

```text
FOLIO/
│
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── requirements.txt
├── test.py
├── folio_logo.png
│
├── media/
│   └── FOLIO.mp4
│
├── folio/
│   ├── __init__.py
│   ├── config.py
│   ├── imports.py
│   │
│   ├── core/
│   │   ├── agent.py
│   │   ├── agent1.py
│   │   ├── agent2.py
│   │   ├── agent3.py
│   │   ├── agent_executor.py
│   │   ├── agent_router.py
│   │   ├── brain.py
│   │   ├── cache_manager.py
│   │   ├── compressor.py
│   │   ├── data_clean.py
│   │   ├── final.py
│   │   └── identifier.py
│   │
│   ├── rag/
│   │   ├── bm25_retriever.py
│   │   ├── chunk.py
│   │   ├── embedder.py
│   │   ├── hybrid_retriever.py
│   │   ├── loader.py
│   │   ├── pipeline.py
│   │   ├── reranker.py
│   │   ├── vector_retriever.py
│   │   └── vector_store.py
│   │
│   └── _mcp/
│       ├── client.py
│       ├── server.py
│       ├── memory/
│       └── tools/
│
└── task/
    ├── normalizer.py
    ├── pipeline.py
    ├── planner.py
    ├── selector.py
    ├── splitter.py
    ├── tool_matcher.py
    └── validator.py
```

> **Note:** Runtime-generated files such as `.env`, databases, caches, logs, `__pycache__/`, and generated outputs should not be committed to GitHub.

---

# 🧱 Core Modules

### `folio/core/agent.py`

The main public `Agent` interface.

Supports:

- MCP execution
- RAG
- Custom agent prompts
- Model selection
- Conversation history
- Context compression

### `folio/core/brain.py`

Converts a user task into an executable workflow plan.

Handles:

- Task planning
- Tool dependencies
- Input references
- Output keys
- Plan conversion

### `folio/core/agent1.py`

Handles direct MCP execution for deterministic tools.

### `folio/core/agent2.py`

Handles LLM-powered MCP execution.

Agent 2:

1. Receives the selected tool
2. Loads the MCP schema
3. Sends the task to the selected model
4. Calls the MCP tool
5. Processes the tool result
6. Returns the final cleaned/customized output

### `folio/core/agent3.py`

Handles command/system-level operations.

### `folio/core/observer.py`

Monitors tool execution and provides recovery/substitution logic when a tool fails.

### `folio/core/data_clean.py`

Cleans tool output before presenting it to the user.

It can remove unnecessary:

- Markdown formatting
- URLs where appropriate
- Images and thumbnails
- HTML
- Tool-specific clutter

---

# 🔄 Task Pipeline

The task system is divided into small modules:

```text
normalizer.py
      │
      ▼
splitter.py
      │
      ▼
validator.py
      │
      ▼
tool_matcher.py
      │
      ▼
planner.py
      │
      ▼
selector.py
      │
      ▼
pipeline.py
```

| Module | Responsibility |
|---|---|
| `normalizer.py` | Cleans and normalizes user requests |
| `splitter.py` | Splits compound requests into tasks |
| `validator.py` | Validates generated tasks |
| `tool_matcher.py` | Ranks MCP tools against tasks |
| `planner.py` | Builds the execution flow |
| `selector.py` | Selects the best tool candidate |
| `pipeline.py` | Connects planning with agent routing |

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/parin0127-png/folio.git
cd folio
```

## 2. Create a virtual environment

### Windows

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install FOLIO locally

```bash
pip install -e .
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Additional API keys may be required depending on the MCP tools you use.

**Never commit `.env` to GitHub.**

---

# 🤖 Build Your Own Agents

FOLIO uses one simple interface for different agent workflows:

```python
from folio import Agent

agent = Agent(...)
agent.run("Your task here")
```

## 🌐 1. Normal Agent

Use MCP to let FOLIO access tools such as weather, web search, Wikipedia, and more.

```python
from folio import Agent

agent = Agent(enable_mcp=True)

agent.run("Get the current weather in Mumbai and get information about Japan.")
```

### Flow

```text
User Request
     ↓
FOLIO Brain
     ↓
Task Splitting
     ↓
Tool Matching
     ↓
MCP Tools
     ↓
Result
```

---

## 📚 2. RAG Agent

Use RAG when you want FOLIO to answer questions from your own documents.

```python
from folio import Agent

# Enable RAG
agent = Agent(enable_rag=True)

# Upload your file
agent.ingest(r"C:/Users/Parin/Downloads/t.pdf")

# Ask questions
print("<>-----------------------------------------<>")
agent.run("What is the name of company ?")
print("<>-----------------------------------------<>")

agent.run("Give me Financial Performance of year 2024.")
print("<>-----------------------------------------<>")

agent.run("Define Key Risks?")
print("<>-----------------------------------------<>")

agent.run("What are the growth strategy?")
print("<>-----------------------------------------<>")

agent.run("Who is the CEO of this company, and when was it founded?")
print("<>-----------------------------------------<>")
```

### Flow

```text
Your Document
      ↓
    Ingest
      ↓
   RAG System
      ↓
   Question
      ↓
    Answer
```

---

## 🛡️ 3. Observer Agent

FOLIO's Observer watches tool execution and can recover from tool failures.

```python
from folio import Agent

agent = Agent(enable_mcp=True)

agent.run(
    "Get information about the top programming languages "
    "and make it an excel."
)
```

If a selected tool fails, the Observer can find another available tool that can complete the task.

---

## ✨ 4. Customized Agent

Customize how Agent 2 processes the tool result with `agent_prompt`.

You can also choose the Mistral model with `agent_model`.

```python
from folio import Agent

agent = Agent(
    enable_mcp=True,
    agent_model="mistral-medium-latest",
    agent_prompt="summarize the content into 5 lines and no bullet points"
)

agent.run("give me information about Elon Musk")
```

### Customization Flow

```text
MCP Tool
   ↓
Tool Result
   ↓
Agent Prompt
   ↓
Customized Output
```

---

## 🔗 5. Multi-Tasking Agent

FOLIO can handle multiple tasks from a single request.

```python
from folio import Agent

agent = Agent(enable_mcp=True)

agent.run(
    "give me information about Virat Kohli and make pdf of that information and "
    "send that information to parin122007@gmail.com on email and upload to slack"
)
```

A workflow can look like:

```text
Get Information
      ↓
   Make PDF
      ↓
  Send Email
      ↓
 Upload to Slack
```

The tasks and tools are selected dynamically from the user's request.

---

# 🧠 Model Support

FOLIO separates the planning model from the execution model.

```python
from folio import Agent

agent = Agent(
    brain_model="openai/gpt-oss-20b",
    agent_model="mistral-small-latest"
)
```

This allows different models to be used for:

- Workflow planning
- Tool execution
- Result processing

You can override the execution model when creating an agent:

```python
agent = Agent(
    enable_mcp=True,
    agent_model="mistral-medium-latest"
)
```

---

# 🔗 Example Workflow

### Input

```text
Get information about Rohit Sharma,
make a PDF from that information,
and send the PDF to Slack.
```

### Execution

```text
User
 │
 ▼
Task Splitter
 │
 ├── Get information about Rohit Sharma
 ├── Make PDF
 └── Send PDF to Slack
        │
        ▼
   Tool Matcher
        │
        ▼
      Planner
        │
        ▼
 Wikipedia Search
        │
        ▼
       wiki
        │
        ▼
  PDF Generator
        │
        ▼
       pdf
        │
        ▼
      Slack
        │
        ▼
    Completed
```

---

# 🛡️ Error Recovery

If a selected tool fails:

```text
Selected Tool
     │
     ▼
 Execution
     │
     ▼
   ERROR
     │
     ▼
  Observer
     │
     ├── Predefined substitute
     │
     └── AI-assisted recovery
             │
             ▼
       Replacement Tool
```

This allows FOLIO to continue a workflow when a suitable fallback exists.

---

# 📦 Package Structure

FOLIO is designed to be distributed as a Python package.

Package metadata is defined in:

```text
pyproject.toml
```

Dependencies are also provided through:

```text
requirements.txt
```

The package exposes a CLI entry point:

```text
folio
```

configured through:

```toml
[project.scripts]

folio = "main:main"
```

---

# 🧪 Development

Run the local test/demo:

```bash
py -3.11 test.py
```

Run the application:

```bash
py -3.11 main.py
```

For development, use a virtual environment.

---

# 🎯 Design Philosophy

FOLIO is built around a few principles:

- **Keep orchestration modular**
- **Use deterministic logic where possible**
- **Use LLMs only when they add value**
- **Keep prompts small**
- **Make tool selection dynamic**
- **Support multi-step workflows**
- **Preserve outputs between tasks**
- **Recover from tool failures**
- **Keep the public API simple**

The goal is to make complex AI workflows feel like a normal Python function call.

---

# 🗺️ Roadmap

Planned areas of development include:

- Improved tool selection
- More robust tool argument generation
- Better Observer recovery
- More MCP tools
- Improved RAG evaluation
- Streaming responses
- Better workflow visualization
- Expanded CLI support
- PyPI releases
- More model providers

---

# 📄 License

FOLIO is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

# 👨‍💻 Author

**Parin Prajapati**

- GitHub: [parin0127-png/folio](https://github.com/parin0127-png/folio)
- LinkedIn: [Parin Prajapati](https://www.linkedin.com/in/parin-prajapati-5b0579376/)

---

<div align="center">

### FOLIO

**Natural language → intelligent workflow → execution**

Built with Python, MCP, RAG, and modern LLMs.

</div>
