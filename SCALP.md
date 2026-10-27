# Range-Scalp Bot

*Updated Tue Oct 27 17:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36828 | 32157 | 4671 (44) | 4 | $-10213.23 | -4.4% |
| **+10¢** | 27515 | 22104 | 5411 (66) | 3 | $-9087.00 | -5.2% |
| **+15¢** | 23020 | 17213 | 5807 (90) | 3 | $-8019.58 | -5.5% |
| **+20¢** | 20402 | 14324 | 6078 (115) | 3 | $-6990.23 | -5.5% |
| **+10¢ (15¢ stop)** | 45136 | 45072 | 64 (33) | 0 | $-17214.07 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 17:22 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-27 17:21 | +10 stop | SOL | DOWN | 0.50 | 0.29 | -2.43 |
| 10-27 17:21 | +10 stop | XRP | UP | 0.64 | 0.76 | 0.90 |
| 10-27 17:21 | +15 | XRP | UP | 0.64 | 0.85 | 1.84 |
| 10-27 17:21 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-27 17:21 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-27 17:20 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-27 17:20 | +10 stop | ZEC | DOWN | 0.51 | 0.26 | -2.82 |
| 10-27 17:20 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-27 17:20 | +10 stop | SOL | DOWN | 0.66 | 0.47 | -2.24 |
| 10-27 17:19 | +10 stop | BTC | DOWN | 0.57 | 0.37 | -2.35 |
| 10-27 17:19 | +20 | BTC | DOWN | 0.57 | open |  |
| 10-27 17:19 | +15 | BTC | DOWN | 0.57 | open |  |
| 10-27 17:19 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-27 17:19 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-27 17:18 | +15 | BNB | UP | 0.51 | 0.67 | 1.26 |
| 10-27 17:18 | +10 stop | XRP | UP | 0.46 | 0.64 | 1.45 |
| 10-27 17:18 | +20 | XRP | UP | 0.46 | 0.76 | 2.69 |
| 10-27 17:18 | +15 | XRP | UP | 0.46 | 0.64 | 1.45 |
| 10-27 17:18 | +10 | XRP | UP | 0.46 | 0.64 | 1.45 |
| 10-27 17:18 | +5 | XRP | UP | 0.46 | 0.55 | 0.54 |
| 10-27 17:18 | +10 stop | SOL | UP | 0.53 | 0.38 | -1.85 |
| 10-27 17:18 | +10 | SOL | UP | 0.53 | 0.70 | 1.37 |
| 10-27 17:18 | +5 | SOL | UP | 0.53 | 0.62 | 0.55 |
| 10-27 17:18 | +10 stop | NEAR | UP | 0.63 | 0.46 | -2.05 |
| 10-27 17:18 | +10 | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-27 17:18 | +5 | NEAR | UP | 0.63 | 0.71 | 0.48 |
| 10-27 17:18 | +15 | SOL | UP | 0.59 | 0.80 | 1.81 |
| 10-27 17:18 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 10-27 17:17 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.76 |
| 10-27 17:17 | +10 | BNB | UP | 0.56 | 0.67 | 0.76 |
| 10-27 17:17 | +10 stop | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 10-27 17:17 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-27 17:17 | +10 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-27 17:17 | +5 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-27 17:17 | +10 stop | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 10-27 17:17 | +20 | NEAR | UP | 0.56 | 0.84 | 2.52 |
| 10-27 17:17 | +15 | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 10-27 17:17 | +10 | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 10-27 17:17 | +5 | NEAR | UP | 0.56 | 0.66 | 0.66 |
