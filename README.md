# Kalshi Paper Bots — Results

*Updated Thu Oct 1, 2:48 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 78 | 36 | 42% | -$33.67 | -18.3% | 42 | Losing |
| **Rain** | 22 | 14 | 29% | -$3.82 | -8.7% | 8 | Too early |
| **Longshot fade** | 953 | 710 | 92% | -$195.94 | -2.9% | 243 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 303 | 92% | -$58.47 | -2.0% |
| NFL | 211 | 209 | 89% | -$114.59 | -5.8% |
| Weather | 89 | 82 | 96% | $12.86 | +1.7% |
| MLB | 68 | 68 | 96% | $7.20 | +1.1% |
| College football | 68 | 0 | — | — | — |
| Crypto | 39 | 20 | 95% | $1.32 | +0.7% |
| Soccer | 27 | 25 | 76% | -$46.07 | -19.5% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| NHL | 1 | 1 | 100% | $0.74 | +8.0% |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01 | MIA 87-88 | YES | 12¢ | 23% | Open | — |
| 2026-10-01 | LAX 83-84 | YES | 5¢ | 23% | Open | — |
| 2026-10-01 | PHIL 78-79 | YES | 6¢ | 23% | Open | — |
| 2026-10-01 | PHIL 82-83 | NO | 67¢ | 81% | Open | — |
| 2026-10-01 | PHIL 84-85 | NO | 75¢ | 91% | Open | — |
| 2026-10-01 | LAX 79-80 | NO | 65¢ | 81% | Open | — |
| 2026-10-01 | LAX <79 | NO | 53¢ | 88% | Open | — |
| 2026-10-01 | DEN 68-69 | NO | 66¢ | 77% | Open | — |
| 2026-10-01 | DEN 70-71 | NO | 64¢ | 74% | Open | — |
| 2026-10-01 | DEN 72-73 | YES | 6¢ | 19% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01 | PIT | YES | 5¢ | 16% | Open | — |
| 2026-10-01 | MIA | NO | 7¢ | 18% | Open | — |
| 2026-10-01 | NOLA | YES | 57¢ | 74% | Open | — |
| 2026-10-01 | DEN | NO | 64¢ | 82% | Open | — |
| 2026-09-30 | MIA | NO | 12¢ | 28% | Open | — |
| 2026-09-30 | DAL | NO | 34¢ | 55% | Open | — |
| 2026-09-30 | CLL | YES | 35¢ | 48% | Open | — |
| 2026-09-30 | OKC | YES | 85¢ | 97% | Open | — |
| 2026-09-29 | LV | YES | 38¢ | 56% | YES | $6.03 |
| 2026-09-29 | DEN | YES | 44¢ | 65% | NO | -$4.58 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
