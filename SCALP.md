# Range-Scalp Bot

*Updated Sat Nov 07 19:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51400 | 44816 | 6584 (79) | 2 | $-14282.93 | -4.4% |
| **+10¢** | 38360 | 30684 | 7676 (105) | 1 | $-13285.86 | -5.5% |
| **+15¢** | 32117 | 23843 | 8274 (134) | 1 | $-12204.24 | -6.1% |
| **+20¢** | 28567 | 19894 | 8673 (177) | 1 | $-10769.11 | -6.0% |
| **+10¢ (15¢ stop)** | 62602 | 62499 | 103 (61) | 0 | $-23162.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 19:28 | +10 stop | DOGE | UP | 0.63 | 0.87 | 2.15 |
| 11-07 19:28 | +20 | DOGE | UP | 0.64 | 0.87 | 2.02 |
| 11-07 19:28 | +15 | DOGE | UP | 0.63 | 0.87 | 2.15 |
| 11-07 19:28 | +10 | DOGE | UP | 0.64 | 0.87 | 2.02 |
| 11-07 19:28 | +10 stop | NEAR | DOWN | 0.58 | 0.92 | 3.12 |
| 11-07 19:25 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 11-07 19:25 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-07 19:24 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-07 19:24 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-07 19:24 | +10 stop | NEAR | DOWN | 0.71 | 0.51 | -2.33 |
| 11-07 19:24 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 11-07 19:24 | +15 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 11-07 19:24 | +10 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 11-07 19:24 | +5 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 11-07 19:24 | +10 stop | ETH | DOWN | 0.69 | 0.51 | -2.13 |
| 11-07 19:23 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-07 19:22 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
| 11-07 19:22 | +5 | DOGE | DOWN | 0.59 | open |  |
| 11-07 19:22 | +10 stop | XRP | DOWN | 0.59 | 0.41 | -2.14 |
| 11-07 19:20 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 11-07 19:19 | +10 stop | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 11-07 19:19 | +5 | DOGE | UP | 0.50 | 0.63 | 0.94 |
| 11-07 19:19 | +10 stop | BTC | UP | 0.57 | 0.41 | -1.95 |
| 11-07 19:19 | +5 | BTC | UP | 0.58 | 0.95 | 3.51 |
| 11-07 19:19 | +10 stop | SOL | DOWN | 0.51 | 0.61 | 0.65 |
| 11-07 19:18 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.74 |
| 11-07 19:18 | +10 stop | ZEC | UP | 0.62 | 0.89 | 2.46 |
| 11-07 19:18 | +10 stop | XRP | DOWN | 0.66 | 0.49 | -2.04 |
| 11-07 19:17 | +10 stop | BNB | DOWN | 0.58 | 0.43 | -1.86 |
| 11-07 19:17 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-07 19:17 | +15 | BNB | DOWN | 0.59 | open |  |
| 11-07 19:17 | +10 | BNB | DOWN | 0.59 | open |  |
| 11-07 19:17 | +5 | BNB | DOWN | 0.53 | open |  |
| 11-07 19:17 | +10 stop | SOL | DOWN | 0.71 | 0.56 | -1.83 |
| 11-07 19:17 | +10 stop | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 11-07 19:17 | +20 | HYPE | UP | 0.60 | 0.83 | 2.03 |
| 11-07 19:17 | +15 | HYPE | UP | 0.60 | 0.76 | 1.30 |
| 11-07 19:17 | +10 | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 11-07 19:17 | +5 | HYPE | UP | 0.60 | 0.67 | 0.37 |
| 11-07 19:17 | +10 stop | BTC | DOWN | 0.56 | 0.35 | -2.44 |
