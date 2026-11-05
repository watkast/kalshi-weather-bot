# Kalshi Paper Bots — Results

*Updated Thu Nov 5, 2:59 PM MT. Paper money only — no real trades. Study pages refresh about every 10 minutes; this page every few hours.*

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
| **Temperature** | 736 | 700 | 36% | -$366.38 | -12.8% | 36 | Losing |
| **Rain** | 208 | 194 | 32% | -$13.89 | -2.2% | 14 | Break-even |
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
| 2026-11-06 | PHIL 69-70 | NO | 49¢ | 74% | Open | — |
| 2026-11-06 | LAX 79-80 | YES | 11¢ | 23% | Open | — |
| 2026-11-06 | LAX 81-82 | NO | 48¢ | 74% | Open | — |
| 2026-11-06 | DEN 54-55 | YES | 5¢ | 19% | Open | — |
| 2026-11-06 | DEN 58-59 | NO | 55¢ | 77% | Open | — |
| 2026-11-06 | AUS 75-76 | NO | 56¢ | 74% | Open | — |
| 2026-11-06 | AUS <73 | YES | 7¢ | 20% | Open | — |
| 2026-11-06 | MIA 86-87 | NO | 26¢ | 74% | Open | — |
| 2026-11-06 | CHI 48-49 | NO | 58¢ | 77% | Open | — |
| 2026-11-06 | CHI 50-51 | NO | 60¢ | 74% | Open | — |

## Latest rain bets

| Day | Market | Bet | Paid | Bot's odds | Outcome | P&L |
|---|---|---|---|---|---|---|
| 2026-11-06 | CMH | YES | 24¢ | 36% | Open | — |
| 2026-11-05 | SEA | NO | 58¢ | 79% | Open | — |
| 2026-11-05 | MKE | NO | 34¢ | 52% | Open | — |
| 2026-11-05 | BOS | NO | 61¢ | 77% | Open | — |
| 2026-11-05 | ATL | NO | 31¢ | 52% | Open | — |
| 2026-11-05 | TTN | NO | 15¢ | 35% | Open | — |
| 2026-11-05 | PIT | NO | 16¢ | 27% | Open | — |
| 2026-11-05 | PHIL | NO | 22¢ | 37% | Open | — |
| 2026-11-05 | OKC | NO | 24¢ | 43% | Open | — |
| 2026-11-05 | NYC | NO | 22¢ | 52% | Open | — |

## The bots

| Bot | What it does | Full log |
|---|---|---|
| Temperature | NWS forecast high vs Kalshi daily high brackets (7 cities) | [trades.csv](trades.csv) |
| Rain | NWS hourly rain chance vs Kalshi "Will it rain?" (28 cities) | [rain_trades.csv](rain_trades.csv) |
| Longshot fade | Bets NO on liquid long shots (YES ≤ 10¢) closing within a week (NFL dropped Sep 27) | [longshot_trades.csv](longshot_trades.csv) |

Retired: the first MLB / NFL / NHL 1¢ bots (replaced by the 1¢ Study) — [mlb_trades.csv](mlb_trades.csv), [nfl_trades.csv](nfl_trades.csv), [nhl_trades.csv](nhl_trades.csv).

Run everything now: **Actions → paper-trade → Run workflow**.
