# Kalshi Paper Bots — Results

*Updated Mon Sep 28, 1:50 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 35 | 0 | — | — | — | 35 | Too early |
| **Rain** | 12 | 0 | — | — | — | 12 | Too early |
| **Longshot fade** | 713 | 362 | 90% | -$151.25 | -4.4% | 351 | Losing |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 316 | 90 | 93% | -$9.25 | -1.1% |
| NFL | 211 | 197 | 89% | -$111.92 | -6.0% |
| Weather | 56 | 9 | 100% | $4.50 | +5.3% |
| MLB | 50 | 48 | 94% | -$4.39 | -1.0% |
| Crypto | 28 | 0 | — | — | — |
| Soccer | 25 | 16 | 75% | -$31.26 | -20.7% |
| College football | 25 | 0 | — | — | — |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29 | DEN >72 | NO | 83¢ | 98% | Open | — |
| 2026-09-29 | MIA <83 | NO | 82¢ | 93% | Open | — |
| 2026-09-29 | PHIL 77-78 | NO | 74¢ | 86% | Open | — |
| 2026-09-29 | LAX 86-87 | YES | 7¢ | 19% | Open | — |
| 2026-09-29 | DEN 65-66 | YES | 16¢ | 26% | Open | — |
| 2026-09-29 | DEN 71-72 | NO | 83¢ | 95% | Open | — |
| 2026-09-29 | DEN <65 | YES | 19¢ | 31% | Open | — |
| 2026-09-29 | MIA 89-90 | YES | 7¢ | 19% | Open | — |
| 2026-09-29 | CHI 76-77 | NO | 56¢ | 74% | Open | — |
| 2026-09-29 | CHI 78-79 | NO | 64¢ | 77% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29 | OKC | YES | 17¢ | 41% | Open | — |
| 2026-09-29 | MIA | NO | 19¢ | 41% | Open | — |
| 2026-09-29 | AUS | YES | 14¢ | 33% | Open | — |
| 2026-09-29 | SATX | YES | 24¢ | 37% | Open | — |
| 2026-09-29 | HOU | YES | 25¢ | 40% | Open | — |
| 2026-09-29 | BOS | YES | 38¢ | 70% | Open | — |
| 2026-09-28 | SEA | NO | 82¢ | 96% | Open | — |
| 2026-09-28 | PHX | NO | 13¢ | 24% | Open | — |
| 2026-09-28 | OKC | YES | 9¢ | 21% | Open | — |
| 2026-09-28 | LV | YES | 49¢ | 62% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
