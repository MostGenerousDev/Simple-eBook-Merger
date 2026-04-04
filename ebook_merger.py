#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║              Simple eBook Merger v1.0                             ║
║              github.com/GenerousGreivous/Simple-eBook-Merger      ║
╚══════════════════════════════════════════════════════════════╝

Merges multiple eBook files into a single EPUB.
Supports EPUB, plain text (.txt), and HTML (.htm/.html) inputs.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Python 3.8+  →  https://python.org/downloads
  (check "Add Python to PATH" during install)

  Then run once in Command Prompt / Terminal:
    pip install ebooklib beautifulsoup4 lxml

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUICK START
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Place the eBook files you want to merge into a single folder
  2. Edit the CONFIG section below:
       - Set INPUT_DIR to the folder containing your eBooks
       - Set OUTPUT_FILE to where you want the merged EPUB saved
       - Optionally set BOOK_TITLE and BOOK_AUTHOR
  3. Run the script:
       Windows:   python ebook_merger.py
       Mac/Linux: python3 ebook_merger.py

  The files are merged in alphabetical order by filename.
  Tip: prefix your files with numbers to control the order:
    01_prologue.epub, 02_chapter1.epub, 03_chapter2.txt, etc.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUPPORTED FORMATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .epub  — Full EPUB eBooks (chapters, formatting, and
           embedded images are all preserved)
  .txt   — Plain text files (converted to a single EPUB
           chapter with basic paragraph formatting)
  .html  — HTML files (converted to an EPUB chapter with
  .htm     formatting preserved)

  Files with other extensions are skipped with a warning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Files are sorted alphabetically by filename within
    INPUT_DIR. Use numbered prefixes (01_, 02_, ...) to
    control merge order.
  - Each input file becomes one or more chapters in the
    output. EPUB inputs keep their original chapter splits;
    TXT and HTML files each become a single chapter.
  - A divider page is inserted between each source file
    so you can tell where one book ends and the next begins.
    Set ADD_DIVIDERS = False to disable this.
  - Images embedded in EPUB files are carried over into the
    merged output.
  - The output is always a standard EPUB 3 file, compatible
    with most eBook readers (Calibre, Apple Books, Kobo,
    Kindle via conversion, etc.).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠  LEGAL DISCLAIMER — READ BEFORE USE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BY DOWNLOADING, INSTALLING, OR RUNNING THIS SCRIPT IN ANY
  WAY, YOU ACKNOWLEDGE THAT YOU HAVE READ, UNDERSTOOD, AND
  AGREE TO BE BOUND BY ALL OF THE FOLLOWING TERMS. IF YOU DO
  NOT AGREE, DO NOT USE THIS SCRIPT.

  1. PERSONAL USE ONLY
     This script is provided strictly for personal,
     non-commercial use. It is intended to merge eBook files
     that you own or have lawful access to for your own
     private reading convenience. Any other use is strictly
     prohibited.

  2. COPYRIGHT & INTELLECTUAL PROPERTY
     The content of the eBook files you merge using this
     script may be protected by copyright law, including but
     not limited to the U.S. Copyright Act (17 U.S.C.), the
     Digital Millennium Copyright Act (DMCA), and equivalent
     legislation worldwide (Berne Convention, EU Copyright
     Directive, etc.).

     You may NOT, under any circumstances:
       • Merge files you do not own or have lawful access to
       • Distribute, share, upload, or transmit the merged
         output to any other person or platform
       • Publish, republish, or post the merged content online
       • Sell, license, or monetise the merged content
       • Use the content for AI training or data harvesting
       • Remove or alter any copyright notices within the
         source files
       • Create derivative works for distribution
     Doing so may constitute civil copyright infringement
     and/or criminal copyright theft, punishable by
     significant fines and/or imprisonment.

  3. NO CIRCUMVENTION OF ACCESS CONTROLS
     This script does not bypass, crack, or circumvent any
     DRM or access control mechanism. If your eBook files
     contain DRM, this script will not process them. Using
     third-party tools to strip DRM before merging may
     violate the DMCA (17 U.S.C. §1201) and is strictly
     prohibited.

  4. NO WARRANTY
     THIS SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF
     ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
     TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
     PARTICULAR PURPOSE, ACCURACY, OR NON-INFRINGEMENT.
     THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF
     THIS SCRIPT IS WITH YOU.

  5. LIMITATION OF LIABILITY
     TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW,
     IN NO EVENT SHALL THE SCRIPT'S AUTHOR(S), CONTRIBUTORS,
     DISTRIBUTORS, OR ANY ASSOCIATED PARTIES BE LIABLE FOR
     ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
     CONSEQUENTIAL, OR PUNITIVE DAMAGES WHATSOEVER,
     INCLUDING BUT NOT LIMITED TO:
       • Loss of data, revenue, profits, or goodwill
       • Legal fees, fines, or penalties incurred by you
       • Claims brought against you by third parties
       • Any copyright infringement you commit
       • Any damage to your computer, files, or systems
     ARISING OUT OF OR IN CONNECTION WITH YOUR USE OR
     INABILITY TO USE THIS SCRIPT, EVEN IF ADVISED OF THE
     POSSIBILITY OF SUCH DAMAGES.

  6. INDEMNIFICATION
     By using this script you agree to fully indemnify,
     defend, and hold harmless the script's author(s),
     contributors, and distributors from and against any
     and all claims, damages, losses, liabilities, costs,
     and expenses (including reasonable legal fees) arising
     out of or relating to your use of this script, your
     violation of these terms, or your violation of any
     third-party rights, including copyright.

  7. USER RESPONSIBILITY
     You, the end user, bear sole and complete
     responsibility for:
       • How you use this script and its output
       • Ensuring the files you merge are lawfully obtained
       • Ensuring your use complies with all applicable
         local, national, and international laws
       • Any consequences, legal or otherwise, of your use
     Ignorance of these terms or applicable law is not a
     defence.
