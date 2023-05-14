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
            openai.api_key = f.readline().split('=')[1]

    @neovim.command('Chat', nargs='*')
    def chat(self, args):
        # You can replace the following lines with the actual API call
        # Make a GET request
        # response = requests.get('http://example.com')

        prompt = ' '.join(args)

        try:
            completion = openai.Completion.create(model="text-davinci-003", prompt=prompt)
            response = completion.choices[0].text
        except Exception as e:
            self.nvim.out_write(f'Error: {e}\n')

        # Feed the query back to the user
        self.nvim.out_write(response)
