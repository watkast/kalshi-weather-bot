# Range-Scalp Bot

*Updated Tue Nov 03 05:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45632 | 39730 | 5902 (69) | 1 | $-13182.52 | -4.6% |
| **+10¢** | 34065 | 27225 | 6840 (91) | 1 | $-12080.40 | -5.6% |
| **+15¢** | 28508 | 21149 | 7359 (119) | 1 | $-11081.50 | -6.2% |
| **+20¢** | 25319 | 17609 | 7710 (154) | 4 | $-9859.65 | -6.2% |
| **+10¢ (15¢ stop)** | 55682 | 55593 | 89 (53) | 1 | $-20962.59 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 05:32 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 11-03 05:32 | +10 stop | ZEC | DOWN | 0.67 | 0.93 | 2.41 |
| 11-03 05:32 | +20 | ZEC | DOWN | 0.68 | 0.93 | 2.31 |
| 11-03 05:32 | +15 | ZEC | DOWN | 0.68 | 0.93 | 2.31 |
| 11-03 05:32 | +10 | ZEC | DOWN | 0.68 | 0.93 | 2.31 |
| 11-03 05:32 | +5 | ZEC | DOWN | 0.67 | 0.93 | 2.41 |
| 11-03 05:31 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 05:31 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-03 05:31 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 05:31 | +10 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-03 05:31 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-03 05:31 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 11-03 05:31 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-03 05:31 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-03 05:31 | +10 | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 11-03 05:31 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-03 05:31 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 11-03 05:31 | +20 | BNB | DOWN | 0.55 | open |  |
| 11-03 05:31 | +15 | BNB | DOWN | 0.55 | 0.73 | 1.48 |
| 11-03 05:31 | +10 | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 11-03 05:31 | +5 | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 11-03 05:31 | +10 stop | ETH | DOWN | 0.61 | 0.81 | 1.72 |
| 11-03 05:31 | +20 | ETH | DOWN | 0.61 | 0.81 | 1.72 |
| 11-03 05:31 | +15 | ETH | DOWN | 0.61 | 0.81 | 1.72 |
| 11-03 05:31 | +10 | ETH | DOWN | 0.61 | 0.81 | 1.72 |
| 11-03 05:31 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.41 |
| 11-03 05:31 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-03 05:31 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-03 05:31 | +15 | SOL | DOWN | 0.58 | 0.75 | 1.38 |
| 11-03 05:31 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 05:31 | +5 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 05:30 | +10 stop | NEAR | UP | 0.61 | 0.42 | -2.25 |
| 11-03 05:30 | +20 | NEAR | UP | 0.61 | open |  |
| 11-03 05:30 | +15 | NEAR | UP | 0.61 | open |  |
| 11-03 05:30 | +10 | NEAR | UP | 0.61 | open |  |
| 11-03 05:30 | +5 | NEAR | UP | 0.61 | open |  |
| 11-03 05:27 | +10 stop | ETH | UP | 0.15 | 0.66 | 4.85 |
| 11-03 05:27 | +20 | ETH | UP | 0.15 | 0.66 | 4.85 |
| 11-03 05:27 | +15 | ETH | UP | 0.15 | 0.66 | 4.85 |
| 11-03 05:27 | +10 | ETH | UP | 0.15 | 0.66 | 4.85 |
