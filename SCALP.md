# Range-Scalp Bot

*Updated Sun Oct 18 12:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22560 | 19640 | 2920 (29) | 7 | $-6579.94 | -4.6% |
| **+10¢** | 16970 | 13596 | 3374 (43) | 8 | $-5858.51 | -5.5% |
| **+15¢** | 14209 | 10567 | 3642 (63) | 7 | $-5367.40 | -6.0% |
| **+20¢** | 12576 | 8763 | 3813 (81) | 8 | $-4788.44 | -6.1% |
| **+10¢ (15¢ stop)** | 27737 | 27687 | 50 (29) | 4 | $-10589.04 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 12:22 | +5 | SOL | DOWN | 0.58 | open |  |
| 10-18 12:22 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 10-18 12:21 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 10-18 12:21 | +10 stop | NEAR | UP | 0.51 | 0.36 | -1.85 |
| 10-18 12:21 | +10 stop | DOGE | UP | 0.66 | open |  |
| 10-18 12:21 | +10 stop | BNB | UP | 0.60 | 0.30 | -3.32 |
| 10-18 12:20 | +10 stop | XRP | UP | 0.65 | open |  |
| 10-18 12:20 | +10 stop | BNB | UP | 0.64 | 0.46 | -2.15 |
| 10-18 12:20 | +10 | BNB | UP | 0.64 | open |  |
| 10-18 12:19 | +5 | BNB | UP | 0.62 | open |  |
| 10-18 12:19 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 10-18 12:19 | +10 stop | SOL | DOWN | 0.50 | open |  |
| 10-18 12:19 | +10 stop | DOGE | DOWN | 0.55 | 0.37 | -2.15 |
| 10-18 12:19 | +5 | DOGE | DOWN | 0.55 | open |  |
| 10-18 12:18 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-18 12:18 | +10 stop | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-18 12:18 | +10 | DOGE | DOWN | 0.56 | open |  |
| 10-18 12:18 | +5 | DOGE | DOWN | 0.56 | 0.64 | 0.45 |
| 10-18 12:18 | +10 stop | NEAR | DOWN | 0.59 | 0.44 | -1.85 |
| 10-18 12:18 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-18 12:18 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-18 12:18 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-18 12:17 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.93 |
| 10-18 12:17 | +5 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-18 12:17 | +10 stop | BNB | UP | 0.50 | 0.63 | 0.95 |
| 10-18 12:17 | +20 | BNB | UP | 0.50 | open |  |
| 10-18 12:17 | +15 | BNB | UP | 0.50 | open |  |
| 10-18 12:17 | +10 | BNB | UP | 0.50 | 0.63 | 0.95 |
| 10-18 12:17 | +5 | BNB | UP | 0.50 | 0.55 | 0.14 |
| 10-18 12:17 | +10 stop | DOGE | UP | 0.51 | 0.62 | 0.75 |
| 10-18 12:17 | +20 | DOGE | UP | 0.51 | open |  |
| 10-18 12:17 | +15 | DOGE | UP | 0.51 | 0.70 | 1.57 |
| 10-18 12:17 | +10 | DOGE | UP | 0.51 | 0.62 | 0.75 |
| 10-18 12:17 | +5 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-18 12:17 | +20 | NEAR | UP | 0.52 | open |  |
| 10-18 12:17 | +15 | NEAR | UP | 0.52 | open |  |
| 10-18 12:17 | +5 | NEAR | UP | 0.54 | open |  |
| 10-18 12:17 | +10 stop | SOL | UP | 0.55 | 0.34 | -2.44 |
| 10-18 12:17 | +20 | SOL | UP | 0.55 | open |  |
| 10-18 12:17 | +15 | SOL | UP | 0.56 | open |  |
