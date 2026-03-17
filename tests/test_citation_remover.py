from citation_remover import process_text


def test_process_text_removes_citations():
    text = (
        "This is a sentence [cite_start]with a citation[cite_end]. "
        "Another one [cite:123] and [source:abc]."
    )
    # process_text does re.sub(r'[ \t]+', ' ', content)
    result = process_text(text)
    assert result == "This is a sentence with a citation. Another one and ."


def test_process_text_pulls_up_citations():
    text = "This is a sentence\n[cite:123] on a new line."
    result = process_text(text)
    assert "[cite:123]" not in result
    assert result == "This is a sentence on a new line."


def test_process_text_fixes_markdown_lists():
    text = "* \n **Bold item**"
    result = process_text(text)
    assert result == "* **Bold item**"


def test_process_text_fixes_multiple_newlines():
    text = "Line 1\n\n\n\nLine 2"
    result = process_text(text)
    assert result == "Line 1\n\nLine 2"


def test_process_text_cleans_spaces():
    text = "Too    many    spaces. "
    result = process_text(text)
    assert result == "Too many spaces."
