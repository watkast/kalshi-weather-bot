# Kalshi Paper Bots — Results

*Updated Wed Oct 14, 9:05 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 322 | 294 | 39% | -$135.73 | -10.6% | 28 | Losing |
| **Rain** | 98 | 88 | 39% | $39.58 | +13.2% | 10 | Promising |
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
| 2026-10-14 | PHIL 83-84 | NO | 66¢ | 77% | Open | — |
| 2026-10-14 | PHIL 85-86 | NO | 58¢ | 74% | Open | — |
| 2026-10-14 | LAX 78-79 | NO | 67¢ | 77% | Open | — |
| 2026-10-14 | AUS >96 | YES | 7¢ | 20% | Open | — |
| 2026-10-14 | MIA 90-91 | YES | 7¢ | 19% | Open | — |
| 2026-10-14 | CHI 65-66 | YES | 16¢ | 26% | Open | — |
| 2026-10-14 | NY 78-79 | NO | 67¢ | 81% | Open | — |
| 2026-10-14 | NY 80-81 | YES | 15¢ | 26% | Open | — |
| 2026-10-14 | PHIL 87-88 | YES | 5¢ | 14% | Open | — |
| 2026-10-14 | LAX 76-77 | YES | 8¢ | 26% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-14 | SEA | NO | 64¢ | 79% | Open | — |
| 2026-10-14 | MKE | YES | 7¢ | 19% | Open | — |
| 2026-10-14 | EWR | YES | 9¢ | 20% | Open | — |
| 2026-10-14 | CLL | YES | 37¢ | 52% | Open | — |
| 2026-10-14 | AUS | YES | 44¢ | 66% | Open | — |
| 2026-10-14 | PVD | YES | 8¢ | 23% | Open | — |
| 2026-10-14 | HOU | YES | 15¢ | 34% | Open | — |
| 2026-10-14 | BOS | YES | 25¢ | 37% | Open | — |
| 2026-10-13 | PHX | YES | 49¢ | 69% | Open | — |
| 2026-10-13 | LV | YES | 9¢ | 22% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
