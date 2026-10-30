# Kalshi Paper Bots — Results

*Updated Fri Oct 30, 1:16 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 634 | 608 | 36% | -$334.93 | -13.3% | 26 | Losing |
| **Rain** | 172 | 159 | 35% | $12.62 | +2.3% | 13 | Break-even |
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
| 2026-10-31 | PHIL 61-62 | NO | 36¢ | 77% | Open | — |
| 2026-10-31 | PHIL 63-64 | YES | 10¢ | 26% | Open | — |
| 2026-10-31 | LAX 67-68 | YES | 5¢ | 23% | Open | — |
| 2026-10-31 | LAX 69-70 | NO | 77¢ | 86% | Open | — |
| 2026-10-31 | LAX >70 | NO | 29¢ | 93% | Open | — |
| 2026-10-31 | AUS 81-82 | YES | 5¢ | 19% | Open | — |
| 2026-10-31 | AUS <77 | NO | 58¢ | 80% | Open | — |
| 2026-10-31 | MIA 85-86 | NO | 41¢ | 77% | Open | — |
| 2026-10-31 | CHI 62-63 | NO | 58¢ | 74% | Open | — |
| 2026-10-31 | CHI <60 | YES | 8¢ | 20% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-31 | SFO | YES | 25¢ | 42% | Open | — |
| 2026-10-31 | SATX | YES | 36¢ | 56% | Open | — |
| 2026-10-31 | MIA | NO | 13¢ | 25% | Open | — |
| 2026-10-31 | LV | YES | 73¢ | 91% | Open | — |
| 2026-10-31 | DAL | YES | 33¢ | 61% | Open | — |
| 2026-10-31 | AUS | YES | 36¢ | 62% | Open | — |
| 2026-10-30 | SATX | NO | 10¢ | 25% | Open | — |
| 2026-10-30 | HOU | NO | 52¢ | 73% | Open | — |
| 2026-10-30 | CLL | NO | 27¢ | 60% | Open | — |
| 2026-10-30 | SEA | NO | 22¢ | 50% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
