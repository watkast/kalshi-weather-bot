# Kalshi Paper Bots — Results

*Updated Tue Nov 17, 9:14 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 941 | 905 | 36% | -$346.79 | -9.6% | 36 | Losing |
| **Rain** | 273 | 270 | 31% | -$40.49 | -4.7% | 3 | Losing |
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
| 2026-11-18 | PHIL 64-65 | NO | 42¢ | 81% | Open | — |
| 2026-11-18 | LAX 66-67 | YES | 15¢ | 26% | Open | — |
| 2026-11-18 | LAX 68-69 | NO | 41¢ | 77% | Open | — |
| 2026-11-18 | DEN 58-59 | NO | 59¢ | 77% | Open | — |
| 2026-11-18 | DEN 60-61 | NO | 75¢ | 86% | Open | — |
| 2026-11-18 | AUS 66-67 | YES | 6¢ | 23% | Open | — |
| 2026-11-18 | AUS 68-69 | YES | 9¢ | 26% | Open | — |
| 2026-11-18 | AUS 70-71 | NO | 69¢ | 81% | Open | — |
| 2026-11-18 | AUS 72-73 | NO | 56¢ | 91% | Open | — |
| 2026-11-18 | MIA 78-79 | NO | 53¢ | 86% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-18 | SEA | NO | 17¢ | 34% | Open | — |
| 2026-11-18 | LAX | YES | 14¢ | 65% | Open | — |
| 2026-11-17 | MIA | NO | 5¢ | 23% | Open | — |
| 2026-11-16 | SEA | YES | 30¢ | 52% | NO | -$3.15 |
| 2026-11-16 | LAX | NO | 28¢ | 41% | NO | $7.05 |
| 2026-11-16 | DAL | NO | 64¢ | 89% | NO | $3.43 |
| 2026-11-16 | SFO | NO | 6¢ | 21% | YES | -$0.64 |
| 2026-11-16 | NOLA | NO | 18¢ | 46% | YES | -$1.91 |
| 2026-11-16 | MIA | YES | 16¢ | 33% | YES | $8.30 |
| 2026-11-16 | HOU | NO | 34¢ | 58% | YES | -$3.56 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
