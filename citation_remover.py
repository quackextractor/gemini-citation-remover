import os
import re
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

def process_text(content):
    """
    Cleans citation tags, fixes formatting issues caused by them,
    and automatically repairs common markdown structural errors.
    """
    # 1. Pull up citation tags that got pushed to a new line to fix broken headings/sentences
    content = re.sub(r'\n[ \t]*(\[(?:cite_start|cite_end|cite:|source:)[^\]]*\])', r' \1', content)
    
    # Run a second time just in case multiple tags were stacked on separate newlines
    content = re.sub(r'\n[ \t]*(\[(?:cite_start|cite_end|cite:|source:)[^\]]*\])', r' \1', content)
    
    # 2. Remove all the citation tags completely
    pattern = r'\[(?:cite_start|cite_end|cite:[^\]]*|source:[^\]]*)\]'
    content = re.sub(pattern, '', content)
    
    # 3. Autofix Markdown issues
    # Fix detached bullet points (an asterisk on one line, bold text on the next)
    content = re.sub(r'\*\s*\n\s*\*\*', '* **', content)
    
    # Fix collapsed sub-bullets (a bullet immediately following a colon on the same line)
    content = re.sub(r'(?<=:)\s*\*\s*\*\*', '\n  * **', content)
    
    # Remove excessive vertical spacing (reduce 3 or more newlines down to 2)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 4. Clean up multiple horizontal spaces left behind
    content = re.sub(r'[ \t]+', ' ', content)
    
    # 5. Remove trailing spaces right before a new line
    content = re.sub(r'[ \t]+\n', '\n', content)
    
    return content.strip()

def clean_citations_in_file(filepath):
    """
    Creates a backup and removes citation markings from the given file.
    """
    try:
        backup_path = filepath + '.bak'
        shutil.copy2(filepath, backup_path)

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()

        cleaned_content = process_text(content)

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
            
        return True, "Success"
    except Exception as e:
        return False, str(e)

def clean_pasted_text(event=None):
    """
    Grabs text from the clipboard, cleans citations, saves to a fixed file,
    and copies the cleaned text back to the clipboard.
    """
    try:
        content = window.clipboard_get()
        if not content.strip():
            messagebox.showwarning("Warning", "Clipboard is empty.")
            return

        cleaned_content = process_text(content)

        output_filename = "pasted-no-citation.txt"
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
            
        # Copy the cleaned text back to the system clipboard
        window.clipboard_clear()
        window.clipboard_append(cleaned_content)
        window.update() # Required on some systems to finalize clipboard operations
            
        messagebox.showinfo("Success", f"Successfully cleaned pasted text, saved to {output_filename}, and copied back to your clipboard.")
        
    except tk.TclError:
        messagebox.showwarning("Error", "No text found in clipboard.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def on_drop(event):
    """
    Handles the drop event, processes each dropped file, and shows a summary.
    """
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
        errors = "\n".join(error_messages)
        messagebox.showwarning("Completed with errors", f"Processed {success_count} files.\n\nErrors:\n{errors}")
    elif success_count > 0:
        messagebox.showinfo("Success", f"Successfully cleaned {success_count} file(s).")


# Initialize the main window using TkinterDnD
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
window.bind('<Command-v>', clean_pasted_text)

if __name__ == "__main__":
    window.mainloop()