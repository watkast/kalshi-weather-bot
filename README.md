# Kalshi Paper Bots — Results

*Updated Mon Oct 26, 10:55 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 572 | 534 | 36% | -$294.62 | -13.2% | 38 | Losing |
| **Rain** | 151 | 145 | 37% | $33.48 | +6.7% | 6 | Promising |
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
| 2026-10-27 | PHIL 64-65 | YES | 12¢ | 26% | Open | — |
| 2026-10-27 | DEN 65-66 | NO | 64¢ | 74% | Open | — |
| 2026-10-27 | AUS <80 | NO | 78¢ | 88% | Open | — |
| 2026-10-27 | CHI 66-67 | YES | 6¢ | 19% | Open | — |
| 2026-10-27 | CHI 70-71 | NO | 42¢ | 77% | Open | — |
| 2026-10-27 | CHI 72-73 | YES | 5¢ | 14% | Open | — |
| 2026-10-27 | PHIL 66-67 | NO | 38¢ | 77% | Open | — |
| 2026-10-27 | LAX 76-77 | NO | 39¢ | 81% | Open | — |
| 2026-10-27 | AUS 82-83 | NO | 64¢ | 74% | Open | — |
| 2026-10-27 | AUS 84-85 | YES | 14¢ | 23% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-27 | OKC | NO | 37¢ | 56% | Open | — |
| 2026-10-27 | SEA | YES | 83¢ | 96% | Open | — |
| 2026-10-27 | DAL | YES | 10¢ | 29% | Open | — |
| 2026-10-26 | SEA | NO | 29¢ | 42% | Open | — |
| 2026-10-26 | MKE | YES | 5¢ | 19% | Open | — |
| 2026-10-26 | DEN | NO | 31¢ | 52% | Open | — |
| 2026-10-25 | DEN | YES | 45¢ | 66% | NO | -$4.68 |
| 2026-10-25 | SEA | NO | 10¢ | 27% | YES | -$1.07 |
| 2026-10-25 | MIN | NO | 30¢ | 51% | YES | -$3.15 |
| 2026-10-24 | DEN | NO | 36¢ | 48% | NO | $6.23 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
