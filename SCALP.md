# Range-Scalp Bot

*Updated Thu Nov 26 21:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72913 | 63642 | 9271 (158) | 2 | $-19409.10 | -4.2% |
| **+10¢** | 54355 | 43532 | 10823 (203) | 3 | $-17992.44 | -5.3% |
| **+15¢** | 45518 | 33859 | 11659 (261) | 3 | $-16083.33 | -5.6% |
| **+20¢** | 40507 | 28231 | 12276 (327) | 2 | $-14474.91 | -5.7% |
| **+10¢ (15¢ stop)** | 88788 | 88579 | 209 (128) | 0 | $-32729.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 21:12 | +10 stop | ETH | DOWN | 0.64 | 0.44 | -2.35 |
| 11-26 21:12 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-26 21:12 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-26 21:12 | +5 | ETH | DOWN | 0.64 | open |  |
| 11-26 21:12 | +10 stop | XRP | DOWN | 0.52 | 0.21 | -3.40 |
| 11-26 21:10 | +15 | XRP | UP | 0.71 | 0.87 | 1.40 |
| 11-26 21:10 | +5 | NEAR | UP | 0.65 | 0.74 | 0.60 |
| 11-26 21:10 | +5 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 11-26 21:10 | +10 stop | DOGE | UP | 0.65 | 0.48 | -2.02 |
| 11-26 21:09 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 11-26 21:09 | +10 | XRP | UP | 0.69 | 0.81 | 0.94 |
| 11-26 21:09 | +10 stop | NEAR | UP | 0.58 | 0.41 | -2.05 |
| 11-26 21:08 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-26 21:07 | +10 stop | XRP | UP | 0.53 | 0.64 | 0.75 |
| 11-26 21:07 | +15 | XRP | UP | 0.53 | 0.68 | 1.16 |
| 11-26 21:07 | +10 | XRP | UP | 0.53 | 0.64 | 0.75 |
| 11-26 21:07 | +5 | XRP | UP | 0.53 | 0.60 | 0.35 |
| 11-26 21:07 | +5 | NEAR | UP | 0.52 | 0.59 | 0.35 |
| 11-26 21:06 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
| 11-26 21:05 | +10 stop | HYPE | UP | 0.67 | 0.80 | 1.02 |
| 11-26 21:05 | +10 stop | DOGE | UP | 0.61 | 0.74 | 1.01 |
| 11-26 21:05 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 11-26 21:04 | +10 stop | ETH | UP | 0.68 | 0.81 | 1.03 |
| 11-26 21:04 | +20 | ETH | UP | 0.68 | 0.93 | 2.25 |
| 11-26 21:04 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 11-26 21:04 | +10 | ETH | UP | 0.68 | 0.81 | 1.03 |
| 11-26 21:04 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 11-26 21:04 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.15 |
| 11-26 21:04 | +5 | ZEC | UP | 0.61 | 0.70 | 0.53 |
| 11-26 21:03 | +10 stop | XRP | UP | 0.67 | 0.42 | -2.84 |
| 11-26 21:03 | +10 | XRP | UP | 0.64 | 0.74 | 0.69 |
| 11-26 21:03 | +5 | XRP | UP | 0.64 | 0.74 | 0.69 |
| 11-26 21:03 | +10 stop | DOGE | UP | 0.61 | 0.44 | -2.07 |
| 11-26 21:03 | +20 | NEAR | UP | 0.68 | open |  |
| 11-26 21:03 | +15 | NEAR | UP | 0.68 | open |  |
| 11-26 21:03 | +10 | NEAR | UP | 0.68 | open |  |
| 11-26 21:03 | +5 | NEAR | UP | 0.68 | 0.73 | 0.24 |
| 11-26 21:03 | +10 stop | ZEC | UP | 0.57 | 0.70 | 0.97 |
| 11-26 21:03 | +20 | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 11-26 21:03 | +15 | ZEC | UP | 0.57 | 0.74 | 1.38 |
