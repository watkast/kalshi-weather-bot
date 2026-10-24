# Range-Scalp Bot

*Updated Sat Oct 24 00:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31168 | 27163 | 4005 (40) | 1 | $-8996.24 | -4.6% |
| **+10¢** | 23316 | 18687 | 4629 (58) | 1 | $-8006.04 | -5.5% |
| **+15¢** | 19506 | 14526 | 4980 (81) | 1 | $-7209.25 | -5.9% |
| **+20¢** | 17277 | 12061 | 5216 (103) | 1 | $-6456.56 | -5.9% |
| **+10¢ (15¢ stop)** | 38228 | 38169 | 59 (32) | 0 | $-14582.38 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 00:18 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.79 |
| 10-24 00:18 | +10 | ZEC | DOWN | 0.68 | 0.81 | 0.99 |
| 10-24 00:18 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.61 |
| 10-24 00:18 | +10 stop | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 10-24 00:17 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-24 00:17 | +20 | SOL | DOWN | 0.66 | 0.89 | 2.07 |
| 10-24 00:17 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-24 00:17 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-24 00:17 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 10-24 00:16 | +10 stop | ZEC | DOWN | 0.52 | 0.63 | 0.75 |
| 10-24 00:16 | +20 | ZEC | DOWN | 0.53 | 0.75 | 1.90 |
| 10-24 00:16 | +15 | ZEC | DOWN | 0.53 | 0.69 | 1.29 |
| 10-24 00:16 | +10 | ZEC | DOWN | 0.53 | 0.63 | 0.67 |
| 10-24 00:16 | +5 | ZEC | DOWN | 0.53 | 0.63 | 0.65 |
| 10-24 00:16 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 00:16 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-24 00:16 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 00:16 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 00:16 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 10-24 00:16 | +10 stop | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-24 00:16 | +20 | NEAR | DOWN | 0.66 | 0.86 | 1.75 |
| 10-24 00:16 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-24 00:16 | +10 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-24 00:16 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-24 00:16 | +10 stop | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-24 00:16 | +20 | ETH | DOWN | 0.57 | 0.80 | 2.00 |
| 10-24 00:16 | +15 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 10-24 00:16 | +10 | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-24 00:16 | +5 | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-24 00:16 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-24 00:16 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-24 00:16 | +15 | BTC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-24 00:16 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-24 00:16 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-24 00:16 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 10-24 00:16 | +20 | XRP | DOWN | 0.58 | 0.78 | 1.69 |
| 10-24 00:16 | +15 | XRP | DOWN | 0.58 | 0.76 | 1.49 |
| 10-24 00:16 | +10 | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 10-24 00:16 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.56 |
| 10-24 00:16 | +10 stop | BNB | UP | 0.55 | 0.36 | -2.25 |
