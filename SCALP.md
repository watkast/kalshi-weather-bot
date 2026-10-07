# Range-Scalp Bot

*Updated Wed Oct 07 07:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6136 | 5320 | 816 (9) | 0 | $-1884.40 | -4.9% |
| **+10¢** | 4678 | 3721 | 957 (16) | 1 | $-1755.73 | -6.0% |
| **+15¢** | 3930 | 2918 | 1012 (20) | 2 | $-1493.92 | -6.1% |
| **+20¢** | 3514 | 2456 | 1058 (27) | 1 | $-1230.25 | -5.6% |
| **+10¢ (15¢ stop)** | 7441 | 7426 | 15 (9) | 0 | $-2567.75 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 07:23 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-07 07:23 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-07 07:23 | +20 | BTC | DOWN | 0.63 | 0.88 | 2.25 |
| 10-07 07:23 | +15 | BTC | DOWN | 0.63 | 0.88 | 2.25 |
| 10-07 07:23 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-07 07:23 | +5 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-07 07:23 | +5 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-07 07:23 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-07 07:23 | +10 | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-07 07:23 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-07 07:23 | +10 stop | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-07 07:23 | +15 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 10-07 07:23 | +10 | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-07 07:23 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.63 |
| 10-07 07:23 | +10 stop | ETH | UP | 0.51 | 0.33 | -2.14 |
| 10-07 07:23 | +15 | ETH | UP | 0.51 | open |  |
| 10-07 07:23 | +10 | ETH | UP | 0.51 | open |  |
| 10-07 07:23 | +5 | ETH | UP | 0.51 | 0.60 | 0.55 |
| 10-07 07:22 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-07 07:22 | +10 stop | ETH | DOWN | 0.48 | 0.69 | 1.77 |
| 10-07 07:22 | +20 | ETH | DOWN | 0.50 | 0.77 | 2.39 |
| 10-07 07:22 | +15 | ETH | DOWN | 0.50 | 0.69 | 1.57 |
| 10-07 07:22 | +10 | ETH | DOWN | 0.50 | 0.69 | 1.57 |
| 10-07 07:22 | +5 | ETH | DOWN | 0.50 | 0.69 | 1.57 |
| 10-07 07:22 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-07 07:22 | +20 | HYPE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-07 07:22 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 10-07 07:22 | +10 | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-07 07:22 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-07 07:19 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.39 |
| 10-07 07:19 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-07 07:19 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-07 07:19 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-07 07:18 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-07 07:18 | +10 stop | BNB | DOWN | 0.51 | 0.35 | -1.94 |
| 10-07 07:18 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.14 |
| 10-07 07:18 | +10 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-07 07:18 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-07 07:17 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-07 07:17 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
