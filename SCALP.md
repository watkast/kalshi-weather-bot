# Range-Scalp Bot

*Updated Tue Oct 20 04:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25118 | 21864 | 3254 (31) | 3 | $-7382.00 | -4.7% |
| **+10¢** | 18896 | 15136 | 3760 (46) | 4 | $-6566.27 | -5.5% |
| **+15¢** | 15814 | 11766 | 4048 (70) | 4 | $-5915.43 | -6.0% |
| **+20¢** | 13982 | 9744 | 4238 (88) | 4 | $-5323.44 | -6.1% |
| **+10¢ (15¢ stop)** | 30823 | 30771 | 52 (30) | 0 | $-11461.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 04:57 | +10 stop | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-20 04:57 | +10 | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-20 04:57 | +5 | BTC | UP | 0.59 | 0.67 | 0.47 |
| 10-20 04:56 | +10 stop | HYPE | UP | 0.58 | 0.23 | -3.81 |
| 10-20 04:56 | +10 stop | ETH | DOWN | 0.42 | 0.62 | 1.65 |
| 10-20 04:56 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-20 04:56 | +15 | BTC | UP | 0.69 | 0.91 | 2.01 |
| 10-20 04:56 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-20 04:56 | +5 | BTC | UP | 0.69 | 0.78 | 0.62 |
| 10-20 04:55 | +10 stop | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 04:55 | +5 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 04:55 | +10 stop | ETH | UP | 0.61 | 0.35 | -2.93 |
| 10-20 04:55 | +5 | ETH | UP | 0.61 | 0.86 | 2.24 |
| 10-20 04:55 | +10 stop | HYPE | DOWN | 0.58 | 0.34 | -2.74 |
| 10-20 04:54 | +5 | SOL | UP | 0.64 | 0.75 | 0.79 |
| 10-20 04:53 | +10 stop | BTC | DOWN | 0.70 | 0.40 | -3.32 |
| 10-20 04:52 | +10 stop | HYPE | DOWN | 0.65 | 0.84 | 1.60 |
| 10-20 04:52 | +10 stop | SOL | DOWN | 0.66 | 0.42 | -2.74 |
| 10-20 04:50 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.35 |
| 10-20 04:50 | +10 stop | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 10-20 04:50 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-20 04:50 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-20 04:50 | +10 stop | BNB | UP | 0.55 | 0.69 | 1.07 |
| 10-20 04:49 | +10 stop | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 10-20 04:49 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 10-20 04:49 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-20 04:49 | +10 stop | XRP | DOWN | 0.71 | 0.85 | 1.16 |
| 10-20 04:49 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-20 04:49 | +10 stop | HYPE | DOWN | 0.67 | 0.46 | -2.44 |
| 10-20 04:48 | +5 | ETH | UP | 0.45 | 0.56 | 0.74 |
| 10-20 04:48 | +5 | SOL | UP | 0.59 | 0.66 | 0.37 |
| 10-20 04:48 | +10 stop | NEAR | DOWN | 0.52 | 0.68 | 1.26 |
| 10-20 04:47 | +10 | SOL | UP | 0.59 | 0.75 | 1.29 |
| 10-20 04:47 | +5 | SOL | UP | 0.59 | 0.65 | 0.27 |
| 10-20 04:47 | +10 stop | XRP | UP | 0.56 | 0.36 | -2.35 |
| 10-20 04:47 | +10 | XRP | UP | 0.56 | open |  |
| 10-20 04:47 | +5 | XRP | UP | 0.56 | 0.62 | 0.25 |
| 10-20 04:47 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 10-20 04:47 | +20 | ETH | UP | 0.62 | 0.86 | 2.14 |
| 10-20 04:47 | +15 | ETH | UP | 0.62 | 0.86 | 2.14 |
