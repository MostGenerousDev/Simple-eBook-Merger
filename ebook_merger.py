#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║              Simple eBook Merger v2.0                             ║
║              github.com/GenerousGreivous/Simple-eBook-Merger      ║
╚══════════════════════════════════════════════════════════════╝

Merges multiple eBook files into a single EPUB.
Supports EPUB, plain text (.txt), and HTML (.htm/.html) inputs.

Wrote this because I got tired of juggling 30+ chapter files on
my eReader whenever an author splits their work into individual
files. Just toss them in a folder, run this, done.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOW TO RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Just double-click the script or run it from the terminal:

    python ebook_merger.py          (opens the GUI)
    python ebook_merger.py --nogui  (headless / terminal mode)

  In terminal mode you'll need to edit the CONFIG section below
  before running. The GUI handles everything through the window.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python 3.8+  →  https://python.org/downloads
  (check "Add Python to PATH" during install)

  Then run once in your terminal:
    pip install ebooklib beautifulsoup4 lxml

  tkinter ships with Python on Windows and Mac by default.
  On Linux you might need:  sudo apt install python3-tk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUPPORTED FORMATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .epub  — chapters, formatting, images all carried over
  .txt   — turned into a single chapter, paragraphs kept
  .html  — turned into a chapter, formatting kept
  .htm   — same as .html

  Anything else gets skipped automatically.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Files get merged in alphabetical order by filename.
    Prefix with numbers to control order (01_, 02_, etc.)
  - Divider pages go between each source file by default,
    so you know where one ends and the next starts.
  - EPUB inputs keep their chapter structure, TXT and HTML
    each become one chapter.
  - Images from EPUB files are preserved.
  - Output is EPUB 3, works with Calibre, Apple Books, Kobo,
    Kindle (via Send to Kindle / conversion), Rockbox, etc.
  - DRM-protected files won't work — the script doesn't and
    can't strip DRM.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠  LEGAL DISCLAIMER — PLEASE READ, I'M BEGGING YOU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BY DOWNLOADING, VIEWING, THINKING ABOUT, DREAMING ABOUT,
  MENTIONING IN PASSING, RUNNING, COMPILING, DECOMPILING,
  REVERSE-ENGINEERING, SCREEN-SHOTTING, PRINTING OUT AND
  FOLDING INTO A PAPER AIRPLANE, OR OTHERWISE INTERACTING
  WITH THIS SOFTWARE IN ANY WAY — INCLUDING BUT NOT LIMITED
  TO STARING AT IT REAL HARD — YOU ACKNOWLEDGE THAT YOU HAVE
  READ, UNDERSTOOD, MEMORIZED, AND TATTOOED THE FOLLOWING
  TERMS ONTO YOUR SOUL. IF YOU DO NOT AGREE, CLOSE THIS
  IMMEDIATELY, DELETE IT FROM YOUR COMPUTER, BURN THE HARD
  DRIVE, AND BURY THE ASHES AT A CROSSROADS AT MIDNIGHT.

  1. PERSONAL USE ONLY — SERIOUSLY
     This script exists for one reason: so you can merge
     ebook files YOU ALREADY OWN into one file for YOUR OWN
     eyeballs. That's it. If you use it for literally
     anything else, that's a you problem, not a me problem.

  2. COPYRIGHT — DON'T BE THAT GUY
     The stuff you merge is almost certainly copyrighted by
     someone who isn't you. You may NOT, under any
     circumstances, in this universe or any parallel one:
       • Share, upload, email, fax, telegraph, send via
         carrier pigeon, or otherwise transmit the output
       • Sell it, trade it, barter it for goats, or
         monetize it in any way whatsoever
       • Post it online anywhere — not even "just for
         friends," not even on a private Discord, not even
         on a USB stick you "accidentally" leave somewhere
       • Use it for AI training, data mining, or feeding
         to any kind of machine learning model
       • Strip DRM to feed files into this — that violates
         the DMCA (17 U.S.C. §1201) and I am NOT catching
         a federal charge because you wanted free books
       • Print it out and wallpaper your bathroom with it
         (actually that one might be fine, but I'm still
         not liable)
     Violating copyright law can get you fined into the
     shadow realm and/or imprisoned. Don't test it.

  3. ABSOLUTELY ZERO WARRANTY — NONE — VOID — NADA
     This software is provided "AS IS" and "AS AVAILABLE"
     and "WITH ALL FAULTS" and "GOOD LUCK" and "DON'T LOOK
     AT ME" — without warranty of any kind, express, implied,
     spiritual, hypothetical, or interdimensional, including
     but not limited to the warranties of merchantability,
     fitness for a particular purpose, non-infringement,
     accuracy, reliability, or the warranty that it won't
     set your computer on fire (it won't, probably, but
     legally speaking I make no promises).

     I tested this thing. It works on my machine. If it
     doesn't work on yours: skill issue. (Kidding. Mostly.
     But still not my fault.)

  4. LIMITATION OF LIABILITY — THE BIG ONE
     TO THE MAXIMUM EXTENT PERMITTED BY EVERY LAW THAT HAS
     EVER BEEN WRITTEN, IS CURRENTLY BEING WRITTEN, OR WILL
     BE WRITTEN IN THE FUTURE BY ANY GOVERNING BODY ON
     EARTH, IN SPACE, OR ON ANY CELESTIAL BODY THAT MAY
     EVENTUALLY BE COLONIZED:

     I am not liable for ANYTHING. Not for:
       • Your computer exploding (it won't)
       • Your files getting corrupted (back them up)
       • Your eReader bricking (not how that works)
       • Your cat walking across the keyboard mid-merge
       • Lost profits, lost data, lost time, lost sleep,
         lost friendships, existential dread, or emotional
         distress caused by a poorly formatted chapter break
       • Any lawsuits, fines, cease-and-desists, angry
         emails, or strongly worded letters you receive
       • Acts of God, acts of war, acts of Congress, acts
         of your IT department, or acts of sheer stupidity
       • Anything else that happens, has happened, or could
         theoretically happen in any timeline

     My total liability to you, for everything, forever,
     across all claims, is exactly $0.00 USD. Not a penny
     more. You paid nothing for this. You get nothing back.
     That's how free software works.

  5. INDEMNIFICATION — YOU PROTECT ME, NOT THE OTHER WAY AROUND
     If someone comes after me because of something YOU did
     with this script, YOU agree to:
       • Pay all my legal fees (and my lawyer isn't cheap)
       • Defend me in court (bring snacks)
       • Cover any damages, settlements, fines, or
         judgments — including the ones that haven't been
         invented yet
       • Basically make me whole, as if your reckless
         behavior never happened
     This applies even if I somehow contributed to the
     problem by, say, writing a script that works too well.

  6. YOUR RESPONSIBILITY — ALL OF IT
     You are a grown human being (or a very talented dog,
     I don't judge) and you bear SOLE, COMPLETE, ABSOLUTE,
     TOTAL, UNQUALIFIED, NO-TAKEBACKS responsibility for:
       • Everything you do with this script
       • Everything that happens as a result
       • Making sure you're not breaking any laws —
         federal, state, local, international, maritime,
         intergalactic, or HOA
       • Any consequences, legal or otherwise, including
         but not limited to imprisonment, fines, social
         ostracism, bad karma, or haunting by the ghost
         of a displeased author
     "I didn't read the disclaimer" is not a defense.
     "I didn't know" is not a defense. "My dog did it"
     is not a defense (even if your dog is the talented
     one mentioned above).

  7. SUPPORT THE AUTHORS — THE MORAL PART
     Look, I built this so reading is more convenient,
     not so people can rip off writers. If you're merging
     chapters from a series you love, MAKE SURE you
     actually paid for it. Authors are real people with
     rent to pay. Support them. Buy their stuff. Leave
     nice reviews. Don't be the reason they quit writing.

  8. SEVERABILITY — THE LEGAL SAFETY NET
     If any part of this disclaimer is found to be
     unenforceable by a court of law (or a particularly
     aggressive homeowners association), the rest of it
     still stands. You don't get to throw out the whole
     thing because one clause was too spicy.

  9. GOVERNING LAW
     This disclaimer is governed by the laws of whatever
     jurisdiction the author happens to reside in at the
     time of the dispute — and no, I'm not telling you
     where that is. If there's a legal conflict, it gets
     resolved wherever I feel like filing. You agreed to
     this. Good luck with that.

  10. FINAL CLAUSE — THE "I REALLY MEAN IT" CLAUSE
      By using this software you acknowledge that:
        • You read all of this (yes, ALL of it)
        • You understood it (or at least tried)
        • You agree to every single word
        • You will not now, or at any point in the
          future, try to hold me responsible for
          anything related to this script
        • You accept that this disclaimer may be
          updated at any time and it's on you to
          check for changes
        • If you somehow find a loophole, congrats,
          but the spirit of this disclaimer still
          applies and you know it
"""

import os
import sys
import uuid
import threading
from datetime import datetime

# ── dependency checks ──
# doing these early so we can bail with a helpful message
# instead of a cryptic traceback

_missing = []

try:
    from ebooklib import epub
except ImportError:
    _missing.append("ebooklib")

try:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
    import warnings
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except ImportError:
    _missing.append("beautifulsoup4")

if _missing:
    print(
        "\n  Missing libraries: " + ", ".join(_missing) + "\n"
        "  Fix it by running:\n"
        "    pip install ebooklib beautifulsoup4 lxml\n"
    )
    sys.exit(1)


# ══════════════════════════════════════════════════════════════
# CONFIG — only matters in --nogui (terminal) mode
# ══════════════════════════════════════════════════════════════
# In GUI mode all of this is set through the window instead.

# Folder with the ebook files you want to merge
INPUT_DIR = r"PUT_YOUR_FOLDER_PATH_HERE"

# Where to save the merged epub
OUTPUT_FILE = "merged_book.epub"

# Metadata
BOOK_TITLE  = "My Merged eBook"
BOOK_AUTHOR = "Various Authors"

# Stick a divider page between each source file?
ADD_DIVIDERS = True

# ══════════════════════════════════════════════════════════════
# END OF CONFIG
# ══════════════════════════════════════════════════════════════


ALLOWED_EXTENSIONS = {".epub", ".txt", ".html", ".htm"}


# ──────────────────────────────────────────────────────────────
# Core merge logic (shared by GUI and terminal mode)
# ──────────────────────────────────────────────────────────────

def find_ebook_files(folder):
    """Grab every supported file from a folder, sorted by name."""
    hits = []
    skipped = []
    for name in sorted(os.listdir(folder)):
        full = os.path.join(folder, name)
        if not os.path.isfile(full):
            continue
        ext = os.path.splitext(name)[1].lower()
        if ext in ALLOWED_EXTENSIONS:
            hits.append((full, name))
        else:
            skipped.append(name)
    return hits, skipped


def _uid(prefix="item"):
    """Short random id so filenames inside the epub don't collide."""
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def _make_divider(source_name, idx):
    """Builds a simple centered title page to go between files."""
    label = os.path.splitext(source_name)[0]
    xhtml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{t}</title></head>\n'
        '<body style="text-align:center; padding-top:40%;">\n'
        '  <h1 style="font-size:1.8em; margin-bottom:0.3em;">{t}</h1>\n'
        '  <hr style="width:50%; margin:1em auto;"/>\n'
        '</body>\n'
        '</html>\n'
    ).format(t=label)
    ch = epub.EpubHtml(title=label, file_name=f"divider_{idx}.xhtml", lang="en")
    ch.set_content(xhtml.encode("utf-8"))
    return ch


def _pull_epub_chapters(path, name, book, counter):
    """
    Crack open an epub and pull its chapters + images into the
    merged book. Keeps spine order when possible.
    """
    try:
        src = epub.read_epub(path, options={"ignore_ncx": True})
    except Exception as exc:
        return [], counter, f"couldn't read epub: {exc}"

    added = []
    img_map = {}
    css_map = {}
    docs = []

    for item in src.get_items():
        kind = item.get_type()
        if kind == 9:        # xhtml document / chapter
            docs.append(item)
        elif kind == 6:      # image
            new = f"images/{_uid('img')}_{os.path.basename(item.get_name())}"
            img_map[item.get_name()] = new
            img = epub.EpubImage()
            img.file_name = new
            img.media_type = item.media_type
            img.set_content(item.get_content())
            book.add_item(img)
        elif kind == 3:      # css
            new = f"styles/{_uid('css')}_{os.path.basename(item.get_name())}"
            css_map[item.get_name()] = new
            css = epub.EpubItem(
                file_name=new, media_type="text/css",
                content=item.get_content(),
            )
            book.add_item(css)

    # figure out spine order
    spine_ids = []
    try:
        spine_ids = [sid for sid, _ in src.spine]
    except Exception:
        pass

    by_id = {}
    for item in src.get_items():
        if item.get_id():
            by_id[item.get_id()] = item

    if spine_ids:
        ordered, seen = [], set()
        for sid in spine_ids:
            if sid in by_id and by_id[sid].get_type() == 9:
                ordered.append(by_id[sid])
                seen.add(by_id[sid].get_name())
        for d in docs:
            if d.get_name() not in seen:
                ordered.append(d)
        docs = ordered

    for doc in docs:
        counter += 1
        fname = f"chapter_{counter:04d}.xhtml"

        raw = doc.get_content()
        try:
            html = raw.decode("utf-8", errors="replace")
        except AttributeError:
            html = str(raw)

        # rewrite image + css paths so they point to our renamed copies
        for old, new in img_map.items():
            base = os.path.basename(old)
            html = html.replace(old, new).replace(f"../{old}", new)
            if base != old:
                html = html.replace(base, os.path.basename(new))
        for old, new in css_map.items():
            html = html.replace(old, new).replace(f"../{old}", new)

        # try to fish out a chapter title from the html
        title = None
        try:
            soup = BeautifulSoup(html, "lxml")
            tag = soup.find(["h1", "h2", "h3", "title"])
            if tag:
                title = tag.get_text(strip=True)
        except Exception:
            pass
        if not title:
            title = os.path.basename(doc.get_name())
            title = title.replace(".xhtml", "").replace(".html", "")
            title = title.replace("_", " ").replace("-", " ").title()

        ch = epub.EpubHtml(title=title, file_name=fname, lang="en")
        ch.set_content(html.encode("utf-8"))
        book.add_item(ch)
        added.append((ch, title))

    return added, counter, None


def _txt_to_chapter(path, name, counter):
    """Turn a .txt into a single epub chapter."""
    counter += 1
    label = os.path.splitext(name)[0]
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
    except Exception as exc:
        return None, counter, str(exc)

    paras = []
    for ln in raw.split("\n"):
        ln = ln.rstrip()
        if ln:
            ln = ln.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            paras.append(f"    <p>{ln}</p>")
        else:
            paras.append("    <p><br/></p>")

    words = len(raw.split())
    body = "\n".join(paras)
    xhtml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{t}</title></head>\n'
        '<body>\n  <h1>{t}</h1>\n{b}\n</body>\n</html>\n'
    ).format(t=label, b=body)

    ch = epub.EpubHtml(title=label, file_name=f"chapter_{counter:04d}.xhtml", lang="en")
    ch.set_content(xhtml.encode("utf-8"))
    return (ch, label, words), counter, None


def _html_to_chapter(path, name, counter):
    """Turn an .html/.htm file into a single epub chapter."""
    counter += 1
    label = os.path.splitext(name)[0]
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
    except Exception as exc:
        return None, counter, str(exc)

    try:
        soup = BeautifulSoup(raw, "lxml")
        tag = soup.find(["h1", "h2", "h3", "title"])
        if tag:
            label = tag.get_text(strip=True)
        words = len(soup.get_text().split())
    except Exception:
        words = len(raw.split())

    try:
        soup = BeautifulSoup(raw, "lxml")
        body_tag = soup.find("body")
        inner = body_tag.decode_contents() if body_tag else raw
    except Exception:
        inner = raw

    xhtml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{t}</title></head>\n'
        '<body>\n{b}\n</body>\n</html>\n'
    ).format(t=label, b=inner)

    ch = epub.EpubHtml(title=label, file_name=f"chapter_{counter:04d}.xhtml", lang="en")
    ch.set_content(xhtml.encode("utf-8"))
    return (ch, label, words), counter, None


