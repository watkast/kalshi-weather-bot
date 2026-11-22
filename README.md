# Kalshi Paper Bots — Results

*Updated Sat Nov 21, 6:26 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 1010 | 977 | 36% | -$386.81 | -9.9% | 33 | Losing |
| **Rain** | 300 | 280 | 30% | -$43.48 | -4.9% | 20 | Losing |
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
| 2026-11-22 | PHIL 65-66 | NO | 61¢ | 77% | Open | — |
| 2026-11-22 | LAX 65-66 | YES | 12¢ | 23% | Open | — |
| 2026-11-22 | CHI 58-59 | NO | 57¢ | 77% | Open | — |
| 2026-11-22 | NY 63-64 | YES | 14¢ | 23% | Open | — |
| 2026-11-22 | NY <61 | NO | 49¢ | 69% | Open | — |
| 2026-11-22 | LAX 67-68 | NO | 36¢ | 74% | Open | — |
| 2026-11-22 | DEN 45-46 | NO | 60¢ | 74% | Open | — |
| 2026-11-22 | DEN >48 | YES | 9¢ | 20% | Open | — |
| 2026-11-22 | AUS 73-74 | NO | 53¢ | 77% | Open | — |
| 2026-11-22 | AUS 75-76 | NO | 72¢ | 86% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-22 | PHIL | YES | 73¢ | 89% | Open | — |
| 2026-11-22 | EWR | YES | 85¢ | 96% | Open | — |
| 2026-11-22 | OKC | NO | 9¢ | 22% | Open | — |
| 2026-11-22 | ATL | NO | 42¢ | 74% | Open | — |
| 2026-11-22 | SFO | YES | 36¢ | 52% | Open | — |
| 2026-11-22 | SEA | NO | 34¢ | 55% | Open | — |
| 2026-11-22 | SATX | YES | 49¢ | 63% | Open | — |
| 2026-11-22 | MIA | YES | 19¢ | 30% | Open | — |
| 2026-11-22 | LEX | NO | 48¢ | 74% | Open | — |
| 2026-11-22 | LAX | YES | 20¢ | 41% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
