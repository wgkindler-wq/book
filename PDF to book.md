# Implementation Plan - Calculus Notes to LaTeX Book

The goal is to convert handwritten Hebrew class and recitation notes into a professional English LaTeX book format.

## User Review Required
- **Terminology**: Confirm with user mathematical terms if ambiguous in translation.
- **Structure**: Confirm with user LaTeX chapter/section structure.

## Proposed Changes

### 1. Image Extraction
Since `pdftotext` is unavailable and these are handwritten scans, we will:
- Use `extract_pages.swift` to convert **all** pages of files such as  `חדווא שיעור 1.pdf`, `חדווא תירגול 1.pdf`, and `Class 1.pdf`  into PNG images.
- Store images in `scratch/images/class1/` and `scratch/images/recitation1/` (change number to reflect current class or chapter).

### 2. Transcription & Translation
- Iterate through each image.
- Transcribe the Hebrew/Math content.
- Translate the text to English, maintaining mathematical rigor.
- Organize the content into logical sections (Definitions, Theorems, Proofs, Examples).

### 3. LaTeX Generation
- **Files**:
    - Write the translated and formatted content to `chapter1.tex` in LaTeX format (change name to reflect current chapter).
    - `main.tex`: Master file with preamble (packages for math, theorems, etc.) and chapter/section organization.

## Verification Plan
### Manual Verification
- Compile the LaTeX file (if `pdflatex` is available). Observer the log for any errors and correct them.
- User reviews the generated PDF/Code against the original notes.
