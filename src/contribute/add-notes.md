# Add Written Notes

Use this path for original Markdown: a new explanation, a worked example, a glossary entry, or a
longer guide. It is the easiest contribution because GitHub can render and review the change in
the browser.

## Decide what kind of page you are writing

| Your content | Where it goes | Needs `SUMMARY.md`? |
| --- | --- | --- |
| A correction or clarification | The existing page | No |
| A new section inside an existing guide | The existing guide chapter | No |
| A new resource link | The relevant `src/resources/*.md` page | No |
| A new standalone chapter or guide | A new `.md` file under `src/guides/` or `src/academics/` | **Yes** |
| A glossary term | `src/glossary.md` | No |

Most first contributions should **not** touch `src/SUMMARY.md`. That keeps pull requests small and
avoids conflicts.

## Step 1 — Fork and branch

Fork [FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library) to your account, then
create a branch in your fork:

```text
docs/add-terminal-shortcuts
```

In the browser: open your fork, click the branch selector, type the new name and choose
**Create branch**.

With Git:

```bash
git clone https://github.com/YOUR-USERNAME/foss-mec-library.git
cd foss-mec-library
git remote add upstream https://github.com/FossMec/foss-mec-library.git
git switch -c docs/add-terminal-shortcuts
```

## Step 2 — Write the page

Create or edit a Markdown file under `src/`. Follow the existing style:

- exactly one `#` heading at the top;
- `##` for main sections and `###` below that;
- short paragraphs, lists and tables;
- fenced code blocks with a language tag;
- relative links to other chapters and assets;
- no HTML layout unless the existing page already uses it (the home page and resource labels do).

A minimal chapter:

````markdown
# Understanding the Git staging area

The staging area is the draft of your next commit.

## Why it exists

It lets you choose which changes belong in a snapshot.

## Try it

```bash
git add README.md
git status
git commit -m "docs: explain staging"
```
````

Do not copy the example line `git add` blindly; run commands before documenting them.

## Step 3 — Add it to `SUMMARY.md` (only for a new chapter)

`src/SUMMARY.md` controls the sidebar. Add one line in the correct section:

```markdown
- [Understanding the staging area](guides/git/staging.md)
```

The path is relative to `src/`. `create-missing = false` means a summary entry without a file
**fails the build**, which is intentional.

If you are editing an existing page, skip this step.

## Step 4 — Link images and files

Put images in `src/assets/images/` (or a subject folder under `src/assets/materials/`). Link them
relative to the Markdown file:

```markdown
![Stack diagram](../../assets/images/stack-diagram.png)
```

From `src/guides/git/staging.md`, `../../assets/images/...` resolves correctly. A leading
`/assets/...` breaks on GitHub Pages because the site lives under `/foss-mec-library/`.

## Step 5 — State authorship and licence

By opening the pull request you agree to publish your original text under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with attribution to you as the author.
Say in the PR description:

- your name (or the name you want credited);
- whether the text is entirely yours;
- any sources you paraphrased;
- if you adapted existing material, its licence and a link.

Do not paste large extracts from textbooks, paid courses or other websites.

## Step 6 — Check the Markdown

You do not need mdBook to submit a PR: CI builds the book for you. If you have mdBook installed
locally, preview with:

```bash
mdbook serve --open
```

Then run the same content check as CI:

```bash
python3 scripts/validate_content.py
```

## Step 7 — Open the pull request

Commit with a clear message:

```bash
git add src/guides/git/staging.md src/SUMMARY.md
git commit -m "docs: add staging area guide"
git push -u origin docs/add-terminal-shortcuts
```

Open the pull request against `main` and complete the template. In the description, say what the
reader will learn and list the commands you tested.

## Review checklist

- [ ] One topic, one focused change.
- [ ] Original wording; sources paraphrased, not copied.
- [ ] One `#` heading; sensible nested headings.
- [ ] Local links are relative and resolve.
- [ ] New chapter added to `SUMMARY.md`; existing page left out of it.
- [ ] Author, source and licence stated in the PR.
- [ ] No personal data, secrets or copyrighted uploads.
- [ ] CI `build` check passes.

A maintainer may edit wording for clarity or ask for a split if the PR covers too much. That is
normal review, not rejection.
