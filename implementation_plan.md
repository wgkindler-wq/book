# Implementation Plan - Calculus Notes to LaTeX Book

The goal is to convert handwritten Hebrew class and recitation notes (Class 1 & Recitation 1) into a professional English LaTeX book format.

## User Review Required
- **Terminology**: Confirmation on specific mathematical terms if ambiguous in translation.
- **Structure**: Approval of the proposed LaTeX chapter/section structure.

## Proposed Changes

### 1. Image Extraction
Since `pdftotext` is unavailable and these are handwritten scans, we will:
- Use `sips` (or Python script) to convert **all** pages of `חדווא שיעור 1.pdf` and `חדווא תירגול 1.pdf` into PNG images.
- Store images in `scratch/images/class1/` and `scratch/images/recitation1/`.

### 2. Transcription & Translation
- Iterate through each image.
- Transcribe the Hebrew/Math content.
- Translate the text to English, maintaining mathematical rigor.
- Organize the content into logical sections (Definitions, Theorems, Proofs, Examples).

### 3. LaTeX Generation
- Create a `book_project` directory.
- **Files**:
    - `main.tex`: Master file with preamble (packages for math, theorems, etc.).
    - `chapter1.tex`: Combined content of Class 1 and Recitation 1 (or separate chapters if length warrants).
- **Structure**:
    - Chapter 1: Introduction to Vectors and Affine Spaces (Tentative Title)
        - Section 1.1: Lecture Notes (Class 1 Content)
        - Section 1.2: Recitation Notes (Recitation 1 Content)

## Verification Plan
### Manual Verification
- Compile the LaTeX file (if `pdflatex` is available) or present the raw LaTeX code to the user.
- User reviews the generated PDF/Code against the original notes.
