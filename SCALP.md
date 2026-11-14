# Range-Scalp Bot

*Updated Sat Nov 14 23:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60006 | 52342 | 7664 (107) | 7 | $-16339.47 | -4.3% |
| **+10¢** | 44831 | 35853 | 8978 (143) | 8 | $-15414.65 | -5.5% |
| **+15¢** | 37562 | 27881 | 9681 (181) | 8 | $-14050.75 | -6.0% |
| **+20¢** | 33466 | 23310 | 10156 (233) | 8 | $-12384.17 | -5.9% |
| **+10¢ (15¢ stop)** | 73060 | 72917 | 143 (82) | 2 | $-26877.81 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 23:21 | +5 | DOGE | UP | 0.71 | open |  |
| 11-14 23:20 | +5 | ETH | UP | 0.62 | 0.73 | 0.78 |
| 11-14 23:20 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 11-14 23:20 | +5 | ETH | UP | 0.56 | 0.63 | 0.35 |
| 11-14 23:19 | +10 stop | BTC | UP | 0.66 | open |  |
| 11-14 23:19 | +10 stop | HYPE | UP | 0.68 | 0.82 | 1.17 |
| 11-14 23:19 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-14 23:19 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 11-14 23:19 | +10 stop | XRP | UP | 0.68 | 0.82 | 1.13 |
| 11-14 23:19 | +5 | DOGE | UP | 0.53 | 0.62 | 0.55 |
| 11-14 23:19 | +10 stop | SOL | UP | 0.71 | open |  |
| 11-14 23:18 | +10 stop | ETH | DOWN | 0.50 | 0.26 | -2.72 |
| 11-14 23:18 | +15 | ETH | DOWN | 0.48 | open |  |
| 11-14 23:18 | +10 | ETH | DOWN | 0.49 | open |  |
| 11-14 23:18 | +5 | ETH | DOWN | 0.49 | 0.58 | 0.54 |
| 11-14 23:18 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-14 23:17 | +10 | XRP | DOWN | 0.60 | open |  |
| 11-14 23:17 | +10 stop | DOGE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-14 23:17 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-14 23:17 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-14 23:17 | +10 | DOGE | DOWN | 0.62 | open |  |
| 11-14 23:17 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-14 23:17 | +10 stop | XRP | DOWN | 0.57 | 0.37 | -2.35 |
| 11-14 23:17 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-14 23:17 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-14 23:17 | +15 | SOL | DOWN | 0.66 | open |  |
| 11-14 23:17 | +10 stop | BTC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-14 23:17 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-14 23:17 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-14 23:17 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-14 23:17 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-14 23:16 | +10 stop | BNB | DOWN | 0.70 | 0.43 | -3.03 |
| 11-14 23:16 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-14 23:16 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-14 23:16 | +10 | BNB | DOWN | 0.71 | open |  |
| 11-14 23:16 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-14 23:16 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 11-14 23:16 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-14 23:16 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-14 23:16 | +10 stop | HYPE | DOWN | 0.61 | 0.35 | -2.93 |
