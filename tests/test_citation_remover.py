import os
from citation_remover import process_text, ensure_out_folder, clean_citations_in_file


def test_process_text_basic_removal():
    """Verify that standard citation and source tags are removed."""
    input_text = "Scientific fact. Research data ."
    expected = "Scientific fact . Research data ."
    assert process_text(input_text) == expected


def test_process_text_start_end_tags():
    """Verify that cite_start and cite_end tags are handled correctly."""
    input_text = "Header Body text [cite_end] Footer"
    expected = "Header  Body text  Footer"
    assert process_text(input_text) == expected


def test_process_text_pull_up_citations():
    """Verify citations on new lines are pulled up before removal."""
    input_text = "Sentence ending here.\n"
    # The logic moves it to "Sentence ending here." then removes the tag.
    assert process_text(input_text) == "Sentence ending here."


def test_process_text_consecutive_pull_up():
    """Verify multiple consecutive citation lines are handled."""
    input_text = "Main text\n[cite: 1]\n"
    # The code runs the pull-up regex twice to catch stacked citations.
    assert process_text(input_text) == "Main text"


def test_process_text_markdown_repairs():
    """Test automated Markdown structural fixes for bolding and spacing."""
    # Fix spacing between bullet and bold marks
    assert process_text("* \n **Bold Item**") == "* **Bold Item**"

    # Reduce triple newlines to double newlines
    assert process_text("Paragraph A\n\n\nParagraph B") == "Paragraph A\n\nParagraph B"


def test_process_text_indentation_preservation():
    """Ensure trailing spaces are removed while preserving start-of-line indentation."""
    input_text = "    Indented line with space    \nNon-indented line  "
    expected = "    Indented line with space\nNon-indented line"
    assert process_text(input_text) == expected


def test_ensure_out_folder(tmp_path, monkeypatch):
    """Verify the /out directory is created in the current working directory."""
    monkeypatch.setattr(os, "getcwd", lambda: str(tmp_path))
    out_path = ensure_out_folder()

    assert os.path.exists(out_path)
    assert os.path.isdir(out_path)
    assert out_path.endswith("out")


def test_clean_citations_in_file(tmp_path, monkeypatch):
    """Verify the full file-to-file processing pipeline."""
    monkeypatch.setattr(os, "getcwd", lambda: str(tmp_path))

    # Create a source file with citations
    input_file = tmp_path / "input.txt"
    input_file.write_text("Hello world [cite: 1]", encoding="utf-8")

    success, message = clean_citations_in_file(str(input_file))

    assert success is True
    assert "Saved to out/input.txt" in message

    # Check the processed content
    output_file = tmp_path / "out" / "input.txt"
    assert output_file.read_text(encoding="utf-8") == "Hello world"


def test_process_text_empty_input():
    """Ensure the function handles empty strings gracefully."""
    assert process_text("") == ""
