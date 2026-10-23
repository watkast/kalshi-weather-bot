# Range-Scalp Bot

*Updated Fri Oct 23 16:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30610 | 26673 | 3937 (39) | 6 | $-8854.52 | -4.6% |
| **+10¢** | 22911 | 18354 | 4557 (56) | 5 | $-7927.32 | -5.5% |
| **+15¢** | 19174 | 14271 | 4903 (79) | 5 | $-7149.32 | -5.9% |
| **+20¢** | 16983 | 11847 | 5136 (102) | 5 | $-6409.18 | -6.0% |
| **+10¢ (15¢ stop)** | 37549 | 37490 | 59 (32) | 0 | $-14239.93 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 16:25 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-23 16:24 | +10 stop | ZEC | UP | 0.61 | 0.42 | -2.25 |
| 10-23 16:24 | +10 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-23 16:24 | +5 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-23 16:24 | +10 stop | HYPE | UP | 0.68 | 0.36 | -3.53 |
| 10-23 16:24 | +15 | HYPE | UP | 0.68 | open |  |
| 10-23 16:24 | +10 | HYPE | UP | 0.68 | open |  |
| 10-23 16:24 | +5 | HYPE | UP | 0.69 | open |  |
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
| 10-23 16:20 | +10 stop | BTC | DOWN | 0.57 | 0.39 | -2.15 |
| 10-23 16:20 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-23 16:18 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 16:18 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-23 16:18 | +10 stop | HYPE | UP | 0.63 | 0.47 | -1.93 |
| 10-23 16:18 | +10 stop | ZEC | UP | 0.61 | 0.78 | 1.40 |
| 10-23 16:17 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-23 16:17 | +10 stop | NEAR | DOWN | 0.54 | 0.67 | 0.96 |
| 10-23 16:17 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 10-23 16:17 | +5 | ETH | UP | 0.58 | open |  |
| 10-23 16:16 | +10 stop | BTC | UP | 0.64 | 0.48 | -1.95 |
| 10-23 16:16 | +10 stop | SOL | UP | 0.63 | 0.42 | -2.45 |
| 10-23 16:16 | +20 | SOL | UP | 0.63 | open |  |
