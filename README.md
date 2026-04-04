# Simple eBook Merger

Merge a bunch of eBook files into one EPUB. That's it.

I wrote this because I was sick of dealing with 20+ individual chapter files on my eReader every time an author publishes a series in parts. Now I just dump them all in a folder and run this.

Supports **EPUB**, **TXT**, and **HTML** inputs. Output is always a single, clean EPUB.

================================================================================

## Requirements

- **Python 3.8+** — grab it from https://python.org/downloads
  - During install, check "Add Python to PATH" (important!)
- **tkinter** — ships with Python on Windows and Mac. Linux users might need `sudo apt install python3-tk`.

Install the Python dependencies (one time):

```
pip install ebooklib beautifulsoup4 lxml
```

================================================================================

## How to Use

### Option A — GUI (default, recommended)

Double-click `ebook_merger.py` or run:

```
python ebook_merger.py
```

A window opens. Pick your input folder, set a title/author, hit **Merge**. Done.

The GUI shows you which files it found, a live log as it processes, and a summary when it's finished.

### Option B — Terminal / headless

If you're on a server without a display, or you just prefer the command line:

```
python ebook_merger.py --nogui
```

In this mode you'll need to edit the `CONFIG` section near the top of the script first:

```python
INPUT_DIR    = r"C:\Users\You\Documents\my_series"
OUTPUT_FILE  = "merged_book.epub"
BOOK_TITLE   = "My Merged eBook"
BOOK_AUTHOR  = "Various Authors"
ADD_DIVIDERS = True
```

Then just run it.

================================================================================

## Supported Formats

| Format | Extension | What happens |
|---|---|---|
| EPUB | .epub | Chapters, formatting, and images are all preserved |
| Plain Text | .txt | Turned into a single chapter with paragraph formatting |
| HTML | .html, .htm | Turned into a chapter, formatting preserved |

Anything else in the folder gets skipped automatically — it won't break anything.

================================================================================

## Tips

- **Control the merge order** by naming your files with number prefixes: `01_prologue.epub`, `02_chapter1.epub`, `03_chapter2.txt`, etc. Files are merged alphabetically.
- **Divider pages** are inserted between each source file by default, so you can tell where one ends and the next starts. You can turn this off in the GUI (uncheck the box) or by setting `ADD_DIVIDERS = False` in the config.
- **Images** from EPUB files carry over into the merged output.
- **Table of contents** is auto-generated. Multi-chapter EPUBs get nested entries.
- The output is **EPUB 3**, which works with pretty much everything: Calibre, Apple Books, Kobo, Rockbox, Kindle (via Send to Kindle or Calibre conversion), you name it.
- **DRM-protected files won't work.** The script can't strip DRM and I'm not going to add that. If a file has DRM it'll just get skipped.

================================================================================

## Config Reference (terminal mode only)

The GUI handles all of this through the window. These settings only matter if you run with `--nogui`.

| Setting | What it does | Example |
|---|---|---|
| INPUT_DIR | Folder with your eBook files | `r"C:\Users\You\ebooks"` |
| OUTPUT_FILE | Where to save the merged EPUB | `"merged_book.epub"` |
| BOOK_TITLE | Title in the EPUB metadata | `"My Merged eBook"` |
| BOOK_AUTHOR | Author in the EPUB metadata | `"Various Authors"` |
| ADD_DIVIDERS | Put a divider page between each file | `True` |

================================================================================

## Legal Disclaimer

By using this you agree to the following.

This is for **personal use only** — merging files you already own for your own reading convenience.

The content you merge is probably copyrighted. You **cannot** share, upload, sell, or redistribute the merged output. You also can't use this as a reason to strip DRM from protected files — that violates the DMCA and other laws.

No warranty. Provided "as is." I've tested it thoroughly but I'm not responsible if something goes sideways on your setup.

**You** are responsible for how you use this tool and for making sure you're not breaking any laws. If you get in trouble, that's on you — you agree to hold me harmless from any claims.

If you're merging chapters from a series you love, make sure you actually paid for it. This tool makes reading more convenient — it's not meant to help anyone rip off the authors who wrote the stuff.

================================================================================

## License

Released for personal use. See the disclaimer above.
I don't claim ownership over anything this script processes.
