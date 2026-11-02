# Quickstart — your first pull request

This walkthrough takes about 15 minutes and uses only a browser. You will fork the library, make
one small documentation change and open a pull request.

> **What is a pull request?** A request to merge your branch into the project's `main` branch.
> A maintainer reviews it, automated checks build the book, and then it is merged.

## 1. Sign in and fork

1. Open [github.com/FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library).
2. Sign in. If you do not have an account, create one and verify your email.
3. Click **Fork** at the top right.
4. Choose your own account as the destination and click **Create fork**.

You now have `https://github.com/YOUR-USERNAME/foss-mec-library`.

If the **Fork** button is missing, you are probably not signed in, or your email is unverified.

## 2. Pick one small change

Choose **one** of these. They touch different files, which keeps the workshop free of merge
conflicts.

| Change | File to edit |
| --- | --- |
| Add a term to the glossary | `src/glossary.md` |
| Improve one sentence in the Git guide | `src/guides/git/README.md` |
| Add a free official Git resource | `src/resources/git.md` |
| Improve the Linux guide | `src/guides/linux/README.md` |
| Add a free Linux resource | `src/resources/linux.md` |

Read the page first. The change must be true, useful and in your own words.

## 3. Edit in the browser

1. In **your fork**, open the file from the table above.
2. Click the pencil icon (**Edit this file**).
3. Make the change. Keep Markdown formatting intact:

   ```markdown
   | [Git reference manual](https://git-scm.com/docs) | <span class="fmt fmt-docs">Docs</span> | Official command reference. | Git project — free |
   ```

4. Scroll down to **Commit changes**.
5. In the message box, write what changed, for example:

   ```text
   docs: add glossary entry for upstream
   ```

6. Choose **Create a new branch for this commit and start a pull request**.
7. Name the branch `docs/add-upstream-term` and click **Propose changes**.

## 4. Open the pull request

GitHub opens the compare page. Check:

- **base repository:** `FossMec/foss-mec-library`
- **base branch:** `main`
- **head repository:** `YOUR-USERNAME/foss-mec-library`
- **compare branch:** the branch you just created

Write a title beginning with `docs:` and complete the pull request template:

- **Summary:** one or two sentences.
- **Content type:** tick `Documentation fix` or `Resource link`.
- **Permission:** tick the confirmation that the text is yours or appropriately licensed.
- **Checklist:** tick what you actually checked.

Click **Create pull request**.

## 5. Watch the checks

Two things happen:

1. **`build`** runs the content validator and builds the book. It usually takes a minute.
2. A maintainer reviews the change.

A red check is normal while you are learning. Open the failed step and read the message. A broken
local link, a disallowed file or an unlisted chapter are the usual causes. Fix the file in your
branch and commit again; the same pull request updates.

**Deployment does not run on pull requests.** Only merged changes to `main` are published.

## 6. After review

- If changes are requested, edit the same file again and commit to the same branch.
- When approved and green, a maintainer squash-merges the pull request.
- GitHub Actions rebuilds and deploys the site automatically.
- Your change appears at [fossmec.github.io/foss-mec-library](https://fossmec.github.io/foss-mec-library/)
  within a few minutes.

## If something goes wrong

| Problem | Fix |
| --- | --- |
| No **Fork** button | Sign in and verify your email |
| Cannot edit the file | Make sure you are in **your fork**, not `FossMec/foss-mec-library` |
| No **Compare & pull request** banner | Open the **Pull requests** tab → **New pull request** → **compare across forks** |
| Check failed on a link | Open the log, find the file and line, fix the path |
| Merge conflict | Ask a maintainer; do not force anything |
| Wrong base repository | Edit the pull request and change the base to `FossMec/foss-mec-library` |

## Practice complete

You have used the same workflow as every contributor to this library. Next, try one of the
[workshop exercises](exercises.md) or read
[Collaborating on GitHub](../guides/git/collaboration.md) for the command-line version.
