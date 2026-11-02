# Contributing to the FOSS MEC Library

Thank you for helping build a permanent, open knowledge library for MEC. This guide covers the
browser-only workflow, the command-line workflow, content rules and review expectations.

**You need a free GitHub account.** You do **not** need Rust, mdBook, Git or a local editor to
contribute. The website has no upload form or account system; GitHub is the contribution system.

## Choose a contribution

| I want to… | Path | Guide |
| --- | --- | --- |
| Add original notes or fix a page | Written Markdown | [Add written notes](https://fossmec.github.io/foss-mec-library/contribute/add-notes.html) |
| Upload a PDF or slides I may share | File upload | [Upload a file](https://fossmec.github.io/foss-mec-library/contribute/upload-file.html) |
| Suggest a free external link | GitHub issue form | [Suggest a resource](https://fossmec.github.io/foss-mec-library/contribute/suggest-resource.html) |
| Report a broken or outdated page | GitHub issue form | [Report a broken link](https://github.com/FossMec/foss-mec-library/issues/new?template=report-broken-link.yml) |
| Request a new course/topic | GitHub issue form | [Request a topic](https://github.com/FossMec/foss-mec-library/issues/new?template=request-topic.yml) |

Start with a small change. One focused pull request is easier to review, teach and merge.

## Browser-only workflow (recommended for workshops)

No local installation.

1. **Sign in** to GitHub and verify your email.
2. Open [FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library) and click
   **Fork**. Choose your own account.
3. In **your fork**, open the page you want to change and click the pencil
   (**Edit this file**), or use **Add file → Create new file** / **Upload files**.
4. Make one focused change. Keep the existing Markdown style.
5. Scroll to **Commit changes**:
   - write a message such as `docs: clarify git restore example`;
   - choose **Create a new branch for this commit**;
   - name the branch `docs/short-description`.
6. Click **Propose changes**, then **Create pull request** against
   `FossMec/foss-mec-library:main`.
7. Complete the pull request template, including the permission statement.
8. Wait for the `build` check and maintainer review. Push fixes to the same branch.

If **Fork** is missing, sign in and verify your email. If **Compare & pull request** is missing:
open the **Pull requests** tab → **New pull request** → **compare across forks**, then select your
fork and branch.

The full walkthrough with screenshots-in-words is in the live
[Quickstart](https://fossmec.github.io/foss-mec-library/workshop/quickstart.html).

## Command-line workflow

### 1. Fork and clone

Fork on GitHub, then:

```bash
git clone https://github.com/YOUR-USERNAME/foss-mec-library.git
cd foss-mec-library
git remote add upstream https://github.com/FossMec/foss-mec-library.git
git remote -v
```

### 2. Create a branch

```bash
git switch main
git pull upstream main
git switch -c docs/short-description
```

### 3. Make the change

- **Markdown chapter:** add or edit a file under `src/`.
- **New chapter:** also add it to `src/SUMMARY.md`; a missing file fails the build.
- **Uploaded material:** put it under
  `src/assets/materials/<semester>/<subject>/<descriptive-name>.<ext>`.
- **External link:** add a row to the relevant `src/resources/*.md` page.

### 4. Preview and validate

Install mdBook 0.5.4 from the
[releases page](https://github.com/rust-lang/mdBook/releases/tag/v0.5.4), then:

```bash
mdbook --version
python3 scripts/validate_content.py
mdbook build
mdbook serve --open
```

`mdbook test` is not used: it runs Rust code examples and does not validate PDFs or notes.

### 5. Commit and push

```bash
git status
git diff
git add path/to/changed-files
git commit -m "docs: short imperative description"
git push -u origin docs/short-description
```

### 6. Open the pull request

Use the link GitHub prints, or open the upstream repository and click
**Compare & pull request**. Target `main`. Complete every section of the template.

## Content rules

### General

- Write in your own words. Paraphrase sources; do not paste copyrighted text.
- One topic per pull request.
- Use lowercase `kebab-case` for filenames and folders; no spaces.
- Use `#` once at the top of a page and `##` for sections.
- Keep prose searchable: include subject, topic and keywords in the page, not only in a PDF.
- No personal data: names, roll numbers, marks, phone numbers or emails of other people.
- No secrets, API keys, executables, archives, password-protected files or malware.
- No affiliate links, pirated books, leaked exam papers or auto-generated content dumps.

### Markdown and links

- Local links must be **relative** to the current file: `../../assets/materials/...`.
- Never use `/assets/...`; GitHub Pages serves this project under `/foss-mec-library/`.
- External links must use the canonical author/project URL.
- Every local link is checked by `scripts/validate_content.py`; external links are checked by a
  human during review, not fetched in CI.

### Uploaded files

| Rule | Value |
| --- | --- |
| Maximum size | 10 MiB per file |
| Allowed extensions | `.md`, `.pdf`, `.pptx`, `.docx`, `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg` |
| Naming | lowercase `kebab-case`, descriptive |
| Location | `src/assets/materials/<semester>/<subject>/` |
| Listing | Required: title, format, description, author, licence, relative link |

GitHub's browser upload limit is 25 MiB, but this project's policy is stricter. For larger or
already-hosted material, link to the authorised source instead. Git LFS is not used for
Pages-hosted assets.

### Permission and licensing

By submitting original documentation you agree to publish it under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with attribution to you. In the pull
request, state:

- your name or preferred credit;
- that you wrote the text/file;
- any sources or licences for adapted material;
- for third-party files, the author's explicit permission (link or quote in the PR thread).

Do not assume that previously shared student material can be relicensed. If permission is
unclear, link to the original instead of uploading a copy. Maintainers may reject a file whose
origin cannot be verified; that protects the organisation and the contributor.

## Pull request review

Every PR runs the `build` check:

1. `python3 scripts/validate_content.py`
2. `mdbook build`

Deployment **does not** run on pull requests. Review covers:

- accuracy and clarity;
- original authorship and attribution;
- licence/permission;
- link quality and canonical URLs;
- file type and size;
- scope and Markdown structure.

A maintainer may request changes, edit wording, or ask you to split the PR. Review is a
conversation. Push fixes to the same branch rather than opening duplicates.

## Branch rules

`main` is protected by a repository ruleset:

- changes land through pull requests;
- the `build` check must pass;
- force-push and deletion are blocked.

Once two active maintainers are available, one approving review will also be required. Until
then, a single maintainer reviews and merges, and a second reviewer should be recruited before the
approval requirement is enabled. There is no permanent admin bypass.

## If CI fails

| Message | Fix |
| --- | --- |
| `missing chapter` | Create the file listed in `src/SUMMARY.md` or correct the path |
| `broken local link` | Fix the relative path; check percent-encoding |
| `root-relative link` | Replace `/assets/...` with a path relative to the page |
| `disallowed extension` | Remove the file or link to its canonical host |
| `file too large` | Compress, split, or link out |
| `example.org placeholder` | Replace it with a real, verified URL |

Run the validator locally for the same message with a line number. If a message is unclear, ask in
the pull request or open an issue with the exact output.

## Maintainer notes

- Merge with **squash**; delete the branch after merge.
- Do not merge content with unclear provenance, even if CI passes.
- After merge, confirm the deploy workflow and the live page.
- Keep `CODEOWNERS` current with real maintainers who have repository access.
- Use labels `good first issue`, `documentation`, `resource suggestion`, `new guide`,
  `broken link` and `workshop`.

## Questions

- Live contribution guide: https://fossmec.github.io/foss-mec-library/contribute/
- Issues: https://github.com/FossMec/foss-mec-library/issues
- FOSS MEC: https://foss.mec.ac.in · foss@mec.ac.in
