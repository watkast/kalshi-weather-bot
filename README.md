# Kalshi Paper Bots — Results

*Updated Tue Sep 29, 12:08 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 47 | 14 | 29% | -$22.87 | -36.4% | 33 | Too early |
| **Rain** | 15 | 6 | 50% | $9.17 | +44.0% | 9 | Too early |
| **Longshot fade** | 953 | 581 | 91% | -$179.85 | -3.3% | 372 | Losing |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 240 | 93% | -$35.88 | -1.6% |
| NFL | 211 | 209 | 89% | -$114.59 | -5.8% |
| Weather | 89 | 50 | 96% | $6.38 | +1.3% |
| MLB | 68 | 48 | 94% | -$4.39 | -1.0% |
| College football | 68 | 0 | — | — | — |
| Crypto | 39 | 12 | 100% | $6.03 | +5.3% |
| Soccer | 27 | 20 | 75% | -$38.47 | -20.4% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| NHL | 1 | 0 | — | — | — |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-30 | PHIL 78-79 | NO | 63¢ | 74% | Open | — |
| 2026-09-30 | PHIL 80-81 | NO | 57¢ | 77% | Open | — |
| 2026-09-30 | LAX 80-81 | NO | 61¢ | 77% | Open | — |
| 2026-09-30 | LAX 84-85 | YES | 7¢ | 19% | Open | — |
| 2026-09-30 | AUS 95-96 | NO | 63¢ | 77% | Open | — |
| 2026-09-30 | AUS 99-100 | YES | 5¢ | 19% | Open | — |
| 2026-09-30 | MIA 84-85 | NO | 68¢ | 81% | Open | — |
| 2026-09-30 | MIA 86-87 | NO | 62¢ | 74% | Open | — |
| 2026-09-30 | CHI 69-70 | NO | 56¢ | 81% | Open | — |
| 2026-09-30 | CHI 73-74 | YES | 8¢ | 23% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-30 | OKC | YES | 85¢ | 97% | Open | — |
| 2026-09-29 | LV | YES | 38¢ | 56% | Open | — |
| 2026-09-29 | DEN | YES | 44¢ | 65% | Open | — |
| 2026-09-29 | OKC | YES | 17¢ | 41% | Open | — |
| 2026-09-29 | MIA | NO | 19¢ | 41% | Open | — |
| 2026-09-29 | AUS | YES | 14¢ | 33% | Open | — |
| 2026-09-29 | SATX | YES | 24¢ | 37% | Open | — |
| 2026-09-29 | HOU | YES | 25¢ | 40% | Open | — |
| 2026-09-29 | BOS | YES | 38¢ | 70% | Open | — |
| 2026-09-28 | SEA | NO | 82¢ | 96% | NO | $1.69 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
