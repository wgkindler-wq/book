# Fixed Compilation Warnings

I have successfully resolved all compilation warnings found in `main.log`.

## Changes Applied

### [main.tex](file:///Users/guykindler/My Drive/courses/Calculus/book/main.tex)
- Increased `\headheight` to `15pt` to resolve `fancyhdr` warnings.

### [points_and_translations.tex](file:///Users/guykindler/My Drive/courses/Calculus/book/chapter1_sections/points_and_translations.tex)
- Updated section and subsection titles to use `\texorpdfstring` for mathematical symbols (`$\mathbb{R}^n$`). This fixes `hyperref` warnings about tokens not allowed in PDF strings.

### [shapes_as_equivalence_classes.tex](file:///Users/guykindler/My Drive/courses/Calculus/book/chapter1_sections/shapes_as_equivalence_classes.tex)
- Updated subsection title to use `\texorpdfstring` for `$\mathbb{R}^2$`.

## Verification Results

### Automated Build
Ran `pdflatex main.tex` and checked for warnings.
- **Result**: No warnings found in `main.log`.

The build is now clean.
