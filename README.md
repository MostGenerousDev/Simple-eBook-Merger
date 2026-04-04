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

By downloading, viewing, thinking about, dreaming about, or otherwise interacting with this software — including staring at it real hard — you agree to the following.

### Personal Use Only

This is for merging ebook files **you already own** into one file for **your own eyeballs.** That's it. If you use it for literally anything else, that's a you problem, not a me problem.

### Copyright — Don't Be That Guy

The stuff you merge is almost certainly copyrighted. You may NOT:

- Share, upload, email, fax, telegraph, or send via carrier pigeon the output
- Sell it, trade it, barter it for goats, or monetize it in any way
- Post it online anywhere — not even "just for friends," not even on a private Discord
- Use it for AI training or data mining
- Strip DRM to feed files into this — that violates the DMCA (17 U.S.C. §1201) and I am NOT catching a federal charge because you wanted free books

### Absolutely Zero Warranty

This software is provided "AS IS" and "AS AVAILABLE" and "WITH ALL FAULTS" and "GOOD LUCK" — without warranty of any kind, express, implied, spiritual, or interdimensional, including warranties of merchantability, fitness for a particular purpose, or the warranty that it won't set your computer on fire (it won't, probably, but legally I make no promises). I tested it. It works on my machine.

### Limitation of Liability — The Big One

To the maximum extent permitted by every law that has ever been written, is currently being written, or will be written in the future by any governing body on Earth, in space, or on any celestial body that may eventually be colonized: **I am not liable for anything.** Not your files, not your computer, not your cat walking across the keyboard, not lost data, not emotional distress from a bad chapter break, not acts of God, acts of Congress, or acts of sheer stupidity. My total liability across all claims is **$0.00 USD.** You paid nothing. You get nothing back.

### Indemnification — You Protect Me

If someone comes after me because of something you did with this script, you agree to pay all my legal fees, defend me in court (bring snacks), and cover any damages. This applies even if I somehow contributed by writing a script that works too well.

### Your Responsibility

You bear sole, complete, absolute, no-takebacks responsibility for everything you do with this. "I didn't read the disclaimer" is not a defense. "My dog did it" is also not a defense.

### Severability

If any part of this is found unenforceable, the rest still stands. You don't get to throw out the whole thing because one clause was too spicy.

### Governing Law

Governed by California law. Disputes settled in California courts. Yes, you'd have to fly here. No, I won't pay for your ticket.

### Support the Authors

I built this so reading is more convenient, not so people can rip off writers. If you're merging chapters from a series you love, make sure you actually paid for it. Authors have rent to pay. Buy their stuff. Leave nice reviews. Don't be the reason they quit.

================================================================================

## License

Released for personal use. See the disclaimer above (seriously, read it — it's actually pretty funny).
I don't claim ownership over anything this script processes.
