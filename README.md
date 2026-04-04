# Simple eBook Merger

Merge multiple eBook files into a single EPUB for personal offline reading.
Supports EPUB, plain text (.txt), and HTML (.htm/.html) inputs.

================================================================================

## Requirements

- Python 3.8 or higher: https://python.org/downloads
- During install, check "Add Python to PATH"

Install dependencies by running this once in your terminal:

```
pip install ebooklib beautifulsoup4 lxml
```

================================================================================

## Quick Start

### Step 1 — Organise your files

Place all the eBook files you want to merge into a single folder.

Files are merged in **alphabetical order** by filename. To control the order, prefix your files with numbers:

```
01_prologue.epub
02_chapter_one.epub
03_chapter_two.txt
04_appendix.html
```

### Step 2 — Edit the config

Open `ebook_merger.py` in any text editor and fill in the CONFIG section near the top:

```python
INPUT_DIR    = r"C:\Users\YourName\Documents\ebooks"
OUTPUT_FILE  = "merged_book.epub"
BOOK_TITLE   = "My Merged eBook"
BOOK_AUTHOR  = "Various Authors"
ADD_DIVIDERS = True
```

### Step 3 — Run

Windows (Command Prompt):

```
cd C:\path\to\script
python ebook_merger.py
```

Mac or Linux (Terminal):

```
cd /path/to/script
python3 ebook_merger.py
```

The script will print progress as it processes each file, then save the merged .epub to the path set in OUTPUT_FILE.

================================================================================

## Supported Formats

| Format | Extension | Notes |
|---|---|---|
| EPUB | .epub | Full support — chapters, formatting, and embedded images are preserved |
| Plain Text | .txt | Converted to a single EPUB chapter with paragraph formatting |
| HTML | .html, .htm | Converted to an EPUB chapter with formatting preserved |

Files with other extensions are automatically skipped with a warning.

================================================================================

## Config Reference

| Setting | Description | Example |
|---|---|---|
| INPUT_DIR | Folder containing the eBook files to merge | `r"C:\Users\You\ebooks"` |
| OUTPUT_FILE | Path and filename for the merged EPUB output | `"merged_book.epub"` |
| BOOK_TITLE | Title shown in the merged EPUB's metadata | `"My Merged eBook"` |
| BOOK_AUTHOR | Author shown in the merged EPUB's metadata | `"Various Authors"` |
| ADD_DIVIDERS | Insert a divider page between each source file (True/False) | `True` |

================================================================================

## Notes

- The output is a standard **EPUB 3** file, compatible with most eBook readers: Calibre, Apple Books, Kobo, Kindle (via conversion), Rockbox, and more.
- Each input file becomes one or more chapters in the output. EPUB inputs keep their original chapter structure; TXT and HTML files each become a single chapter.
- Images embedded in source EPUB files are carried over into the merged output.
- A **table of contents** is automatically generated. EPUB sources with multiple chapters get nested TOC entries.
- Divider pages (enabled by default) are inserted between source files so you can tell where one book ends and the next begins. Set `ADD_DIVIDERS = False` to disable.
- The script does **not** handle DRM-protected files. If an EPUB has DRM, it will fail to read and be skipped.
- Word counts are printed for each file as it processes so you can confirm it is working.

================================================================================

## Legal Disclaimer

BY USING THIS SCRIPT YOU AGREE TO THE FOLLOWING IN FULL.

This script is provided strictly for personal, non-commercial use, solely for private reading convenience. Any other use is strictly prohibited.

All content contained in the eBook files you process may be protected by copyright law, including the U.S. Copyright Act (17 U.S.C.), the Digital Millennium Copyright Act (DMCA), and equivalent legislation worldwide (Berne Convention, EU Copyright Directive, etc.).

### You may NOT:

- Merge files you do not own or have lawful access to
- Distribute, share, upload, or transmit the merged output to any other person or platform
- Publish, republish, or post the merged content online
- Sell, license, or monetise the merged content in any form
- Use the content for AI training or data harvesting
- Remove or alter any copyright notices within source files
- Create derivative works for distribution

Doing so may constitute civil copyright infringement and/or criminal copyright theft, punishable by significant fines and/or imprisonment.

### No Circumvention

This script does not bypass, crack, or circumvent any DRM or access control mechanism. Using third-party tools to strip DRM before merging may violate the DMCA (17 U.S.C. §1201) and is strictly prohibited.

### No Warranty

This script is provided "as is", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, or non-infringement. The entire risk as to quality and performance is with you.

### Limitation of Liability

To the maximum extent permitted by applicable law, the script's author(s), contributors, and distributors shall not be liable for any direct, indirect, incidental, special, exemplary, consequential, or punitive damages whatsoever — including legal fees, fines, penalties, or claims brought against you by third parties — arising out of or in connection with your use or misuse of this script.

### Indemnification

By using this script you agree to fully indemnify, defend, and hold harmless the script's author(s), contributors, and distributors from and against any and all claims, damages, losses, liabilities, costs, and expenses (including reasonable legal fees) arising out of your use of this script or your violation of any third-party rights, including copyright.

### User Responsibility

You bear sole and complete responsibility for how you use this script and its output, and for ensuring compliance with all applicable local, national, and international laws. Ignorance of these terms or applicable law is not a defence.

================================================================================

## License

This script is released for personal use. See the disclaimer above.
The author(s) of this script claim no ownership over any content processed by it.
