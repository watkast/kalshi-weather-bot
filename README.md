# Kalshi Paper Bots — Results

*Updated Wed Sep 30, 12:25 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 61 | 28 | 43% | -$20.18 | -14.4% | 33 | Losing |
| **Rain** | 21 | 12 | 25% | -$5.27 | -14.9% | 9 | Too early |
| **Longshot fade** | 953 | 681 | 92% | -$181.23 | -2.8% | 272 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 287 | 93% | -$36.82 | -1.4% |
| NFL | 211 | 209 | 89% | -$114.59 | -5.8% |
| Weather | 89 | 72 | 96% | $7.49 | +1.1% |
| MLB | 68 | 68 | 96% | $7.20 | +1.1% |
| College football | 68 | 0 | — | — | — |
| Crypto | 39 | 20 | 95% | $1.32 | +0.7% |
| Soccer | 27 | 22 | 73% | -$47.64 | -22.9% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| NHL | 1 | 1 | 100% | $0.74 | +8.0% |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-30 | DEN <59 | YES | 5¢ | 20% | Open | — |
| 2026-09-30 | DEN >66 | NO | 87¢ | 97% | Open | — |
| 2026-09-30 | PHIL 76-77 | YES | 11¢ | 23% | Open | — |
| 2026-09-30 | LAX 78-79 | NO | 74¢ | 86% | Open | — |
| 2026-09-30 | DEN 59-60 | YES | 10¢ | 23% | Open | — |
| 2026-09-30 | DEN 63-64 | NO | 71¢ | 81% | Open | — |
| 2026-09-30 | DEN 65-66 | NO | 82¢ | 91% | Open | — |
| 2026-09-30 | AUS 93-94 | YES | 12¢ | 23% | Open | — |
| 2026-09-30 | AUS 97-98 | NO | 61¢ | 81% | Open | — |
| 2026-09-30 | AUS <93 | YES | 10¢ | 20% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01 | MIA | NO | 7¢ | 18% | Open | — |
| 2026-10-01 | NOLA | YES | 57¢ | 74% | Open | — |
| 2026-10-01 | DEN | NO | 64¢ | 82% | Open | — |
| 2026-09-30 | MIA | NO | 12¢ | 28% | Open | — |
| 2026-09-30 | DAL | NO | 34¢ | 55% | Open | — |
| 2026-09-30 | CLL | YES | 35¢ | 48% | Open | — |
| 2026-09-30 | OKC | YES | 85¢ | 97% | Open | — |
| 2026-09-29 | LV | YES | 38¢ | 56% | Open | — |
| 2026-09-29 | DEN | YES | 44¢ | 65% | Open | — |
| 2026-09-29 | OKC | YES | 17¢ | 41% | NO | -$1.80 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
