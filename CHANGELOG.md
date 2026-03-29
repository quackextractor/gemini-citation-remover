# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-03-29

### Fixed
* **Resolved Header Merging**: Corrected an issue where double newlines (paragraph breaks) following headers were being incorrectly stripped, causing headers and body text to merge onto a single line.
* **Refined Citation Pull-up Logic**: Updated the `cite_pat` regular expression to use a capture group for preceding non-newline characters, ensuring only single line breaks are targeted while preserving intentional structural spacing.
* **Removed Aggressive Markdown Autofix**: Eliminated destructive formatting rules that forced indentation on bulleted lists following colons, which previously broke the layout of the **Output** and **Features** sections.
* **Standardized Line Breaks**: Implemented a safer approach to condense excessive whitespace into standard paragraph breaks without compromising the overall document hierarchy.

## [0.1.5] - 2026-03-18

### Changed
Dev env improvements

## [0.1.4] - 2026-03-18

### Added
Add pre-commit config and dev deps

## [0.1.3] - 2026-03-17

### Fixed
- CI failure where `pytest` could not find the `citation_remover` module. Fixed by using `python -m pytest` in the GitHub Actions workflow.

### Changed
- Refactored `citation_remover.py` to move `tkinter` and `tkinterdnd2` imports inside of functions. This allows the core logic to be imported and tested in headless environments without requiring Tcl/Tk system libraries.
- Added `<Control-V>` (uppercase) keyboard shortcut binding for pasting.

## [0.1.2] - 2026-03-17

### Added
- `.flake8` configuration file to automatically ignore directories like `venv` and `out`, matching `.gitignore` patterns.

### Changed
- Updated `.gitignore` to include virtual environment folders (`venv/`, `.venv/`).

## [0.1.1] - 2026-03-17

### Added
- `setup_and_run.bat` for easy environment setup and launching on Windows.

### Changed
- Improved dependency installation in `setup_and_run.bat` by using `requirements.txt`.

## [0.1.0] - 2026-03-17

### Added
- Initial project structure.
- `citation_remover.py` script with GUI support for drag-and-drop and clipboard.
- Removal of citation tags (e.g., `[cite:...]`, `[source:...]`).
- Markdown formatting fixes for lists and excessive newlines.
- Output redirection to `/out` directory.
- This CHANGELOG, README, and MIT LICENSE.
- GitHub Actions workflow for linting and testing.
