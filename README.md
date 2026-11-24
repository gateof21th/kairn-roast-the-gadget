# One-Line Roast: The Gadget You Use Every Day

[![make.fun bounty](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/gateof21th/kairn-roast-the-gadget/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/gateof21th/kairn-roast-the-gadget/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

An entry for the make.fun bounty [One-Line Roast: The Gadget You Use Every Day](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) — one original line, at most 200 characters, roasting a gadget used every day.

## The roast

> My robot vacuum has obstacle avoidance, so it politely steers around the exact pile of crumbs it exists to clean, then wedges under the sofa and texts me a map of where it gave up.

## How it runs

`main.py` (Python 3, standard library only) reads the line from `line.txt`, checks it against the gate (UTF-8, 1–200 characters, not only whitespace), and writes it verbatim to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that environment variable is set. The write is atomic (temp file + rename) and verified by a round-trip byte comparison. The program is deterministic: repeated runs produce byte-identical output.

## Referral

Find this bounty and more on [make.fun](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) — referral code: `02v5hyzp`.

## License

MIT — see [LICENSE](LICENSE).
