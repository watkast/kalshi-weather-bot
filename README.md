# Kalshi Paper Bots — Results

*Updated Thu Nov 12, 11:52 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 839 | 807 | 35% | -$420.41 | -13.0% | 32 | Losing |
| **Rain** | 248 | 230 | 33% | -$1.05 | -0.1% | 18 | Break-even |
| **Longshot fade** | 953 | 951 | 93% | -$167.12 | -1.9% | 2 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 448 | 94% | -$40.32 | -1.0% |
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
| 2026-11-12 | PHIL <61 | NO | 57¢ | 69% | Open | — |
| 2026-11-12 | NY 61-62 | YES | 5¢ | 14% | Open | — |
| 2026-11-12 | PHIL 61-62 | NO | 68¢ | 81% | Open | — |
| 2026-11-12 | PHIL 65-66 | YES | 11¢ | 23% | Open | — |
| 2026-11-12 | LAX 77-78 | NO | 62¢ | 81% | Open | — |
| 2026-11-12 | LAX 79-80 | YES | 5¢ | 26% | Open | — |
| 2026-11-12 | LAX <77 | NO | 44¢ | 88% | Open | — |
| 2026-11-12 | DEN 64-65 | YES | 9¢ | 23% | Open | — |
| 2026-11-12 | DEN 66-67 | NO | 54¢ | 74% | Open | — |
| 2026-11-12 | DEN 68-69 | NO | 59¢ | 81% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-13 | SEA | NO | 9¢ | 21% | Open | — |
| 2026-11-13 | LV | YES | 18¢ | 34% | Open | — |
| 2026-11-13 | LEX | NO | 15¢ | 50% | Open | — |
| 2026-11-13 | DC | YES | 21¢ | 52% | Open | — |
| 2026-11-12 | MKE | YES | 42¢ | 62% | Open | — |
| 2026-11-12 | CHI | YES | 57¢ | 82% | Open | — |
| 2026-11-12 | SFO | YES | 16¢ | 35% | Open | — |
| 2026-11-12 | SEA | YES | 6¢ | 36% | Open | — |
| 2026-11-12 | MIA | NO | 44¢ | 68% | Open | — |
| 2026-11-12 | LEX | NO | 17¢ | 51% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
