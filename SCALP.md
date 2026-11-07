# Range-Scalp Bot

*Updated Sat Nov 07 23:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51658 | 45042 | 6616 (80) | 2 | $-14332.40 | -4.4% |
| **+10¢** | 38546 | 30831 | 7715 (106) | 3 | $-13352.48 | -5.5% |
| **+15¢** | 32277 | 23962 | 8315 (135) | 5 | $-12255.76 | -6.1% |
| **+20¢** | 28710 | 19992 | 8718 (180) | 6 | $-10814.61 | -6.0% |
| **+10¢ (15¢ stop)** | 62906 | 62803 | 103 (61) | 2 | $-23316.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 23:23 | +10 stop | ZEC | DOWN | 0.57 | open |  |
| 11-07 23:23 | +10 stop | ETH | UP | 0.68 | open |  |
| 11-07 23:22 | +10 stop | HYPE | DOWN | 0.59 | 0.40 | -2.24 |
| 11-07 23:22 | +10 stop | BNB | DOWN | 0.46 | 0.58 | 0.84 |
| 11-07 23:22 | +20 | BNB | DOWN | 0.46 | open |  |
| 11-07 23:22 | +10 | BNB | DOWN | 0.46 | 0.58 | 0.84 |
| 11-07 23:22 | +5 | BNB | DOWN | 0.46 | 0.58 | 0.84 |
| 11-07 23:22 | +10 stop | SOL | DOWN | 0.60 | 0.40 | -2.34 |
| 11-07 23:21 | +10 stop | DOGE | DOWN | 0.58 | 0.30 | -3.13 |
| 11-07 23:21 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 11-07 23:20 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 23:20 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-07 23:20 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 23:20 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 11-07 23:20 | +5 | BTC | DOWN | 0.63 | open |  |
| 11-07 23:19 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-07 23:19 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-07 23:19 | +5 | NEAR | UP | 0.70 | 0.78 | 0.52 |
| 11-07 23:19 | +10 stop | HYPE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-07 23:19 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-07 23:19 | +20 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 11-07 23:19 | +15 | NEAR | UP | 0.61 | 0.78 | 1.40 |
| 11-07 23:19 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-07 23:19 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 11-07 23:18 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-07 23:17 | +5 | BNB | DOWN | 0.63 | 0.72 | 0.58 |
| 11-07 23:17 | +10 stop | DOGE | UP | 0.64 | 0.41 | -2.64 |
| 11-07 23:17 | +20 | DOGE | UP | 0.64 | open |  |
| 11-07 23:17 | +15 | DOGE | UP | 0.64 | open |  |
| 11-07 23:17 | +10 | DOGE | UP | 0.64 | open |  |
| 11-07 23:17 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 11-07 23:17 | +10 stop | SOL | UP | 0.65 | 0.48 | -2.04 |
| 11-07 23:17 | +20 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 11-07 23:17 | +15 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 11-07 23:17 | +10 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 11-07 23:17 | +5 | SOL | UP | 0.65 | 0.72 | 0.39 |
| 11-07 23:17 | +10 stop | ETH | UP | 0.58 | 0.43 | -1.86 |
| 11-07 23:17 | +20 | ETH | UP | 0.58 | open |  |
| 11-07 23:17 | +15 | ETH | UP | 0.58 | open |  |
| 11-07 23:17 | +10 | ETH | UP | 0.58 | 0.71 | 0.97 |
