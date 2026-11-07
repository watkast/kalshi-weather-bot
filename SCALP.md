# Range-Scalp Bot

*Updated Sat Nov 07 11:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50913 | 44386 | 6527 (76) | 3 | $-14256.96 | -4.4% |
| **+10¢** | 38010 | 30402 | 7608 (102) | 2 | $-13229.42 | -5.5% |
| **+15¢** | 31818 | 23621 | 8197 (131) | 3 | $-12144.44 | -6.1% |
| **+20¢** | 28292 | 19701 | 8591 (173) | 4 | $-10719.91 | -6.0% |
| **+10¢ (15¢ stop)** | 62010 | 61911 | 99 (58) | 0 | $-22906.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 11:11 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-07 11:11 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 11:11 | +5 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 11:11 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 11:11 | +20 | BTC | DOWN | 0.69 | 0.96 | 2.49 |
| 11-07 11:11 | +15 | BTC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-07 11:11 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 11:11 | +5 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 11:10 | +10 stop | NEAR | DOWN | 0.65 | 0.81 | 1.36 |
| 11-07 11:09 | +10 stop | SOL | UP | 0.59 | 0.34 | -2.83 |
| 11-07 11:09 | +20 | SOL | UP | 0.59 | open |  |
| 11-07 11:09 | +15 | SOL | UP | 0.59 | open |  |
| 11-07 11:09 | +10 | SOL | UP | 0.59 | open |  |
| 11-07 11:09 | +5 | SOL | UP | 0.59 | open |  |
| 11-07 11:09 | +10 stop | ETH | UP | 0.53 | 0.26 | -3.02 |
| 11-07 11:09 | +20 | ETH | UP | 0.54 | open |  |
| 11-07 11:09 | +15 | ETH | UP | 0.55 | open |  |
| 11-07 11:09 | +10 | ETH | UP | 0.55 | open |  |
| 11-07 11:09 | +5 | ETH | UP | 0.55 | open |  |
| 11-07 11:08 | +10 stop | XRP | UP | 0.64 | 0.79 | 1.21 |
| 11-07 11:08 | +20 | XRP | UP | 0.65 | open |  |
| 11-07 11:08 | +5 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 11-07 11:07 | +10 stop | NEAR | UP | 0.47 | 0.64 | 1.35 |
| 11-07 11:07 | +10 stop | HYPE | DOWN | 0.48 | 0.59 | 0.75 |
| 11-07 11:07 | +10 | HYPE | DOWN | 0.48 | 0.59 | 0.75 |
| 11-07 11:07 | +5 | HYPE | DOWN | 0.48 | 0.57 | 0.54 |
| 11-07 11:07 | +10 stop | DOGE | DOWN | 0.50 | 0.78 | 2.49 |
| 11-07 11:07 | +10 | DOGE | DOWN | 0.50 | 0.78 | 2.49 |
| 11-07 11:05 | +5 | XRP | UP | 0.59 | 0.74 | 1.19 |
| 11-07 11:05 | +10 stop | XRP | DOWN | 0.49 | 0.25 | -2.72 |
| 11-07 11:05 | +15 | XRP | DOWN | 0.49 | 0.68 | 1.56 |
| 11-07 11:05 | +10 | XRP | DOWN | 0.49 | 0.63 | 1.05 |
| 11-07 11:05 | +5 | XRP | DOWN | 0.49 | 0.58 | 0.54 |
| 11-07 11:05 | +10 stop | NEAR | DOWN | 0.70 | 0.53 | -2.03 |
| 11-07 11:05 | +20 | NEAR | DOWN | 0.70 | 0.93 | 2.09 |
| 11-07 11:05 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 11-07 11:05 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-07 11:05 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-07 11:05 | +10 stop | BTC | UP | 0.56 | 0.73 | 1.38 |
| 11-07 11:04 | +5 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
