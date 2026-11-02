# Academic Materials

This section is for notes, slides, diagrams and question banks for MEC courses, organised by
semester and subject. Materials are published **only** when the contributor wrote them or has
explicit permission to redistribute them.

## Browse by semester

<div class="card-grid">
  <a class="card" href="semester-1/">
    <span class="card__kicker">First year</span>
    <span class="card__title">Semester 1</span>
    <span class="card__text">First-semester material, listed only after a verified contribution.</span>
    <span class="card__arrow">Open semester 1 →</span>
  </a>
  <a class="card" href="semester-2/">
    <span class="card__kicker">First year</span>
    <span class="card__title">Semester 2</span>
    <span class="card__text">Second-semester material, listed only after a verified contribution.</span>
    <span class="card__arrow">Open semester 2 →</span>
  </a>
</div>

Semester 3 onwards will get their own pages when the first verified material for those semesters
is accepted. Until then, use the [Open Learning Resources](../resources/) directory for
free official references.

## What belongs here

| Accepted | Not accepted |
| --- | --- |
| Original notes you wrote in Markdown, PDF or slides | Copyrighted textbook PDFs or publisher slides |
| Diagrams and summaries created by you | Scanned pages from a textbook |
| Question papers only where the institution permits sharing | Leaked or confidential exam papers |
| Material with a clear licence or written permission | Files containing personal student data |

Each listing must include a human-readable title, the subject, relevant keywords, a one-line
description, the author/credit, the licence or permission note, and a working relative link.

## Listing format

Use a Markdown table with four columns: **Resource** (a relative link), **Format**
(Notes/PDF/Slides), **Description** (one line) and **Credit / licence** (author and permission).
Do not publish a row until the file and permission are verified.

Place the file at:

```text
src/assets/materials/<semester>/<subject>/<descriptive-name>.<ext>
```

Then link it from the page with a path **relative to the Markdown file**:

```markdown
[descriptive title](../../assets/materials/<semester>/<subject>/<descriptive-name>.<ext>)
```

Do not use a leading `/assets/...` path: the site is published under
`https://fossmec.github.io/foss-mec-library/`, so root-relative links break.

## Before you upload

- **Size:** keep each file at or below **10 MiB**.
- **Formats:** `.pdf`, `.pptx`, `.docx`, `.png`, `.jpg`, `.webp`, `.svg` and `.md`.
- **Name:** lowercase `kebab-case`, descriptive, with a version suffix only when needed.
- **Permission:** state the licence (for example CC BY 4.0) or attach the author's written permission
  in the pull request description.
- **Search:** describe the content in the Markdown listing, because search cannot read inside a PDF.

<div class="contribute-band">
  <p><strong>Have material to add?</strong> The browser-only guide walks you through forking,
  uploading and opening a pull request.</p>
  <p><a href="../contribute/upload-file.md">Upload a file →</a> ·
  <a href="../contribute/">All contribution paths →</a></p>
</div>
