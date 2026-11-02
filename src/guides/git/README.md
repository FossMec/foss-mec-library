# Git Essentials

Git records the history of a project as a series of snapshots. You decide when to take a
snapshot, what goes into it, and which line of history it belongs to. This guide covers the
commands you need for the [Let's Git It workshop](../../workshop/) and for everyday
coursework.

## Check that Git is installed

```bash
git --version
```

If the command is missing, install Git from [git-scm.com/downloads](https://git-scm.com/downloads).
On Debian or Ubuntu:

```bash
sudo apt install git
```

## Configure your identity once

Git writes an author into every commit. Use the same email as your GitHub account.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Check the result:

```bash
git config --list --show-origin
```

Use `--global` for your laptop. Omit it inside a repository when a project needs a different
identity.

## Create a repository

A repository is a folder whose history Git tracks.

```bash
mkdir hello-git
cd hello-git
git init
```

`git init` creates a hidden `.git/` directory. Do not delete or edit it by hand.

Check what Git sees:

```bash
git status
```

## The three places a change can be

Understanding these three places prevents most beginner confusion:

```text
working directory  →  staging area  →  repository
   (your files)        (git add)        (git commit)
```

- The **working directory** is the folder you edit.
- The **staging area** (also called the index) is the draft of your next commit.
- The **repository** is the recorded history inside `.git/`.

## Make your first commit

Create a file, stage it, then commit:

```bash
echo "# Hello Git" > README.md
git add README.md
git status
git commit -m "docs: add initial readme"
```

`git add .` stages every change below the current directory. That is convenient, but check
`git status` first so you do not commit generated files or secrets.

A commit message should say **what changed and why**. The project uses short imperative
messages, for example:

```text
docs: fix broken Linux permissions example
feat: add semester 3 data structures page
fix: correct the workshop fork instructions
```

## Inspect what happened

```bash
git status              # what is modified or staged
git diff                # unstaged changes
git diff --staged       # staged changes
git log --oneline       # compact history
git log --oneline --graph --all
git show HEAD           # the latest commit
```

`HEAD` means "the commit you currently have checked out".

## Ignore files you should not commit

Create a `.gitignore` in the repository root:

```gitignore
book/
target/
node_modules/
.env
*.log
```

Rules apply to untracked files. If a file is already tracked, remove it from the index first:

```bash
git rm --cached .env
```

Never commit passwords, API keys, private student data or generated build output.

## Branches

A branch is a movable name for a line of commits. `main` is the default branch in most projects.

```bash
git branch                  # list local branches
git switch -c fix-typo      # create and switch
git switch main             # switch back
git branch -d fix-typo      # delete a merged branch
```

Make a branch for every independent change. This keeps `main` clean and makes pull requests easy
to review.

## Merge a branch

```bash
git switch main
git merge fix-typo
```

If both branches changed the same lines, Git stops and marks a conflict:

```text
<<<<<<< HEAD
current version
=======
incoming version
>>>>>>> fix-typo
```

Edit the file to keep the correct result, delete the markers, then:

```bash
git add path/to/file
git commit
```

Do not blindly choose one side. Read both versions and test the result.

## Remotes

A remote is a copy of the repository hosted somewhere else, usually GitHub.

```bash
git remote -v
git remote add origin git@github.com:USERNAME/REPO.git
git push -u origin main
```

`-u` links your local `main` to `origin/main`, so later you can run plain `git push` and
`git pull`.

Clone an existing repository with:

```bash
git clone https://github.com/FossMec/foss-mec-library.git
```

## Undo without panic

| Situation | Command |
| --- | --- |
| Discard unstaged edits to one file | `git restore path/to/file` |
| Unstage a file but keep the edits | `git restore --staged path/to/file` |
| Amend the last commit message or contents | `git commit --amend` |
| Undo the last commit, keep changes staged | `git reset --soft HEAD~1` |
| Create a new commit that reverses an old one | `git revert <commit>` |
| Find a lost commit after a bad reset | `git reflog` |

`git reset --hard` throws away uncommitted work. Use it only when you are certain.

## Read the status output

When `git status` says:

```text
Changes not staged for commit:
  modified:   README.md
```

the file is changed but not staged. Run `git add README.md`, then commit.

When it says:

```text
Your branch is ahead of 'origin/main' by 1 commit.
```

you have a local commit that has not been pushed. Run `git push`.

## Next step

Continue with [Collaborating on GitHub](collaboration.md) to turn a local branch into a pull
request. For a printable reminder, open the [Git cheat sheet](../../workshop/cheatsheet.md).
