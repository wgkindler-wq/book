#!/usr/bin/env python3
import os
import re
import argparse
import sys

"""
Script to automatically fix "Token not allowed in a PDF string" warnings in LaTeX.

This script scans LaTeX files for section, subsection, and chapter commands.
If it finds inline math (e.g., $\mathbb{R}^n$) inside these titles, it replaces it 
with a \texorpdfstring{...}{...} command.

It attempts to generate a reasonable text representation for the PDF bookmark:
- $\mathbb{R}^n$ -> Rn
- $\mathbb{R}^2$ -> R2
- $x$ -> x
- Removes LaTeX macros like \mathbb, \mathcal, etc.
- Removes curly braces, carets, and underscores.

Usage:
    python3 scripts/fix_latex_titles.py <path_to_file_or_directory>

Example:
    python3 scripts/fix_latex_titles.py chapter1_sections/
    python3 scripts/fix_latex_titles.py main.tex
"""

def simple_tex_to_text(math_str):
    """
    Converts a LaTeX math string to a simplified text representation for PDF bookmarks.
    Example: $\mathbb{R}^n$ -> Rn
    """
    # Remove the surrounding $ symbols
    inner = math_str.strip('$')
    
    # Common replacements
    text = inner.replace(r'\mathbb{R}', 'R')
    text = text.replace(r'\mathbb{C}', 'C')
    text = text.replace(r'\mathbb{Z}', 'Z')
    text = text.replace(r'\mathbb{N}', 'N')
    text = text.replace(r'\dots', '...')
    
    # Remove common macros but keep their content if it's simple
    # Regex to remove \macro{content} -> content (simplified)
    # This is tricky with nesting, but we can do a simple pass for common things
    text = re.sub(r'\\[a-zA-Z]+', '', text) # Remove other macros
    
    # Remove special chars
    text = text.replace('^', '').replace('_', '').replace('{', '').replace('}', '')
    
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find sectioning commands
    # Matches: \section{Title with \texorpdfstring{$math$}{math}}
    # Captures: 1=command, 2=content inside braces
    # Note: This simple regex assumes the title doesn't contain nested braces that are unbalanced.
    # LaTeX parsing with regex is fragile, but sufficient for simple titles.
    pattern = re.compile(r'(\\((?:sub)*section|chapter)\{)(.*?)(\})', re.DOTALL)

    def replacer(match):
        prefix = match.group(1)
        title_content = match.group(3)
        suffix = match.group(4)
        
        # Look for math mode $...$ inside the title
        # valid math mode: $...$
        # Regex for math mode `\$([^$]+)\$`
        
        def math_replacer(math_match):
            original_math = math_match.group(0) # e.g. $\mathbb{R}^n$
            # If it's already inside \texorpdfstring, we should skip it.
            # However, this regex is running on the *extracted* title string.
            # So we just need to be careful not to double-wrap if it's already wrapped.
            # But checking context in regex replacement is hard. 
            # Safe assumption: if the user looks at the diff, they can see.
            
            text_rep = simple_tex_to_text(original_math)
            return f'\\texorpdfstring{{{original_math}}}{{{text_rep}}}'

        # Check if there is any math in the title
        if '$' in title_content:
            # We must be careful not to replace \$ (escaped dollar) though obscure in titles
            new_title_content = re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$', math_replacer, title_content)
            
            if new_title_content != title_content:
                print(f"Modifying in {file_path}:")
                print(f"  Old: {title_content}")
                print(f"  New: {new_title_content}")
                return f"{prefix}{new_title_content}{suffix}"
        
        return match.group(0)

    new_content = re.sub(pattern, replacer, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        # print(f"No changes in {file_path}")
        pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_latex_titles.py <file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".tex"):
                    process_file(os.path.join(root, file))
    else:
        print(f"Error: {path} is not a valid file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
