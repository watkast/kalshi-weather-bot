# Range-Scalp Bot

*Updated Sat Nov 14 20:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59830 | 52201 | 7629 (107) | 0 | $-16193.96 | -4.3% |
| **+10¢** | 44700 | 35766 | 8934 (143) | 0 | $-15229.65 | -5.4% |
| **+15¢** | 37448 | 27814 | 9634 (180) | 0 | $-13870.65 | -5.9% |
| **+20¢** | 33361 | 23252 | 10109 (232) | 0 | $-12218.10 | -5.8% |
| **+10¢ (15¢ stop)** | 72809 | 72666 | 143 (82) | 0 | $-26729.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 20:28 | +10 stop | SOL | UP | 0.25 | 0.59 | 3.09 |
| 11-14 20:28 | +10 | SOL | UP | 0.25 | 0.59 | 3.09 |
| 11-14 20:28 | +5 | SOL | UP | 0.25 | 0.59 | 3.09 |
| 11-14 20:27 | +10 stop | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-14 20:27 | +10 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-14 20:27 | +5 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-14 20:27 | +10 stop | SOL | UP | 0.50 | 0.64 | 1.05 |
| 11-14 20:27 | +10 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 11-14 20:27 | +5 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 11-14 20:27 | +10 stop | BNB | DOWN | 0.63 | 0.80 | 1.40 |
| 11-14 20:27 | +15 | BNB | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 20:27 | +10 | BNB | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 20:27 | +5 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-14 20:26 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-14 20:26 | +15 | BTC | DOWN | 0.58 | 0.84 | 2.32 |
| 11-14 20:26 | +10 | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-14 20:26 | +5 | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-14 20:26 | +10 stop | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 11-14 20:26 | +5 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 11-14 20:24 | +10 stop | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-14 20:24 | +10 | BTC | DOWN | 0.48 | 0.61 | 0.95 |
| 11-14 20:24 | +5 | BTC | DOWN | 0.48 | 0.61 | 0.95 |
| 11-14 20:24 | +10 stop | XRP | DOWN | 0.45 | 0.55 | 0.64 |
| 11-14 20:23 | +10 stop | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-14 20:23 | +10 stop | DOGE | DOWN | 0.61 | 0.78 | 1.40 |
| 11-14 20:23 | +20 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-14 20:23 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-14 20:23 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-14 20:23 | +5 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-14 20:23 | +5 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-14 20:22 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 20:22 | +15 | BNB | DOWN | 0.62 | 0.86 | 2.14 |
| 11-14 20:22 | +10 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-14 20:22 | +5 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-14 20:21 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 11-14 20:21 | +15 | XRP | DOWN | 0.70 | 0.94 | 2.16 |
| 11-14 20:21 | +10 | XRP | DOWN | 0.70 | 0.94 | 2.16 |
| 11-14 20:21 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-14 20:21 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-14 20:21 | +20 | ETH | DOWN | 0.67 | 0.90 | 2.11 |
