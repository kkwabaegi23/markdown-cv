# Luca-CV

forked from [Luca-CV](https://github.com/lucafrance/luca-cv/) with some modifications:
- replace powershell make script with Python
- ability to process multiple markdown files at once - allows you to create different CVs (e.g. in multiple languages, different specializations) with a single execution
- saves all created files (pdf, Word) to the folder output
- removed photo


Use
- Replace `photo.jpg` with your photo.
- Update `cv_en_john_doe.md`.
- Run `make_cv.ps1` to generate `cv_en_john_doe.docx`,`cv_en_john_doe.tex`, `cv_en_john_doe.pdf`.

Requirements
- [Python](https://www.python.org/)
- [Pandoc](https://pandoc.org/)
- pdflatex (included in [MiKTeX](https://miktex.org))
