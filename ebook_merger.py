#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║              Simple eBook Merger v3.0                             ║
║              github.com/GenerousGreivous/Simple-eBook-Merger      ║
╚══════════════════════════════════════════════════════════════╝

Merges multiple eBook files into a single output file.
Supports EPUB, TXT, HTML, PDF, DOCX, RTF, Markdown, FB2, ODT,
and CBZ inputs. Output formats: EPUB, TXT, HTML, PDF, DOCX.

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
    pip install ebooklib beautifulsoup4 lxml pypdf python-docx striprtf markdown odfpy fpdf2 Pillow

  tkinter ships with Python on Windows and Mac by default.
  On Linux you might need:  sudo apt install python3-tk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUPPORTED INPUT FORMATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .epub  — chapters, formatting, images all carried over
  .txt   — turned into a single chapter, paragraphs kept
  .html  — turned into a chapter, formatting kept
  .htm   — same as .html
  .pdf   — text extracted from each page
  .docx  — paragraphs extracted, basic formatting kept
  .rtf   — RTF tags stripped, plain text wrapped into HTML
  .md    — Markdown converted to HTML
  .fb2   — FictionBook XML parsed into chapters
  .odt   — OpenDocument text extracted
  .cbz   — comic book images extracted as pages

  Anything else gets skipped automatically.

SUPPORTED OUTPUT FORMATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .epub  — EPUB 3 (default)
  .txt   — plain text
  .html  — single HTML file
  .pdf   — PDF document
  .docx  — Word document

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
  - Output is EPUB 3 by default, works with Calibre, Apple
    Books, Kobo, Kindle (via Send to Kindle / conversion),
    Rockbox, etc.
  - DRM-protected files won't work — the script doesn't and
    can't strip DRM.
  - Every output file gets a hidden watermark fingerprint
    for tracing. The fingerprint is shown in the log.

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
import hashlib
import random
import re
import html as html_module
import threading
import xml.etree.ElementTree as ET
import zipfile
import io
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

try:
    from pypdf import PdfReader
except ImportError:
    _missing.append("pypdf")

try:
    import docx as python_docx
except ImportError:
    _missing.append("python-docx")

try:
    from striprtf.striprtf import rtf_to_text
except ImportError:
    _missing.append("striprtf")

try:
    import markdown as md_lib
except ImportError:
    _missing.append("markdown")

try:
    from odf.opendocument import load as odf_load
    from odf.text import P as OdfP
    from odf import teletype as odf_teletype
except ImportError:
    _missing.append("odfpy")

try:
    from fpdf import FPDF
except ImportError:
    _missing.append("fpdf2")

try:
    from PIL import Image
except ImportError:
    _missing.append("Pillow")

if _missing:
    print(
        "\n  Missing libraries: " + ", ".join(_missing) + "\n"
        "  Fix it by running:\n"
        "    pip install ebooklib beautifulsoup4 lxml pypdf python-docx"
        " striprtf markdown odfpy fpdf2 Pillow\n"
    )
    sys.exit(1)


# ══════════════════════════════════════════════════════════════
# CONFIG — only matters in --nogui (terminal) mode
# ══════════════════════════════════════════════════════════════
# In GUI mode all of this is set through the window instead.

# Folder with the ebook files you want to merge
INPUT_DIR = r"PUT_YOUR_FOLDER_PATH_HERE"

# Where to save the merged file
OUTPUT_FILE = "merged_book.epub"

# Metadata
BOOK_TITLE  = "My Merged eBook"
BOOK_AUTHOR = "Various Authors"

# Stick a divider page between each source file?
ADD_DIVIDERS = True

# Output format: "epub", "txt", "html", "pdf", "docx"
OUTPUT_FORMAT = "epub"

# ══════════════════════════════════════════════════════════════
# END OF CONFIG
# ══════════════════════════════════════════════════════════════


ALLOWED_EXTENSIONS = {
    ".epub", ".txt", ".html", ".htm", ".pdf", ".docx",
    ".rtf", ".md", ".fb2", ".odt", ".cbz",
}

OUTPUT_FORMATS = ["epub", "txt", "html", "pdf", "docx"]

OUTPUT_EXT_MAP = {
    "epub": ".epub",
    "txt": ".txt",
    "html": ".html",
    "pdf": ".pdf",
    "docx": ".docx",
}


