# Range-Scalp Bot

*Updated Wed Nov 11 22:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56284 | 49085 | 7199 (95) | 5 | $-15377.28 | -4.3% |
| **+10¢** | 42058 | 33656 | 8402 (125) | 5 | $-14349.04 | -5.4% |
| **+15¢** | 35268 | 26214 | 9054 (159) | 5 | $-13028.70 | -5.9% |
| **+20¢** | 31420 | 21920 | 9500 (209) | 5 | $-11384.63 | -5.8% |
| **+10¢ (15¢ stop)** | 68596 | 68475 | 121 (73) | 3 | $-25299.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 22:21 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 11-11 22:21 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-11 22:21 | +10 | NEAR | UP | 0.58 | open |  |
| 11-11 22:21 | +5 | NEAR | UP | 0.58 | open |  |
| 11-11 22:20 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-11 22:19 | +5 | BTC | UP | 0.62 | open |  |
| 11-11 22:19 | +5 | XRP | UP | 0.66 | open |  |
| 11-11 22:18 | +10 stop | XRP | UP | 0.67 | 0.47 | -2.34 |
| 11-11 22:18 | +20 | XRP | UP | 0.67 | open |  |
| 11-11 22:18 | +15 | XRP | UP | 0.67 | open |  |
| 11-11 22:18 | +10 | XRP | UP | 0.67 | open |  |
| 11-11 22:18 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-11 22:17 | +10 stop | BNB | UP | 0.68 | 0.86 | 1.55 |
| 11-11 22:16 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-11 22:16 | +20 | NEAR | UP | 0.70 | open |  |
| 11-11 22:16 | +15 | NEAR | UP | 0.70 | open |  |
| 11-11 22:16 | +10 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-11 22:16 | +5 | NEAR | UP | 0.71 | 0.76 | 0.22 |
| 11-11 22:16 | +10 stop | BTC | UP | 0.69 | 0.53 | -1.93 |
| 11-11 22:16 | +20 | BTC | UP | 0.69 | open |  |
| 11-11 22:16 | +15 | BTC | UP | 0.69 | open |  |
| 11-11 22:16 | +10 | BTC | UP | 0.69 | open |  |
| 11-11 22:16 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 11-11 22:16 | +10 | ZEC | UP | 0.71 | 0.95 | 2.18 |
| 11-11 22:16 | +5 | ZEC | UP | 0.71 | 0.79 | 0.53 |
| 11-11 22:16 | +10 stop | DOGE | DOWN | 0.50 | 0.29 | -2.39 |
| 11-11 22:16 | +20 | DOGE | DOWN | 0.48 | open |  |
| 11-11 22:16 | +15 | DOGE | DOWN | 0.50 | open |  |
| 11-11 22:16 | +10 | DOGE | DOWN | 0.50 | open |  |
| 11-11 22:16 | +5 | DOGE | DOWN | 0.50 | open |  |
| 11-11 22:15 | +10 stop | BNB | DOWN | 0.65 | 0.40 | -2.83 |
| 11-11 22:15 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-11 22:15 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-11 22:15 | +10 | BNB | DOWN | 0.65 | open |  |
| 11-11 22:15 | +5 | BNB | DOWN | 0.65 | open |  |
| 11-11 22:07 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-11 22:06 | +10 stop | SOL | DOWN | 0.49 | 0.33 | -1.94 |
| 11-11 22:06 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 11-11 22:05 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-11 22:05 | +20 | BTC | UP | 0.60 | 0.82 | 1.92 |
