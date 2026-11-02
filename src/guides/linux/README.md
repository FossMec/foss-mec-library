# Linux Command Line

> **Starter draft.** This page is workshop reference material, not a student submission. Check
> commands against your distribution's manual pages and improve the page with a pull request.

A short, practical introduction to the commands used in FOSS MEC workshops. It is not a complete
Linux course; it is enough to navigate a system, edit files, inspect what is running and ask the
right question.

## The shell

When you open a terminal, a **shell** reads commands and runs programs. Most distributions use
Bash or Zsh. The prompt usually shows your user, host and current directory:

```text
dijith@laptop:~/projects$
```

`$` means a normal user. `#` means root (administrator). Be careful with root commands.

## Where am I?

```bash
pwd                 # print working directory
ls                  # list files
ls -la              # long listing, including hidden files
cd Documents        # enter a directory
cd ..               # go up one level
cd ~                # go to your home directory
cd -                # go back to the previous directory
```

Paths beginning with `/` are absolute: `/home/dijith/notes`. Paths without a leading slash are
relative to the current directory.

Useful path shortcuts:

| Shortcut | Meaning |
| --- | --- |
| `.` | current directory |
| `..` | parent directory |
| `~` | your home directory |
| `-` | previous directory (for `cd`) |
| `/` | filesystem root |

## Create, copy, move, remove

```bash
touch notes.md              # create an empty file (or update its timestamp)
mkdir projects              # create a directory
mkdir -p projects/git/demo  # create nested directories
cp notes.md backup.md       # copy a file
cp -r projects projects-old # copy a directory recursively
mv notes.md drafts/         # move or rename
rm backup.md                # delete a file
rm -r old-folder            # delete a directory and its contents
```

`rm` does not use a trash bin. Check the path before pressing Enter. Never run
`rm -rf /` or paste a destructive command you do not understand.

## Read files

```bash
cat notes.md            # print the whole file
less notes.md           # scrollable viewer: q to quit, / to search
head -n 20 notes.md     # first 20 lines
tail -n 20 notes.md     # last 20 lines
tail -f server.log      # follow a growing log, Ctrl+C to stop
wc -l notes.md          # count lines
```

`less` is safer than `cat` for large files. Inside `less`: `Space` next page, `b` previous page,
`/pattern` search, `n` next match, `q` quit.

## Search

```bash
grep "TODO" notes.md              # lines containing TODO
grep -rn "TODO" src/              # recursive, with line numbers
grep -i "error" server.log        # case-insensitive
find . -name "*.md"               # files by name below the current directory
find . -type f -size +10M         # files larger than 10 MiB
```

Quote patterns that contain spaces or shell characters. Prefer `grep -F` when searching for
literal text rather than a regular expression.

## Pipes and redirection

A **pipe** sends the output of one command into another:

```bash
ls -la | less
grep -rn "TODO" src/ | wc -l
cat names.txt | sort | uniq
```

Redirection writes output to a file:

```bash
echo "hello" > hello.txt      # create or overwrite
echo "world" >> hello.txt     # append
command 2> errors.log         # redirect standard error
command > output.log 2>&1     # both stdout and stderr
```

`>` overwrites. Use `>>` when you mean to append.

## Permissions

```bash
ls -l script.sh
# -rwxr-xr-- 1 dijith users 120 Jan 1 10:00 script.sh
```

The first character is the file type (`-` file, `d` directory). The next nine characters are
permissions for **user**, **group** and **others**: read (`r`), write (`w`), execute (`x`).

```bash
chmod +x script.sh        # make a script executable
chmod 644 notes.md        # owner read/write; group and others read
chmod 755 script.sh       # owner read/write/execute; others read/execute
```

`sudo` runs one command with administrator privileges. Use it only when a task genuinely requires
it, and never pipe an unknown script straight into `sudo bash`.

## Processes

```bash
ps aux                 # all running processes
top                    # live process viewer, q to quit
htop                   # friendlier viewer if installed
pgrep -af python       # find processes matching a name
kill 1234              # politely stop process ID 1234
kill -9 1234           # force stop; last resort
```

`Ctrl+C` interrupts the foreground process. `Ctrl+Z` suspends it; `fg` resumes it, `bg` continues
it in the background.

## Packages

Package managers install, update and remove software. Use the one for your distribution:

| Distribution | Install | Update index | Upgrade |
| --- | --- | --- | --- |
| Debian / Ubuntu | `sudo apt install PACKAGE` | `sudo apt update` | `sudo apt upgrade` |
| Fedora | `sudo dnf install PACKAGE` | `sudo dnf check-update` | `sudo dnf upgrade` |
| Arch | `sudo pacman -S PACKAGE` | `sudo pacman -Sy` | `sudo pacman -Syu` |
| macOS (Homebrew) | `brew install PACKAGE` | `brew update` | `brew upgrade` |

Avoid mixing package managers on the same system.

## Manuals

```bash
man ls                 # manual page for ls
man 5 passwd           # section 5: file formats
apropos "copy files"   # search manual descriptions
ls --help              # short built-in help
```

Inside `man`: `Space` next page, `/pattern` search, `q` quit. If a command behaves unexpectedly,
read its manual before searching the web.

## SSH

Secure Shell connects to another machine:

```bash
ssh username@host.example.com
ssh -i ~/.ssh/id_ed25519 username@host
```

Generate a key pair if you do not have one:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

This creates a private key (never share it) and a public key ending in `.pub` (safe to add to
GitHub or a server).

## Environment and PATH

```bash
echo $HOME             # print a variable
echo $PATH             # directories searched for commands
export EDITOR=nano     # set a variable for this shell session
which git              # locate the executable
```

If a command is "not found", its directory is usually missing from `PATH`, or the package is not
installed.

## A first script

```bash
#!/usr/bin/env bash
set -euo pipefail

name="${1:-world}"
echo "Hello, ${name}!"
```

Save as `hello.sh`, then:

```bash
chmod +x hello.sh
./hello.sh
./hello.sh MEC
```

`set -euo pipefail` makes the script stop on errors, undefined variables and failed pipes. It is a
good default for anything you will run more than once.

## Practice

Work through [Bandit](https://overthewire.org/wargames/bandit/) or the
[Let's Git It exercises](../../workshop/exercises.md). For a structured course, see
[Linux and the Command Line](../../resources/linux.md).
