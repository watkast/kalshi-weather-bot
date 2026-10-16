# Range-Scalp Bot

*Updated Fri Oct 16 00:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18382 | 15962 | 2420 (28) | 6 | $-5613.23 | -4.8% |
| **+10¢** | 13862 | 11062 | 2800 (40) | 4 | $-5075.33 | -5.8% |
| **+15¢** | 11625 | 8614 | 3011 (59) | 5 | $-4579.67 | -6.3% |
| **+20¢** | 10326 | 7178 | 3148 (78) | 6 | $-3974.80 | -6.1% |
| **+10¢ (15¢ stop)** | 22602 | 22552 | 50 (29) | 2 | $-8734.91 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 00:06 | +10 stop | ETH | UP | 0.65 | open |  |
| 10-16 00:06 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-16 00:06 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-16 00:06 | +15 | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-16 00:06 | +5 | NEAR | DOWN | 0.56 | 0.65 | 0.56 |
| 10-16 00:04 | +10 stop | SOL | UP | 0.57 | 0.69 | 0.87 |
| 10-16 00:04 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 10-16 00:04 | +20 | BNB | UP | 0.64 | open |  |
| 10-16 00:04 | +15 | BNB | UP | 0.64 | open |  |
| 10-16 00:04 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 10-16 00:04 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-16 00:04 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-16 00:04 | +10 | DOGE | DOWN | 0.67 | open |  |
| 10-16 00:04 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.42 |
| 10-16 00:04 | +10 stop | ZEC | DOWN | 0.58 | 0.32 | -2.94 |
| 10-16 00:04 | +5 | ZEC | DOWN | 0.58 | open |  |
| 10-16 00:03 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.06 |
| 10-16 00:03 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 10-16 00:03 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-16 00:03 | +15 | ETH | DOWN | 0.67 | open |  |
| 10-16 00:03 | +10 | ETH | DOWN | 0.67 | open |  |
| 10-16 00:03 | +5 | ETH | DOWN | 0.67 | open |  |
| 10-16 00:03 | +5 | NEAR | DOWN | 0.59 | 0.68 | 0.57 |
| 10-16 00:03 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.21 |
| 10-16 00:03 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-16 00:03 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-16 00:03 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-16 00:02 | +10 stop | BNB | DOWN | 0.70 | 0.49 | -2.43 |
| 10-16 00:02 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-16 00:02 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-16 00:02 | +5 | NEAR | DOWN | 0.58 | 0.63 | 0.15 |
| 10-16 00:02 | +5 | ZEC | DOWN | 0.58 | 0.66 | 0.46 |
| 10-16 00:02 | +10 stop | ZEC | UP | 0.46 | 0.30 | -1.95 |
| 10-16 00:02 | +20 | ZEC | UP | 0.46 | 0.78 | 2.88 |
| 10-16 00:02 | +15 | ZEC | UP | 0.47 | 0.66 | 1.56 |
| 10-16 00:02 | +10 | ZEC | UP | 0.47 | 0.66 | 1.56 |
| 10-16 00:02 | +5 | ZEC | UP | 0.47 | 0.55 | 0.44 |
| 10-16 00:02 | +10 stop | BTC | UP | 0.57 | 0.70 | 0.97 |
| 10-16 00:02 | +10 | BTC | UP | 0.57 | 0.70 | 0.97 |
| 10-16 00:02 | +5 | BTC | UP | 0.57 | 0.70 | 0.97 |
