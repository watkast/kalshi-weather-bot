# Kalshi Paper Bots — Results

*Updated Tue Oct 13, 11:00 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 314 | 290 | 40% | -$122.06 | -9.6% | 24 | Losing |
| **Rain** | 93 | 84 | 39% | $38.65 | +13.3% | 9 | Promising |
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
| 2026-10-14 | PHIL 87-88 | YES | 5¢ | 14% | Open | — |
| 2026-10-14 | LAX 76-77 | YES | 8¢ | 26% | Open | — |
| 2026-10-14 | LAX >79 | NO | 31¢ | 88% | Open | — |
| 2026-10-14 | DEN 48-49 | NO | 67¢ | 81% | Open | — |
| 2026-10-14 | DEN 50-51 | NO | 69¢ | 91% | Open | — |
| 2026-10-14 | DEN <48 | YES | 22¢ | 69% | Open | — |
| 2026-10-14 | AUS 91-92 | YES | 12¢ | 23% | Open | — |
| 2026-10-14 | AUS 93-94 | NO | 63¢ | 74% | Open | — |
| 2026-10-14 | AUS 95-96 | NO | 65¢ | 81% | Open | — |
| 2026-10-14 | MIA 88-89 | NO | 35¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-14 | PVD | YES | 8¢ | 23% | Open | — |
| 2026-10-14 | HOU | YES | 15¢ | 34% | Open | — |
| 2026-10-14 | BOS | YES | 25¢ | 37% | Open | — |
| 2026-10-13 | PHX | YES | 49¢ | 69% | Open | — |
| 2026-10-13 | LV | YES | 9¢ | 22% | Open | — |
| 2026-10-13 | BOS | NO | 13¢ | 25% | Open | — |
| 2026-10-13 | MKE | YES | 33¢ | 46% | Open | — |
| 2026-10-13 | CLL | YES | 23¢ | 48% | Open | — |
| 2026-10-13 | AUS | YES | 17¢ | 28% | Open | — |
| 2026-10-12 | SATX | YES | 18¢ | 39% | NO | -$1.91 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
