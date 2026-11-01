# Kalshi Paper Bots — Results

*Updated Sun Nov 1, 12:36 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 653 | 634 | 35% | -$358.32 | -13.8% | 19 | Losing |
| **Rain** | 186 | 172 | 33% | -$6.43 | -1.1% | 14 | Break-even |
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
| 2026-11-01 | LAX 69-70 | NO | 63¢ | 74% | Open | — |
| 2026-11-01 | AUS 85-86 | NO | 58¢ | 74% | Open | — |
| 2026-11-01 | NY <60 | NO | 50¢ | 80% | Open | — |
| 2026-11-01 | PHIL 62-63 | NO | 55¢ | 77% | Open | — |
| 2026-11-01 | PHIL 64-65 | NO | 60¢ | 74% | Open | — |
| 2026-11-01 | PHIL 66-67 | YES | 5¢ | 19% | Open | — |
| 2026-11-01 | PHIL <62 | YES | 6¢ | 20% | Open | — |
| 2026-11-01 | LAX >70 | NO | 39¢ | 69% | Open | — |
| 2026-11-01 | AUS 83-84 | NO | 62¢ | 77% | Open | — |
| 2026-11-01 | MIA 81-82 | NO | 53¢ | 77% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-02 | NOLA | NO | 54¢ | 71% | Open | — |
| 2026-11-02 | LEX | NO | 18¢ | 59% | Open | — |
| 2026-11-02 | DEN | NO | 11¢ | 27% | Open | — |
| 2026-11-02 | DAL | YES | 59¢ | 91% | Open | — |
| 2026-11-02 | CMH | NO | 40¢ | 71% | Open | — |
| 2026-11-01 | HOU | YES | 7¢ | 18% | Open | — |
| 2026-11-01 | SFO | NO | 33¢ | 49% | Open | — |
| 2026-11-01 | OKC | YES | 8¢ | 22% | Open | — |
| 2026-11-01 | NOLA | YES | 36¢ | 69% | Open | — |
| 2026-11-01 | LV | NO | 8¢ | 30% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
