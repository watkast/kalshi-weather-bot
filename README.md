# Kalshi Paper Bots — Results

*Updated Mon Nov 2, 11:57 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 683 | 653 | 36% | -$333.05 | -12.4% | 30 | Losing |
| **Rain** | 192 | 181 | 33% | -$3.53 | -0.6% | 11 | Break-even |
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
| 2026-11-03 | DEN 57-58 | YES | 6¢ | 19% | Open | — |
| 2026-11-03 | PHIL 71-72 | NO | 41¢ | 77% | Open | — |
| 2026-11-03 | PHIL <69 | YES | 6¢ | 31% | Open | — |
| 2026-11-03 | LAX 71-72 | YES | 8¢ | 23% | Open | — |
| 2026-11-03 | LAX 73-74 | NO | 35¢ | 74% | Open | — |
| 2026-11-03 | DEN 55-56 | NO | 49¢ | 74% | Open | — |
| 2026-11-03 | DEN <55 | YES | 24¢ | 43% | Open | — |
| 2026-11-03 | AUS 77-78 | YES | 13¢ | 26% | Open | — |
| 2026-11-03 | AUS 79-80 | NO | 56¢ | 81% | Open | — |
| 2026-11-03 | AUS >80 | NO | 60¢ | 88% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-03 | AUS | NO | 8¢ | 19% | Open | — |
| 2026-11-03 | SATX | NO | 8¢ | 23% | Open | — |
| 2026-11-03 | MIN | NO | 7¢ | 19% | Open | — |
| 2026-11-03 | CHI | YES | 82¢ | 95% | Open | — |
| 2026-11-02 | PIT | YES | 9¢ | 24% | Open | — |
| 2026-11-02 | MKE | NO | 31¢ | 46% | Open | — |
| 2026-11-02 | NOLA | NO | 54¢ | 71% | Open | — |
| 2026-11-02 | LEX | NO | 18¢ | 59% | Open | — |
| 2026-11-02 | DEN | NO | 11¢ | 27% | Open | — |
| 2026-11-02 | DAL | YES | 59¢ | 91% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