# ──────────────────────────────────────────────────────────────
# Watermark engine
# ──────────────────────────────────────────────────────────────

# Zero-width characters used to encode fingerprint bits
_ZW_CHARS = ["\u200b", "\u200c", "\u200d", "\ufeff"]


def _generate_watermark():
    """
    Create a fresh watermark fingerprint for this merge.
    Returns a dict with the watermark ID, timestamp, and hash.
    """
    wm_id = uuid.uuid4().hex
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    raw = f"{wm_id}-{ts}"
    wm_hash = hashlib.sha256(raw.encode()).hexdigest()[:16]
    return {
        "id": wm_id,
        "timestamp": ts,
        "hash": wm_hash,
        "short": wm_id[:12],
        "full_tag": f"wm:{wm_id[:12]}:{ts}:{wm_hash}",
    }


def _encode_zw(text, fingerprint):
    """
    Encode a fingerprint string as zero-width characters and
    sprinkle them into the text at random-ish positions.
    """
    # convert fingerprint to a sequence of zero-width chars
    zw_seq = ""
    for ch in fingerprint:
        idx = ord(ch) % len(_ZW_CHARS)
        zw_seq += _ZW_CHARS[idx]

    if len(text) < 10:
        return text + zw_seq

    # insert the zero-width sequence in chunks at spaced positions
    chunk_size = max(1, len(zw_seq) // 5)
    chunks = [zw_seq[i:i+chunk_size] for i in range(0, len(zw_seq), chunk_size)]

    positions = sorted(random.sample(
        range(10, max(11, len(text) - 1)),
        min(len(chunks), max(1, len(text) // 50))
    ))

    result = list(text)
    for pos, chunk in zip(positions, chunks):
        if pos < len(result):
            result[pos] = result[pos] + chunk
    return "".join(result)


def _embed_watermark_epub(book, wm):
    """Add watermark to EPUB: metadata + HTML comments + zero-width chars."""
    book.add_metadata(None, "meta", "", {"name": "wm", "content": wm["full_tag"]})
    book.add_metadata("DC", "description",
                       f"<!-- wm:{wm['short']} -->")

    for item in book.get_items():
        if item.get_type() == 9:  # xhtml
            try:
                content = item.get_content().decode("utf-8", errors="replace")
                # add HTML comment watermark
                comment = f"<!-- wm:{wm['full_tag']} -->"
                if "</body>" in content:
                    content = content.replace("</body>", f"{comment}\n</body>", 1)
                # add zero-width chars to text
                content = _encode_zw(content, wm["short"])
                item.set_content(content.encode("utf-8"))
            except Exception:
                pass


def _embed_watermark_text(text, wm):
    """Add watermark to plain text: zero-width chars + whitespace patterns."""
    # add zero-width encoded fingerprint
    text = _encode_zw(text, wm["full_tag"])

    # add trailing whitespace pattern to encode bits of the hash
    lines = text.split("\n")
    hash_bits = bin(int(wm["hash"][:8], 16))[2:].zfill(32)
    for i, bit in enumerate(hash_bits):
        if i < len(lines):
            lines[i] = lines[i].rstrip() + (" " * (1 + int(bit)))
    return "\n".join(lines)


def _embed_watermark_html(html_str, wm):
    """Add watermark to HTML: comments + zero-width chars + meta tag."""
    comment = f"<!-- wm:{wm['full_tag']} -->"
    meta = f'<meta name="wm" content="{wm["full_tag"]}">'

    if "<head>" in html_str:
        html_str = html_str.replace("<head>", f"<head>\n{meta}", 1)
    if "</body>" in html_str:
        html_str = html_str.replace("</body>", f"\n{comment}\n</body>", 1)

    html_str = _encode_zw(html_str, wm["short"])
    return html_str


def _embed_watermark_pdf(pdf, wm):
    """Add watermark to PDF metadata."""
    pdf.set_creator(f"eBook Merger 3.0 [wm:{wm['short']}]")
    pdf.set_subject(f"wm:{wm['full_tag']}")
    pdf.set_keywords(wm["full_tag"])


def _embed_watermark_docx(doc, wm):
    """Add watermark to DOCX: custom properties + zero-width chars in first para."""
    props = doc.core_properties
    props.comments = f"wm:{wm['full_tag']}"
    props.keywords = wm["full_tag"]

    # add zero-width chars to first paragraph if it exists
    if doc.paragraphs:
        for para in doc.paragraphs[:3]:
            if para.text.strip():
                for run in para.runs:
                    if run.text.strip():
                        run.text = _encode_zw(run.text, wm["short"])
                        break
                break


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


# ── input format readers ──

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


def _read_pdf(path, name, counter):
    """Extract text from a PDF, one chapter per page (or all as one)."""
    label = os.path.splitext(name)[0]
    chapters = []
    total_words = 0

    try:
        reader = PdfReader(path)
    except Exception as exc:
        return None, counter, f"couldn't read PDF: {exc}"

    all_text = []
    for page_num, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        all_text.append(text)

    combined = "\n\n".join(all_text)
    if not combined.strip():
        return None, counter, "no text found in PDF"

    counter += 1
    words = len(combined.split())
    total_words += words

    paras = []
    for ln in combined.split("\n"):
        ln = ln.rstrip()
        if ln:
            ln = html_module.escape(ln)
            paras.append(f"    <p>{ln}</p>")
        else:
            paras.append("    <p><br/></p>")

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


def _read_docx(path, name, counter):
    """Extract paragraphs from a DOCX file."""
    label = os.path.splitext(name)[0]

    try:
        doc = python_docx.Document(path)
    except Exception as exc:
        return None, counter, f"couldn't read DOCX: {exc}"

    counter += 1
    paras = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            paras.append("    <p><br/></p>")
            continue

        # basic formatting: bold, italic, headings
        style_name = (para.style.name or "").lower()
        if "heading 1" in style_name:
            paras.append(f"    <h1>{html_module.escape(text)}</h1>")
        elif "heading 2" in style_name:
            paras.append(f"    <h2>{html_module.escape(text)}</h2>")
        elif "heading 3" in style_name:
            paras.append(f"    <h3>{html_module.escape(text)}</h3>")
        else:
            # build inline formatting from runs
            parts = []
            for run in para.runs:
                t = html_module.escape(run.text)
                if run.bold and run.italic:
                    t = f"<b><i>{t}</i></b>"
                elif run.bold:
                    t = f"<b>{t}</b>"
                elif run.italic:
                    t = f"<i>{t}</i>"
                parts.append(t)
            paras.append(f"    <p>{''.join(parts)}</p>")

    full_text = " ".join(p.text for p in doc.paragraphs)
    words = len(full_text.split())

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


def _read_rtf(path, name, counter):
    """Strip RTF formatting and turn into a chapter."""
    label = os.path.splitext(name)[0]

    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        text = rtf_to_text(raw)
    except Exception as exc:
        return None, counter, f"couldn't read RTF: {exc}"

    if not text.strip():
        return None, counter, "empty RTF file"

    counter += 1
    words = len(text.split())

    paras = []
    for ln in text.split("\n"):
        ln = ln.rstrip()
        if ln:
            paras.append(f"    <p>{html_module.escape(ln)}</p>")
        else:
            paras.append("    <p><br/></p>")

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


def _read_markdown(path, name, counter):
    """Convert Markdown to HTML and make a chapter."""
    label = os.path.splitext(name)[0]

    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        html_content = md_lib.markdown(raw, extensions=["extra", "codehilite"])
    except Exception as exc:
        return None, counter, f"couldn't read Markdown: {exc}"

    if not raw.strip():
        return None, counter, "empty Markdown file"

    counter += 1
    words = len(raw.split())

    xhtml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{t}</title></head>\n'
        '<body>\n  <h1>{t}</h1>\n{b}\n</body>\n</html>\n'
    ).format(t=label, b=html_content)

    ch = epub.EpubHtml(title=label, file_name=f"chapter_{counter:04d}.xhtml", lang="en")
    ch.set_content(xhtml.encode("utf-8"))
    return (ch, label, words), counter, None


def _read_fb2(path, name, counter):
    """Parse FictionBook2 XML into a chapter."""
    label = os.path.splitext(name)[0]

    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as exc:
        return None, counter, f"couldn't read FB2: {exc}"

    # FB2 namespace
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"

    # extract text from all <p> elements in <body>
    body = root.find(f".//{ns}body")
    if body is None:
        return None, counter, "no body found in FB2"

    paras = []
    for p in body.iter(f"{ns}p"):
        text = "".join(p.itertext()).strip()
        if text:
            paras.append(f"    <p>{html_module.escape(text)}</p>")

    if not paras:
        return None, counter, "no text found in FB2"

    # try to get title from <title-info><book-title>
    try:
        ti = root.find(f".//{ns}title-info/{ns}book-title")
        if ti is not None and ti.text:
            label = ti.text.strip()
    except Exception:
        pass

    counter += 1
    full_text = " ".join("".join(p.itertext()) for p in body.iter(f"{ns}p"))
    words = len(full_text.split())

    body_html = "\n".join(paras)
    xhtml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{t}</title></head>\n'
        '<body>\n  <h1>{t}</h1>\n{b}\n</body>\n</html>\n'
    ).format(t=html_module.escape(label), b=body_html)

    ch = epub.EpubHtml(title=label, file_name=f"chapter_{counter:04d}.xhtml", lang="en")
    ch.set_content(xhtml.encode("utf-8"))
    return (ch, label, words), counter, None


def _read_odt(path, name, counter):
    """Extract text from an ODT (OpenDocument Text) file."""
    label = os.path.splitext(name)[0]

    try:
        doc = odf_load(path)
    except Exception as exc:
        return None, counter, f"couldn't read ODT: {exc}"

    paras = []
    for p in doc.getElementsByType(OdfP):
        text = odf_teletype.extractText(p).strip()
        if text:
            paras.append(f"    <p>{html_module.escape(text)}</p>")
        else:
            paras.append("    <p><br/></p>")

    if not any(t.strip() for t in paras):
        return None, counter, "no text found in ODT"

    counter += 1
    full_text = " ".join(
        odf_teletype.extractText(p) for p in doc.getElementsByType(OdfP)
    )
    words = len(full_text.split())

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


def _read_cbz(path, name, book, counter):
    """
    Extract images from a CBZ (comic book zip) and add each
    as a page in the output.
    """
    label = os.path.splitext(name)[0]
    added = []

    try:
        with zipfile.ZipFile(path, "r") as zf:
            image_names = sorted([
                n for n in zf.namelist()
                if n.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))
                and not n.startswith("__MACOSX")
            ])

            if not image_names:
                return [], counter, "no images found in CBZ"

            for img_name in image_names:
                counter += 1
                img_data = zf.read(img_name)

                # figure out the media type
                ext = os.path.splitext(img_name)[1].lower()
                media_types = {
                    ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                    ".png": "image/png", ".gif": "image/gif",
                    ".webp": "image/webp",
                }
                media_type = media_types.get(ext, "image/jpeg")

                # add image to epub
                img_fname = f"images/{_uid('cbz')}_{os.path.basename(img_name)}"
                img_item = epub.EpubImage()
                img_item.file_name = img_fname
                img_item.media_type = media_type
                img_item.set_content(img_data)
                book.add_item(img_item)

                # create an xhtml page for this image
                page_title = f"{label} - Page {counter}"
                xhtml = (
                    '<?xml version="1.0" encoding="UTF-8"?>\n'
                    '<!DOCTYPE html>\n'
                    '<html xmlns="http://www.w3.org/1999/xhtml"'
                    ' xml:lang="en" lang="en">\n'
                    '<head><title>{t}</title></head>\n'
                    '<body style="text-align:center; margin:0; padding:0;">\n'
                    '  <img src="{src}" alt="{t}"'
                    ' style="max-width:100%; max-height:100vh;"/>\n'
                    '</body>\n</html>\n'
                ).format(t=page_title, src=img_fname)

                ch = epub.EpubHtml(
                    title=page_title,
                    file_name=f"chapter_{counter:04d}.xhtml",
                    lang="en",
                )
                ch.set_content(xhtml.encode("utf-8"))
                book.add_item(ch)
                added.append((ch, page_title))

    except zipfile.BadZipFile:
        return [], counter, "not a valid CBZ/zip file"
    except Exception as exc:
        return [], counter, f"couldn't read CBZ: {exc}"

    return added, counter, None


