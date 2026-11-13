# Range-Scalp Bot

*Updated Fri Nov 13 10:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58133 | 50727 | 7406 (102) | 3 | $-15676.72 | -4.3% |
| **+10¢** | 43433 | 34772 | 8661 (134) | 3 | $-14650.26 | -5.4% |
| **+15¢** | 36411 | 27085 | 9326 (168) | 4 | $-13221.85 | -5.8% |
| **+20¢** | 32440 | 22650 | 9790 (219) | 5 | $-11587.90 | -5.7% |
| **+10¢ (15¢ stop)** | 70828 | 70699 | 129 (79) | 2 | $-26031.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 10:23 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 10:23 | +10 stop | NEAR | DOWN | 0.55 | open |  |
| 11-13 10:23 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 11-13 10:23 | +10 stop | SOL | DOWN | 0.55 | open |  |
| 11-13 10:23 | +5 | SOL | DOWN | 0.55 | open |  |
| 11-13 10:22 | +10 stop | NEAR | DOWN | 0.49 | 0.60 | 0.75 |
| 11-13 10:22 | +10 | SOL | DOWN | 0.49 | open |  |
| 11-13 10:22 | +5 | SOL | DOWN | 0.49 | 0.54 | 0.14 |
| 11-13 10:22 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-13 10:22 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-13 10:22 | +5 | ETH | DOWN | 0.59 | 0.66 | 0.37 |
| 11-13 10:22 | +10 stop | SOL | DOWN | 0.56 | 0.67 | 0.80 |
| 11-13 10:22 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-13 10:21 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-13 10:21 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-13 10:21 | +20 | HYPE | UP | 0.67 | 0.88 | 1.86 |
| 11-13 10:21 | +15 | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 11-13 10:21 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-13 10:21 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 11-13 10:21 | +10 stop | NEAR | UP | 0.61 | 0.43 | -2.15 |
| 11-13 10:21 | +20 | NEAR | UP | 0.61 | open |  |
| 11-13 10:21 | +15 | NEAR | UP | 0.61 | open |  |
| 11-13 10:21 | +10 | NEAR | UP | 0.61 | open |  |
| 11-13 10:21 | +5 | NEAR | UP | 0.61 | open |  |
| 11-13 10:21 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.95 |
| 11-13 10:20 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 10:20 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 10:20 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-13 10:20 | +10 stop | SOL | UP | 0.61 | 0.41 | -2.34 |
| 11-13 10:20 | +10 stop | ZEC | UP | 0.57 | 0.30 | -3.03 |
| 11-13 10:20 | +15 | ZEC | UP | 0.57 | open |  |
| 11-13 10:20 | +10 | ZEC | UP | 0.57 | open |  |
| 11-13 10:20 | +5 | ZEC | UP | 0.58 | open |  |
| 11-13 10:18 | +10 stop | BTC | DOWN | 0.51 | 0.35 | -1.94 |
| 11-13 10:18 | +20 | BTC | DOWN | 0.51 | 0.74 | 1.98 |
| 11-13 10:18 | +15 | BTC | DOWN | 0.51 | 0.66 | 1.16 |
| 11-13 10:18 | +10 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-13 10:18 | +5 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-13 10:18 | +10 stop | ETH | UP | 0.66 | 0.49 | -2.04 |
| 11-13 10:18 | +10 stop | BNB | UP | 0.68 | 0.46 | -2.54 |
