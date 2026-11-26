# Range-Scalp Bot

*Updated Thu Nov 26 04:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72339 | 63143 | 9196 (158) | 1 | $-19237.86 | -4.2% |
| **+10¢** | 53957 | 43220 | 10737 (203) | 1 | $-17807.34 | -5.3% |
| **+15¢** | 45177 | 33612 | 11565 (260) | 1 | $-15902.29 | -5.6% |
| **+20¢** | 40216 | 28034 | 12182 (326) | 2 | $-14320.02 | -5.7% |
| **+10¢ (15¢ stop)** | 88072 | 87863 | 209 (128) | 1 | $-32302.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 04:08 | +10 stop | DOGE | UP | 0.63 | open |  |
| 11-26 04:08 | +20 | DOGE | UP | 0.63 | open |  |
| 11-26 04:08 | +15 | DOGE | UP | 0.63 | open |  |
| 11-26 04:08 | +10 | DOGE | UP | 0.62 | open |  |
| 11-26 04:08 | +5 | DOGE | UP | 0.62 | open |  |
| 11-26 04:02 | +5 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-26 04:01 | +10 stop | ZEC | UP | 0.54 | 0.70 | 1.27 |
| 11-26 04:01 | +20 | ZEC | UP | 0.54 | 0.78 | 2.09 |
| 11-26 04:01 | +15 | ZEC | UP | 0.54 | 0.70 | 1.27 |
| 11-26 04:01 | +10 | ZEC | UP | 0.54 | 0.70 | 1.27 |
| 11-26 04:01 | +5 | ZEC | UP | 0.56 | 0.63 | 0.35 |
| 11-26 04:01 | +10 stop | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-26 04:01 | +15 | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 11-26 04:01 | +10 | NEAR | UP | 0.70 | 0.83 | 1.05 |
| 11-26 04:01 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-26 04:01 | +10 stop | NEAR | DOWN | 0.40 | 0.55 | 1.15 |
| 11-26 04:01 | +20 | NEAR | DOWN | 0.40 | open |  |
| 11-26 04:01 | +15 | NEAR | DOWN | 0.40 | 0.55 | 1.15 |
| 11-26 04:01 | +10 | NEAR | DOWN | 0.40 | 0.55 | 1.15 |
| 11-26 04:01 | +5 | NEAR | DOWN | 0.40 | 0.55 | 1.15 |
| 11-26 03:58 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.05 |
| 11-26 03:58 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 11-26 03:58 | +10 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 11-26 03:58 | +5 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 11-26 03:57 | +10 stop | ZEC | DOWN | 0.54 | 0.22 | -3.51 |
| 11-26 03:56 | +10 stop | NEAR | UP | 0.49 | 0.87 | 3.51 |
| 11-26 03:56 | +20 | NEAR | UP | 0.49 | 0.87 | 3.54 |
| 11-26 03:56 | +15 | NEAR | UP | 0.49 | 0.87 | 3.54 |
| 11-26 03:56 | +10 | NEAR | UP | 0.49 | 0.87 | 3.54 |
| 11-26 03:56 | +5 | NEAR | UP | 0.49 | 0.56 | 0.34 |
| 11-26 03:56 | +10 stop | SOL | UP | 0.54 | 0.33 | -2.44 |
| 11-26 03:56 | +20 | SOL | UP | 0.61 | no | -6.27 |
| 11-26 03:56 | +15 | SOL | UP | 0.61 | no | -6.27 |
| 11-26 03:56 | +10 | SOL | UP | 0.61 | no | -6.27 |
| 11-26 03:56 | +5 | SOL | UP | 0.61 | no | -6.27 |
| 11-26 03:55 | +10 | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 11-26 03:55 | +5 | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 11-26 03:52 | +10 stop | ZEC | UP | 0.69 | 0.51 | -2.13 |
| 11-26 03:51 | +10 stop | HYPE | UP | 0.68 | 0.82 | 1.13 |
| 11-26 03:51 | +20 | HYPE | UP | 0.66 | 0.86 | 1.75 |
