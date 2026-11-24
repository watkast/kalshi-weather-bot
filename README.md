# Kalshi Paper Bots — Results

*Updated Tue Nov 24, 6:55 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 1041 | 1021 | 36% | -$413.20 | -10.1% | 20 | Losing |
| **Rain** | 317 | 307 | 29% | -$95.79 | -9.6% | 10 | Losing |
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
| 2026-11-24 | PHIL 51-52 | YES | 15¢ | 26% | Open | — |
| 2026-11-24 | PHIL 53-54 | NO | 34¢ | 81% | Open | — |
| 2026-11-24 | LAX 70-71 | YES | 7¢ | 26% | Open | — |
| 2026-11-24 | LAX 72-73 | NO | 48¢ | 77% | Open | — |
| 2026-11-24 | LAX 74-75 | NO | 62¢ | 86% | Open | — |
| 2026-11-24 | DEN 48-49 | YES | 10¢ | 23% | Open | — |
| 2026-11-24 | DEN 50-51 | NO | 43¢ | 74% | Open | — |
| 2026-11-24 | AUS 53-54 | NO | 44¢ | 74% | Open | — |
| 2026-11-24 | MIA 79-80 | NO | 56¢ | 81% | Open | — |
| 2026-11-24 | MIA 81-82 | NO | 61¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-25 | DC | NO | 79¢ | 92% | Open | — |
| 2026-11-25 | CHI | YES | 10¢ | 22% | Open | — |
| 2026-11-25 | ATL | NO | 6¢ | 18% | Open | — |
| 2026-11-24 | SFO | YES | 72¢ | 99% | Open | — |
| 2026-11-24 | MIA | NO | 48¢ | 82% | Open | — |
| 2026-11-24 | CLL | NO | 50¢ | 72% | Open | — |
| 2026-11-24 | SATX | YES | 38¢ | 65% | Open | — |
| 2026-11-24 | NOLA | NO | 45¢ | 74% | Open | — |
| 2026-11-24 | HOU | NO | 44¢ | 68% | Open | — |
| 2026-11-23 | NOLA | NO | 41¢ | 58% | NO | $5.73 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
