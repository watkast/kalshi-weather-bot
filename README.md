# Kalshi Paper Bots — Results

*Updated Wed Nov 25, 10:00 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 1066 | 1041 | 36% | -$423.51 | -10.2% | 25 | Losing |
| **Rain** | 318 | 314 | 29% | -$107.70 | -10.5% | 4 | Losing |
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
| 2026-11-26 | LAX 82-83 | NO | 59¢ | 74% | Open | — |
| 2026-11-26 | CHI 42-43 | YES | 5¢ | 19% | Open | — |
| 2026-11-26 | PHIL <57 | NO | 34¢ | 57% | Open | — |
| 2026-11-26 | LAX 80-81 | NO | 57¢ | 77% | Open | — |
| 2026-11-26 | LAX 84-85 | YES | 7¢ | 19% | Open | — |
| 2026-11-26 | DEN 60-61 | NO | 51¢ | 81% | Open | — |
| 2026-11-26 | AUS 60-61 | NO | 40¢ | 81% | Open | — |
| 2026-11-26 | MIA 76-77 | YES | 6¢ | 19% | Open | — |
| 2026-11-26 | MIA 78-79 | NO | 54¢ | 74% | Open | — |
| 2026-11-26 | MIA 80-81 | NO | 54¢ | 77% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-26 | MKE | YES | 30¢ | 42% | Open | — |
| 2026-11-25 | DC | NO | 79¢ | 92% | Open | — |
| 2026-11-25 | CHI | YES | 10¢ | 22% | Open | — |
| 2026-11-25 | ATL | NO | 6¢ | 18% | Open | — |
| 2026-11-24 | SFO | YES | 72¢ | 99% | YES | $2.65 |
| 2026-11-24 | MIA | NO | 48¢ | 82% | YES | -$4.98 |
| 2026-11-24 | CLL | NO | 50¢ | 72% | YES | -$5.18 |
| 2026-11-24 | SATX | YES | 38¢ | 65% | NO | -$3.97 |
| 2026-11-24 | NOLA | NO | 45¢ | 74% | YES | -$4.68 |
| 2026-11-24 | HOU | NO | 44¢ | 68% | YES | -$4.58 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
