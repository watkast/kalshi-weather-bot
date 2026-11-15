# Kalshi Paper Bots — Results

*Updated Sun Nov 15, 10:02 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 902 | 867 | 36% | -$343.92 | -9.9% | 35 | Losing |
| **Rain** | 267 | 262 | 31% | -$43.74 | -5.2% | 5 | Losing |
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
| 2026-11-16 | PHIL 53-54 | NO | 63¢ | 81% | Open | — |
| 2026-11-16 | PHIL 55-56 | NO | 50¢ | 74% | Open | — |
| 2026-11-16 | PHIL 57-58 | YES | 5¢ | 23% | Open | — |
| 2026-11-16 | LAX 70-71 | NO | 46¢ | 74% | Open | — |
| 2026-11-16 | DEN 60-61 | YES | 11¢ | 23% | Open | — |
| 2026-11-16 | DEN 64-65 | NO | 63¢ | 81% | Open | — |
| 2026-11-16 | AUS 52-53 | YES | 5¢ | 26% | Open | — |
| 2026-11-16 | AUS 56-57 | NO | 72¢ | 91% | Open | — |
| 2026-11-16 | AUS >57 | NO | 51¢ | 97% | Open | — |
| 2026-11-16 | MIA 80-81 | NO | 32¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-16 | SFO | NO | 6¢ | 21% | Open | — |
| 2026-11-16 | NOLA | NO | 18¢ | 46% | Open | — |
| 2026-11-16 | MIA | YES | 16¢ | 33% | Open | — |
| 2026-11-16 | HOU | NO | 34¢ | 58% | Open | — |
| 2026-11-15 | NOLA | NO | 61¢ | 94% | Open | — |
| 2026-11-14 | PIT | NO | 23¢ | 35% | NO | $7.57 |
| 2026-11-14 | OKC | NO | 12¢ | 24% | YES | -$1.28 |
| 2026-11-14 | LV | YES | 7¢ | 18% | NO | -$0.75 |
| 2026-11-14 | DEN | YES | 34¢ | 56% | NO | -$3.56 |
| 2026-11-14 | SFO | YES | 29¢ | 44% | YES | $6.95 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
