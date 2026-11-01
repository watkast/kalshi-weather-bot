# Range-Scalp Bot

*Updated Sun Nov 01 23:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44058 | 38375 | 5683 (65) | 2 | $-12679.61 | -4.6% |
| **+10¢** | 32880 | 26316 | 6564 (86) | 3 | $-11407.21 | -5.5% |
| **+15¢** | 27520 | 20456 | 7064 (113) | 3 | $-10407.07 | -6.0% |
| **+20¢** | 24447 | 17050 | 7397 (147) | 3 | $-9157.02 | -6.0% |
| **+10¢ (15¢ stop)** | 53743 | 53657 | 86 (51) | 0 | $-20324.13 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 23:23 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-01 23:21 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-01 23:20 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-01 23:19 | +10 stop | SOL | DOWN | 0.56 | 0.70 | 1.07 |
| 11-01 23:18 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-01 23:18 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.69 |
| 11-01 23:17 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-01 23:17 | +10 stop | HYPE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-01 23:17 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-01 23:17 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 11-01 23:17 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-01 23:17 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-01 23:17 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-01 23:17 | +10 stop | SOL | DOWN | 0.69 | 0.54 | -1.83 |
| 11-01 23:17 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-01 23:17 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 11-01 23:17 | +15 | NEAR | DOWN | 0.66 | 0.83 | 1.44 |
| 11-01 23:17 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-01 23:17 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 11-01 23:17 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 23:17 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 11-01 23:17 | +15 | ETH | DOWN | 0.65 | 0.83 | 1.54 |
| 11-01 23:17 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 23:17 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-01 23:17 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-01 23:17 | +20 | XRP | DOWN | 0.68 | 0.91 | 2.09 |
| 11-01 23:17 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-01 23:17 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-01 23:17 | +5 | XRP | DOWN | 0.68 | 0.76 | 0.51 |
| 11-01 23:16 | +10 stop | ZEC | UP | 0.54 | 0.31 | -2.63 |
| 11-01 23:16 | +20 | ZEC | UP | 0.54 | open |  |
| 11-01 23:16 | +15 | ZEC | UP | 0.54 | open |  |
| 11-01 23:16 | +10 | ZEC | UP | 0.54 | open |  |
| 11-01 23:16 | +5 | ZEC | UP | 0.54 | open |  |
| 11-01 23:16 | +10 stop | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-01 23:16 | +20 | BNB | UP | 0.71 | 0.92 | 1.94 |
| 11-01 23:16 | +15 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-01 23:16 | +10 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-01 23:16 | +5 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-01 23:16 | +10 stop | BTC | UP | 0.54 | 0.32 | -2.54 |
