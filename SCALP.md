# Range-Scalp Bot

*Updated Sat Oct 24 03:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31360 | 27329 | 4031 (40) | 5 | $-9055.20 | -4.6% |
| **+10¢** | 23462 | 18806 | 4656 (58) | 5 | $-8045.51 | -5.5% |
| **+15¢** | 19636 | 14633 | 5003 (81) | 5 | $-7180.80 | -5.8% |
| **+20¢** | 17395 | 12155 | 5240 (103) | 7 | $-6407.13 | -5.9% |
| **+10¢ (15¢ stop)** | 38486 | 38427 | 59 (32) | 3 | $-14653.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 03:23 | +10 stop | DOGE | UP | 0.57 | open |  |
| 10-24 03:23 | +5 | DOGE | UP | 0.57 | open |  |
| 10-24 03:23 | +10 stop | NEAR | UP | 0.70 | open |  |
| 10-24 03:22 | +5 | DOGE | DOWN | 0.52 | 0.67 | 1.17 |
| 10-24 03:22 | +5 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 03:21 | +10 stop | ZEC | DOWN | 0.69 | 0.46 | -2.63 |
| 10-24 03:21 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-24 03:21 | +10 stop | NEAR | UP | 0.47 | 0.70 | 1.97 |
| 10-24 03:21 | +10 stop | XRP | UP | 0.54 | 0.65 | 0.76 |
| 10-24 03:20 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 10-24 03:20 | +10 stop | ETH | UP | 0.71 | 0.82 | 0.84 |
| 10-24 03:19 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-24 03:19 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 10-24 03:19 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 03:19 | +15 | HYPE | DOWN | 0.60 | open |  |
| 10-24 03:19 | +10 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 03:19 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-24 03:19 | +5 | BNB | UP | 0.58 | 0.65 | 0.36 |
| 10-24 03:17 | +10 stop | ZEC | DOWN | 0.63 | 0.44 | -2.25 |
| 10-24 03:17 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-24 03:17 | +10 stop | ETH | DOWN | 0.54 | 0.36 | -2.15 |
| 10-24 03:17 | +10 stop | XRP | DOWN | 0.60 | 0.38 | -2.54 |
| 10-24 03:17 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.28 |
| 10-24 03:17 | +10 stop | BTC | DOWN | 0.55 | 0.38 | -2.05 |
| 10-24 03:17 | +10 | BTC | DOWN | 0.55 | open |  |
| 10-24 03:17 | +5 | BTC | DOWN | 0.55 | open |  |
| 10-24 03:17 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-24 03:17 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 10-24 03:17 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-24 03:17 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-24 03:17 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-24 03:17 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-24 03:17 | +10 stop | NEAR | DOWN | 0.66 | 0.48 | -2.14 |
| 10-24 03:17 | +10 stop | DOGE | DOWN | 0.66 | 0.36 | -3.33 |
| 10-24 03:17 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-24 03:17 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-24 03:17 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-24 03:17 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-24 03:17 | +10 stop | BNB | UP | 0.53 | 0.65 | 0.86 |
| 10-24 03:17 | +20 | BNB | UP | 0.53 | 0.74 | 1.78 |
