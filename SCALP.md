# Range-Scalp Bot

*Updated Tue Oct 20 13:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25670 | 22355 | 3315 (31) | 0 | $-7505.62 | -4.6% |
| **+10¢** | 19316 | 15488 | 3828 (46) | 0 | $-6627.68 | -5.5% |
| **+15¢** | 16172 | 12050 | 4122 (70) | 0 | $-5933.21 | -5.8% |
| **+20¢** | 14306 | 9992 | 4314 (88) | 1 | $-5285.70 | -5.9% |
| **+10¢ (15¢ stop)** | 31496 | 31443 | 53 (30) | 0 | $-11616.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 13:01 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 13:01 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-20 13:01 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 10-20 13:01 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 13:01 | +5 | SOL | DOWN | 0.67 | 0.75 | 0.50 |
| 10-20 13:01 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-20 13:01 | +20 | ZEC | DOWN | 0.66 | 0.91 | 2.28 |
| 10-20 13:01 | +15 | ZEC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 13:01 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-20 13:01 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-20 13:01 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 13:01 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.85 |
| 10-20 13:01 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-20 13:01 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 13:01 | +5 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-20 13:01 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-20 13:01 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-20 13:01 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-20 13:01 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.22 |
| 10-20 13:01 | +5 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-20 13:01 | +10 stop | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-20 13:01 | +20 | NEAR | DOWN | 0.69 | 0.90 | 1.88 |
| 10-20 13:01 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-20 13:01 | +10 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-20 13:01 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 12:57 | +10 stop | BTC | DOWN | 0.47 | 0.65 | 1.46 |
| 10-20 12:57 | +5 | BTC | DOWN | 0.47 | 0.65 | 1.46 |
| 10-20 12:56 | +10 stop | XRP | UP | 0.59 | 0.16 | -4.54 |
| 10-20 12:56 | +20 | XRP | UP | 0.59 | no | -6.04 |
| 10-20 12:56 | +5 | XRP | UP | 0.58 | no | -5.98 |
| 10-20 12:55 | +10 stop | NEAR | UP | 0.33 | 0.55 | 1.86 |
| 10-20 12:54 | +5 | BTC | UP | 0.49 | 0.58 | 0.54 |
| 10-20 12:54 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 10-20 12:54 | +10 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 12:53 | +10 stop | BTC | UP | 0.53 | 0.38 | -1.85 |
| 10-20 12:53 | +5 | BTC | UP | 0.53 | 0.61 | 0.45 |
| 10-20 12:53 | +10 stop | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-20 12:53 | +20 | DOGE | DOWN | 0.65 | 0.91 | 2.32 |
| 10-20 12:53 | +15 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-20 12:53 | +10 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
