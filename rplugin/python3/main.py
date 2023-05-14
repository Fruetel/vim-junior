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
            completion = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=150)
            response = completion.choices[0].text.strip()
        except Exception as e:
            response = f'Error: {e}'

        # Feed the query back to the user
        self.nvim.out_write(response + '\n')

