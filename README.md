# Kalshi Paper Bots — Results

*Updated Sat Oct 10, 11:48 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 271 | 233 | 42% | -$75.22 | -7.2% | 38 | Losing |
| **Rain** | 76 | 69 | 41% | $48.21 | +20.8% | 7 | Promising |
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
| 2026-10-11 | PHIL 66-67 | NO | 57¢ | 77% | Open | — |
| 2026-10-11 | PHIL <64 | YES | 5¢ | 31% | Open | — |
| 2026-10-11 | LAX 70-71 | YES | 11¢ | 26% | Open | — |
| 2026-10-11 | LAX 72-73 | NO | 48¢ | 81% | Open | — |
| 2026-10-11 | LAX 74-75 | NO | 77¢ | 91% | Open | — |
| 2026-10-11 | LAX <70 | YES | 8¢ | 43% | Open | — |
| 2026-10-11 | DEN 82-83 | NO | 57¢ | 74% | Open | — |
| 2026-10-11 | AUS 90-91 | YES | 9¢ | 19% | Open | — |
| 2026-10-11 | AUS 92-93 | NO | 54¢ | 74% | Open | — |
| 2026-10-11 | AUS 94-95 | NO | 62¢ | 77% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11 | ATL | YES | 16¢ | 35% | Open | — |
| 2026-10-10 | PIT | NO | 83¢ | 96% | Open | — |
| 2026-10-10 | CMH | YES | 25¢ | 58% | Open | — |
| 2026-10-10 | PHX | YES | 77¢ | 90% | Open | — |
| 2026-10-10 | NOLA | YES | 30¢ | 44% | Open | — |
| 2026-10-10 | LV | YES | 27¢ | 55% | Open | — |
| 2026-10-10 | LAX | YES | 30¢ | 45% | Open | — |
| 2026-10-09 | MKE | YES | 21¢ | 34% | YES | $7.78 |
| 2026-10-09 | ATL | NO | 52¢ | 73% | YES | -$5.38 |
| 2026-10-09 | NOLA | YES | 72¢ | 86% | NO | -$7.35 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
