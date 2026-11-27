# Range-Scalp Bot

*Updated Fri Nov 27 23:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74019 | 64604 | 9415 (171) | 0 | $-19656.47 | -4.2% |
| **+10¢** | 55153 | 44157 | 10996 (216) | 0 | $-18275.31 | -5.3% |
| **+15¢** | 46181 | 34338 | 11843 (274) | 0 | $-16340.98 | -5.6% |
| **+20¢** | 41100 | 28626 | 12474 (341) | 0 | $-14752.80 | -5.7% |
| **+10¢ (15¢ stop)** | 90119 | 89900 | 219 (135) | 0 | $-33321.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 23:26 | +10 stop | ETH | DOWN | 0.61 | 0.44 | -2.05 |
| 11-27 23:24 | +10 stop | ETH | UP | 0.44 | 0.56 | 0.84 |
| 11-27 23:24 | +5 | BNB | UP | 0.49 | 0.59 | 0.65 |
| 11-27 23:23 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 11-27 23:22 | +5 | ETH | DOWN | 0.61 | yes | -6.27 |
| 11-27 23:22 | +10 stop | BNB | UP | 0.52 | 0.63 | 0.75 |
| 11-27 23:22 | +5 | BNB | UP | 0.52 | 0.57 | 0.14 |
| 11-27 23:21 | +10 stop | ETH | DOWN | 0.54 | 0.38 | -1.95 |
| 11-27 23:21 | +10 | ETH | DOWN | 0.54 | yes | -5.58 |
| 11-27 23:21 | +5 | ETH | DOWN | 0.54 | 0.60 | 0.25 |
| 11-27 23:21 | +10 stop | BTC | UP | 0.65 | 0.50 | -1.84 |
| 11-27 23:21 | +10 stop | SOL | DOWN | 0.52 | 0.33 | -2.24 |
| 11-27 23:21 | +10 stop | BTC | DOWN | 0.45 | 0.60 | 1.15 |
| 11-27 23:21 | +10 stop | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 11-27 23:21 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 11-27 23:21 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 11-27 23:19 | +10 stop | BTC | UP | 0.63 | 0.45 | -2.15 |
| 11-27 23:19 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 11-27 23:18 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 11-27 23:18 | +20 | DOGE | UP | 0.64 | 0.88 | 2.13 |
| 11-27 23:18 | +15 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-27 23:18 | +10 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 11-27 23:18 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 11-27 23:17 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 11-27 23:17 | +10 stop | SOL | DOWN | 0.69 | 0.54 | -1.83 |
| 11-27 23:17 | +20 | SOL | DOWN | 0.69 | yes | -7.05 |
| 11-27 23:17 | +15 | SOL | DOWN | 0.69 | yes | -7.05 |
| 11-27 23:17 | +10 | SOL | DOWN | 0.69 | yes | -7.05 |
| 11-27 23:17 | +5 | SOL | DOWN | 0.69 | yes | -7.05 |
| 11-27 23:16 | +10 stop | BNB | DOWN | 0.58 | 0.42 | -1.96 |
| 11-27 23:16 | +20 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-27 23:16 | +15 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-27 23:16 | +10 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-27 23:16 | +5 | BNB | DOWN | 0.58 | 0.66 | 0.46 |
| 11-27 23:16 | +10 stop | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 11-27 23:16 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.71 |
| 11-27 23:16 | +15 | NEAR | DOWN | 0.59 | 0.79 | 1.72 |
| 11-27 23:16 | +10 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-27 23:16 | +5 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-27 23:16 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
