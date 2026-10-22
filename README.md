# Kalshi Paper Bots — Results

*Updated Wed Oct 21, 10:58 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets

### → [Range-Scalp Bot](SCALP.md) — buys 15-minute crypto sides holding at 55–70¢, sells at +20¢, repeats

### → [Momentum Bot](MOMENTUM.md) — buys a 15-minute crypto side after a 20¢+ price jump, sells at +5¢ or more

### → [Lag Tracker](LAG.md) — times how fast Kalshi's 15-minute crypto prices follow live Coinbase/Kraken moves, and paper-trades the gap

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 476 | 441 | 37% | -$266.47 | -14.1% | 35 | Losing |
| **Rain** | 136 | 128 | 38% | $60.12 | +14.0% | 8 | Promising |
| **Longshot fade** | 953 | 948 | 93% | -$169.26 | -1.9% | 5 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 445 | 93% | -$42.46 | -1.0% |
| NFL | 211 | 209 | 89% | -$114.59 | -5.8% |
| Weather | 89 | 89 | 97% | $16.09 | +1.9% |
| MLB | 68 | 68 | 96% | $7.20 | +1.1% |
| College football | 68 | 68 | 96% | $7.27 | +1.1% |
| Crypto | 39 | 39 | 95% | $0.19 | +0.1% |
| Soccer | 27 | 27 | 78% | -$44.77 | -17.6% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| NHL | 1 | 1 | 100% | $0.74 | +8.0% |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-22 | DEN 75-76 | YES | 14¢ | 23% | Open | — |
| 2026-10-22 | MIA 82-83 | NO | 59¢ | 74% | Open | — |
| 2026-10-22 | MIA 86-87 | YES | 5¢ | 14% | Open | — |
| 2026-10-22 | PHIL 66-67 | YES | 5¢ | 23% | Open | — |
| 2026-10-22 | PHIL 70-71 | NO | 46¢ | 81% | Open | — |
| 2026-10-22 | LAX 66-67 | YES | 7¢ | 26% | Open | — |
| 2026-10-22 | LAX 70-71 | NO | 57¢ | 86% | Open | — |
| 2026-10-22 | LAX >71 | NO | 66¢ | 93% | Open | — |
| 2026-10-22 | DEN 73-74 | NO | 69¢ | 86% | Open | — |
| 2026-10-22 | DEN 77-78 | YES | 8¢ | 26% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-22 | LV | YES | 65¢ | 80% | Open | — |
| 2026-10-22 | LAX | YES | 83¢ | 95% | Open | — |
| 2026-10-22 | SEA | YES | 13¢ | 26% | Open | — |
| 2026-10-22 | DEN | NO | 67¢ | 84% | Open | — |
| 2026-10-22 | SFO | NO | 21¢ | 37% | Open | — |
| 2026-10-21 | PHX | YES | 79¢ | 92% | Open | — |
| 2026-10-21 | OKC | YES | 6¢ | 18% | Open | — |
| 2026-10-21 | LV | YES | 36¢ | 55% | Open | — |
| 2026-10-20 | SFO | YES | 15¢ | 53% | NO | -$1.59 |
| 2026-10-20 | PHX | YES | 20¢ | 63% | NO | -$2.12 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
