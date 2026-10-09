# Kalshi Paper Bots — Results

*Updated Fri Oct 9, 12:00 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 236 | 201 | 43% | -$45.42 | -5.0% | 35 | Losing |
| **Rain** | 69 | 61 | 44% | $60.25 | +28.7% | 8 | Promising |
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
| 2026-10-09 | NY 69-70 | NO | 65¢ | 77% | Open | — |
| 2026-10-09 | PHIL 72-73 | YES | 11¢ | 26% | Open | — |
| 2026-10-09 | PHIL 74-75 | NO | 62¢ | 81% | Open | — |
| 2026-10-09 | PHIL 76-77 | NO | 59¢ | 91% | Open | — |
| 2026-10-09 | LAX 81-82 | YES | 10¢ | 26% | Open | — |
| 2026-10-09 | LAX <79 | NO | 39¢ | 88% | Open | — |
| 2026-10-09 | DEN 86-87 | NO | 59¢ | 77% | Open | — |
| 2026-10-09 | AUS 90-91 | YES | 15¢ | 26% | Open | — |
| 2026-10-09 | AUS 92-93 | NO | 45¢ | 77% | Open | — |
| 2026-10-09 | AUS 94-95 | NO | 75¢ | 86% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-09 | MKE | YES | 21¢ | 34% | Open | — |
| 2026-10-09 | ATL | NO | 52¢ | 73% | Open | — |
| 2026-10-09 | NOLA | YES | 72¢ | 86% | Open | — |
| 2026-10-09 | HOU | YES | 6¢ | 27% | Open | — |
| 2026-10-09 | CHI | YES | 34¢ | 48% | Open | — |
| 2026-10-08 | PVD | YES | 9¢ | 40% | Open | — |
| 2026-10-08 | BOS | YES | 10¢ | 41% | Open | — |
| 2026-10-08 | NOLA | YES | 8¢ | 19% | Open | — |
| 2026-10-07 | HOU | YES | 8¢ | 26% | NO | -$0.86 |
| 2026-10-06 | MIA | NO | 33¢ | 45% | NO | $6.54 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
