# Range-Scalp Bot

*Updated Tue Oct 20 00:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24807 | 21594 | 3213 (31) | 1 | $-7279.37 | -4.7% |
| **+10¢** | 18656 | 14943 | 3713 (46) | 1 | $-6482.15 | -5.5% |
| **+15¢** | 15615 | 11615 | 4000 (70) | 1 | $-5861.01 | -6.0% |
| **+20¢** | 13805 | 9615 | 4190 (88) | 3 | $-5294.44 | -6.1% |
| **+10¢ (15¢ stop)** | 30450 | 30398 | 52 (30) | 0 | $-11402.09 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 00:16 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 10-20 00:16 | +20 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-20 00:16 | +15 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 00:16 | +10 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 00:16 | +5 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 00:16 | +10 stop | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:16 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-20 00:16 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 00:16 | +10 | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:16 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-20 00:16 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.86 |
| 10-20 00:16 | +20 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
| 10-20 00:16 | +15 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
| 10-20 00:16 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.86 |
| 10-20 00:16 | +5 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-20 00:15 | +10 stop | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 00:15 | +20 | HYPE | DOWN | 0.59 | open |  |
| 10-20 00:15 | +15 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 00:15 | +10 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 00:15 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-20 00:15 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.74 |
| 10-20 00:15 | +20 | ZEC | UP | 0.64 | open |  |
| 10-20 00:15 | +15 | ZEC | UP | 0.64 | open |  |
| 10-20 00:15 | +10 | ZEC | UP | 0.64 | open |  |
| 10-20 00:15 | +5 | ZEC | UP | 0.64 | open |  |
| 10-20 00:15 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.73 |
| 10-20 00:15 | +20 | SOL | DOWN | 0.59 | 0.81 | 1.92 |
| 10-20 00:15 | +15 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 10-20 00:15 | +10 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-20 00:15 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-20 00:05 | +10 stop | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-20 00:05 | +10 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 10-20 00:05 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-20 00:05 | +10 stop | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:05 | +15 | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-20 00:05 | +10 | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:04 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-20 00:04 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-20 00:04 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 00:04 | +10 stop | NEAR | UP | 0.41 | 0.54 | 0.95 |
