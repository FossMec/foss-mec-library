# How to Contribute

The library is a static website built from Markdown in one GitHub repository. There is no upload
server, login system or admin panel. Contributions travel through GitHub, where a maintainer can
review them before they are published.

**You need a free [GitHub account](https://github.com/signup).** You do not need Rust, mdBook, Git
or a code editor — every path below can be completed in a browser.

## Choose a path

<div class="card-grid">
  <a class="card" href="add-notes.md">
    <span class="card__kicker">Path A</span>
    <span class="card__title">Add written notes</span>
    <span class="card__text">Write original Markdown: notes, a guide section or a glossary entry.</span>
    <span class="card__arrow">Add notes →</span>
  </a>
  <a class="card" href="upload-file.md">
    <span class="card__kicker">Path B</span>
    <span class="card__title">Upload a file</span>
    <span class="card__text">Add a PDF, slide deck or diagram you wrote or may share.</span>
    <span class="card__arrow">Upload a file →</span>
  </a>
  <a class="card" href="suggest-resource.md">
    <span class="card__kicker">Path C</span>
    <span class="card__title">Suggest a resource</span>
    <span class="card__text">Send a free official link through a structured issue form.</span>
    <span class="card__arrow">Suggest a resource →</span>
  </a>
  <a class="card" href="https://github.com/FossMec/foss-mec-library/issues/new?template=report-broken-link.yml">
    <span class="card__kicker">Path D</span>
    <span class="card__title">Report an issue</span>
    <span class="card__text">A broken link, an outdated page, a missing topic or a typo.</span>
    <span class="card__arrow">Report an issue →</span>
  </a>
</div>

## The shortest successful path

1. **Find the page** you want to improve. Use the **Suggest an edit** pencil in the top bar; it
   opens the exact source file on GitHub.
2. **Fork** the repository if you do not already have a fork.
3. **Create a branch** with a short name, for example `docs/fix-linux-permissions`.
4. **Make one focused change** in the browser editor or upload the file through GitHub.
5. **Open a pull request** against `FossMec/foss-mec-library:main`.
6. **Respond to review.** Push fixes to the same branch; the pull request updates.
7. After merge, **GitHub Actions deploys automatically**. No manual deploy step.

The [quickstart](../workshop/quickstart.md) walks through this in 15 minutes.

## What maintainers review

| Check | Why it matters |
| --- | --- |
| Accuracy | Wrong commands or claims are worse than no page |
| Permission | Material must be yours or explicitly shareable |
| Attribution | Author, source and licence must be clear |
| Links | Canonical, free and working |
| Scope | One focused change is easier to review and revert |
| Build | The validator and `mdbook build` must pass |

Review is a conversation, not a gate. If a maintainer asks a question, answer in the pull request
thread. If you disagree, explain why with a source.

## Content rules

- Write in your own words. Do not paste copyrighted text.
- Do not upload textbook scans, publisher slides, leaked question papers or personal student data.
- Do not add executables, archives, password-protected files or secrets.
- Keep files at or below **10 MiB**.
- Use lowercase `kebab-case` filenames with no spaces.
- Link local files with **relative** paths, never `/assets/...`.
- New original documentation is contributed under **CC BY 4.0**; code and scripts use MIT.
- Do not add unreviewed link dumps. Curate a few genuinely useful entries.

See [LICENSE-CONTENT.md](https://github.com/FossMec/foss-mec-library/blob/main/LICENSE-CONTENT.md)
and [CONTRIBUTING.md](https://github.com/FossMec/foss-mec-library/blob/main/CONTRIBUTING.md) in the
repository for the full policy.

## What this site cannot do

To set expectations honestly:

- it cannot accept a file directly from the website;
- it cannot create a GitHub account for you;
- it cannot publish a change before review;
- it cannot search inside a PDF or slide deck — only the Markdown listing is indexed;
- it cannot notify you outside GitHub (no email newsletter or account system).

If a workshop facilitator gives you a different route (for example, a shared issue thread), follow
their instructions for the session and still use the pull request template for the final change.

## Need help?

- Read the [workshop exercises](../workshop/exercises.md) for small, well-defined tasks.
- Open an issue with the exact step, command and error message.
- Ask a FOSS MEC maintainer at a workshop or through the community channels listed at
  [foss.mec.ac.in](https://foss.mec.ac.in).
