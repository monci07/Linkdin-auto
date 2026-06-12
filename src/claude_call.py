import anthropic

class claude_call:
    
    def __init__(self):
        self.client = anthropic.Anthropic(api_key="")

    def call(self, message):
        respons = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": message}],
        )
        return respons.content[0].text