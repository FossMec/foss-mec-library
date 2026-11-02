# Git Cheat Sheet

A one-page reference for the workshop. Commands are safe unless marked otherwise.

## Setup

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

## Start a repository

```bash
git init                     # start tracking the current folder
git clone URL                # copy an existing repository
git status                   # what changed?
```

## Everyday loop

```bash
git status
git diff                     # unstaged changes
git add FILE                 # stage one file
git add .                    # stage everything below this folder
git diff --staged            # review what will be committed
git commit -m "docs: message"
git log --oneline
```

## Branches

```bash
git branch                   # list branches
git switch -c my-branch      # create and switch
git switch main              # switch back
git merge my-branch          # merge into the current branch
git branch -d my-branch      # delete a merged branch
```

## Remotes

```bash
git remote -v
git remote add upstream https://github.com/FossMec/foss-mec-library.git
git fetch upstream
git merge --ff-only upstream/main
git push -u origin my-branch
git pull
```

## Undo

```bash
git restore FILE                 # discard unstaged edits (destructive)
git restore --staged FILE        # unstage, keep edits
git commit --amend               # edit the last commit
git reset --soft HEAD~1          # undo last commit, keep changes staged
git revert COMMIT                # safe undo with a new commit
git reflog                       # find lost commits
```

## Fork → pull request

1. **Fork** the repository on GitHub.
2. Clone **your fork**: `git clone https://github.com/YOU/REPO.git`.
3. Add upstream: `git remote add upstream https://github.com/OWNER/REPO.git`.
4. Update `main`: `git switch main && git pull upstream main`.
5. Branch: `git switch -c docs/short-description`.
6. Edit, then `git add FILE` and `git commit -m "docs: ..."`.
7. Push: `git push -u origin docs/short-description`.
8. Open the link GitHub prints and create the pull request.
9. Push more commits to the same branch to answer review.

## Markdown used in this library

````markdown
# Page title

## Section

**bold**  *italic*  `inline code`

- list item
- [Git reference](https://git-scm.com/docs)

| Column | Column |
| --- | --- |
| cell | cell |

> A note or warning.

```bash
git status
```
````

## Format labels

Use the existing HTML labels inside tables:

```html
<span class="fmt fmt-notes">Notes</span>
<span class="fmt fmt-pdf">PDF</span>
<span class="fmt fmt-slides">Slides</span>
<span class="fmt fmt-docs">Docs</span>
<span class="fmt fmt-book">Book</span>
<span class="fmt fmt-video">Video</span>
<span class="fmt fmt-repo">Repository</span>
<span class="fmt fmt-course">Course</span>
```

## File naming

- lowercase `kebab-case`: `stack-basics.pdf`, not `Stack Basics.PDF`;
- materials under `src/assets/materials/<semester>/<subject>/`;
- maximum 10 MiB per file;
- allowed: `.md`, `.pdf`, `.pptx`, `.docx`, `.png`, `.jpg`, `.webp`, `.svg`;
- never commit secrets, personal data or unlicensed textbooks.

## Pull request checklist

- [ ] One focused change.
- [ ] Links opened and working.
- [ ] Commands tested.
- [ ] Source, author and licence stated.
- [ ] `src/SUMMARY.md` updated only if a new chapter was added.
- [ ] No leading `/` in local asset links.
- [ ] PR template completed.

## If a check fails

| Message | Likely fix |
| --- | --- |
| `missing chapter` | Add the file listed in `src/SUMMARY.md`, or correct the path |
| `broken local link` | Fix the relative path; decode `%20` spaces |
| `disallowed extension` | Use an allowed format or link to the original host |
| `file too large` | Compress it, or link to the authorised source instead |
| `create-missing` error | Create the missing `README.md` or remove the summary entry |

Ask in the pull request if the message is unclear. Do not close and reopen a new PR for the same
change.
