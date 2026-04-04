# eBook Merger v3.0 Upgrade Specification

## Overview
Expand the merger to support as many input and output formats as possible using pure Python libraries (no Calibre dependency). Keep the existing code structure, humanized style, dark-theme GUI, and legal disclaimer.

## New Input Formats to Add
On top of the existing .epub, .txt, .html, .htm:

1. **PDF** (.pdf) — use `pypdf` (PdfReader, page.extract_text())
2. **DOCX** (.docx) — use `python-docx` (Document, paragraphs, runs — preserve bold/italic as HTML tags)
3. **RTF** (.rtf) — use `striprtf` (rtf_to_text to get plain text)
4. **Markdown** (.md) — use `markdown` library (markdown.markdown() to convert to HTML)
5. **FB2** (.fb2) — parse XML directly with BeautifulSoup (it's just XML with <body><section><p> tags)
6. **ODT** (.odt) — use `odfpy` (load doc, getElementsByType for text:p paragraphs)
7. **CBZ** (.cbz) — it's a zip of images; extract images and create image-based chapters

## New Output Formats to Add
On top of the existing EPUB output:

1. **Plain Text** (.txt) — extract all text from the merged chapters, write to file
2. **Single HTML** (.html) — concatenate all chapter HTML into one styled HTML file
3. **PDF** (.pdf) — use `fpdf2` library to write text paragraphs to PDF pages
4. **DOCX** (.docx) — use `python-docx` to write a Word document with chapters

## Dependencies (pip install line)
```
pip install ebooklib beautifulsoup4 lxml pypdf python-docx striprtf markdown odfpy fpdf2
```

## GUI Changes
- Add an "Output format" dropdown/combobox next to the "Save as" row with options: EPUB, TXT, HTML, PDF, DOCX
- When the user changes the format, update the file extension in the output path automatically
- Update the "Browse..." save dialog filetypes based on selected format
- Update the file discovery to show all the new extensions
- Update the status/file count text

## Terminal Mode Changes
- Add OUTPUT_FORMAT config option (default "epub")
- Support the same output formats

## Architecture
- Each new input format gets its own `_FORMAT_to_chapter()` function (like the existing `_txt_to_chapter`, `_html_to_chapter`)
- Each output format gets its own `_write_FORMAT()` function
- The merge_files() function builds the internal EPUB structure as before, then at the end calls the appropriate writer
- For non-EPUB outputs, the writer reads the merged EPUB chapters' content and converts

## Important Style Notes (HUMANIZATION)
- Keep the same casual, first-person voice throughout ("I wrote this because...", "Seriously, don't do it")
- NO AI-sounding words: avoid "comprehensive", "robust", "leverage", "utilize", "streamline", "facilitate", "delve", "certainly"
- Keep variable names short and natural
- Comments should sound like a person talking, not documentation
- Keep the same docstring style with the ASCII art header
- Keep the legal disclaimer in the same casual-but-thorough style
