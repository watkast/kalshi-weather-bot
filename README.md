# Kalshi Paper Bots — Results

*Updated Tue Nov 3, 11:37 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 702 | 667 | 36% | -$339.99 | -12.4% | 35 | Losing |
| **Rain** | 194 | 188 | 32% | -$16.64 | -2.7% | 6 | Break-even |
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
| 2026-11-04 | LAX 77-78 | YES | 5¢ | 19% | Open | — |
| 2026-11-04 | DEN <54 | YES | 9¢ | 31% | Open | — |
| 2026-11-04 | AUS 75-76 | YES | 7¢ | 26% | Open | — |
| 2026-11-04 | AUS 79-80 | NO | 72¢ | 91% | Open | — |
| 2026-11-04 | PHIL 74-75 | NO | 38¢ | 74% | Open | — |
| 2026-11-04 | PHIL 76-77 | YES | 11¢ | 23% | Open | — |
| 2026-11-04 | LAX 73-74 | NO | 60¢ | 74% | Open | — |
| 2026-11-04 | LAX 75-76 | NO | 50¢ | 77% | Open | — |
| 2026-11-04 | DEN 54-55 | NO | 53¢ | 81% | Open | — |
| 2026-11-04 | DEN 56-57 | NO | 62¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-04 | NOLA | NO | 48¢ | 62% | Open | — |
| 2026-11-04 | MIA | NO | 14¢ | 32% | Open | — |
| 2026-11-03 | AUS | NO | 8¢ | 19% | Open | — |
| 2026-11-03 | SATX | NO | 8¢ | 23% | Open | — |
| 2026-11-03 | MIN | NO | 7¢ | 19% | Open | — |
| 2026-11-03 | CHI | YES | 82¢ | 95% | Open | — |
| 2026-11-02 | PIT | YES | 9¢ | 24% | NO | -$0.96 |
| 2026-11-02 | MKE | NO | 31¢ | 46% | YES | -$3.25 |
| 2026-11-02 | NOLA | NO | 54¢ | 71% | NO | $4.42 |
| 2026-11-02 | LEX | NO | 18¢ | 59% | YES | -$1.91 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
