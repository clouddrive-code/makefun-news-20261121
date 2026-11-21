# makefun-news-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/clouddrive-code/makefun-news-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/clouddrive-code/makefun-news-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

The World Today — 21 November 2026 in one image. Sum up 21 November's world news in one image. $100 pot, 50 paid places (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20). Deadline: 2026-11-23T00:00:00Z (2026-11-23 08:00 Asia/Shanghai).

`news.png` is a front-page poster for Saturday 21 November 2026:

- Lead: Russian Kh-101 missiles and a drone crash in Poland — Tusk calls it an intentional provocation, NATO's Rutte a grave violation; no injuries reported.
- Ukraine under fire: 400+ drones, 110+ missiles overnight, 8+ killed.
- COP31 in Antalya stalls / into overtime; draft drops fossil fuels.
- Wall Street AI rout: Nasdaq erases 2026 gains, S&P 500 into correction.
- Denmark expels Russia's envoy; Saudi forces intercept a Houthi missile, debris in Riyadh.

Stories verified from AP / Reuters reporting on 21 Nov 2026.

## How it works

`main.py` (stdlib only, no network, no clock) copies the bundled `news.png` to `/output/entry.png`. The image is 1024x1024, ~117 KB, well under the 1 MiB limit. Two runs write identical bytes (sha256 547f8b1dd251727ca28f62d8f0af7d2dae9c18438697ea2dfd8012b2175a939c), so the deterministic rule is satisfied.

`news.png` was generated locally by `generate.py` (Pillow, fixed text / colours / layout).

## Run it

```sh
python3 main.py
```

## Licence

MIT — see LICENSE.

---

<sub>Entered on [make.fun](https://make.fun/?ref=d11xy5cq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
