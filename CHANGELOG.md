# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
