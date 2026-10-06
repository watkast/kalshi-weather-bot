# Kalshi Paper Bots — Results

*Updated Tue Oct 6, 11:09 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 195 | 157 | 44% | -$41.46 | -5.7% | 38 | Losing |
| **Rain** | 61 | 58 | 45% | $55.64 | +27.2% | 3 | Promising |
| **Longshot fade** | 953 | 945 | 93% | -$170.46 | -1.9% | 8 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 442 | 93% | -$43.66 | -1.0% |
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
| 2026-10-07 | PHIL 71-72 | NO | 51¢ | 77% | Open | — |
| 2026-10-07 | LAX >90 | NO | 69¢ | 80% | Open | — |
| 2026-10-07 | DEN 84-85 | NO | 60¢ | 77% | Open | — |
| 2026-10-07 | AUS 85-86 | YES | 5¢ | 14% | Open | — |
| 2026-10-07 | AUS 87-88 | YES | 11¢ | 23% | Open | — |
| 2026-10-07 | AUS 89-90 | NO | 57¢ | 74% | Open | — |
| 2026-10-07 | AUS 91-92 | NO | 63¢ | 81% | Open | — |
| 2026-10-07 | MIA 89-90 | NO | 54¢ | 74% | Open | — |
| 2026-10-07 | MIA 91-92 | NO | 61¢ | 77% | Open | — |
| 2026-10-07 | CHI 74-75 | YES | 11¢ | 23% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-07 | HOU | YES | 8¢ | 26% | Open | — |
| 2026-10-06 | MIA | NO | 33¢ | 45% | Open | — |
| 2026-10-06 | HOU | YES | 10¢ | 29% | Open | — |
| 2026-10-05 | NOLA | NO | 26¢ | 40% | NO | $7.26 |
| 2026-10-05 | ATL | NO | 35¢ | 54% | NO | $6.34 |
| 2026-10-05 | BOS | YES | 8¢ | 24% | NO | -$0.86 |
| 2026-10-04 | MIA | YES | 19¢ | 31% | NO | -$2.01 |
| 2026-10-04 | HOU | YES | 56¢ | 74% | YES | $4.22 |
| 2026-10-04 | NYC | YES | 55¢ | 68% | YES | $4.32 |
| 2026-10-04 | MKE | YES | 10¢ | 27% | NO | -$1.07 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
