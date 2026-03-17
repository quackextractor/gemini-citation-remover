# Citation Remover & Markdown Fixer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1.2-blue.svg)](https://github.com/quackextractor/gemini-citation-remover)

A simple Python-based GUI application to clean citation tags and fix common markdown formatting issues from text files or clipboard content.

## Features

- **Remove Citations**: Completely removes tags like `[cite_start]`, `[cite_end]`, `[cite:...]`, and `[source:...]`.
- **Markdown Fixes**: 
  - Pulls up citation tags that got pushed to a new line.
  - Fixes broken list items (e.g., `* \n **`).
  - Reduces multiple empty lines to a maximum of two.
  - Cleans up trailing and redundant spaces.
- **Easy Input**: Support for drag-and-drop file processing and direct clipboard cleaning (Ctrl+V).
- **Safe Output**: Cleaned content is saved to a dedicated `out/` folder to prevent overwriting original files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/quackextractor/gemini-citation-remover.git
   cd gemini-citation-remover
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python citation_remover.py
```

- **Drag & Drop**: Drag your `.txt` or `.md` files onto the application window.
- **Clipboard**: Copy text to your clipboard and hit the **Paste Text** button or press **Ctrl+V**.

## Development

### Running Tests

```bash
pytest
```

### Linting

```bash
flake8 .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