def merge_files(files, output_path, title, author, dividers=True, log=print):
    """
    The actual merge. Takes a list of (path, filename) tuples,
    builds one epub, writes it to output_path.

    `log` is a callable — in terminal mode it's just print(),
    in GUI mode it pushes text to the log widget.

    Returns a dict with stats or raises on fatal errors.
    """
    book = epub.EpubBook()
    book.set_identifier(f"merged-{uuid.uuid4().hex[:12]}")
    book.set_title(title)
    book.set_language("en")
    book.add_author(author)
    book.add_metadata("DC", "date", datetime.today().strftime("%Y-%m-%d"))

    spine_items = []
    toc = []
    ch_count = 0
    ok_count = 0
    total_words = 0

    for i, (fpath, fname) in enumerate(files):
        ext = os.path.splitext(fname)[1].lower()
        log(f"  [{i+1}/{len(files)}] {fname}")

        if dividers and i > 0:
            d = _make_divider(fname, i)
            book.add_item(d)
            spine_items.append(d)

        if ext == ".epub":
            chapters, ch_count, err = _pull_epub_chapters(fpath, fname, book, ch_count)
            if err:
                log(f"    ⚠ {err}")
                continue
            if not chapters:
                log(f"    ⚠ no chapters found")
                continue

            for ch, _ in chapters:
                spine_items.append(ch)

            if len(chapters) == 1:
                toc.append(chapters[0])
            else:
                sec = os.path.splitext(fname)[0]
                toc.append((epub.Section(sec), [ch for ch, _ in chapters]))

            wc = sum(
                len(BeautifulSoup(ch.get_content(), "lxml").get_text().split())
                for ch, _ in chapters
            )
            total_words += wc
            log(f"    ✓ {len(chapters)} chapter(s), ~{wc:,} words")
            ok_count += 1

        elif ext == ".txt":
            result, ch_count, err = _txt_to_chapter(fpath, fname, ch_count)
            if err or not result:
                log(f"    ⚠ {err or 'empty file'}")
                continue
            ch, label, wc = result
            book.add_item(ch)
            spine_items.append(ch)
            toc.append(ch)
            total_words += wc
            log(f"    ✓ 1 chapter, ~{wc:,} words")
            ok_count += 1

        elif ext in (".html", ".htm"):
            result, ch_count, err = _html_to_chapter(fpath, fname, ch_count)
            if err or not result:
                log(f"    ⚠ {err or 'empty file'}")
                continue
            ch, label, wc = result
            book.add_item(ch)
            spine_items.append(ch)
            toc.append(ch)
            total_words += wc
            log(f"    ✓ 1 chapter, ~{wc:,} words")
            ok_count += 1

    if not spine_items:
        raise RuntimeError("Nothing to merge — no chapters were produced.")

    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + spine_items

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    epub.write_epub(output_path, book, {})

    size = os.path.getsize(output_path)
    if size > 1024 * 1024:
        size_nice = f"{size / (1024*1024):.1f} MB"
    else:
        size_nice = f"{size / 1024:.1f} KB"

    return {
        "files_merged": ok_count,
        "chapters": ch_count,
        "words": total_words,
        "size": size_nice,
        "path": os.path.abspath(output_path),
    }


