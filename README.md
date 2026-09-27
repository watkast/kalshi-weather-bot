# Kalshi Paper Bots — Results

*Updated Sun Sep 27, 4:21 PM MT. Paper money only — no real trades. Refreshes about every 15 minutes.*

## Scoreboard

| Bot | Bets | Settled | Win rate | Paper P&L | Return | Open | Verdict |
|---|---|---|---|---|---|---|---|
| **Temperature** | 14 | 0 | — | — | — | 14 | Too early |
| **Rain** | 4 | 0 | — | — | — | 4 | Too early |
| **Longshot fade** | 240 | 67 | 94% | -$5.33 | -0.8% | 173 | Break-even |
| **MLB 1¢** | 11 | 11 | 0% | -$11.77 | -100.0% | 0 | Too early |
| **NFL 1¢** | 0 | 0 | — | — | — | 0 | Too early |
| **NHL 1¢** | 0 | 0 | — | — | — | 0 | Too early |

*Return = profit ÷ money risked on settled bets. Verdicts need at least 20 settled bets.*

## Longshot fade by category

| Category | Bets | Settled | Win rate | Paper P&L | Return |
|---|---|---|---|---|---|
| NFL | 127 | 16 | 94% | -$2.60 | -1.7% |
| MLB | 48 | 48 | 94% | -$4.39 | -1.0% |
| Other | 44 | 3 | 100% | $1.66 | +5.9% |
| Crypto | 9 | 0 | — | — | — |
| Weather | 7 | 0 | — | — | — |
| Soccer | 4 | 0 | — | — | — |
| NBA / WNBA | 1 | 0 | — | — | — |

## MLB 1¢ bets

| Date | Team | Entry situation | Highest price after | Result | P&L |
|---|---|---|---|---|---|
| 2026-09-27 | LAA | Bottom 8 · LAA 3-7 SEA | 1¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | SF | Bottom 10 · LAD 5-1 SF | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | ARI | Bottom 8 · AZ 4-9 SD | 1¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | BOS | Top 9 · CHC 6-2 BOS | 1¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | DET | Bottom 9 · PIT 4-2 DET | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | TEX | Top 9 · TEX 4-6 MIN | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | STL | Top 9 · STL 4-6 MIL | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | CIN | Top 9 · CIN 1-5 TOR | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | CLE | Top 9 · CLE 2-3 KC | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | ATH | Top 7 · HOU 7-0 ATH | 0¢ | ❌ Lost | -$1.07 |
| 2026-09-27 | TB | Top 9 · TB 3-7 PHI | 0¢ | ❌ Lost | -$1.07 |

*Highest price after = best price you could have sold at before the end. Minute-by-minute prices are in the price log files.*

## NFL 1¢ bets

*No 1¢ moments caught yet.*

## NHL 1¢ bets

*No 1¢ moments caught yet.*

## Latest temperature bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28 | MIA >90 | NO | 58¢ | 69% | Open | — |
| 2026-09-28 | PHIL 69-70 | NO | 69¢ | 81% | Open | — |
| 2026-09-28 | PHIL <65 | YES | 10¢ | 20% | Open | — |
| 2026-09-28 | PHIL 67-68 | NO | 61¢ | 74% | Open | — |
| 2026-09-28 | LAX 76-77 | NO | 62¢ | 77% | Open | — |
| 2026-09-28 | LAX 78-79 | NO | 57¢ | 74% | Open | — |
| 2026-09-28 | LAX <76 | YES | 7¢ | 20% | Open | — |
| 2026-09-28 | DEN 77-78 | YES | 12¢ | 23% | Open | — |
| 2026-09-28 | DEN <73 | NO | 67¢ | 88% | Open | — |
| 2026-09-28 | AUS 97-98 | NO | 47¢ | 77% | Open | — |

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
| MLB 1¢ | Buys a team at 1¢ mid-game, holds to the final out | [mlb_trades.csv](mlb_trades.csv) |
| NFL 1¢ | Same, NFL | [nfl_trades.csv](nfl_trades.csv) |
| NHL 1¢ | Same, NHL | [nhl_trades.csv](nhl_trades.csv) |

Run everything now: **Actions → paper-trade → Run workflow**.
