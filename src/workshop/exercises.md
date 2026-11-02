# Workshop Exercises

Seven non-conflicting tasks. Pick **one**, read the linked file, and open a pull request. Each
task lists the file to change and what counts as done.

> **Rule:** one exercise per pull request. Do not edit `src/SUMMARY.md` — none of these tasks need
> a new chapter.

## 1. Add a glossary term

**File:** [`src/glossary.md`](../glossary.md)

Add one term that a first-year would meet in this library, for example *repository*, *remote*,
*staging area*, *fork*, *upstream*, *merge conflict* or *pull request*. Keep the existing
alphabetical order and the existing format.

**Done when:**

- the term is defined in one or two plain-English sentences;
- the definition is original;
- the table still renders correctly;
- no other glossary rows are changed.

## 2. Fix an unclear sentence

**File:** [`src/guides/git/README.md`](../guides/git/)

Find one sentence that assumes too much or could be misread. Rewrite it without changing the
meaning of the commands.

**Done when:**

- the change is limited to a few lines;
- the technical meaning stays correct;
- the page still builds.

## 3. Add a free Git resource

**File:** [`src/resources/git.md`](../resources/git.md)

Add one official, free, currently maintained resource. It must be new to the page. Include its
canonical URL, a format label, a one-line description and the source/licence.

**Done when:**

- the link opens without a paywall or sign-up;
- the title matches the destination page;
- the description says why a student would use it;
- the entry appears in the correct table.

## 4. Improve the Linux guide

**File:** [`src/guides/linux/README.md`](../guides/linux/)

Add a short, tested example to an existing section — for example one more safe `find` pattern or a
note about a common error message. Do not create a new page.

**Done when:**

- the command is correct and safe;
- the explanation says what the output means;
- no unrelated section is reformatted.

## 5. Add a free Linux resource

**File:** [`src/resources/linux.md`](../resources/linux.md)

Add one authoritative, free resource that is not already listed. Official documentation, a free
book, or a recognised university course are good candidates.

**Done when:**

- the URL is the canonical source;
- access is genuinely free (no trial or institutional login);
- attribution and licence/access are stated.

## 6. Add a programming resource

**File:** [`src/resources/programming.md`](../resources/programming.md)

Add one beginner-friendly free resource for Python, the web or computer-science foundations. Avoid
link dumps and SEO listicles.

**Done when:**

- it teaches, rather than only linking onward;
- it is free to access;
- the description is specific enough to choose it over the alternatives.

## 7. Report a problem

**No file edit needed.**

Use the structured issue form:

- [Report a broken link](https://github.com/FossMec/foss-mec-library/issues/new?template=report-broken-link.yml)
- [Request a topic](https://github.com/FossMec/foss-mec-library/issues/new?template=request-topic.yml)
- [Suggest a resource](https://github.com/FossMec/foss-mec-library/issues/new?template=suggest-resource.yml)

**Done when:**

- the form is complete;
- the page/resource is identified precisely;
- the expected and actual behaviour are clear.

## Review your own work

Before submitting, check:

- [ ] I changed only the files needed for this task.
- [ ] I opened every link I added.
- [ ] I ran the commands I documented, or marked them clearly as examples.
- [ ] The text is mine, or the source and licence are stated.
- [ ] I did not upload copyrighted material or personal data.
- [ ] The pull request description follows the template.

A maintainer will review content, attribution and links. CI will validate the build. If a check
fails, read the message and push a fix to the same branch.
