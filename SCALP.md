# Range-Scalp Bot

*Updated Sun Oct 25 10:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33021 | 28811 | 4210 (42) | 1 | $-9263.73 | -4.5% |
| **+10¢** | 24712 | 19839 | 4873 (60) | 0 | $-8241.88 | -5.3% |
| **+15¢** | 20681 | 15437 | 5244 (83) | 0 | $-7400.73 | -5.7% |
| **+20¢** | 18322 | 12831 | 5491 (105) | 0 | $-6528.94 | -5.7% |
| **+10¢ (15¢ stop)** | 40515 | 40455 | 60 (32) | 0 | $-15434.79 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 10:25 | +10 stop | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-25 10:25 | +10 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-25 10:25 | +5 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-25 10:24 | +5 | BNB | UP | 0.62 | open |  |
| 10-25 10:23 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 10-25 10:23 | +5 | BNB | UP | 0.57 | 0.64 | 0.35 |
| 10-25 10:23 | +5 | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 10-25 10:23 | +10 stop | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 10:23 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 10:23 | +10 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 10:23 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-25 10:22 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 10:22 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 10:22 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 10:22 | +10 stop | HYPE | UP | 0.63 | 0.42 | -2.41 |
| 10-25 10:21 | +10 stop | NEAR | DOWN | 0.56 | 0.77 | 1.79 |
| 10-25 10:21 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 10-25 10:20 | +10 stop | HYPE | DOWN | 0.67 | 0.47 | -2.34 |
| 10-25 10:20 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 10:20 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 10:20 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 10-25 10:20 | +5 | NEAR | DOWN | 0.48 | 0.55 | 0.34 |
| 10-25 10:19 | +5 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-25 10:18 | +10 stop | NEAR | DOWN | 0.64 | 0.45 | -2.25 |
| 10-25 10:18 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-25 10:18 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 10-25 10:17 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-25 10:17 | +20 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-25 10:17 | +15 | ETH | DOWN | 0.67 | 0.85 | 1.55 |
| 10-25 10:17 | +10 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-25 10:17 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-25 10:17 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-25 10:17 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 10-25 10:17 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-25 10:17 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-25 10:17 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-25 10:17 | +5 | BNB | DOWN | 0.46 | 0.60 | 1.05 |
| 10-25 10:16 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-25 10:16 | +20 | HYPE | DOWN | 0.70 | 0.96 | 2.41 |
| 10-25 10:16 | +15 | HYPE | DOWN | 0.70 | 0.89 | 1.68 |
