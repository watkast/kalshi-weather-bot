# Range-Scalp Bot

*Updated Tue Oct 20 00:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24809 | 21596 | 3213 (31) | 1 | $-7278.04 | -4.7% |
| **+10¢** | 18657 | 14944 | 3713 (46) | 2 | $-6481.31 | -5.5% |
| **+15¢** | 15616 | 11616 | 4000 (70) | 2 | $-5859.75 | -6.0% |
| **+20¢** | 13807 | 9617 | 4190 (88) | 3 | $-5290.79 | -6.1% |
| **+10¢ (15¢ stop)** | 30454 | 30402 | 52 (30) | 0 | $-11411.06 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 00:26 | +10 stop | SOL | UP | 0.51 | 0.12 | -4.15 |
| 10-20 00:26 | +20 | SOL | UP | 0.51 | open |  |
| 10-20 00:26 | +15 | SOL | UP | 0.51 | open |  |
| 10-20 00:26 | +10 | SOL | UP | 0.51 | open |  |
| 10-20 00:26 | +5 | SOL | UP | 0.49 | 0.58 | 0.49 |
| 10-20 00:25 | +10 stop | ZEC | UP | 0.70 | 0.40 | -3.32 |
| 10-20 00:25 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.94 |
| 10-20 00:25 | +20 | HYPE | UP | 0.70 | open |  |
| 10-20 00:25 | +15 | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 10-20 00:25 | +10 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 10-20 00:25 | +5 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 10-20 00:24 | +10 stop | ZEC | DOWN | 0.54 | 0.33 | -2.44 |
| 10-20 00:16 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 10-20 00:16 | +20 | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 10-20 00:16 | +15 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 00:16 | +10 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 00:16 | +5 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 00:16 | +10 stop | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:16 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-20 00:16 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 00:16 | +10 | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 00:16 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-20 00:16 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.86 |
| 10-20 00:16 | +20 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
| 10-20 00:16 | +15 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
| 10-20 00:16 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.86 |
| 10-20 00:16 | +5 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-20 00:15 | +10 stop | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 00:15 | +20 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
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
