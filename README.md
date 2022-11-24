# Template for building a Custom Block for Boto.io

## Getting Started

### For unix-based OSes

1. Install Poetry
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    # Add `export PATH="/Users/tudor/.local/bin:$PATH"` to your shell configuration file.
    poetry --version
    poetry install
    poetry shell
    ```
    More info at: https://python-poetry.org/docs/cli/#shell
2. Run tests
    ```
    python -m pytest
    ```
3. Exit the `poetry` shell with the following command
    ```
    exit
    ```

### For Windows

1. TBD

## Using it on Boto.io

1. Ensure all tests pass inside your repository.
1. Go to [TODO: insert URL] and create a new Custom Block.
1. Copy the Python code from inside the `block.py` into: [TODO: insert URL].
1. Copy the JSON code from inside `block_config.json` into: [TODO: insert URL].
1. Publish your block by clicking on the green "Publish" button on [TODO: insert URL].

## To do

1. Don't forget to update this!
1. Add repo description on GitHub
1. Figure out how to run tests

