# Collaborating on GitHub

Git tracks history on your machine. GitHub adds a shared home for that history, issues for
discussion, and pull requests for review. This guide follows the fork-and-pull-request workflow
used by the FOSS MEC Library.

## The model

You usually do **not** have write access to the organisation repository. Instead:

```text
FossMec/foss-mec-library          (upstream, read-only for you)
        │ fork
        ▼
your-username/foss-mec-library    (your copy, writable)
        │ clone / branch / commit / push
        ▼
pull request → review → merge → deploy
```

A **fork** is a full copy of the repository under your account. A **pull request** (PR) asks the
maintainers to merge one of your branches into theirs.

## Before you start

- Create a free GitHub account.
- Set your name and email in Git (see [Git Essentials](./#configure-your-identity-once)).
- Decide which contribution path you are following:
  [written notes](../../contribute/add-notes.md),
  [a file upload](../../contribute/upload-file.md), or
  [an external resource suggestion](../../contribute/suggest-resource.md).

## Option A — entirely in the browser

This is the workshop path and needs no local tools.

1. Open [FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library).
2. Click **Fork** (top right) and choose your account.
3. In your fork, open the Markdown page you want to change, for example
   `src/guides/git/collaboration.md`.
4. Click the pencil (**Edit this file**) or **Add file → Create new file**.
5. Make one small, meaningful change.
6. Scroll to **Commit changes**. Choose **Create a new branch for this commit**, give it a short
   name such as `docs/fix-clone-command`, and commit.
7. GitHub offers **Compare & pull request**. Open the PR against `FossMec/foss-mec-library`,
   branch `main`.
8. Fill in the pull request template and submit.

If you do not see the **Fork** button, check that you are signed in. If your account is new,
GitHub may ask you to verify your email before enabling forks.

## Option B — with Git on your machine

### Fork and clone

Fork on GitHub, then clone **your fork**, not the organisation repository:

```bash
git clone https://github.com/YOUR-USERNAME/foss-mec-library.git
cd foss-mec-library
git remote add upstream https://github.com/FossMec/foss-mec-library.git
git remote -v
```

You should see:

```text
origin    https://github.com/YOUR-USERNAME/foss-mec-library.git
upstream  https://github.com/FossMec/foss-mec-library.git
```

`origin` is your fork. `upstream` is the canonical project.

### Create a branch

```bash
git switch main
git pull upstream main
git switch -c docs/add-git-tip
```

Use a branch name that describes the change. Avoid working directly on `main` in your fork.

### Make and preview the change

Edit one or two files. If you changed Markdown, you can preview the book locally:

```bash
mdbook serve --open
```

If mdBook is not installed, skip the preview — CI will build the book for you. Keep the change
focused; unrelated edits make review harder.

### Stage, commit and push

```bash
git status
git diff
git add src/guides/git/README.md
git commit -m "docs: explain how to unstage a file"
git push -u origin docs/add-git-tip
```

The push output includes a link like:

```text
https://github.com/YOUR-USERNAME/foss-mec-library/pull/new/docs/add-git-tip
```

Open it, or go to the upstream repository and click **Compare & pull request**.

### Open the pull request

Write a title in the same style as your commit. In the description:

- say what changed and why;
- name the target subject or page;
- state the source, author and licence for any uploaded file;
- confirm you have permission to share the material;
- list what you checked (for example, "opened the page in `mdbook serve`").

A maintainer reviews the content, the licence and the links. CI builds the book on every PR.
When both are green, the PR is squash-merged and the site deploys automatically.

## Keep your fork up to date

GitHub's web interface has **Sync fork → Update branch** on your fork's main page. From the
command line:

```bash
git switch main
git fetch upstream
git merge --ff-only upstream/main
git push origin main
```

If you use the GitHub CLI:

```bash
gh repo sync YOUR-USERNAME/foss-mec-library --source FossMec/foss-mec-library
```

Start each new contribution from an updated `main` to reduce conflicts.

## Review and merge

A review may ask for changes. Push more commits to the same branch; the PR updates
automatically.

```bash
git add .
git commit -m "docs: apply review feedback"
git push
```

Do not open a second PR for the same change. Do not force-push after review unless a maintainer
asks you to, because it hides the review history.

## Resolve a conflict

If `main` changed the same lines while your PR was open, GitHub reports a conflict. On your
branch:

```bash
git fetch upstream
git merge upstream/main
```

Git marks the conflicting lines. Keep the correct combination, remove the `<<<<<<<`, `=======`
and `>>>>>>>` markers, then:

```bash
git add path/to/conflicted-file
git commit
git push
```

The PR becomes mergeable again.

## What makes a good contribution

- **Small:** one typo fix, one new resource, one guide section.
- **Accurate:** commands tested, links opened, syllabus claims verified.
- **Attributed:** source and licence stated for anything you did not write.
- **Kind:** review comments are about the change, not the person.

## Glossary

| Term | Meaning |
| --- | --- |
| Fork | Your own copy of someone else's repository |
| Clone | A local copy of a repository |
| Branch | A named line of commits |
| Commit | A recorded snapshot with a message |
| Push | Upload commits to a remote |
| Pull | Fetch and integrate remote commits |
| Pull request | A request to merge a branch into another |
| Merge | Combine histories, usually after review |
| Upstream | The canonical repository you forked from |

Still stuck? Open an issue and describe the step, the command and the exact error message.
