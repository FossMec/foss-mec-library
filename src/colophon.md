# Colophon

## About

**FOSS MEC Library** is a knowledge library from
[FOSS MEC](https://foss.mec.ac.in), the Free and Open Source Software community at Government
Model Engineering College, Kochi. It will collect permission-cleared notes, curated open
resources and contributor-maintained guides in one permanent, searchable place.

## Provenance

The initial Git, GitHub and Linux guides and the contribution checklist were drafted as workshop
starting points. They are **not** student submissions and are not attributed to any student. They
are published so that contributors can correct and improve them. Academic sections remain empty
until a real, permission-cleared file is accepted through review.

External resources are linked at their canonical source and remain under their own licences.

## How it is built

- **Generator:** [mdBook](https://rust-lang.github.io/mdBook/) 0.5.4, pinned in CI.
- **Source:** Markdown under [`src/`](https://github.com/FossMec/foss-mec-library/tree/main/src).
- **Hosting:** GitHub Pages, deployed from GitHub Actions on every merge to `main`.
- **Search:** mdBook's built-in full-text search over rendered Markdown.
- **Backend:** none. There is no database, account system or upload service.

## Theme

The visual language follows the FOSS MEC website theme:

- navy `#0C2444` and paper `#F2F7FC`;
- accent yellow `#FFD022` and the logo gradient `#FDCE21` → `#F69D1D`;
- the official FOSS MEC logo;
- Martian Mono for display type, Uncut Sans for body text and DM Mono for code.

The theme menu includes **Light, Rust, Material, Nord, Everforest, Pine, Coal, Navy and Ayu**.
Navy is the default dark theme; the others are alternate palettes for reader preference. Only
`theme/foss-mec.css`, `theme/index.hbs`, `theme/header.hbs` and `theme/head.hbs` override mdBook's
defaults. Navigation, search, keyboard shortcuts and theme persistence remain mdBook's built-in
behaviour.

## Licensing

- **Original documentation and notes:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
  with attribution to the named contributor.
- **Code, scripts and theme overrides:** [MIT](https://opensource.org/license/mit).
- **Fonts:** SIL Open Font License 1.1; see
  [FONT-LICENSES.md](https://github.com/FossMec/foss-mec-library/blob/main/src/assets/fonts/FONT-LICENSES.md).
- **External resources:** remain under their own licences and are linked, not mirrored.

## Contributors

The curated list of people who have contributed to this library is on the
[Contributors](contributors.md) page. It is updated after a contribution is merged and contains no
placeholder names.

## Contact

- Website: [foss.mec.ac.in](https://foss.mec.ac.in)
- Email: [foss@mec.ac.in](mailto:foss@mec.ac.in)
- Repository: [github.com/FossMec/foss-mec-library](https://github.com/FossMec/foss-mec-library)

For corrections, use the **Suggest an edit** pencil on any page or open an issue. Do not email
attachments of copyrighted material.
