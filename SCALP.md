# Range-Scalp Bot

*Updated Thu Nov 12 15:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57077 | 49757 | 7320 (101) | 3 | $-15696.58 | -4.4% |
| **+10¢** | 42664 | 34124 | 8540 (133) | 3 | $-14623.09 | -5.5% |
| **+15¢** | 35766 | 26576 | 9190 (167) | 5 | $-13209.61 | -5.9% |
| **+20¢** | 31865 | 22223 | 9642 (217) | 5 | $-11571.82 | -5.8% |
| **+10¢ (15¢ stop)** | 69613 | 69485 | 128 (78) | 0 | $-25719.71 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 15:27 | +10 stop | BTC | UP | 0.59 | 0.44 | -1.85 |
| 11-12 15:27 | +10 | BTC | UP | 0.59 | 0.74 | 1.19 |
| 11-12 15:27 | +5 | BTC | UP | 0.59 | 0.68 | 0.57 |
| 11-12 15:27 | +10 stop | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 15:26 | +10 stop | BTC | DOWN | 0.44 | 0.58 | 1.04 |
| 11-12 15:26 | +10 | BTC | DOWN | 0.44 | 0.58 | 1.04 |
| 11-12 15:26 | +5 | BTC | DOWN | 0.44 | 0.58 | 1.04 |
| 11-12 15:26 | +10 | BNB | UP | 0.63 | 0.75 | 0.89 |
| 11-12 15:26 | +10 stop | DOGE | DOWN | 0.55 | 0.28 | -3.03 |
| 11-12 15:26 | +20 | DOGE | DOWN | 0.55 | open |  |
| 11-12 15:26 | +15 | DOGE | DOWN | 0.55 | open |  |
| 11-12 15:26 | +10 | DOGE | DOWN | 0.55 | open |  |
| 11-12 15:26 | +5 | DOGE | DOWN | 0.55 | open |  |
| 11-12 15:26 | +10 stop | BNB | UP | 0.67 | 0.86 | 1.65 |
| 11-12 15:26 | +20 | BNB | UP | 0.68 | 0.95 | 2.46 |
| 11-12 15:26 | +15 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-12 15:26 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-12 15:24 | +10 stop | BTC | DOWN | 0.68 | 0.48 | -2.34 |
| 11-12 15:24 | +10 stop | BNB | DOWN | 0.60 | 0.33 | -3.03 |
| 11-12 15:23 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-12 15:23 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.28 |
| 11-12 15:22 | +10 stop | BNB | UP | 0.71 | 0.45 | -2.93 |
| 11-12 15:22 | +10 stop | DOGE | DOWN | 0.48 | 0.60 | 0.85 |
| 11-12 15:22 | +10 | BNB | UP | 0.71 | 0.85 | 1.16 |
| 11-12 15:22 | +5 | BNB | UP | 0.71 | 0.85 | 1.16 |
| 11-12 15:22 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-12 15:22 | +10 stop | BTC | UP | 0.63 | 0.42 | -2.45 |
| 11-12 15:22 | +10 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-12 15:22 | +5 | BTC | UP | 0.70 | 0.76 | 0.32 |
| 11-12 15:22 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 11-12 15:22 | +10 stop | DOGE | UP | 0.65 | 0.45 | -2.34 |
| 11-12 15:21 | +10 stop | XRP | DOWN | 0.66 | 0.84 | 1.54 |
| 11-12 15:21 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-12 15:21 | +10 stop | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-12 15:21 | +10 stop | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-12 15:21 | +10 | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-12 15:21 | +5 | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-12 15:21 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-12 15:21 | +15 | BNB | UP | 0.61 | 0.85 | 2.14 |
| 11-12 15:21 | +10 | BNB | UP | 0.62 | 0.72 | 0.69 |
