import neovim
import requests  # To make HTTP requests

@neovim.plugin
class JuniorPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('Chat', sync=True)
    def chat(self, args):
        # You can replace the following lines with the actual API call
        # Make a GET request
        # response = requests.get('http://example.com')

        # Print the status code
        self.nvim.out_write(f'Hello World!\n')
