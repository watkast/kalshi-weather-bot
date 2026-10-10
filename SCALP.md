# Range-Scalp Bot

*Updated Sat Oct 10 23:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11066 | 9539 | 1527 (22) | 0 | $-3772.03 | -5.4% |
| **+10¢** | 8382 | 6603 | 1779 (36) | 0 | $-3611.29 | -6.8% |
| **+15¢** | 7066 | 5184 | 1882 (52) | 0 | $-3056.45 | -6.9% |
| **+20¢** | 6289 | 4331 | 1958 (66) | 0 | $-2578.47 | -6.5% |
| **+10¢ (15¢ stop)** | 13640 | 13599 | 41 (25) | 0 | $-5480.66 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 23:27 | +10 stop | BTC | UP | 0.24 | 0.63 | 3.60 |
| 10-10 23:27 | +10 stop | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 10-10 23:27 | +20 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 10-10 23:27 | +15 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 10-10 23:27 | +10 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 10-10 23:27 | +5 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 10-10 23:26 | +10 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-10 23:26 | +5 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-10 23:26 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-10 23:24 | +10 stop | XRP | DOWN | 0.71 | 0.91 | 1.80 |
| 10-10 23:24 | +10 stop | HYPE | DOWN | 0.68 | 0.90 | 1.97 |
| 10-10 23:24 | +10 | HYPE | DOWN | 0.68 | 0.90 | 1.97 |
| 10-10 23:24 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-10 23:24 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-10 23:24 | +5 | NEAR | DOWN | 0.68 | 0.75 | 0.40 |
| 10-10 23:22 | +10 stop | BTC | DOWN | 0.66 | 0.49 | -2.04 |
| 10-10 23:21 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.85 |
| 10-10 23:21 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.76 |
| 10-10 23:21 | +5 | SOL | DOWN | 0.63 | 0.74 | 0.76 |
| 10-10 23:20 | +5 | HYPE | DOWN | 0.70 | 0.90 | 1.78 |
| 10-10 23:20 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-10 23:20 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-10 23:20 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-10 23:20 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 10-10 23:20 | +10 stop | XRP | DOWN | 0.55 | 0.37 | -2.11 |
| 10-10 23:20 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-10 23:20 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 23:20 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 23:18 | +10 stop | BTC | UP | 0.55 | 0.37 | -2.15 |
| 10-10 23:18 | +20 | BTC | UP | 0.55 | no | -5.68 |
| 10-10 23:18 | +15 | BTC | UP | 0.55 | no | -5.68 |
| 10-10 23:18 | +10 | BTC | UP | 0.55 | no | -5.68 |
| 10-10 23:18 | +5 | BTC | UP | 0.55 | 0.63 | 0.45 |
| 10-10 23:18 | +10 stop | ZEC | UP | 0.59 | 0.36 | -2.64 |
| 10-10 23:17 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-10 23:16 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 10-10 23:16 | +20 | BNB | DOWN | 0.56 | 0.82 | 2.31 |
| 10-10 23:16 | +15 | BNB | DOWN | 0.56 | 0.82 | 2.31 |
| 10-10 23:16 | +10 | BNB | DOWN | 0.57 | 0.68 | 0.78 |
| 10-10 23:16 | +5 | BNB | DOWN | 0.56 | 0.66 | 0.66 |
