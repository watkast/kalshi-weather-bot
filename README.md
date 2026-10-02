# Kalshi Paper Bots — Results

*Updated Thu Oct 1, 7:37 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

### → [15-Minute 1¢ Study](FIFTEEN.md) — every 1¢ moment in Kalshi's 15-minute up/down markets

### → [Fair-Value Bot](FAIRVALUE.md) — buys 15-minute crypto markets when a model says the price is wrong

### → [Gold & Silver Fair-Value Bot](METALS.md) — the same idea on 15-minute gold and silver markets

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 100 | 61 | 41% | -$47.41 | -15.9% | 39 | Losing |
| **Rain** | 29 | 18 | 28% | -$10.91 | -17.9% | 11 | Too early |
| **Longshot fade** | 953 | 781 | 92% | -$171.38 | -2.3% | 172 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| Other | 448 | 355 | 93% | -$42.79 | -1.3% |
| NFL | 211 | 209 | 89% | -$114.59 | -5.8% |
| Weather | 89 | 89 | 97% | $16.09 | +1.9% |
| MLB | 68 | 68 | 96% | $7.20 | +1.1% |
| College football | 68 | 0 | — | — | — |
| Crypto | 39 | 30 | 97% | $5.67 | +2.0% |
| Soccer | 27 | 27 | 78% | -$44.77 | -17.6% |
| NBA / WNBA | 2 | 2 | 100% | $1.07 | +5.7% |
| NHL | 1 | 1 | 100% | $0.74 | +8.0% |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02 | LAX 89-90 | YES | 16¢ | 26% | Open | — |
| 2026-10-02 | LAX <85 | NO | 77¢ | 93% | Open | — |
| 2026-10-02 | DEN 83-84 | NO | 72¢ | 91% | Open | — |
| 2026-10-02 | MIA 91-92 | YES | 5¢ | 19% | Open | — |
| 2026-10-02 | PHIL 82-83 | YES | 5¢ | 19% | Open | — |
| 2026-10-02 | PHIL 84-85 | YES | 11¢ | 26% | Open | — |
| 2026-10-02 | PHIL 86-87 | NO | 63¢ | 77% | Open | — |
| 2026-10-02 | PHIL 88-89 | NO | 58¢ | 86% | Open | — |
| 2026-10-02 | LAX 85-86 | NO | 79¢ | 91% | Open | — |
| 2026-10-02 | LAX 87-88 | NO | 66¢ | 81% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02 | OKC | YES | 44¢ | 76% | Open | — |
| 2026-10-02 | MIA | NO | 16¢ | 37% | Open | — |
| 2026-10-02 | DC | YES | 30¢ | 44% | Open | — |
| 2026-10-02 | CHI | NO | 59¢ | 80% | Open | — |
| 2026-10-02 | BOS | NO | 49¢ | 65% | Open | — |
| 2026-10-02 | PIT | YES | 71¢ | 94% | Open | — |
| 2026-10-02 | CLL | YES | 84¢ | 96% | Open | — |
| 2026-10-01 | PIT | YES | 5¢ | 16% | Open | — |
| 2026-10-01 | MIA | NO | 7¢ | 18% | Open | — |
| 2026-10-01 | NOLA | YES | 57¢ | 74% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
