# OpenAI Swarm with LiteLLM Support

This repository is a fork of [openai/swarm](https://github.com/openai/swarm) that adds support for [LiteLLM](https://github.com/BerriAI/litellm), enabling integration with 100+ Large Language Models.

> **Note**: Unlike the original swarm project which is experimental, we are actively using this fork in production environments with success. Feel free to try it in your production systems!

## Features

- All original features from openai/swarm
- Extended LLM support through LiteLLM integration
- Compatible with 100+ LLM providers including:
  - OpenAI
  - Anthropic
  - Google
  - Azure
  - And many more through LiteLLM's provider ecosystem

## Getting Started

1. Clone this repository
2. Install dependencies
3. Configure your LLM provider credentials
4. Run your swarm applications with any supported LLM

## Using Different LLM Providers

You can easily use different LLM providers by specifying the model name in your Agent configuration. For example, to use Claude:

```python
from swarm import Swarm, Agent as SwarmAgent

# Initialize an agent with Claude
agent = SwarmAgent(
    name="info_collector",
    instructions="Your instructions here",
    functions=[your_functions],
    model="claude-3-5-haiku-20241022"  # Specify Claude model
)
```

Make sure to:

1. Set up your Anthropic API key in your environment: `ANTHROPIC_API_KEY`
2. Install LiteLLM: `pip install litellm`
3. Configure other provider-specific settings as needed

For other providers, simply use their respective model names as supported by LiteLLM.

## Documentation

For detailed documentation on:

- Original swarm functionality, visit the [openai/swarm documentation](https://github.com/openai/swarm)
- LiteLLM provider setup, check [LiteLLM's documentation](https://docs.litellm.ai/docs/)

## Contributing

We welcome and encourage contributions to this project! Whether it's:

- Adding support for new LLM providers
- Improving documentation
- Fixing bugs
- Adding new features

Feel free to submit a Pull Request or open an issue for discussion.
