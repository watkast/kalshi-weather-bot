# Kalshi Paper Bots — Results

*Updated Thu Oct 15, 8:56 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 345 | 308 | 39% | -$147.93 | -11.1% | 37 | Losing |
| **Rain** | 107 | 93 | 40% | $59.08 | +19.0% | 14 | Promising |
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
| 2026-10-15 | LAX 83-84 | YES | 5¢ | 14% | Open | — |
| 2026-10-15 | LAX 89-90 | NO | 59¢ | 81% | Open | — |
| 2026-10-15 | DEN >54 | YES | 6¢ | 20% | Open | — |
| 2026-10-15 | CHI 61-62 | YES | 12¢ | 26% | Open | — |
| 2026-10-15 | PHIL 68-69 | YES | 12¢ | 26% | Open | — |
| 2026-10-15 | PHIL 70-71 | NO | 67¢ | 77% | Open | — |
| 2026-10-15 | PHIL 72-73 | NO | 68¢ | 86% | Open | — |
| 2026-10-15 | PHIL 74-75 | NO | 85¢ | 95% | Open | — |
| 2026-10-15 | PHIL <68 | YES | 7¢ | 31% | Open | — |
| 2026-10-15 | LAX 85-86 | YES | 12¢ | 23% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-16 | SEA | YES | 11¢ | 39% | Open | — |
| 2026-10-16 | NOLA | NO | 70¢ | 82% | Open | — |
| 2026-10-16 | MIA | YES | 52¢ | 65% | Open | — |
| 2026-10-16 | HOU | YES | 32¢ | 52% | Open | — |
| 2026-10-15 | DEN | NO | 11¢ | 24% | Open | — |
| 2026-10-15 | DAL | NO | 50¢ | 63% | Open | — |
| 2026-10-15 | CMH | NO | 35¢ | 47% | Open | — |
| 2026-10-15 | PIT | NO | 39¢ | 62% | Open | — |
| 2026-10-15 | PHIL | NO | 65¢ | 77% | Open | — |
| 2026-10-14 | SEA | NO | 64¢ | 79% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
