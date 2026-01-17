# Git Commit Policy

## Automatic Commits for LaTeX Files

When working on this calculus book project, agents should commit changes to git after any major modification to `.tex` files.

### When to Commit

Commit immediately after:
- **Adding new sections or subsections** to any chapter
- **Adding or modifying proofs** of theorems, lemmas, or propositions
- **Adding worked examples** or exercises
- **Creating or modifying TikZ figures** or diagrams
- **Completing a chapter revision** or major restructuring
- **Fixing significant errors** (typos, mathematical mistakes, incomplete proofs)
- **Adding new chapters** or removing chapters

### Commit Message Guidelines

Use descriptive commit messages that clearly explain what changed:

**Good examples:**
- `"Chapter 2: Added proof of Cauchy-Schwarz inequality"`
- `"Chapter 1: Fixed typo in section title and added equivalence relation proof"`
- `"Chapters 1-2: Added worked examples and TikZ figures"`
- `"Chapter 3: Added section on O notation with three examples"`
- `"Fixed mathematical error in triangle inequality proof (Chapter 2)"`

**Avoid vague messages:**
- ❌ `"Updated files"`
- ❌ `"Changes"`
- ❌ `"Fix"`

### Workflow

After making changes to `.tex` files:

```bash
cd "/Users/guykindler/My Drive/courses/Calculus/book"
git add *.tex
git status  # Review what's being committed
git commit -m "Descriptive message here"
```

### Files to Track

- **Always commit**: All `.tex` files (main.tex, chapter*.tex)
- **Never commit**: PDF outputs, auxiliary files (covered by .gitignore)
- **Optionally commit**: Documentation files (README.md, notes.md)

### Exception

Do **not** commit for trivial changes like:
- Single-word typo fixes in isolation
- Whitespace-only changes
- Commenting/uncommenting for testing

Instead, batch minor fixes together and commit with a message like:
`"Minor fixes: corrected typos and formatting in Chapters 1-3"`
