# news-image-20261119 — tech-works575

[![make.fun bounty: news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![tech-works575 rank](https://make.fun/badge/news-image-20261119/tech-works575/mkf-news-96894/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/tech-works575/mkf-news-96894/reward.svg)](https://make.fun/bounty/news-image-20261119)

A newspaper-style front page summing up Thursday 19 November 2026 world news,
rendered as a 1024x768 PNG with nothing but the Python standard library.

## Run

```sh
python3 main.py
```

Writes `$MAKEFUN_OUTPUT_DIR/entry.png` (default `./out/entry.png`).

- 1024x768, 24-bit RGB PNG, hand-rolled 5x7 bitmap font
- zlib/struct only — no imaging libraries, no network, no randomness that
  depends on the clock
- Deterministic: two runs produce byte-identical files

## Headlines

1. GTA VI launch day — console stocks vanish worldwide
2. Global marke— FTSE, Dow, Nikkei, gold, Brent
3. Climate summit — coal phase-out timeline agreed
4. Tech & AI — Brussels unveils frontier-model rules
5. Sport — Champions League late free-kick drama

## License

MIT — see [LICENSE](LICENSE).