# vim-junior

**vim-junior** is a Neovim plugin providing chat support using the OpenAI API. You can chat directly in your Neovim environment with the power of OpenAI's language models.

## Setup Instructions

### Prerequisites

1. [Neovim](https://neovim.io/) with Python3 support. Check Python3 support by running `:echo has('python3')` in Neovim. If it returns `1`, then you have Python3 support.

2. [vim-plug](https://github.com/junegunn/vim-plug), a plugin manager for Vim.

### Installation

Add the following line to your `init.vim` file in the appropriate location, usually in the vim-plug plugins section:

```
Plug 'fruetel/vim-junior', {'branch': 'main'}
```

Then, install the plugin by running `:PlugInstall` inside Neovim.

### Configuration

The vim-junior plugin requires your OpenAI API key to function. Add your OpenAI API key to a `.junior` file in your home directory as follows:

```
OPENAI_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual OpenAI API key.

## Dependencies

This plugin requires the `openai` Python library.

A `requirements.txt` file is provided in the root directory of the project. You can install the dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

Once the plugin is installed and configured, you can use the `:Chat` command followed by your message to start a conversation. For example:

```
:Chat Hello, how are you?
```
