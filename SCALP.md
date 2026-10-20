# Range-Scalp Bot

*Updated Tue Oct 20 23:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26383 | 22978 | 3405 (32) | 7 | $-7704.69 | -4.6% |
| **+10¢** | 19852 | 15921 | 3931 (47) | 7 | $-6790.37 | -5.4% |
| **+15¢** | 16614 | 12385 | 4229 (71) | 7 | $-6048.78 | -5.8% |
| **+20¢** | 14699 | 10263 | 4436 (90) | 7 | $-5458.11 | -5.9% |
| **+10¢ (15¢ stop)** | 32316 | 32263 | 53 (30) | 3 | $-11809.37 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 23:36 | +10 stop | HYPE | DOWN | 0.69 | open |  |
| 10-20 23:36 | +5 | ZEC | UP | 0.58 | open |  |
| 10-20 23:36 | +10 stop | ZEC | UP | 0.61 | 0.45 | -1.95 |
| 10-20 23:36 | +15 | ZEC | UP | 0.57 | open |  |
| 10-20 23:36 | +10 | ZEC | UP | 0.57 | open |  |
| 10-20 23:36 | +5 | ZEC | UP | 0.57 | 0.63 | 0.25 |
| 10-20 23:35 | +10 stop | DOGE | UP | 0.67 | open |  |
| 10-20 23:35 | +20 | DOGE | UP | 0.67 | open |  |
| 10-20 23:35 | +15 | DOGE | UP | 0.67 | open |  |
| 10-20 23:35 | +10 | DOGE | UP | 0.67 | open |  |
| 10-20 23:35 | +5 | DOGE | UP | 0.67 | open |  |
| 10-20 23:35 | +15 | XRP | UP | 0.63 | open |  |
| 10-20 23:34 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 10-20 23:34 | +10 stop | ETH | UP | 0.64 | 0.38 | -2.94 |
| 10-20 23:34 | +10 | ETH | UP | 0.64 | open |  |
| 10-20 23:34 | +5 | ETH | UP | 0.64 | open |  |
| 10-20 23:34 | +10 stop | SOL | UP | 0.66 | 0.42 | -2.74 |
| 10-20 23:33 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
| 10-20 23:33 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-20 23:33 | +10 | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-20 23:33 | +5 | DOGE | UP | 0.65 | 0.74 | 0.60 |
| 10-20 23:32 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 10-20 23:32 | +10 stop | XRP | DOWN | 0.60 | 0.45 | -1.85 |
| 10-20 23:32 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-20 23:32 | +5 | XRP | DOWN | 0.60 | open |  |
| 10-20 23:32 | +10 stop | ZEC | UP | 0.61 | 0.72 | 0.80 |
| 10-20 23:32 | +20 | ZEC | UP | 0.61 | open |  |
| 10-20 23:32 | +15 | ZEC | UP | 0.61 | 0.76 | 1.22 |
| 10-20 23:32 | +10 | ZEC | UP | 0.61 | 0.72 | 0.80 |
| 10-20 23:32 | +5 | ZEC | UP | 0.61 | 0.69 | 0.50 |
| 10-20 23:32 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.14 |
| 10-20 23:32 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-20 23:32 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-20 23:32 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-20 23:32 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-20 23:31 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-20 23:31 | +10 | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-20 23:31 | +10 stop | XRP | UP | 0.46 | 0.60 | 1.05 |
| 10-20 23:31 | +20 | XRP | UP | 0.46 | open |  |
| 10-20 23:31 | +15 | XRP | UP | 0.46 | 0.65 | 1.56 |
