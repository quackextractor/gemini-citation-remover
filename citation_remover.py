import os
import re


def process_text(content):
    """
    Cleans citation tags, fixes formatting issues caused by them,
    and automatically repairs common markdown structural errors
    while preserving code indentation.
    """
    # 1. Pull up citation tags that got pushed to a new line
    cite_pat = r'\n[ \t]*(\[(?:cite_start|cite_end|cite:|source:)[^\]]*\])'
    content = re.sub(cite_pat, r' \1', content)
    content = re.sub(cite_pat, r' \1', content)

    # 2. Remove all the citation tags completely
    pattern = r'\[(?:cite_start|cite_end|cite:[^\]]*|source:[^\]]*)\]'
    content = re.sub(pattern, '', content)

    # 3. Autofix Markdown issues
    content = re.sub(r'\*\s*\n\s*\*\*', '* **', content)
    content = re.sub(r'(?<=:)\s*\*\s*\*\*', '\n  * **', content)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 4. Clean up trailing spaces (Fixed to preserve indentation)
    # Using MULTILINE flag to target the end of each line safely
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)

    # Keep .rstrip() instead of .strip() to avoid removing deliberate
    # starting whitespace at the very beginning of the document
    return content.rstrip()


def ensure_out_folder():
    """Ensures the /out directory exists."""
    out_path = os.path.join(os.getcwd(), 'out')
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    return out_path


def clean_citations_in_file(filepath):
    """
    Processes the file and saves the cleaned version to the /out folder.
    """
    try:
        out_dir = ensure_out_folder()
        filename = os.path.basename(filepath)
        output_path = os.path.join(out_dir, filename)

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()

        cleaned_content = process_text(content)

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        return True, f"Saved to out/{filename}"
    except Exception as e:
        return False, str(e)


def clean_pasted_text(event=None):
    """
    Cleans clipboard text and saves it to out/pasted-no-citation.txt.
    """
    import tkinter as tk
    from tkinter import messagebox
    try:
        content = window.clipboard_get()
        if not content.strip():
            messagebox.showwarning("Warning", "Clipboard is empty.")
            return

        cleaned_content = process_text(content)

        out_dir = ensure_out_folder()
        output_filename = os.path.join(out_dir, "pasted-no-citation.txt")

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        window.clipboard_clear()
        window.clipboard_append(cleaned_content)
        window.update()

        msg = (
            "Cleaned text saved to out/pasted-no-citation.txt "
            "and copied to clipboard."
        )
        messagebox.showinfo("Success", msg)

    except tk.TclError:
        messagebox.showwarning("Error", "No text found in clipboard.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def on_drop(event):
    file_paths = window.tk.splitlist(event.data)
    success_count = 0
    error_messages = []

    for path in file_paths:
        if os.path.isfile(path):
            success, msg = clean_citations_in_file(path)
            if success:
                success_count += 1
            else:
                filename = os.path.basename(path)
                error_messages.append(f"{filename}: {msg}")

    if error_messages:
        from tkinter import messagebox
        errors = "\n".join(error_messages)
        messagebox.showwarning(
            "Completed with errors",
            f"Processed {success_count} files.\n\nErrors:\n{errors}"
        )
    elif success_count > 0:
        from tkinter import messagebox
        msg = f"Successfully cleaned {success_count} file(s) into /out."
        messagebox.showinfo("Success", msg)


def setup_ui():
    """Sets up the Tkinter application."""
    import tkinter as tk
    from tkinterdnd2 import DND_FILES, TkinterDnD
    global window
    window = TkinterDnD.Tk()
    window.title("Citation Remover & Markdown Fixer")
    window.geometry("400x300")
    window.configure(bg="#f0f0f0")

    drop_label = tk.Label(
        window,
        text="Drag and drop text files here\nor press Ctrl+V to paste text",
        bg="#e0e0e0",
        font=("Arial", 12),
        relief="ridge",
        borderwidth=2
    )
    drop_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    paste_button = tk.Button(
        window,
        text="Paste Text from Clipboard",
        command=clean_pasted_text,
        font=("Arial", 10),
        bg="#ffffff"
    )
    paste_button.pack(pady=(0, 20))

    drop_label.drop_target_register(DND_FILES)
    drop_label.dnd_bind('<<Drop>>', on_drop)

    window.bind('<Control-v>', clean_pasted_text)
    window.bind('<Control-V>', clean_pasted_text)
    window.bind('<Command-v>', clean_pasted_text)

    return window


if __name__ == "__main__":
    app = setup_ui()
    app.mainloop()
