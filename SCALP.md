# Range-Scalp Bot

*Updated Tue Oct 06 22:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5580 | 4838 | 742 (9) | 1 | $-1692.23 | -4.8% |
| **+10¢** | 4263 | 3390 | 873 (15) | 2 | $-1603.19 | -6.0% |
| **+15¢** | 3574 | 2649 | 925 (19) | 2 | $-1388.80 | -6.2% |
| **+20¢** | 3194 | 2233 | 961 (26) | 2 | $-1105.88 | -5.5% |
| **+10¢ (15¢ stop)** | 6803 | 6788 | 15 (9) | 0 | $-2435.50 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 22:42 | +10 stop | DOGE | DOWN | 0.63 | 0.80 | 1.40 |
| 10-06 22:41 | +10 stop | HYPE | UP | 0.51 | 0.67 | 1.26 |
| 10-06 22:41 | +10 stop | HYPE | DOWN | 0.60 | 0.44 | -1.95 |
| 10-06 22:41 | +20 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 10-06 22:41 | +15 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 10-06 22:41 | +10 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 10-06 22:41 | +5 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 10-06 22:40 | +10 stop | ZEC | DOWN | 0.66 | 0.32 | -3.72 |
| 10-06 22:40 | +10 stop | XRP | UP | 0.61 | 0.75 | 1.09 |
| 10-06 22:40 | +15 | XRP | UP | 0.61 | 0.79 | 1.51 |
| 10-06 22:40 | +10 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 10-06 22:40 | +5 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 10-06 22:39 | +10 stop | ETH | UP | 0.52 | 0.86 | 3.13 |
| 10-06 22:37 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.93 |
| 10-06 22:37 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-06 22:37 | +10 stop | ZEC | DOWN | 0.68 | 0.51 | -2.04 |
| 10-06 22:37 | +5 | ZEC | DOWN | 0.68 | yes | -6.96 |
| 10-06 22:36 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 10-06 22:36 | +10 stop | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 10-06 22:36 | +10 stop | NEAR | UP | 0.59 | 0.38 | -2.44 |
| 10-06 22:36 | +20 | NEAR | UP | 0.59 | open |  |
| 10-06 22:36 | +15 | NEAR | UP | 0.59 | open |  |
| 10-06 22:36 | +10 | NEAR | UP | 0.59 | open |  |
| 10-06 22:36 | +5 | NEAR | UP | 0.59 | 0.64 | 0.16 |
| 10-06 22:36 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 10-06 22:36 | +10 | XRP | UP | 0.59 | 0.70 | 0.78 |
| 10-06 22:36 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-06 22:35 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-06 22:35 | +10 stop | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-06 22:35 | +10 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-06 22:35 | +5 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-06 22:35 | +5 | ZEC | UP | 0.51 | 0.66 | 1.16 |
| 10-06 22:34 | +10 stop | ETH | UP | 0.68 | 0.50 | -2.14 |
| 10-06 22:34 | +10 | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-06 22:34 | +5 | ETH | UP | 0.68 | 0.86 | 1.55 |
| 10-06 22:34 | +10 stop | SOL | UP | 0.56 | 0.33 | -2.64 |
| 10-06 22:34 | +20 | SOL | UP | 0.56 | open |  |
| 10-06 22:34 | +15 | SOL | UP | 0.56 | open |  |
| 10-06 22:34 | +10 | SOL | UP | 0.56 | open |  |
| 10-06 22:34 | +5 | SOL | UP | 0.57 | open |  |
