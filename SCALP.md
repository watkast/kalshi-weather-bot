# Range-Scalp Bot

*Updated Tue Oct 27 14:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36662 | 32015 | 4647 (43) | 1 | $-10147.13 | -4.4% |
| **+10¢** | 27386 | 22008 | 5378 (65) | 1 | $-8988.15 | -5.2% |
| **+15¢** | 22911 | 17140 | 5771 (89) | 2 | $-7906.21 | -5.5% |
| **+20¢** | 20305 | 14262 | 6043 (113) | 3 | $-6908.39 | -5.4% |
| **+10¢ (15¢ stop)** | 44912 | 44849 | 63 (33) | 1 | $-17116.30 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 14:16 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 10-27 14:16 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-27 14:16 | +15 | ZEC | DOWN | 0.65 | open |  |
| 10-27 14:16 | +10 | ZEC | DOWN | 0.65 | open |  |
| 10-27 14:16 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-27 14:15 | +10 stop | HYPE | DOWN | 0.52 | 0.66 | 1.02 |
| 10-27 14:15 | +20 | HYPE | DOWN | 0.53 | open |  |
| 10-27 14:15 | +15 | HYPE | DOWN | 0.53 | 0.72 | 1.53 |
| 10-27 14:15 | +10 | HYPE | DOWN | 0.53 | 0.66 | 0.92 |
| 10-27 14:15 | +5 | HYPE | DOWN | 0.53 | 0.62 | 0.51 |
| 10-27 14:15 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-27 14:15 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-27 14:15 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-27 14:15 | +10 | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-27 14:15 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 10-27 14:11 | +5 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 10-27 14:10 | +10 stop | NEAR | DOWN | 0.54 | 0.24 | -3.31 |
| 10-27 14:10 | +15 | NEAR | DOWN | 0.54 | yes | -5.57 |
| 10-27 14:10 | +10 | NEAR | DOWN | 0.54 | yes | -5.57 |
| 10-27 14:10 | +5 | NEAR | DOWN | 0.53 | 0.58 | 0.16 |
| 10-27 14:10 | +10 stop | HYPE | UP | 0.64 | 0.48 | -1.95 |
| 10-27 14:09 | +10 stop | BTC | UP | 0.60 | 0.74 | 1.09 |
| 10-27 14:08 | +10 stop | ETH | UP | 0.54 | 0.71 | 1.37 |
| 10-27 14:08 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-27 14:07 | +10 stop | NEAR | DOWN | 0.56 | 0.72 | 1.23 |
| 10-27 14:07 | +20 | NEAR | DOWN | 0.57 | yes | -5.88 |
| 10-27 14:07 | +15 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-27 14:07 | +10 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-27 14:07 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.42 |
| 10-27 14:07 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.90 |
| 10-27 14:07 | +10 stop | BTC | UP | 0.71 | 0.54 | -2.03 |
| 10-27 14:07 | +10 stop | XRP | UP | 0.68 | 0.81 | 1.03 |
| 10-27 14:07 | +5 | BTC | UP | 0.64 | 0.70 | 0.28 |
| 10-27 14:06 | +5 | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 10-27 14:06 | +10 stop | ETH | DOWN | 0.46 | 0.23 | -2.61 |
| 10-27 14:06 | +10 stop | ZEC | UP | 0.55 | 0.73 | 1.48 |
| 10-27 14:06 | +5 | ZEC | UP | 0.55 | 0.62 | 0.35 |
| 10-27 14:06 | +10 stop | BNB | UP | 0.53 | 0.65 | 0.86 |
| 10-27 14:06 | +20 | BNB | UP | 0.53 | 0.78 | 2.19 |
| 10-27 14:06 | +15 | BNB | UP | 0.53 | 0.78 | 2.19 |
