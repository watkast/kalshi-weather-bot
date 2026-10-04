# Kalshi Paper Bots — Results

*Updated Sun Oct 4, 5:59 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 160 | 124 | 40% | -$72.13 | -12.6% | 36 | Losing |
| **Rain** | 58 | 43 | 40% | $28.73 | +20.3% | 15 | Promising |
| **Longshot fade** | 953 | 914 | 93% | -$178.06 | -2.1% | 39 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 411 | 93% | -$51.26 | -1.3% |
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
| 2026-10-05 | PHIL 70-71 | YES | 14¢ | 26% | Open | — |
| 2026-10-05 | PHIL 72-73 | NO | 48¢ | 81% | Open | — |
| 2026-10-05 | PHIL 74-75 | NO | 71¢ | 91% | Open | — |
| 2026-10-05 | LAX 97-98 | NO | 76¢ | 86% | Open | — |
| 2026-10-05 | LAX 99-100 | YES | 12¢ | 23% | Open | — |
| 2026-10-05 | LAX <97 | NO | 38¢ | 93% | Open | — |
| 2026-10-05 | DEN 85-86 | YES | 9¢ | 23% | Open | — |
| 2026-10-05 | DEN 87-88 | NO | 46¢ | 74% | Open | — |
| 2026-10-05 | DEN 89-90 | NO | 63¢ | 81% | Open | — |
| 2026-10-05 | AUS 85-86 | NO | 57¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-05 | NOLA | NO | 26¢ | 40% | Open | — |
| 2026-10-05 | ATL | NO | 35¢ | 54% | Open | — |
| 2026-10-05 | BOS | YES | 8¢ | 24% | Open | — |
| 2026-10-04 | MIA | YES | 19¢ | 31% | Open | — |
| 2026-10-04 | HOU | YES | 56¢ | 74% | Open | — |
| 2026-10-04 | NYC | YES | 55¢ | 68% | Open | — |
| 2026-10-04 | MKE | YES | 10¢ | 27% | Open | — |
| 2026-10-04 | DAL | NO | 60¢ | 74% | Open | — |
| 2026-10-04 | CLL | YES | 44¢ | 57% | Open | — |
| 2026-10-04 | TTN | YES | 60¢ | 80% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
