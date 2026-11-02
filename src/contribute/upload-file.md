# Upload a File

Use this path for a PDF, slide deck, diagram or document you wrote — or for material you have
explicit written permission to share. The website has **no upload box**: files are added to the
repository through GitHub, which gives every upload a reviewable history.

## Before you upload

Answer these questions honestly:

1. **Did I create this file?** If yes, state the licence you are granting.
2. **Did someone else create it?** Do you have written permission to redistribute it? A link to
   the original is not permission.
3. **Is it already freely available from the author?** If so, link to the original host instead of
   copying it into the repository.
4. **Does it contain personal data?** Remove names, roll numbers, marks, phone numbers and email
   addresses belonging to other people.
5. **Is it under 10 MiB?** Compress it or link to the authorised source.

**Never upload** textbook scans, publisher slides, leaked question papers, exam answers,
executables, archives, password-protected files or anything you do not have the right to share.

## File rules

| Rule | Value |
| --- | --- |
| Maximum size | **10 MiB** per file (GitHub's browser upload limit is 25 MiB) |
| Allowed extensions | `.pdf`, `.pptx`, `.docx`, `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`, `.md` |
| Filename style | lowercase `kebab-case`, no spaces, descriptive |
| Location | `src/assets/materials/<semester>/<subject>/` |
| Licence | State it in the listing and the pull request |

Examples:

```text
src/assets/materials/semester-1/mathematics-1/limits-worked-examples.pdf
src/assets/materials/semester-2/programming/python-loops-slides.pdf
src/assets/materials/semester-1/physics/lab-record-template.docx
```

Version a file with a suffix only when both versions are genuinely useful:
`notes-v2.pdf`. Do not keep near-duplicate copies.

## Step 1 — Fork the repository

Open [FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library), click **Fork**, and
create the fork under your account. If you already have a fork, click **Sync fork → Update branch**
before starting.

## Step 2 — Create the folders in your fork

GitHub cannot create an empty folder, so navigate to the intended parent and use
**Add file → Create new file**. In the filename box type the full path, including the new folder
name and a temporary `.md` file, for example:

```text
src/assets/materials/semester-1/engineering-graphics/README.md
```

Put a single line in the file:

```markdown
# Engineering graphics — Semester 1
```

Commit it to a new branch such as `materials/semester-1-engineering-graphics`. The folder now
exists in your branch.

> Why a README? It gives the folder a human-readable subject title and keeps the repository
> navigable. It is not added to `SUMMARY.md`, so it is not a website chapter.

## Step 3 — Upload the file

1. In your fork, switch to your new branch.
2. Navigate to the folder you created.
3. Click **Add file → Upload files**.
4. Drag in the PDF or slides, or choose files from your device.
5. Write a commit message:

   ```text
   materials: add semester 1 engineering graphics notes
   ```

6. Commit directly to your branch.

The file must keep its lowercase `kebab-case` name. GitHub preserves the filename exactly.

## Step 4 — Add the listing to a Markdown page

A file becomes discoverable only when a Markdown index describes it. Open the relevant semester
page, for example `src/academics/semester-1/README.md`, click the pencil, and add an entry:

```markdown
## Engineering graphics

| Resource | Format | Description | Credit / licence |
| --- | --- | --- | --- |
| [Orthographic projection notes](LINK) | <span class="fmt fmt-pdf">PDF</span> | Worked examples for first-angle projection, including common mistakes | Your Name — CC BY 4.0 |
```

Replace `LINK` with the path **relative to that Markdown file**. From
`src/academics/semester-1/README.md` to
`src/assets/materials/semester-1/engineering-graphics/orthographic-projection.pdf`:

```markdown
[Orthographic projection notes](../../assets/materials/semester-1/engineering-graphics/orthographic-projection.pdf)
```

The link must start with `../../`, not `/assets/`. Test it after the build deploys.

Include keywords a student would search for in the description: subject, topic, semester, author.
Search indexes the Markdown listing, **not the PDF contents**.

If the subject deserves its own chapter (several files and a long explanation), create a page
under `src/academics/semester-1/<subject>/README.md` and add it to `src/SUMMARY.md` using the
chapter format. One file is usually not enough to justify a new chapter.

## Step 5 — Open the pull request

Commit the listing change, then open a pull request against `FossMec/foss-mec-library:main`.

In the description include:

- **File:** the path you added.
- **Subject and semester:** for example, Semester 1 Engineering Graphics.
- **Author:** the person who created the file.
- **Permission:** "I wrote this file" or "I have written permission from the author; attached in
  this thread."
- **Licence:** for example CC BY 4.0, or the existing licence with a link.
- **Description:** what the file covers and who it helps.
- **Checks:** confirm the file is under 10 MiB, contains no personal data and the relative link
  resolves.

Download the one-page [contribution checklist](../assets/materials/templates/contribution-checklist.pdf)
if you want the requirements beside you while preparing the PR. The checklist is an original
template prepared for this library, not student material.

## Step 6 — CI and review

Two automated checks run:

- `python3 scripts/validate_content.py` checks extensions, size, local links and `SUMMARY.md`.
- `mdbook build` builds the site with `create-missing = false`.

A maintainer then checks origin, permission, attribution and usefulness. If something is missing,
they will ask in the pull request. Push the fix to the same branch.

After merge, GitHub Actions deploys automatically. Open the live page and click the download link
to confirm the file serves correctly.

## Common mistakes

| Mistake | Result | Fix |
| --- | --- | --- |
| File over 10 MiB | Validation fails | Compress, split, or link to the original |
| `.zip`, `.exe`, `.rar` | Disallowed extension | Do not upload; use the canonical source |
| `/assets/materials/...` link | Broken on project Pages | Use `../../assets/materials/...` |
| Spaces or capitals in filename | Inconsistent paths, fragile links | Rename to `kebab-case` |
| New chapter not in `SUMMARY.md` | Build fails with `create-missing` | Add the chapter or do not create a page |
| Listing without description/credit | Review blocked | Add title, description, author, licence |
| PDF only, no Markdown listing | Invisible to search and navigation | Add the table entry |

If a file is rejected, that is not a judgement of its quality. It usually means the licence or
origin cannot be verified, and the library must stay safe to publish.
