<div class="hero">
  <div class="hero__logo-card">
    <img src="assets/images/foss-mec-logo.svg" alt="FOSS MEC logo" width="60" height="48">
  </div>
  <p class="hero__eyebrow">FOSS MEC · Model Engineering College</p>
  <h1>Open notes. Open source. Open to everyone.</h1>
  <p class="hero__lede">A permanent knowledge library for MEC: permission-cleared study material,
  verified open resources, and starter guides maintained by FOSS MEC.</p>
  <div class="hero__actions">
    <a class="button button--primary" href="academics/">Browse notes</a>
    <a class="button button--ghost" href="resources/">Explore open resources</a>
    <a class="button button--ghost" href="guides/">Read guides</a>
    <a class="button button--ghost" href="https://github.com/FossMec/foss-mec-library/issues/new?template=suggest-resource.yml">Suggest a resource</a>
  </div>
</div>

<div class="contribute-band">
  <p><strong>Status:</strong> this library is new. The academic sections show an honest empty state
  until verified, permission-cleared material is accepted. The Git, Linux and workshop pages are
  starter drafts, not student submissions, and are open to correction.</p>
</div>

<p class="eyebrow">Start here</p>

<div class="card-grid">
  <a class="card" href="academics/">
    <span class="card__kicker">Study</span>
    <span class="card__title">Academic materials</span>
    <span class="card__text">Semester-wise notes, slides and question banks shared with permission.</span>
    <span class="card__arrow">Browse by semester →</span>
  </a>
  <a class="card" href="resources/">
    <span class="card__kicker">Reference</span>
    <span class="card__title">Open learning resources</span>
    <span class="card__text">Curated, free and official links for Git, Linux, programming and more.</span>
    <span class="card__arrow">Open the directory →</span>
  </a>
  <a class="card" href="guides/">
    <span class="card__kicker">Learn</span>
    <span class="card__title">Community guides</span>
    <span class="card__text">Starter guides on Git, GitHub and Linux, maintained in this repository.</span>
    <span class="card__arrow">Read the guides →</span>
  </a>
  <a class="card" href="workshop/">
    <span class="card__kicker">Workshop</span>
    <span class="card__title">Let's Git It</span>
    <span class="card__text">Workshop material, browser-only contribution exercises and a Git cheat sheet.</span>
    <span class="card__arrow">Start the workshop →</span>
  </a>
</div>

## What is in the library

The library is deliberately small and human-reviewed. Everything is plain Markdown in one
repository, so it stays searchable, portable and easy for the next team to maintain.

| Section | What you will find | Formats |
| --- | --- | --- |
| [Academic Materials](academics/) | Original notes and study material, organised by semester and subject | <span class="fmt fmt-notes">Notes</span> <span class="fmt fmt-pdf">PDF</span> <span class="fmt fmt-slides">Slides</span> |
| [Open Learning Resources](resources/) | Links to official documentation, open books, courses and repositories | <span class="fmt fmt-docs">Docs</span> <span class="fmt fmt-book">Book</span> <span class="fmt fmt-course">Course</span> <span class="fmt fmt-video">Video</span> |
| [Community Guides](guides/) | Long-form tutorials on Git, GitHub and the Linux command line | <span class="fmt fmt-notes">Notes</span> |
| [Let's Git It](workshop/) | Workshop exercises and a printable Git cheat sheet | <span class="fmt fmt-notes">Notes</span> |

> **Note — search covers the words on the page, not inside PDFs.**
> mdBook search indexes rendered Markdown. A PDF or slide deck is discoverable only through the
> listing page that describes it, so every material listing includes a title, subject, keywords
> and a short description.

## How contributions work

This is a read-only website backed by GitHub. There is no upload form, account system or
database — suggestions and files travel through GitHub Issues and pull requests, where a
maintainer can review them before publication.

<div class="card-grid">
  <a class="card" href="contribute/add-notes.md">
    <span class="card__kicker">Path A</span>
    <span class="card__title">Write notes in Markdown</span>
    <span class="card__text">Best for original explanations, guides and glossary entries.</span>
    <span class="card__arrow">Add written notes →</span>
  </a>
  <a class="card" href="contribute/upload-file.md">
    <span class="card__kicker">Path B</span>
    <span class="card__title">Upload a PDF or slides</span>
    <span class="card__text">For material you wrote or are explicitly allowed to share.</span>
    <span class="card__arrow">Upload a file →</span>
  </a>
  <a class="card" href="contribute/suggest-resource.md">
    <span class="card__kicker">Path C</span>
    <span class="card__title">Suggest an external resource</span>
    <span class="card__text">Send a free, official link for a maintainer to review and add.</span>
    <span class="card__arrow">Suggest a resource →</span>
  </a>
  <a class="card" href="https://github.com/FossMec/foss-mec-library/issues/new?template=report-broken-link.yml">
    <span class="card__kicker">Path D</span>
    <span class="card__title">Report a broken link</span>
    <span class="card__text">Tell us about a dead, outdated or wrongly described resource.</span>
    <span class="card__arrow">Report an issue →</span>
  </a>
</div>

<div class="contribute-band">
  <p><strong>Everything is done in a browser.</strong> You need a free GitHub account, but you do
  not need to install Rust, mdBook, Git or an editor to contribute.</p>
  <p><a href="contribute/">Read the full contribution guide →</a></p>
</div>

## Built for the next team

- **One book, not many sites.** New subjects and guides become chapters, not new deployments.
- **No runtime dependencies.** The site is static HTML, CSS and JavaScript generated by mdBook.
- **Reviewed before publishing.** Every change lands through a pull request and an automatic build.
- **Licensed content only.** Contributors confirm they wrote the material or have permission to share it.

The source lives at [github.com/FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library).
Every page has a **Suggest an edit** pencil in the top bar that opens its exact Markdown file.
