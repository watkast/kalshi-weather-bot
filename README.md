# Kalshi Paper Bots — Results

*Updated Sat Oct 17, 11:05 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 399 | 358 | 38% | -$195.37 | -12.6% | 41 | Losing |
| **Rain** | 124 | 115 | 41% | $75.68 | +19.2% | 9 | Promising |
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
| 2026-10-18 | PHIL 58-59 | YES | 11¢ | 26% | Open | — |
| 2026-10-18 | PHIL 60-61 | NO | 56¢ | 81% | Open | — |
| 2026-10-18 | PHIL 62-63 | NO | 63¢ | 91% | Open | — |
| 2026-10-18 | LAX 80-81 | YES | 6¢ | 19% | Open | — |
| 2026-10-18 | LAX 84-85 | NO | 67¢ | 77% | Open | — |
| 2026-10-18 | LAX >85 | NO | 67¢ | 80% | Open | — |
| 2026-10-18 | DEN 72-73 | YES | 10¢ | 23% | Open | — |
| 2026-10-18 | DEN 76-77 | NO | 60¢ | 81% | Open | — |
| 2026-10-18 | AUS 73-74 | NO | 64¢ | 74% | Open | — |
| 2026-10-18 | AUS 75-76 | NO | 50¢ | 77% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-18 | LV | YES | 9¢ | 29% | Open | — |
| 2026-10-17 | TTN | NO | 38¢ | 68% | Open | — |
| 2026-10-17 | NYC | NO | 40¢ | 64% | Open | — |
| 2026-10-17 | EWR | NO | 47¢ | 65% | Open | — |
| 2026-10-17 | DC | NO | 16¢ | 28% | Open | — |
| 2026-10-17 | PVD | NO | 30¢ | 47% | Open | — |
| 2026-10-17 | PIT | YES | 18¢ | 29% | Open | — |
| 2026-10-17 | PHX | YES | 15¢ | 30% | Open | — |
| 2026-10-17 | PHIL | NO | 33¢ | 51% | Open | — |
| 2026-10-16 | MIN | NO | 14¢ | 37% | YES | -$1.49 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
