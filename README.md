# Kalshi Paper Bots — Results

*Updated Sun Sep 27, 4:29 PM MT. Paper money only — no real trades. Refreshes about every 15 minutes.*

### → [1¢ Study dashboard](STUDY.md) — every 1¢ moment across all sports, tracked to the final whistle

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 15 | 0 | — | — | — | 15 | Too early |
| **Rain** | 4 | 0 | — | — | — | 4 | Too early |
| **Longshot fade** | 280 | 68 | 94% | -$4.96 | -0.8% | 212 | Break-even |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| NFL | 156 | 16 | 94% | -$2.60 | -1.7% |
| Other | 51 | 4 | 100% | $2.03 | +5.3% |
| MLB | 48 | 48 | 94% | -$4.39 | -1.0% |
| Crypto | 10 | 0 | — | — | — |
| Weather | 9 | 0 | — | — | — |
| Soccer | 5 | 0 | — | — | — |
| NBA / WNBA | 1 | 0 | — | — | — |

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28 | MIA 85-86 | YES | 5¢ | 14% | Open | — |
| 2026-09-28 | MIA >90 | NO | 58¢ | 69% | Open | — |
| 2026-09-28 | PHIL 69-70 | NO | 69¢ | 81% | Open | — |
| 2026-09-28 | PHIL <65 | YES | 10¢ | 20% | Open | — |
| 2026-09-28 | PHIL 67-68 | NO | 61¢ | 74% | Open | — |
| 2026-09-28 | LAX 76-77 | NO | 62¢ | 77% | Open | — |
| 2026-09-28 | LAX 78-79 | NO | 57¢ | 74% | Open | — |
| 2026-09-28 | LAX <76 | YES | 7¢ | 20% | Open | — |
| 2026-09-28 | DEN 77-78 | YES | 12¢ | 23% | Open | — |
| 2026-09-28 | DEN <73 | NO | 67¢ | 88% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28 | OKC | YES | 9¢ | 21% | Open | — |
| 2026-09-28 | LV | YES | 49¢ | 62% | Open | — |
| 2026-09-28 | DEN | NO | 36¢ | 51% | Open | — |
| 2026-09-28 | DC | YES | 12¢ | 34% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
