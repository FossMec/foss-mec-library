# FOSS MEC Library

**Open notes, study materials, learning resources and community guides from FOSS MEC.**

[![Documentation](https://github.com/FossMec/foss-mec-library/actions/workflows/docs.yml/badge.svg)](https://github.com/FossMec/foss-mec-library/actions/workflows/docs.yml)

The library is a static [mdBook](https://rust-lang.github.io/mdBook/) site published with GitHub
Pages. It is read-only by design: suggestions and files arrive through GitHub Issues and pull
requests, are reviewed by a maintainer, and are deployed automatically after merge.

- **Live site:** https://fossmec.github.io/foss-mec-library/
- **Repository:** https://github.com/FossMec/foss-mec-library
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Code of conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Content licence:** [CC BY 4.0](LICENSE-CONTENT.md); code and theme overrides are MIT.

## What is inside

| Section | Contents |
| --- | --- |
| Academic Materials | Semester pages with verified, permission-cleared notes and slides |
| Open Learning Resources | Curated free links for Git, Linux, programming and open source |
| Community Guides | Original guides on Git, GitHub collaboration and the Linux command line |
| Let's Git It | Workshop quickstart, exercises and a Git cheat sheet |
| Contribute | Browser-only guides for all four contribution paths |

There are no fake upload widgets, accounts, databases or server functions. GitHub is the
contribution system.

## Local preview

Requirements: [mdBook 0.5.4](https://github.com/rust-lang/mdBook/releases/tag/v0.5.4) and Python 3.

```bash
mdbook --version          # must print mdbook v0.5.4
python3 scripts/validate_content.py
mdbook serve --open
```

Or build the static site:

```bash
mdbook build              # output in book/
python3 -m http.server 8000 --directory book
```

`book/` is generated and gitignored. Never commit it.

## Content checks

CI runs the same two commands on every pull request:

```bash
python3 scripts/validate_content.py
mdbook build
```

The validator checks:

- every chapter referenced by `src/SUMMARY.md` exists;
- local Markdown and HTML links resolve (external links are not fetched);
- root-relative `/...` links are rejected, because the site is served from `/foss-mec-library/`;
- material extensions are on the allowlist;
- no file exceeds the 10 MiB policy;
- no published page contains an `example.org` placeholder.

`create-missing = false` makes a missing chapter a build failure instead of a silent empty page.

## Contribution workflow

1. Fork the repository.
2. Create a branch with a short, descriptive name.
3. Make one focused change (Markdown, a permitted file, or a verified link).
4. Open a pull request against `main` and complete the template.
5. CI runs `build`; a maintainer reviews accuracy, attribution and licence.
6. Squash-merge → GitHub Actions deploys to Pages automatically.

Browser-only instructions are in [CONTRIBUTING.md](CONTRIBUTING.md) and on the live
[Contribute](https://fossmec.github.io/foss-mec-library/contribute/) page.

## Deployment

`.github/workflows/docs.yml` builds on every pull request and deploys only from `main`:

- pull request → validate + `mdbook build` (read-only token, no deploy);
- push to `main` or manual dispatch → validate + build + upload Pages artifact + deploy.

Pages is configured in **GitHub Actions** mode. The only repository-local code executed by CI is
`scripts/validate_content.py` and mdBook itself.

## Repository layout

```text
src/                 Markdown chapters and static assets
theme/               Minimal mdBook overrides (CSS, header, head)
scripts/             Standard-library content validator
.github/             Workflow, issue forms, PR template, CODEOWNERS
book.toml            mdBook configuration and canonical site URL
```

## Licensing

- Original documentation contributed to this library is published under
  [Creative Commons Attribution 4.0](LICENSE-CONTENT.md), with credit to the contributor.
- Scripts, workflow files and theme overrides are [MIT](LICENSE).
- External resources remain under their own licences and are linked at the canonical source.
- Fonts are SIL Open Font License 1.1; see
  [`src/assets/fonts/FONT-LICENSES.md`](src/assets/fonts/FONT-LICENSES.md).

Do not upload copyrighted textbooks, publisher slides, leaked exam papers or personal student
data.
