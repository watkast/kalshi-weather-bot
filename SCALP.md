# Range-Scalp Bot

*Updated Fri Oct 23 16:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30619 | 26676 | 3943 (39) | 0 | $-8892.27 | -4.6% |
| **+10¢** | 22919 | 18357 | 4562 (56) | 0 | $-7958.48 | -5.5% |
| **+15¢** | 19181 | 14273 | 4908 (79) | 0 | $-7179.62 | -6.0% |
| **+20¢** | 16990 | 11849 | 5141 (102) | 0 | $-6439.02 | -6.0% |
| **+10¢ (15¢ stop)** | 37552 | 37493 | 59 (32) | 0 | $-14240.28 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 16:33 | +10 stop | BNB | UP | 0.65 | 0.76 | 0.77 |
| 10-23 16:33 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-23 16:33 | +5 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-23 16:31 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-23 16:31 | +20 | BNB | UP | 0.66 | 0.87 | 1.86 |
| 10-23 16:31 | +15 | BNB | UP | 0.66 | 0.87 | 1.86 |
| 10-23 16:31 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-23 16:31 | +5 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-23 16:30 | +10 stop | DOGE | UP | 0.70 | 0.55 | -1.83 |
| 10-23 16:30 | +20 | DOGE | UP | 0.70 | 0.92 | 1.96 |
| 10-23 16:30 | +15 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-23 16:30 | +10 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 10-23 16:30 | +5 | DOGE | UP | 0.70 | 0.78 | 0.52 |
| 10-23 16:25 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-23 16:24 | +10 stop | ZEC | UP | 0.61 | 0.42 | -2.25 |
| 10-23 16:24 | +10 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-23 16:24 | +5 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-23 16:24 | +10 stop | HYPE | UP | 0.68 | 0.36 | -3.53 |
| 10-23 16:24 | +15 | HYPE | UP | 0.68 | no | -6.96 |
| 10-23 16:24 | +10 | HYPE | UP | 0.68 | no | -6.96 |
| 10-23 16:24 | +5 | HYPE | UP | 0.69 | no | -7.05 |
| 10-23 16:23 | +10 stop | NEAR | DOWN | 0.58 | 0.78 | 1.69 |
| 10-23 16:23 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-23 16:23 | +10 stop | ETH | DOWN | 0.68 | 0.53 | -1.84 |
| 10-23 16:23 | +20 | ETH | DOWN | 0.66 | 0.88 | 1.96 |
| 10-23 16:23 | +15 | ETH | DOWN | 0.66 | 0.88 | 1.96 |
| 10-23 16:23 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-23 16:23 | +10 stop | BTC | UP | 0.45 | 0.57 | 0.84 |
| 10-23 16:22 | +10 stop | DOGE | UP | 0.61 | 0.42 | -2.25 |
| 10-23 16:22 | +10 stop | HYPE | UP | 0.70 | 0.83 | 1.05 |
| 10-23 16:22 | +10 stop | BNB | DOWN | 0.71 | 0.88 | 1.47 |
| 10-23 16:22 | +20 | BNB | DOWN | 0.71 | 0.92 | 1.88 |
| 10-23 16:22 | +15 | BNB | DOWN | 0.71 | 0.88 | 1.47 |
| 10-23 16:22 | +10 | BNB | DOWN | 0.71 | 0.88 | 1.47 |
| 10-23 16:22 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-23 16:22 | +10 stop | SOL | DOWN | 0.57 | 0.71 | 1.10 |
| 10-23 16:22 | +10 stop | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 10-23 16:21 | +10 | BTC | DOWN | 0.56 | 0.74 | 1.48 |
| 10-23 16:21 | +5 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-23 16:20 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.14 |
