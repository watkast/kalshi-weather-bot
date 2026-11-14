# Kalshi Paper Bots — Results

*Updated Sat Nov 14, 3:37 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 872 | 839 | 36% | -$353.14 | -10.5% | 33 | Losing |
| **Rain** | 262 | 244 | 32% | -$24.63 | -3.1% | 18 | Losing |
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
| 2026-11-14 | CHI 44-45 | YES | 6¢ | 19% | Open | — |
| 2026-11-14 | CHI 50-51 | YES | 5¢ | 14% | Open | — |
| 2026-11-14 | NY <46 | YES | 21¢ | 43% | Open | — |
| 2026-11-14 | PHIL 46-47 | YES | 13¢ | 23% | Open | — |
| 2026-11-14 | PHIL 48-49 | NO | 27¢ | 74% | Open | — |
| 2026-11-14 | LAX 71-72 | NO | 36¢ | 74% | Open | — |
| 2026-11-14 | DEN 54-55 | YES | 8¢ | 26% | Open | — |
| 2026-11-14 | DEN <50 | NO | 51¢ | 93% | Open | — |
| 2026-11-14 | AUS <67 | NO | 70¢ | 80% | Open | — |
| 2026-11-14 | MIA 70-71 | YES | 8¢ | 19% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-14 | PIT | NO | 23¢ | 35% | Open | — |
| 2026-11-14 | OKC | NO | 12¢ | 24% | Open | — |
| 2026-11-14 | LV | YES | 7¢ | 18% | Open | — |
| 2026-11-14 | DEN | YES | 34¢ | 56% | Open | — |
| 2026-11-14 | SFO | YES | 29¢ | 44% | Open | — |
| 2026-11-14 | SATX | NO | 19¢ | 31% | Open | — |
| 2026-11-14 | LAX | YES | 55¢ | 82% | Open | — |
| 2026-11-14 | EWR | YES | 6¢ | 20% | Open | — |
| 2026-11-14 | DAL | NO | 26¢ | 49% | Open | — |
| 2026-11-14 | CLL | NO | 59¢ | 80% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
