# AI Multi-Agent System

A multi-agent system built with LangChain that enables different AI models to communicate and collaborate on complex tasks.

## Features

- **Multi-Model Support**: Integrate Claude (Anthropic), GPT (OpenAI), and Gemini (Google)
- **Agent Communication**: Enable AI agents to work together and share context
- **LangChain Framework**: Built on LangChain for flexible agent orchestration
- **Extensible Architecture**: Easy to add new AI models and capabilities

## Architecture

```
┌─────────────────────────────────────────┐
│         Agent Orchestrator              │
│                                         │
│  ┌──────────┐  ┌──────────┐  ┌────────┐│
│  │  Claude  │  │   GPT    │  │ Gemini ││
│  │  Agent   │  │  Agent   │  │ Agent  ││
│  └──────────┘  └──────────┘  └────────┘│
│                                         │
│         Shared Context & Memory         │
└─────────────────────────────────────────┘
```

## Prerequisites

- Python 3.8+
- API keys for:
  - Anthropic (Claude)
  - OpenAI (GPT) - optional
  - Google AI (Gemini) - optional

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd ai-multi-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## Usage

Coming soon...

## Project Structure

```
ai-multi-agent/
├── agents/           # Agent implementations
├── orchestrator/     # Orchestration logic
├── utils/           # Utility functions
├── examples/        # Example use cases
├── tests/           # Test suite
├── .env.example     # Environment template
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Development

Follow the guidelines in `CLAUDE.md` for AI-assisted development workflow.

## License

MIT

## Contributing

This is a private repository. Contributions are welcome from authorized collaborators.