# ──────────────────────────────────────────────────────────────
# GUI (tkinter)
# ──────────────────────────────────────────────────────────────

def launch_gui():
    """
    Opens the graphical interface. Everything's in here so tkinter
    is only imported when we actually need it — keeps the terminal
    mode dependency-free.
    """
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox

    # ── colours / fonts ──
    BG       = "#1e1e2e"
    BG_MID   = "#282840"
    BG_ENTRY = "#313148"
    FG       = "#e0e0e8"
    FG_DIM   = "#8888a0"
    ACCENT   = "#7c6ff7"
    ACCENT2  = "#9b8afb"
    GREEN    = "#50c878"
    RED      = "#ff6b6b"
    FONT     = ("Segoe UI", 10)
    FONT_SM  = ("Segoe UI", 9)
    FONT_LOG = ("Consolas", 9)
    FONT_H   = ("Segoe UI", 13, "bold")

    root = tk.Tk()
    root.title("Simple eBook Merger")
    root.configure(bg=BG)
    root.resizable(True, True)

    # try to set a reasonable starting size
    root.geometry("680x720")
    root.minsize(520, 560)

    # ── styles ──
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background=BG)
    style.configure("Mid.TFrame", background=BG_MID)
    style.configure("TLabel", background=BG, foreground=FG, font=FONT)
    style.configure("Dim.TLabel", background=BG, foreground=FG_DIM, font=FONT_SM)
    style.configure("Head.TLabel", background=BG, foreground=FG, font=FONT_H)

    style.configure("Accent.TButton", font=FONT, padding=(12, 6))
    style.map("Accent.TButton",
        background=[("active", ACCENT2), ("!active", ACCENT)],
        foreground=[("active", "#ffffff"), ("!active", "#ffffff")],
    )
    style.configure("TButton", font=FONT, padding=(10, 5))

    style.configure("TCheckbutton", background=BG, foreground=FG, font=FONT)
    style.map("TCheckbutton", background=[("active", BG)])

    style.configure("TEntry", fieldbackground=BG_ENTRY, foreground=FG,
                     insertcolor=FG, font=FONT, padding=5)

    # ── layout ──
    outer = ttk.Frame(root, padding=20)
    outer.pack(fill="both", expand=True)

    # header
    ttk.Label(outer, text="Simple eBook Merger", style="Head.TLabel").pack(anchor="w")
    ttk.Label(outer, text="Toss your files in a folder, pick it, hit merge.",
              style="Dim.TLabel").pack(anchor="w", pady=(0, 14))

    # ── input folder row ──
    row1 = ttk.Frame(outer)
    row1.pack(fill="x", pady=(0, 8))
    ttk.Label(row1, text="Input folder:").pack(side="left")

    input_var = tk.StringVar()
    input_entry = ttk.Entry(row1, textvariable=input_var)
    input_entry.pack(side="left", fill="x", expand=True, padx=(8, 6))

    def pick_folder():
        d = filedialog.askdirectory(title="Pick folder with your eBooks")
        if d:
            input_var.set(d)
            _refresh_file_list()

    ttk.Button(row1, text="Browse...", command=pick_folder).pack(side="right")

    # ── output file row ──
    row2 = ttk.Frame(outer)
    row2.pack(fill="x", pady=(0, 8))
    ttk.Label(row2, text="Save as:").pack(side="left")

    output_var = tk.StringVar(value="merged_book.epub")
    output_entry = ttk.Entry(row2, textvariable=output_var)
    output_entry.pack(side="left", fill="x", expand=True, padx=(8, 6))

    def pick_output():
        f = filedialog.asksaveasfilename(
            title="Save merged EPUB as",
            defaultextension=".epub",
            filetypes=[("EPUB files", "*.epub"), ("All files", "*.*")],
        )
        if f:
            output_var.set(f)

    ttk.Button(row2, text="Browse...", command=pick_output).pack(side="right")

    # ── title / author row ──
    row3 = ttk.Frame(outer)
    row3.pack(fill="x", pady=(0, 8))

    ttk.Label(row3, text="Title:").pack(side="left")
    title_var = tk.StringVar(value="My Merged eBook")
    ttk.Entry(row3, textvariable=title_var, width=24).pack(side="left", padx=(8, 16))

    ttk.Label(row3, text="Author:").pack(side="left")
    author_var = tk.StringVar(value="Various Authors")
    ttk.Entry(row3, textvariable=author_var).pack(side="left", fill="x", expand=True, padx=(8, 0))

    # ── dividers checkbox ──
    dividers_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(outer, text="Insert divider pages between files",
                     variable=dividers_var).pack(anchor="w", pady=(0, 10))

    # ── file preview ──
    preview_frame = ttk.LabelFrame(outer, text=" Files to merge (alphabetical order) ",
                                    padding=8)
    preview_frame.pack(fill="both", expand=False, pady=(0, 8))
    preview_frame.configure(height=120)

    file_listbox = tk.Listbox(preview_frame, bg=BG_MID, fg=FG, font=FONT_SM,
                               selectbackground=ACCENT, selectforeground="#fff",
                               borderwidth=0, highlightthickness=0, height=6)
    file_listbox.pack(fill="both", expand=True)

    file_count_var = tk.StringVar(value="No folder selected yet")
    ttk.Label(outer, textvariable=file_count_var, style="Dim.TLabel").pack(anchor="w", pady=(0, 6))

    def _refresh_file_list():
        file_listbox.delete(0, "end")
        folder = input_var.get().strip()
        if not folder or not os.path.isdir(folder):
            file_count_var.set("No folder selected yet")
            return
        found, skipped = find_ebook_files(folder)
        for _, name in found:
            ext = os.path.splitext(name)[1].lower()
            file_listbox.insert("end", f"  {name}   ({ext})")
        note = f"{len(found)} supported file(s)"
        if skipped:
            note += f", {len(skipped)} skipped"
        file_count_var.set(note)

    # ── log output ──
    log_frame = ttk.LabelFrame(outer, text=" Log ", padding=6)
    log_frame.pack(fill="both", expand=True, pady=(0, 10))

    log_text = tk.Text(log_frame, bg=BG_MID, fg=FG, font=FONT_LOG,
                        wrap="word", borderwidth=0, highlightthickness=0,
                        state="disabled", height=10)
    log_scroll = ttk.Scrollbar(log_frame, orient="vertical", command=log_text.yview)
    log_text.configure(yscrollcommand=log_scroll.set)
    log_scroll.pack(side="right", fill="y")
    log_text.pack(side="left", fill="both", expand=True)

    # coloured tags
    log_text.tag_configure("ok",   foreground=GREEN)
    log_text.tag_configure("warn", foreground="#e8a838")
    log_text.tag_configure("err",  foreground=RED)
    log_text.tag_configure("dim",  foreground=FG_DIM)

    def write_log(msg, tag=None):
        log_text.configure(state="normal")
        if tag:
            log_text.insert("end", msg + "\n", tag)
        else:
            log_text.insert("end", msg + "\n")
        log_text.see("end")
        log_text.configure(state="disabled")

    # ── bottom bar ──
    bottom = ttk.Frame(outer)
    bottom.pack(fill="x")

    status_var = tk.StringVar(value="Ready")
    ttk.Label(bottom, textvariable=status_var, style="Dim.TLabel").pack(side="left")

    merge_btn = ttk.Button(bottom, text="Merge", style="Accent.TButton")
    merge_btn.pack(side="right")

    # ── merge action ──
    def do_merge():
        folder = input_var.get().strip()
        out    = output_var.get().strip()
        ttl    = title_var.get().strip() or "Merged eBook"
        auth   = author_var.get().strip() or "Unknown"
        divs   = dividers_var.get()

        # clear old log
        log_text.configure(state="normal")
        log_text.delete("1.0", "end")
        log_text.configure(state="disabled")

        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Oops", "Pick a valid input folder first.")
            return
        if not out:
            messagebox.showerror("Oops", "Set an output file path.")
            return

        files, skipped = find_ebook_files(folder)
        if not files:
            messagebox.showwarning("Nothing to merge",
                "No supported files (.epub, .txt, .html, .htm) found in that folder.")
            return

        # disable the button so you can't double-click
        merge_btn.configure(state="disabled")
        status_var.set("Merging...")

        if skipped:
            for s in skipped:
                write_log(f"  skipped: {s}", "dim")
            write_log("")

        def _run():
            try:
                stats = merge_files(
                    files, out, ttl, auth,
                    dividers=divs,
                    log=lambda m: root.after(0, write_log, m),
                )
                def _done():
                    write_log("")
                    write_log(f"  Done! {stats['files_merged']} file(s), "
                              f"{stats['chapters']} chapter(s), "
                              f"~{stats['words']:,} words, {stats['size']}", "ok")
                    write_log(f"  Saved → {stats['path']}", "ok")
                    status_var.set("Done!")
                    merge_btn.configure(state="normal")
                root.after(0, _done)

            except Exception as exc:
                def _fail():
                    write_log(f"\n  ERROR: {exc}", "err")
                    status_var.set("Failed")
                    merge_btn.configure(state="normal")
                root.after(0, _fail)

        # run in a thread so the GUI doesn't freeze
        threading.Thread(target=_run, daemon=True).start()

    merge_btn.configure(command=do_merge)

    # ── go ──
    root.mainloop()


