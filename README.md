# LinkedIn Auto

A Python automation tool that monitors a GitHub repository for new commits and automatically generates and publishes LinkedIn posts using AI.

## How It Works

The program runs a background thread that continuously polls a GitHub repository for new commits. When a new commit is detected, it takes the commit message and sends it to the Claude API, which generates a professional LinkedIn post. The post is then published automatically through Buffer.

```
New commit detected → Claude generates post → Buffer publishes to LinkedIn
```

## Requirements

- Python 3.8+
- A GitHub repository to monitor
- An Anthropic API key
- A Buffer account with a connected LinkedIn channel

## Installation

```bash
pip install PyGithub requests anthropic
```

## Configuration

Create a `keys.json` file in the root of the project with the following structure:

```json
{
    "GitHub": "your_github_token",
    "Anthropic": "your_anthropic_api_key",
    "Buffer": "your_buffer_api_key",
    "ChannelID(linkedin)": "your_buffer_linkedin_channel_id"
}
```

### Getting Your Keys

- **GitHub token** — GitHub → Settings → Developer settings → Personal access tokens
- **Anthropic API key** — [console.anthropic.com](https://console.anthropic.com)
- **Buffer API key** — Buffer → Settings → API
- **LinkedIn Channel ID** — Query the Buffer GraphQL API for your connected channels

## Usage

```bash
python main.py
```

The program will start monitoring the configured repository. Each time a new commit is pushed, a LinkedIn post will be automatically generated and added to your Buffer queue.

## Project Structure

```
linkedin-auto/
├── src/
│   └── main.py
├── keys.json
└── README.md
```

## Notes

- The Buffer free plan supports up to 10 queued posts per channel at a time.
- Posts are added to your Buffer queue and published according to your configured schedule.
- Make sure your LinkedIn channel is connected in Buffer before running the program.
