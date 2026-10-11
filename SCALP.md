# Range-Scalp Bot

*Updated Sun Oct 11 07:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11550 | 9957 | 1593 (24) | 3 | $-3927.84 | -5.4% |
| **+10¢** | 8754 | 6904 | 1850 (37) | 4 | $-3728.25 | -6.8% |
| **+15¢** | 7375 | 5416 | 1959 (53) | 5 | $-3176.37 | -6.9% |
| **+20¢** | 6573 | 4537 | 2036 (67) | 5 | $-2640.78 | -6.4% |
| **+10¢ (15¢ stop)** | 14240 | 14199 | 41 (25) | 1 | $-5682.23 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 07:20 | +10 stop | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-11 07:20 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-11 07:20 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-11 07:20 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-11 07:20 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-11 07:20 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-11 07:20 | +10 stop | BTC | UP | 0.52 | 0.64 | 0.85 |
| 10-11 07:19 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-11 07:19 | +20 | XRP | DOWN | 0.68 | 0.93 | 2.28 |
| 10-11 07:19 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-11 07:19 | +10 | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-11 07:19 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-11 07:19 | +10 stop | ZEC | DOWN | 0.48 | 0.64 | 1.25 |
| 10-11 07:18 | +10 stop | BTC | DOWN | 0.64 | 0.37 | -3.04 |
| 10-11 07:18 | +5 | NEAR | DOWN | 0.48 | 0.56 | 0.44 |
| 10-11 07:18 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 07:18 | +10 stop | DOGE | DOWN | 0.70 | 0.42 | -3.13 |
| 10-11 07:18 | +10 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-11 07:18 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-11 07:18 | +10 stop | NEAR | UP | 0.45 | 0.61 | 1.25 |
| 10-11 07:18 | +20 | NEAR | UP | 0.45 | open |  |
| 10-11 07:18 | +15 | NEAR | UP | 0.45 | 0.61 | 1.25 |
| 10-11 07:18 | +10 | NEAR | UP | 0.46 | 0.61 | 1.16 |
| 10-11 07:18 | +5 | NEAR | UP | 0.46 | 0.51 | 0.14 |
| 10-11 07:17 | +10 stop | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-11 07:17 | +10 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-11 07:17 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-11 07:17 | +5 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-11 07:17 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 07:17 | +10 | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 07:17 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.25 |
| 10-11 07:17 | +10 stop | ZEC | UP | 0.68 | 0.52 | -1.98 |
| 10-11 07:17 | +20 | ZEC | UP | 0.68 | open |  |
| 10-11 07:17 | +15 | ZEC | UP | 0.68 | open |  |
| 10-11 07:17 | +10 | ZEC | UP | 0.68 | open |  |
| 10-11 07:17 | +5 | ZEC | UP | 0.68 | open |  |
| 10-11 07:16 | +10 stop | BNB | UP | 0.50 | 0.28 | -2.53 |
| 10-11 07:16 | +10 stop | BTC | UP | 0.55 | 0.35 | -2.34 |
| 10-11 07:16 | +20 | BTC | UP | 0.55 | open |  |
| 10-11 07:16 | +15 | BTC | UP | 0.55 | open |  |
