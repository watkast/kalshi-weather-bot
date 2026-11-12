# Kalshi Paper Bots — Results

*Updated Thu Nov 12, 1:03 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 852 | 823 | 35% | -$390.18 | -11.8% | 29 | Losing |
| **Rain** | 250 | 236 | 32% | -$13.31 | -1.7% | 14 | Break-even |
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
| 2026-11-13 | PHIL 47-48 | YES | 7¢ | 26% | Open | — |
| 2026-11-13 | PHIL 51-52 | NO | 49¢ | 91% | Open | — |
| 2026-11-13 | PHIL 53-54 | NO | 84¢ | 97% | Open | — |
| 2026-11-13 | LAX 68-69 | NO | 78¢ | 91% | Open | — |
| 2026-11-13 | LAX 70-71 | NO | 46¢ | 81% | Open | — |
| 2026-11-13 | DEN 64-65 | NO | 44¢ | 74% | Open | — |
| 2026-11-13 | AUS 75-76 | YES | 5¢ | 26% | Open | — |
| 2026-11-13 | AUS 79-80 | NO | 36¢ | 86% | Open | — |
| 2026-11-13 | MIA 80-81 | NO | 49¢ | 74% | Open | — |
| 2026-11-13 | CHI 41-42 | NO | 41¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-13 | MKE | YES | 32¢ | 52% | Open | — |
| 2026-11-13 | CMH | NO | 20¢ | 41% | Open | — |
| 2026-11-13 | SEA | NO | 9¢ | 21% | Open | — |
| 2026-11-13 | LV | YES | 18¢ | 34% | Open | — |
| 2026-11-13 | LEX | NO | 15¢ | 50% | Open | — |
| 2026-11-13 | DC | YES | 21¢ | 52% | Open | — |
| 2026-11-12 | MKE | YES | 42¢ | 62% | Open | — |
| 2026-11-12 | CHI | YES | 57¢ | 82% | Open | — |
| 2026-11-12 | SFO | YES | 16¢ | 35% | Open | — |
| 2026-11-12 | SEA | YES | 6¢ | 36% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