# ── output format writers ──

def _strip_html_tags(html_str):
    """Remove HTML tags and return plain text."""
    try:
        soup = BeautifulSoup(html_str, "lxml")
        return soup.get_text(separator="\n")
    except Exception:
        return re.sub(r"<[^>]+>", "", html_str)


def _chapters_to_content_list(chapters_data):
    """
    Normalize chapter data into a list of dicts with
    'title' and 'content' (HTML string) keys.
    """
    result = []
    for item in chapters_data:
        if isinstance(item, dict):
            result.append(item)
        elif isinstance(item, tuple) and len(item) == 2:
            ch, title = item
            try:
                content = ch.get_content().decode("utf-8", errors="replace")
            except Exception:
                content = str(ch.get_content())
            result.append({"title": title, "content": content})
    return result


def _write_epub(chapters_data, spine_items, toc, output_path, title, author,
                dividers_list, book, wm, log=print):
    """Write the merged book as EPUB (the original format)."""
    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + spine_items

    _embed_watermark_epub(book, wm)

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    epub.write_epub(output_path, book, {})


def _write_txt(chapters_data, output_path, title, author, wm, log=print):
    """Write merged content as plain text."""
    lines = []
    lines.append(f"{'=' * 60}")
    lines.append(f"  {title}")
    lines.append(f"  by {author}")
    lines.append(f"{'=' * 60}")
    lines.append("")

    content_list = _chapters_to_content_list(chapters_data)
    for i, ch in enumerate(content_list):
        if i > 0:
            lines.append("")
            lines.append(f"{'─' * 40}")
            lines.append("")
        lines.append(f"  {ch['title']}")
        lines.append(f"{'─' * 40}")
        lines.append("")
        text = _strip_html_tags(ch["content"])
        lines.append(text)

    text_out = "\n".join(lines)
    text_out = _embed_watermark_text(text_out, wm)

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text_out)


