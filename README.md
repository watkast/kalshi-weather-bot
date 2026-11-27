# Kalshi Paper Bots — Results

*Updated Fri Nov 27, 11:55 AM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 1084 | 1057 | 36% | -$436.24 | -10.4% | 27 | Losing |
| **Rain** | 325 | 317 | 29% | -$117.43 | -11.3% | 8 | Losing |
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
| 2026-11-27 | LAX 79-80 | YES | 7¢ | 19% | Open | — |
| 2026-11-27 | DEN 60-61 | YES | 15¢ | 26% | Open | — |
| 2026-11-27 | DEN 64-65 | NO | 74¢ | 91% | Open | — |
| 2026-11-27 | PHIL 57-58 | NO | 67¢ | 81% | Open | — |
| 2026-11-27 | PHIL <57 | YES | 53¢ | 69% | Open | — |
| 2026-11-27 | LAX 83-84 | NO | 63¢ | 74% | Open | — |
| 2026-11-27 | DEN 62-63 | NO | 55¢ | 74% | Open | — |
| 2026-11-27 | AUS 66-67 | YES | 6¢ | 26% | Open | — |
| 2026-11-27 | AUS 68-69 | NO | 40¢ | 81% | Open | — |
| 2026-11-27 | AUS 70-71 | NO | 71¢ | 91% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-28 | PIT | YES | 63¢ | 85% | Open | — |
| 2026-11-27 | TTN | NO | 7¢ | 44% | Open | — |
| 2026-11-27 | PHIL | NO | 16¢ | 53% | Open | — |
| 2026-11-27 | NYC | NO | 7¢ | 20% | Open | — |
| 2026-11-27 | MKE | NO | 41¢ | 57% | Open | — |
| 2026-11-27 | EWR | NO | 7¢ | 20% | Open | — |
| 2026-11-27 | DC | NO | 53¢ | 81% | Open | — |
| 2026-11-26 | MKE | YES | 30¢ | 42% | Open | — |
| 2026-11-25 | DC | NO | 79¢ | 92% | YES | -$8.02 |
| 2026-11-25 | CHI | YES | 10¢ | 22% | NO | -$1.07 |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