"""

import os
import sys
import uuid
from datetime import datetime

try:
    from ebooklib import epub
except ImportError:
    print(
        "\nERROR: Missing required library 'ebooklib'.\n"
        "  Install it by running:\n"
        "    pip install ebooklib beautifulsoup4 lxml\n"
    )
    sys.exit(1)

try:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
    import warnings
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except ImportError:
    print(
        "\nERROR: Missing required library 'beautifulsoup4'.\n"
        "  Install it by running:\n"
        "    pip install beautifulsoup4 lxml\n"
    )
    sys.exit(1)


# ══════════════════════════════════════════════════════════════
# CONFIG — fill these in before running
# ══════════════════════════════════════════════════════════════

# Folder containing the eBook files to merge
# Windows example: r"C:\Users\YourName\Documents\ebooks"
# Mac/Linux example: "/home/yourname/Documents/ebooks"
INPUT_DIR = r"PUT_YOUR_FOLDER_PATH_HERE"

# Where to save the merged EPUB (full path recommended)
# Windows example: r"C:\Users\YourName\Documents\merged_book.epub"
# Mac/Linux example: "/home/yourname/Documents/merged_book.epub"
OUTPUT_FILE = "merged_book.epub"

# Metadata for the merged EPUB
BOOK_TITLE  = "My Merged eBook"
BOOK_AUTHOR = "Various Authors"

# Insert a divider page between each source file?
# True  = adds a page with the source filename between each file's content
# False = chapters flow directly into each other
ADD_DIVIDERS = True

# ══════════════════════════════════════════════════════════════
# END OF CONFIG — no need to edit anything below this line
# ══════════════════════════════════════════════════════════════


SUPPORTED_EXTENSIONS = {".epub", ".txt", ".html", ".htm"}


def validate_config():
    """Check config before starting."""
    errors = []
    if "PUT_YOUR_FOLDER" in INPUT_DIR or not INPUT_DIR.strip():
        errors.append(
            "INPUT_DIR is not set.\n"
            "  Set it to the folder containing your eBook files."
        )
    elif not os.path.isdir(INPUT_DIR):
        errors.append(
            f"INPUT_DIR does not exist or is not a folder:\n"
            f"  {INPUT_DIR}\n"
            f"  Check the path and try again."
        )
    if not OUTPUT_FILE.strip():
        errors.append("OUTPUT_FILE is not set.")
    if errors:
        print("\n" + "=" * 60)
        print("  Setup incomplete — please fix the following:")
        print("=" * 60)
        for e in errors:
            print(f"\n  ✗ {e}")
        print("\nOpen this script in a text editor and fill in the CONFIG section.")
        return False
    return True


def discover_files(input_dir):
    """
    Find all supported eBook files in the input directory.
    Returns a sorted list of (full_path, filename) tuples.
    """
    found = []
    for fname in sorted(os.listdir(input_dir)):
        fpath = os.path.join(input_dir, fname)
        if not os.path.isfile(fpath):
            continue
        ext = os.path.splitext(fname)[1].lower()
        if ext in SUPPORTED_EXTENSIONS:
            found.append((fpath, fname))
        else:
            print(f"  ⚠ Skipping unsupported file: {fname}")
    return found


def make_unique_id(prefix="item"):
    """Generate a unique ID string for EPUB items."""
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def create_divider_chapter(source_filename, index):
    """
    Create an EPUB chapter that acts as a divider page between
    source files. Shows the source filename centered on the page.
    """
    title = os.path.splitext(source_filename)[0]
    html = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{title}</title></head>\n'
        '<body style="text-align:center; padding-top:40%;">\n'
        '  <h1 style="font-size:1.8em; margin-bottom:0.3em;">{title}</h1>\n'
        '  <hr style="width:50%; margin:1em auto;"/>\n'
        '</body>\n'
        '</html>\n'
    ).format(title=title)
    chapter = epub.EpubHtml(
        title=title,
        file_name=f"divider_{index}.xhtml",
        lang="en",
    )
    chapter.set_content(html.encode("utf-8"))
    return chapter


def process_epub(filepath, filename, merged_book, chapter_counter):
    """
    Read an EPUB file and add its chapters and images to the
    merged book. Returns a list of (chapter, toc_label) tuples
    and the updated chapter counter.
    """
    try:
        source = epub.read_epub(filepath, options={"ignore_ncx": True})
    except Exception as e:
        print(f"    ✗ Error reading EPUB: {e}")
        return [], chapter_counter

    chapters_added = []

    # Collect all items from the source EPUB
    images = {}
    stylesheets = {}
    docs = []

    for item in source.get_items():
        itype = item.get_type()

        if itype == 9:  # XHTML document
            docs.append(item)
        elif itype == 6:  # Image
            new_name = f"images/{make_unique_id('img')}_{os.path.basename(item.get_name())}"
            images[item.get_name()] = new_name
            img_item = epub.EpubImage()
            img_item.file_name = new_name
            img_item.media_type = item.media_type
            img_item.set_content(item.get_content())
            merged_book.add_item(img_item)
        elif itype == 3:  # Stylesheet
            new_name = f"styles/{make_unique_id('css')}_{os.path.basename(item.get_name())}"
            stylesheets[item.get_name()] = new_name
            css_item = epub.EpubItem(
                file_name=new_name,
                media_type="text/css",
                content=item.get_content(),
            )
            merged_book.add_item(css_item)

    # Get the reading order from spine if available
    spine_ids = []
    try:
        spine_ids = [sid for sid, _ in source.spine]
    except Exception:
        pass

    # Build an ID→item map
    id_map = {}
    for item in source.get_items():
        if item.get_id():
            id_map[item.get_id()] = item

    # Order documents by spine, fall back to discovery order
    if spine_ids:
        ordered_docs = []
        seen = set()
        for sid in spine_ids:
            if sid in id_map and id_map[sid].get_type() == 9:
                ordered_docs.append(id_map[sid])
                seen.add(id_map[sid].get_name())
        # Add any docs not in spine
        for d in docs:
            if d.get_name() not in seen:
                ordered_docs.append(d)
        docs = ordered_docs

    for doc_item in docs:
        chapter_counter += 1
        new_file_name = f"chapter_{chapter_counter:04d}.xhtml"

        # Rewrite image and CSS references in the HTML
        content = doc_item.get_content()
        try:
            content_str = content.decode("utf-8", errors="replace")
        except AttributeError:
            content_str = str(content)

        # Update image paths
        for old_path, new_path in images.items():
            # Handle both relative and absolute paths
            old_basename = os.path.basename(old_path)
            content_str = content_str.replace(old_path, new_path)
            content_str = content_str.replace(f"../{old_path}", new_path)
            # Also try just the basename in case paths differ
            if old_basename != old_path:
                content_str = content_str.replace(old_basename, os.path.basename(new_path))

        # Update stylesheet paths
        for old_path, new_path in stylesheets.items():
            content_str = content_str.replace(old_path, new_path)
            content_str = content_str.replace(f"../{old_path}", new_path)

        # Extract a title from the HTML if possible
        try:
            soup = BeautifulSoup(content_str, "lxml")
            heading = soup.find(["h1", "h2", "h3", "title"])
            title = heading.get_text(strip=True) if heading else None
        except Exception:
            title = None

        if not title:
            title = doc_item.get_name().replace(".xhtml", "").replace(".html", "")
            title = os.path.basename(title).replace("_", " ").replace("-", " ").title()

        chapter = epub.EpubHtml(
            title=title,
            file_name=new_file_name,
            lang="en",
        )
        chapter.set_content(content_str.encode("utf-8"))
        merged_book.add_item(chapter)
        chapters_added.append((chapter, title))

    return chapters_added, chapter_counter


def process_txt(filepath, filename, chapter_counter):
    """
    Read a plain text file and convert it to an EPUB chapter.
    Returns the chapter, toc label, and updated counter.
    """
    chapter_counter += 1
    title = os.path.splitext(filename)[0]

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        print(f"    ✗ Error reading file: {e}")
        return None, chapter_counter

    # Convert plain text to simple HTML paragraphs
    paragraphs = []
    for line in text.split("\n"):
        line = line.rstrip()
        if line:
            # Escape HTML special characters
            line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            paragraphs.append(f"    <p>{line}</p>")
        else:
            paragraphs.append("    <p><br/></p>")

    body_html = "\n".join(paragraphs)
    word_count = len(text.split())

    html = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{title}</title></head>\n'
        '<body>\n'
        '  <h1>{title}</h1>\n'
        '{body}\n'
        '</body>\n'
        '</html>\n'
    ).format(title=title, body=body_html)

    chapter = epub.EpubHtml(
        title=title,
        file_name=f"chapter_{chapter_counter:04d}.xhtml",
        lang="en",
    )
    chapter.set_content(html.encode("utf-8"))
    return (chapter, title, word_count), chapter_counter


def process_html(filepath, filename, chapter_counter):
    """
    Read an HTML file and convert it to an EPUB chapter.
    Returns the chapter, toc label, and updated counter.
    """
    chapter_counter += 1
    title = os.path.splitext(filename)[0]

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception as e:
        print(f"    ✗ Error reading file: {e}")
        return None, chapter_counter

    # Try to extract a title from the HTML
    try:
        soup = BeautifulSoup(content, "lxml")
        heading = soup.find(["h1", "h2", "h3", "title"])
        if heading:
            title = heading.get_text(strip=True)
        word_count = len(soup.get_text().split())
    except Exception:
        word_count = len(content.split())

    # Ensure the HTML is valid XHTML for EPUB
    try:
        soup = BeautifulSoup(content, "lxml")
        body = soup.find("body")
        body_content = body.decode_contents() if body else content
    except Exception:
        body_content = content

    html = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'
        '<head><title>{title}</title></head>\n'
        '<body>\n'
        '{body}\n'
        '</body>\n'
        '</html>\n'
    ).format(title=title, body=body_content)

    chapter = epub.EpubHtml(
        title=title,
        file_name=f"chapter_{chapter_counter:04d}.xhtml",
        lang="en",
    )
    chapter.set_content(html.encode("utf-8"))
    return (chapter, title, word_count), chapter_counter


def build_merged_epub(files):
    """
    Merge all input files into a single EPUB.
    Returns (total_chapters, total_files_processed).
    """
    merged = epub.EpubBook()

    # Set metadata
    merged.set_identifier(f"merged-ebook-{uuid.uuid4().hex[:12]}")
    merged.set_title(BOOK_TITLE)
    merged.set_language("en")
    merged.add_author(BOOK_AUTHOR)
    merged.add_metadata("DC", "date", datetime.today().strftime("%Y-%m-%d"))
    merged.add_metadata("DC", "description", f"Merged eBook created on {datetime.today().strftime('%B %d, %Y')}")

    all_chapters = []   # ordered list of EpubHtml items for spine
    toc_entries = []     # table of contents entries
    chapter_counter = 0
    files_processed = 0
    total_words = 0

    for i, (fpath, fname) in enumerate(files):
        ext = os.path.splitext(fname)[1].lower()
        print(f"\n  [{i + 1}/{len(files)}] {fname}", end="", flush=True)

        # Add divider between files
        if ADD_DIVIDERS and i > 0:
            divider = create_divider_chapter(fname, i)
            merged.add_item(divider)
            all_chapters.append(divider)

        if ext == ".epub":
            print(f" (EPUB)", flush=True)
            chapters, chapter_counter = process_epub(
                fpath, fname, merged, chapter_counter
            )
            if chapters:
                for ch, label in chapters:
                    all_chapters.append(ch)
                # Add top-level TOC entry pointing to first chapter of this file
                if len(chapters) == 1:
                    toc_entries.append(chapters[0])
                else:
                    # Nested TOC: file name → individual chapters
                    section_title = os.path.splitext(fname)[0]
                    sub_entries = [ch for ch, _ in chapters]
                    toc_entries.append((
                        epub.Section(section_title),
                        sub_entries,
                    ))
                wc = sum(
                    len(BeautifulSoup(ch.get_content(), "lxml").get_text().split())
                    for ch, _ in chapters
                )
                total_words += wc
                print(f"    ✓ {len(chapters)} chapter(s), ~{wc:,} words")
                files_processed += 1
            else:
                print(f"    ⚠ No chapters extracted")

        elif ext == ".txt":
            print(f" (TXT)", flush=True)
            result, chapter_counter = process_txt(fpath, fname, chapter_counter)
            if result:
                chapter, label, wc = result
                merged.add_item(chapter)
                all_chapters.append(chapter)
                toc_entries.append(chapter)
                total_words += wc
                print(f"    ✓ 1 chapter, ~{wc:,} words")
                files_processed += 1
            else:
                print(f"    ⚠ Could not process file")

        elif ext in (".html", ".htm"):
            print(f" (HTML)", flush=True)
            result, chapter_counter = process_html(fpath, fname, chapter_counter)
            if result:
                chapter, label, wc = result
                merged.add_item(chapter)
                all_chapters.append(chapter)
                toc_entries.append(chapter)
                total_words += wc
                print(f"    ✓ 1 chapter, ~{wc:,} words")
                files_processed += 1
            else:
                print(f"    ⚠ Could not process file")

    if not all_chapters:
        print("\n  ✗ No chapters were produced. Nothing to merge.")
        return 0, 0

    # Build table of contents
    merged.toc = toc_entries

    # Add navigation files (required by EPUB spec)
    merged.add_item(epub.EpubNcx())
    merged.add_item(epub.EpubNav())

    # Set spine (reading order)
    merged.spine = ["nav"] + all_chapters

    # Write the merged EPUB
    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    epub.write_epub(OUTPUT_FILE, merged, {})

    print(f"\n  Total words: ~{total_words:,}")
    return chapter_counter, files_processed


def main():
    print("\n" + "=" * 60)
    print("  Simple eBook Merger v1.0")
    print("=" * 60 + "\n")

    print("⚠  LEGAL REMINDER:")
    print("   This script is for PERSONAL USE ONLY.")
    print("   Only merge files you own or have lawful access to.")
    print("   Distributing copyrighted content is ILLEGAL.")
    print("   By proceeding you accept full liability for your use")
    print("   and release the script's author(s) from all liability.")
    print()

    if not validate_config():
        return

    print("→ Scanning input folder...")
    print(f"  {INPUT_DIR}\n")

    files = discover_files(INPUT_DIR)

    if not files:
        print(
            "\nNo supported files found.\n"
            "  Supported formats: .epub, .txt, .html, .htm\n"
            "  Check that INPUT_DIR points to the correct folder."
        )
        return

    print(f"  Found {len(files)} supported file(s):")
    for _, fname in files:
        ext = os.path.splitext(fname)[1].lower()
        print(f"    • {fname}  ({ext})")

    print(f"\n→ Merging into a single EPUB...")

    try:
        total_chapters, total_files = build_merged_epub(files)

        if total_chapters > 0:
            file_size = os.path.getsize(OUTPUT_FILE)
            if file_size > 1024 * 1024:
                size_str = f"{file_size / (1024 * 1024):.1f} MB"
            else:
                size_str = f"{file_size / 1024:.1f} KB"

            print(f"\n" + "=" * 60)
            print(f"  Files merged    : {total_files}")
            print(f"  Chapters total  : {total_chapters}")
            print(f"  Output size     : {size_str}")
            print(f"=" * 60)
            print(f"\n✓ Done! Saved to:\n  {os.path.abspath(OUTPUT_FILE)}")
        else:
            print("\n  ✗ Merge failed — no content was produced.")

    except PermissionError:
        print(
            f"\nERROR: Cannot write to output file.\n"
            f"  {OUTPUT_FILE}\n"
            f"  The file may be open in another program, or you may\n"
            f"  not have write permission to that folder."
        )
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        raise


if __name__ == "__main__":
    main()
