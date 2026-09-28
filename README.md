# Kalshi Paper Bots — Results

*Updated Mon Sep 28, 7:59 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 17 | 0 | — | — | — | 17 | Too early |
| **Rain** | 9 | 0 | — | — | — | 9 | Too early |
| **Longshot fade** | 600 | 298 | 90% | -$127.81 | -4.5% | 302 | Losing |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 253 | 36 | 97% | $9.06 | +2.7% |
| NFL | 211 | 197 | 89% | -$111.92 | -6.0% |
| MLB | 49 | 48 | 94% | -$4.39 | -1.0% |
| Weather | 37 | 2 | 100% | $1.02 | +5.4% |
| Crypto | 24 | 0 | — | — | — |
| Soccer | 22 | 13 | 77% | -$22.65 | -18.5% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| College football | 2 | 0 | — | — | — |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28 | LAX 80-81 | NO | 69¢ | 81% | Open | — |
| 2026-09-28 | NY 64-65 | YES | 16¢ | 26% | Open | — |
| 2026-09-28 | MIA 85-86 | YES | 5¢ | 14% | Open | — |
| 2026-09-28 | MIA >90 | NO | 58¢ | 69% | Open | — |
| 2026-09-28 | PHIL 69-70 | NO | 69¢ | 81% | Open | — |
| 2026-09-28 | PHIL <65 | YES | 10¢ | 20% | Open | — |
| 2026-09-28 | PHIL 67-68 | NO | 61¢ | 74% | Open | — |
| 2026-09-28 | LAX 76-77 | NO | 62¢ | 77% | Open | — |
| 2026-09-28 | LAX 78-79 | NO | 57¢ | 74% | Open | — |
| 2026-09-28 | LAX <76 | YES | 7¢ | 20% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29 | SATX | YES | 24¢ | 37% | Open | — |
| 2026-09-29 | HOU | YES | 25¢ | 40% | Open | — |
| 2026-09-29 | BOS | YES | 38¢ | 70% | Open | — |
| 2026-09-28 | SEA | NO | 82¢ | 96% | Open | — |
| 2026-09-28 | PHX | NO | 13¢ | 24% | Open | — |
| 2026-09-28 | OKC | YES | 9¢ | 21% | Open | — |
| 2026-09-28 | LV | YES | 49¢ | 62% | Open | — |
| 2026-09-28 | DEN | NO | 36¢ | 51% | Open | — |
| 2026-09-28 | DC | YES | 12¢ | 34% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
