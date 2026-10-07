# Range-Scalp Bot

*Updated Wed Oct 07 18:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6653 | 5777 | 876 (10) | 6 | $-2004.27 | -4.8% |
| **+10¢** | 5052 | 4025 | 1027 (17) | 7 | $-1882.69 | -5.9% |
| **+15¢** | 4233 | 3150 | 1083 (21) | 7 | $-1578.65 | -5.9% |
| **+20¢** | 3781 | 2651 | 1130 (28) | 7 | $-1270.39 | -5.4% |
| **+10¢ (15¢ stop)** | 8086 | 8069 | 17 (10) | 0 | $-2864.41 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 18:22 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-07 18:20 | +10 stop | ZEC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-07 18:19 | +10 stop | ZEC | UP | 0.66 | 0.40 | -2.92 |
| 10-07 18:19 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.72 |
| 10-07 18:18 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 10-07 18:18 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.85 |
| 10-07 18:18 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-07 18:18 | +5 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-07 18:17 | +5 | BTC | UP | 0.57 | open |  |
| 10-07 18:17 | +5 | XRP | DOWN | 0.68 | 0.76 | 0.51 |
| 10-07 18:16 | +10 | ZEC | UP | 0.67 | open |  |
| 10-07 18:16 | +5 | ZEC | UP | 0.67 | open |  |
| 10-07 18:16 | +10 stop | NEAR | UP | 0.65 | 0.39 | -2.89 |
| 10-07 18:16 | +20 | NEAR | UP | 0.65 | open |  |
| 10-07 18:16 | +15 | NEAR | UP | 0.64 | open |  |
| 10-07 18:16 | +10 | NEAR | UP | 0.64 | open |  |
| 10-07 18:16 | +5 | NEAR | UP | 0.64 | open |  |
| 10-07 18:16 | +10 stop | SOL | UP | 0.48 | 0.32 | -1.94 |
| 10-07 18:16 | +20 | SOL | UP | 0.48 | open |  |
| 10-07 18:16 | +15 | SOL | UP | 0.48 | open |  |
| 10-07 18:16 | +10 | SOL | UP | 0.48 | open |  |
| 10-07 18:16 | +5 | SOL | UP | 0.48 | 0.53 | 0.14 |
| 10-07 18:16 | +10 stop | BTC | UP | 0.59 | 0.44 | -1.85 |
| 10-07 18:16 | +20 | BTC | UP | 0.59 | open |  |
| 10-07 18:16 | +15 | BTC | UP | 0.59 | open |  |
| 10-07 18:16 | +10 | BTC | UP | 0.59 | open |  |
| 10-07 18:16 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 10-07 18:16 | +10 stop | ETH | UP | 0.58 | 0.37 | -2.45 |
| 10-07 18:16 | +20 | ETH | UP | 0.58 | open |  |
| 10-07 18:16 | +15 | ETH | UP | 0.58 | open |  |
| 10-07 18:16 | +10 | ETH | UP | 0.58 | open |  |
| 10-07 18:16 | +5 | ETH | UP | 0.58 | open |  |
| 10-07 18:16 | +10 stop | ZEC | UP | 0.71 | 0.51 | -2.33 |
| 10-07 18:16 | +20 | ZEC | UP | 0.71 | open |  |
| 10-07 18:16 | +15 | ZEC | UP | 0.71 | open |  |
| 10-07 18:16 | +10 stop | BNB | UP | 0.67 | 0.50 | -2.04 |
| 10-07 18:16 | +20 | BNB | UP | 0.67 | open |  |
| 10-07 18:16 | +15 | BNB | UP | 0.67 | open |  |
| 10-07 18:16 | +10 | BNB | UP | 0.67 | open |  |
| 10-07 18:16 | +5 | BNB | UP | 0.67 | open |  |
