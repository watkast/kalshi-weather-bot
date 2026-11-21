# Kalshi Paper Bots — Results

*Updated Fri Nov 20, 7:26 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 995 | 960 | 36% | -$376.35 | -9.8% | 35 | Losing |
| **Rain** | 286 | 277 | 30% | -$39.33 | -4.5% | 9 | Losing |
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
| 2026-11-21 | AUS 74-75 | NO | 63¢ | 74% | Open | — |
| 2026-11-21 | NY 64-65 | NO | 57¢ | 74% | Open | — |
| 2026-11-21 | NY >65 | YES | 7¢ | 31% | Open | — |
| 2026-11-21 | PHIL 63-64 | YES | 7¢ | 19% | Open | — |
| 2026-11-21 | PHIL 67-68 | NO | 48¢ | 77% | Open | — |
| 2026-11-21 | LAX 65-66 | YES | 6¢ | 19% | Open | — |
| 2026-11-21 | LAX 69-70 | NO | 47¢ | 77% | Open | — |
| 2026-11-21 | LAX >70 | YES | 7¢ | 20% | Open | — |
| 2026-11-21 | DEN 42-43 | YES | 6¢ | 19% | Open | — |
| 2026-11-21 | DEN 46-47 | NO | 53¢ | 77% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-21 | SFO | YES | 84¢ | 96% | Open | — |
| 2026-11-21 | SEA | YES | 65¢ | 82% | Open | — |
| 2026-11-21 | OKC | YES | 57¢ | 70% | Open | — |
| 2026-11-21 | MIN | NO | 16¢ | 39% | Open | — |
| 2026-11-21 | MIA | NO | 31¢ | 67% | Open | — |
| 2026-11-21 | ATL | NO | 39¢ | 94% | Open | — |
| 2026-11-20 | MIA | YES | 15¢ | 40% | Open | — |
| 2026-11-20 | SFO | NO | 12¢ | 51% | Open | — |
| 2026-11-20 | NOLA | YES | 12¢ | 25% | Open | — |
| 2026-11-19 | SEA | YES | 12¢ | 40% | NO | -$1.28 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
