# Kalshi Paper Bots — Results

*Updated Fri Oct 2, 2:05 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets

### → [Range-Scalp Bot](SCALP.md) — buys 15-minute crypto sides holding at 55–70¢, sells at +20¢, repeats

### → [Momentum Bot](MOMENTUM.md) — buys a 15-minute crypto side right after its price jumps, sells at +5¢ or more

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 123 | 78 | 40% | -$56.39 | -15.4% | 45 | Losing |
| **Rain** | 43 | 22 | 32% | -$4.65 | -6.2% | 21 | Losing |
| **Longshot fade** | 953 | 789 | 92% | -$166.69 | -2.2% | 164 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 360 | 93% | -$39.96 | -1.2% |
| NFL | 211 | 209 | 89% | -$114.59 | -5.8% |
| Weather | 89 | 89 | 97% | $16.09 | +1.9% |
| MLB | 68 | 68 | 96% | $7.20 | +1.1% |
| College football | 68 | 3 | 100% | $1.86 | +6.6% |
| Crypto | 39 | 30 | 97% | $5.67 | +2.0% |
| Soccer | 27 | 27 | 78% | -$44.77 | -17.6% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| NHL | 1 | 1 | 100% | $0.74 | +8.0% |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03 | LAX 91-92 | YES | 10¢ | 26% | Open | — |
| 2026-10-03 | LAX 95-96 | NO | 73¢ | 86% | Open | — |
| 2026-10-03 | LAX 97-98 | NO | 77¢ | 95% | Open | — |
| 2026-10-03 | DEN 87-88 | YES | 5¢ | 14% | Open | — |
| 2026-10-03 | PHIL 70-71 | YES | 7¢ | 19% | Open | — |
| 2026-10-03 | PHIL 72-73 | NO | 62¢ | 74% | Open | — |
| 2026-10-03 | PHIL 74-75 | NO | 63¢ | 77% | Open | — |
| 2026-10-03 | LAX 93-94 | YES | 14¢ | 23% | Open | — |
| 2026-10-03 | LAX >98 | NO | 75¢ | 88% | Open | — |
| 2026-10-03 | DEN 83-84 | NO | 56¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03 | ATL | NO | 17¢ | 33% | Open | — |
| 2026-10-03 | TTN | YES | 5¢ | 29% | Open | — |
| 2026-10-03 | SATX | NO | 24¢ | 39% | Open | — |
| 2026-10-03 | PVD | YES | 16¢ | 34% | Open | — |
| 2026-10-03 | PHIL | YES | 8¢ | 35% | Open | — |
| 2026-10-03 | NYC | YES | 8¢ | 49% | Open | — |
| 2026-10-03 | DC | NO | 27¢ | 40% | Open | — |
| 2026-10-03 | DAL | NO | 6¢ | 25% | Open | — |
| 2026-10-03 | AUS | NO | 13¢ | 38% | Open | — |
| 2026-10-03 | OKC | YES | 26¢ | 53% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
