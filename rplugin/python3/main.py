import neovim
import openai
import os

@neovim.plugin
class JuniorPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim
        # Read the API key from a config file
        # It expects a file named .junior in the home directory
        # containing a line like this:
        # OPENAI_API_KEY=your-api-key-here
        with open(os.path.expanduser('~/.junior'), 'r') as f:
            openai.api_key = f.readline().split('=')[1].strip()

    @neovim.command('Chat', nargs='*')
    def chat(self, args):
        prompt = ' '.join(args)

        # Initialize response to an empty string
        response = ''

        try:
            completion = openai.ChatCompletion.create(model="gpt-4",
                                                  messages=[
                                                      {'role': 'system', 'content': 'You are an assistant to a junior developer. You are helping them with their code.'},
                                                      {'role': 'user', 'content': prompt}
                                                    ])
            response = completion.choices[0].message.content
        except Exception as e:
            response = f'Error: {e}'

        # Display the response in a new buffer
        self.nvim.command('new')
        self.nvim.current.buffer.append(response)