# ──────────────────────────────────────────────────────────────
# Terminal (headless) mode — works the same as v1
# ──────────────────────────────────────────────────────────────

def run_terminal():
    print("\n" + "=" * 60)
    print("  Simple eBook Merger v2.0")
    print("=" * 60 + "\n")

    print("⚠  LEGAL REMINDER:")
    print("   Personal use only. Only merge files you actually own.")
    print("   Don't distribute copyrighted material.")
    print("   I am not liable for ANYTHING. Not your files, not your")
    print("   computer, not your cat, not your existential dread.")
    print("   By running this you accept full responsibility and agree")
    print("   to the full disclaimer in the source code. Read it.\n")

    # check config
    problems = []
    if "PUT_YOUR_FOLDER" in INPUT_DIR or not INPUT_DIR.strip():
        problems.append("INPUT_DIR isn't set — edit the CONFIG section at the top of the script.")
    elif not os.path.isdir(INPUT_DIR):
        problems.append(f"INPUT_DIR doesn't exist: {INPUT_DIR}")
    if not OUTPUT_FILE.strip():
        problems.append("OUTPUT_FILE isn't set.")

    if problems:
        print("=" * 60)
        print("  Setup incomplete:")
        print("=" * 60)
        for p in problems:
            print(f"\n  ✗ {p}")
        print("\nOpen this script in a text editor and fill in the CONFIG section.\n")
        return

    print(f"→ Scanning: {INPUT_DIR}\n")
    files, skipped = find_ebook_files(INPUT_DIR)

    for s in skipped:
        print(f"  ⚠ skipping: {s}")

    if not files:
        print("\nNo supported files found.")
        print("  Supported: .epub, .txt, .html, .htm")
        print("  Double-check INPUT_DIR.\n")
        return

    print(f"  Found {len(files)} file(s):")
    for _, name in files:
        print(f"    • {name}")

    print(f"\n→ Merging...\n")

    try:
        stats = merge_files(files, OUTPUT_FILE, BOOK_TITLE, BOOK_AUTHOR,
                            dividers=ADD_DIVIDERS)

        print(f"\n" + "=" * 60)
        print(f"  Files merged   : {stats['files_merged']}")
        print(f"  Chapters total : {stats['chapters']}")
        print(f"  Total words    : ~{stats['words']:,}")
        print(f"  Output size    : {stats['size']}")
        print("=" * 60)
        print(f"\n✓ Done! Saved to:\n  {stats['path']}\n")

    except PermissionError:
        print(f"\nERROR: Can't write to {OUTPUT_FILE}")
        print("  Maybe it's open in another program?\n")
    except RuntimeError as e:
        print(f"\n  ✗ {e}\n")
    except Exception as e:
        print(f"\nSomething went wrong: {e}")
        raise


# ──────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if "--nogui" in sys.argv:
        run_terminal()
    else:
        try:
            launch_gui()
        except ImportError:
            # tkinter not installed (some minimal linux setups)
            print("\n  tkinter isn't available — falling back to terminal mode.")
            print("  (install it with: sudo apt install python3-tk)\n")
            run_terminal()