def _write_html(chapters_data, output_path, title, author, wm, log=print):
    """Write merged content as a single HTML file."""
    content_list = _chapters_to_content_list(chapters_data)

    body_parts = []
    for i, ch in enumerate(content_list):
        if i > 0:
            body_parts.append('    <hr style="margin: 2em 0;"/>')
        body_parts.append(f'    <h2>{html_module.escape(ch["title"])}</h2>')

        # extract just the body content from the xhtml
        try:
            soup = BeautifulSoup(ch["content"], "lxml")
            body_tag = soup.find("body")
            inner = body_tag.decode_contents() if body_tag else ch["content"]
        except Exception:
            inner = ch["content"]
        body_parts.append(f"    {inner}")

    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{html_module.escape(title)}</title>
<style>
  body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 800px;
         margin: 2em auto; padding: 0 1em; line-height: 1.6; color: #222; }}
  h1 {{ text-align: center; border-bottom: 2px solid #333; padding-bottom: 0.5em; }}
  h2 {{ margin-top: 2em; color: #444; }}
  p {{ text-indent: 1.5em; margin: 0.5em 0; }}
  hr {{ border: none; border-top: 1px solid #ccc; }}
</style>
</head>
<body>
  <h1>{html_module.escape(title)}</h1>
  <p style="text-align:center; color:#666;">by {html_module.escape(author)}</p>
{chr(10).join(body_parts)}
</body>
</html>"""

    html_out = _embed_watermark_html(html_out, wm)

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_out)


def _write_pdf(chapters_data, output_path, title, author, wm, log=print):
    """Write merged content as a PDF."""
    content_list = _chapters_to_content_list(chapters_data)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_title(title)
    pdf.set_author(author)

    _embed_watermark_pdf(pdf, wm)

    def _clean_for_pdf(s):
        """Strip zero-width chars and force latin-1 safe text."""
        for zw in "\u200b\u200c\u200d\ufeff":
            s = s.replace(zw, "")
        try:
            s.encode("latin-1")
        except (UnicodeEncodeError, UnicodeDecodeError):
            s = s.encode("ascii", errors="replace").decode("ascii")
        return s

    # title page
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 60, _clean_for_pdf(title), new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "", 14)
    pdf.cell(0, 10, _clean_for_pdf(f"by {author}"), new_x="LMARGIN", new_y="NEXT", align="C")

    for ch in content_list:
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 10, _clean_for_pdf(ch["title"]), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)

        text = _strip_html_tags(ch["content"])
        text = _clean_for_pdf(text)
        pdf.set_font("Helvetica", "", 11)

        for line in text.split("\n"):
            line = line.strip()
            if not line:
                pdf.ln(3)
                continue
            # reset x to left margin before each line just in case
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(w=0, h=5, text=line, new_x="LMARGIN", new_y="NEXT")

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    pdf.output(output_path)


def _write_docx(chapters_data, output_path, title, author, wm, log=print):
    """Write merged content as a DOCX file."""
    content_list = _chapters_to_content_list(chapters_data)

    doc = python_docx.Document()

    # title
    doc.add_heading(title, level=0)
    doc.add_paragraph(f"by {author}")
    doc.add_paragraph("")

    for i, ch in enumerate(content_list):
        if i > 0:
            doc.add_page_break()
        doc.add_heading(ch["title"], level=1)

        text = _strip_html_tags(ch["content"])
        for line in text.split("\n"):
            line = line.strip()
            if line:
                doc.add_paragraph(line)

    _embed_watermark_docx(doc, wm)

    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    doc.save(output_path)


# ── main merge function ──

def merge_files(files, output_path, title, author, dividers=True,
                output_format="epub", log=print):
    """
    The actual merge. Takes a list of (path, filename) tuples,
    builds the output in the requested format, writes it to output_path.

    `log` is a callable — in terminal mode it's just print(),
    in GUI mode it pushes text to the log widget.

    Returns a dict with stats or raises on fatal errors.
    """
    # generate watermark for this merge
    wm = _generate_watermark()

    # we always build chapters using the epub structures internally,
    # then convert to the target format at the end
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
    all_chapters = []  # list of (ch_object, title) for output writers

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
            all_chapters.extend(chapters)

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

        elif ext == ".cbz":
            chapters, ch_count, err = _read_cbz(fpath, fname, book, ch_count)
            if err:
                log(f"    ⚠ {err}")
                continue
            if not chapters:
                log(f"    ⚠ no images found")
                continue

            for ch, _ in chapters:
                spine_items.append(ch)
            all_chapters.extend(chapters)

            if len(chapters) == 1:
                toc.append(chapters[0])
            else:
                sec = os.path.splitext(fname)[0]
                toc.append((epub.Section(sec), [ch for ch, _ in chapters]))

            log(f"    ✓ {len(chapters)} page(s)")
            ok_count += 1

        else:
            # all single-chapter formats
            reader_map = {
                ".txt":  _txt_to_chapter,
                ".html": _html_to_chapter,
                ".htm":  _html_to_chapter,
                ".pdf":  _read_pdf,
                ".docx": _read_docx,
                ".rtf":  _read_rtf,
                ".md":   _read_markdown,
                ".fb2":  _read_fb2,
                ".odt":  _read_odt,
            }
            reader = reader_map.get(ext)
            if not reader:
                log(f"    ⚠ unsupported format: {ext}")
                continue

            result, ch_count, err = reader(fpath, fname, ch_count)
            if err or not result:
                log(f"    ⚠ {err or 'empty file'}")
                continue

            ch, label, wc = result
            book.add_item(ch)
            spine_items.append(ch)
            toc.append(ch)
            all_chapters.append((ch, label))
            total_words += wc
            log(f"    ✓ 1 chapter, ~{wc:,} words")
            ok_count += 1

    if not spine_items:
        raise RuntimeError("Nothing to merge — no chapters were produced.")

    # write output in the requested format
    fmt = output_format.lower().strip()

    if fmt == "epub":
        _write_epub(all_chapters, spine_items, toc, output_path, title, author,
                     [], book, wm, log)
    elif fmt == "txt":
        _write_txt(all_chapters, output_path, title, author, wm, log)
    elif fmt == "html":
        _write_html(all_chapters, output_path, title, author, wm, log)
    elif fmt == "pdf":
        _write_pdf(all_chapters, output_path, title, author, wm, log)
    elif fmt == "docx":
        _write_docx(all_chapters, output_path, title, author, wm, log)
    else:
        raise RuntimeError(f"Unknown output format: {fmt}")

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
        "watermark": wm["full_tag"],
        "watermark_short": wm["short"],
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
    root.title("Simple eBook Merger v3.0")
    root.configure(bg=BG)
    root.resizable(True, True)

    # try to set a reasonable starting size
    root.geometry("680x780")
    root.minsize(520, 600)

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

    style.configure("TCombobox", fieldbackground=BG_ENTRY, foreground=FG,
                     font=FONT, padding=5)

    # ── layout ──
    outer = ttk.Frame(root, padding=20)
    outer.pack(fill="both", expand=True)

    # header
    ttk.Label(outer, text="Simple eBook Merger v3.0", style="Head.TLabel").pack(anchor="w")
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
        fmt = format_var.get().lower()
        ext = OUTPUT_EXT_MAP.get(fmt, ".epub")
        ftypes = [
            ("EPUB files", "*.epub"),
            ("Text files", "*.txt"),
            ("HTML files", "*.html"),
            ("PDF files", "*.pdf"),
            ("Word documents", "*.docx"),
            ("All files", "*.*"),
        ]
        f = filedialog.asksaveasfilename(
            title="Save merged file as",
            defaultextension=ext,
            filetypes=ftypes,
        )
        if f:
            output_var.set(f)

    ttk.Button(row2, text="Browse...", command=pick_output).pack(side="right")

    # ── output format row ──
    row_fmt = ttk.Frame(outer)
    row_fmt.pack(fill="x", pady=(0, 8))
    ttk.Label(row_fmt, text="Output format:").pack(side="left")

    format_var = tk.StringVar(value="EPUB")
    format_combo = ttk.Combobox(
        row_fmt, textvariable=format_var,
        values=["EPUB", "TXT", "HTML", "PDF", "DOCX"],
        state="readonly", width=10,
    )
    format_combo.pack(side="left", padx=(8, 0))

    def _on_format_change(event=None):
        fmt = format_var.get().lower()
        ext = OUTPUT_EXT_MAP.get(fmt, ".epub")
        current = output_var.get().strip()
        if current:
            base = os.path.splitext(current)[0]
            output_var.set(base + ext)

    format_combo.bind("<<ComboboxSelected>>", _on_format_change)

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
        fmt    = format_var.get().lower()

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
            exts = ", ".join(sorted(ALLOWED_EXTENSIONS))
            messagebox.showwarning("Nothing to merge",
                f"No supported files ({exts}) found in that folder.")
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
                    output_format=fmt,
                    log=lambda m: root.after(0, write_log, m),
                )
                def _done():
                    write_log("")
                    write_log(f"  Done! {stats['files_merged']} file(s), "
                              f"{stats['chapters']} chapter(s), "
                              f"~{stats['words']:,} words, {stats['size']}", "ok")
                    write_log(f"  Saved → {stats['path']}", "ok")
                    write_log(f"  Watermark: {stats['watermark']}", "dim")
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
# Terminal (headless) mode — works the same as before, plus
# output format support
# ──────────────────────────────────────────────────────────────

def run_terminal():
    print("\n" + "=" * 60)
    print("  Simple eBook Merger v3.0")
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

    fmt = OUTPUT_FORMAT.lower().strip()
    if fmt not in OUTPUT_FORMATS:
        problems.append(f"OUTPUT_FORMAT '{OUTPUT_FORMAT}' isn't valid. "
                        f"Use one of: {', '.join(OUTPUT_FORMATS)}")

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
        exts = ", ".join(sorted(ALLOWED_EXTENSIONS))
        print(f"\nNo supported files found.")
        print(f"  Supported: {exts}")
        print("  Double-check INPUT_DIR.\n")
        return

    print(f"  Found {len(files)} file(s):")
    for _, name in files:
        print(f"    • {name}")

    print(f"\n→ Merging into {fmt.upper()} format...\n")

    try:
        stats = merge_files(files, OUTPUT_FILE, BOOK_TITLE, BOOK_AUTHOR,
                            dividers=ADD_DIVIDERS, output_format=fmt)

        print(f"\n" + "=" * 60)
        print(f"  Files merged   : {stats['files_merged']}")
        print(f"  Chapters total : {stats['chapters']}")
        print(f"  Total words    : ~{stats['words']:,}")
        print(f"  Output size    : {stats['size']}")
        print(f"  Output format  : {fmt.upper()}")
        print(f"  Watermark      : {stats['watermark']}")
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
