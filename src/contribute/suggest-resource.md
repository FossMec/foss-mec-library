# Suggest a Resource

The fastest contribution: send a free, authoritative link through a structured GitHub issue form.
No fork, no branch, no Markdown required. A maintainer reviews the suggestion and adds it to the
right directory page.

## Submit a suggestion

<div class="card-grid">
  <a class="card" href="https://github.com/FossMec/foss-mec-library/issues/new?template=suggest-resource.yml">
    <span class="card__kicker">Issue form</span>
    <span class="card__title">Suggest a resource</span>
    <span class="card__text">Title, canonical URL, topic, description, attribution and licence.</span>
    <span class="card__arrow">Open the form →</span>
  </a>
  <a class="card" href="https://github.com/FossMec/foss-mec-library/issues/new?template=report-broken-link.yml">
    <span class="card__kicker">Issue form</span>
    <span class="card__title">Report a broken link</span>
    <span class="card__text">Tell us the page, the link and what happens when you open it.</span>
    <span class="card__arrow">Report a link →</span>
  </a>
</div>

You need a GitHub account to submit the form. The issue is public and visible to everyone.

## What the form asks

| Field | What to write |
| --- | --- |
| Resource title | The title shown on the destination page |
| Canonical URL | The original author's or project's URL, not a mirror or shortener |
| Topic / course | Git, Linux, programming, open source, or a specific semester subject |
| Description | One or two sentences: what it teaches and who it is for |
| Source / author | Organisation or person who maintains it |
| Access and licence | "Free, CC BY 4.0", "Free, official docs", "Free to audit", etc. |
| Why it belongs | What gap it fills compared with entries already listed |

## What gets accepted

- **Free to access** without a paywall, trial, invite or misleading "free" login wall.
- **Authoritative:** the project's own documentation, a recognised institution, or the author's
  site.
- **Current:** maintained recently, not an abandoned course from a decade ago.
- **Specific:** teaches something, rather than being a list of more links.
- **Safe:** no pirated textbooks, cracked software, malware, affiliate links or exam leaks.

Link to the original host. Do not ask us to mirror a file unless you own it or it is openly
licensed for redistribution.

## What happens next

1. A maintainer reads the issue and checks the link, author and licence.
2. If it fits, they either add the entry themselves or ask you to open a pull request.
3. The entry is added to the relevant page, for example `src/resources/git.md`.
4. CI builds the change, a maintainer merges it, and the site deploys automatically.
5. The issue is closed with a link to the published page.

Typical turnaround is a few days around workshops, longer during exams. If an issue gets no
response after a week, leave a polite comment — do not open duplicates.

## Prefer to make the edit yourself?

This is the workshop's direct-PR path and teaches the GitHub flow:

1. Fork the repository.
2. Open the relevant page, for example `src/resources/linux.md`.
3. Click the pencil and add one row to the correct table:

   ```markdown
   | [Resource title](https://canonical.example/path) | <span class="fmt fmt-book">Book</span> | One clear sentence about what it teaches. | Author — free, CC BY 4.0 |
   ```

4. Commit to a branch such as `resources/add-linux-book`.
5. Open a pull request with the template completed.

Use the same acceptance rules as above. Do not reorder or reformat unrelated rows; a focused diff
is easier to review.

## Format labels

Use the label that matches the destination:

| Label | Use for |
| --- | --- |
| `<span class="fmt fmt-docs">Docs</span>` | Official documentation or reference |
| `<span class="fmt fmt-book">Book</span>` | A free book or long-form text |
| `<span class="fmt fmt-course">Course</span>` | A structured course or curriculum |
| `<span class="fmt fmt-video">Video</span>` | A video series or recorded lecture |
| `<span class="fmt fmt-repo">Repository</span>` | A code repository or example project |
| `<span class="fmt fmt-pdf">PDF</span>` | A downloadable PDF |
| `<span class="fmt fmt-notes">Notes</span>` | Original written notes |
| `<span class="fmt fmt-slides">Slides</span>` | A slide deck |

## Report a broken link

Use the [broken link form](https://github.com/FossMec/foss-mec-library/issues/new?template=report-broken-link.yml)
and include:

- the library page where you found the link;
- the URL that fails;
- what you expected and what happened (404, redirect to an unrelated page, paywall, wrong content);
- the date you checked, if the site is intermittent.

Do not paste the entire page or personal data. A maintainer will fix or remove the entry through a
pull request. External links are checked by humans during review; the build deliberately does not
fail because a remote server is temporarily down.
