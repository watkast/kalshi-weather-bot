# Range-Scalp Bot

*Updated Fri Oct 16 18:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19637 | 17065 | 2572 (29) | 2 | $-5906.36 | -4.8% |
| **+10¢** | 14803 | 11833 | 2970 (41) | 4 | $-5303.07 | -5.7% |
| **+15¢** | 12390 | 9197 | 3193 (60) | 4 | $-4778.99 | -6.1% |
| **+20¢** | 10991 | 7646 | 3345 (79) | 3 | $-4235.68 | -6.1% |
| **+10¢ (15¢ stop)** | 24170 | 24120 | 50 (29) | 0 | $-9284.04 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 18:42 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-16 18:42 | +5 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-16 18:42 | +10 stop | ETH | UP | 0.51 | 0.09 | -4.48 |
| 10-16 18:42 | +15 | ETH | UP | 0.51 | open |  |
| 10-16 18:42 | +10 | ETH | UP | 0.51 | open |  |
| 10-16 18:42 | +5 | ETH | UP | 0.51 | 0.58 | 0.34 |
| 10-16 18:42 | +10 stop | BTC | UP | 0.64 | 0.01 | -6.53 |
| 10-16 18:42 | +15 | BTC | UP | 0.64 | open |  |
| 10-16 18:42 | +10 | BTC | UP | 0.64 | open |  |
| 10-16 18:42 | +5 | BTC | UP | 0.64 | open |  |
| 10-16 18:42 | +15 | ZEC | UP | 0.52 | open |  |
| 10-16 18:42 | +5 | ZEC | UP | 0.52 | 0.59 | 0.35 |
| 10-16 18:42 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 10-16 18:41 | +10 stop | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 18:41 | +5 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 18:41 | +20 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-16 18:40 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 18:40 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 18:40 | +5 | ZEC | UP | 0.62 | 0.69 | 0.38 |
| 10-16 18:40 | +10 stop | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 10-16 18:40 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 10-16 18:40 | +10 | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 10-16 18:40 | +5 | HYPE | DOWN | 0.67 | 0.81 | 1.13 |
| 10-16 18:40 | +10 stop | XRP | UP | 0.47 | 0.58 | 0.74 |
| 10-16 18:40 | +10 stop | BNB | UP | 0.44 | 0.61 | 1.35 |
| 10-16 18:40 | +10 stop | HYPE | DOWN | 0.46 | 0.64 | 1.45 |
| 10-16 18:40 | +20 | HYPE | DOWN | 0.46 | 0.69 | 1.97 |
| 10-16 18:40 | +15 | HYPE | DOWN | 0.46 | 0.64 | 1.45 |
| 10-16 18:40 | +10 | HYPE | DOWN | 0.46 | 0.64 | 1.45 |
| 10-16 18:40 | +5 | HYPE | DOWN | 0.46 | 0.64 | 1.45 |
| 10-16 18:39 | +5 | BTC | UP | 0.63 | 0.80 | 1.41 |
| 10-16 18:39 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 18:39 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.82 |
| 10-16 18:39 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-16 18:39 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 18:39 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-16 18:39 | +10 stop | ZEC | UP | 0.64 | 0.48 | -1.98 |
| 10-16 18:39 | +10 | ZEC | UP | 0.64 | open |  |
| 10-16 18:39 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-16 18:38 | +10 stop | ZEC | UP | 0.49 | 0.60 | 0.72 |
