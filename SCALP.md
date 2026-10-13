# Range-Scalp Bot

*Updated Tue Oct 13 10:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14512 | 12544 | 1968 (27) | 1 | $-4728.99 | -5.2% |
| **+10¢** | 10980 | 8696 | 2284 (39) | 1 | $-4442.91 | -6.4% |
| **+15¢** | 9228 | 6786 | 2442 (57) | 2 | $-3954.25 | -6.8% |
| **+20¢** | 8213 | 5670 | 2543 (72) | 1 | $-3407.98 | -6.6% |
| **+10¢ (15¢ stop)** | 17809 | 17760 | 49 (29) | 0 | $-6924.79 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 10:28 | +10 stop | NEAR | UP | 0.65 | 0.96 | 2.90 |
| 10-13 10:27 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-13 10:25 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 10:25 | +10 stop | XRP | DOWN | 0.67 | 0.89 | 1.97 |
| 10-13 10:23 | +10 stop | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-13 10:23 | +15 | ETH | UP | 0.60 | open |  |
| 10-13 10:23 | +10 | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-13 10:23 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-13 10:23 | +10 stop | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 10-13 10:23 | +20 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 10-13 10:23 | +15 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 10-13 10:23 | +10 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 10-13 10:23 | +5 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 10-13 10:22 | +20 | BTC | DOWN | 0.69 | 0.97 | 2.65 |
| 10-13 10:22 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-13 10:22 | +5 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-13 10:21 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-13 10:21 | +10 stop | NEAR | UP | 0.53 | 0.68 | 1.16 |
| 10-13 10:21 | +10 stop | BTC | DOWN | 0.66 | 0.41 | -2.83 |
| 10-13 10:21 | +10 | BTC | DOWN | 0.63 | 0.87 | 2.15 |
| 10-13 10:21 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 10-13 10:20 | +10 stop | XRP | DOWN | 0.71 | 0.53 | -2.13 |
| 10-13 10:20 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.87 |
| 10-13 10:20 | +15 | XRP | DOWN | 0.71 | 0.89 | 1.58 |
| 10-13 10:20 | +10 | XRP | DOWN | 0.71 | 0.89 | 1.58 |
| 10-13 10:20 | +5 | XRP | DOWN | 0.71 | 0.89 | 1.58 |
| 10-13 10:20 | +10 stop | ZEC | DOWN | 0.55 | 0.33 | -2.56 |
| 10-13 10:20 | +10 stop | DOGE | DOWN | 0.71 | 0.53 | -2.13 |
| 10-13 10:20 | +20 | DOGE | DOWN | 0.71 | 0.94 | 2.13 |
| 10-13 10:20 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-13 10:20 | +10 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-13 10:20 | +5 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-13 10:20 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-13 10:20 | +20 | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 10-13 10:20 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 10-13 10:20 | +10 | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-13 10:20 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.30 |
| 10-13 10:20 | +10 stop | HYPE | DOWN | 0.53 | 0.28 | -2.83 |
| 10-13 10:20 | +20 | HYPE | DOWN | 0.53 | 0.74 | 1.78 |
| 10-13 10:20 | +15 | HYPE | DOWN | 0.53 | 0.74 | 1.78 |
