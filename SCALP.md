# Range-Scalp Bot

*Updated Mon Nov 23 22:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70198 | 61262 | 8936 (147) | 1 | $-18850.27 | -4.3% |
| **+10¢** | 52377 | 41940 | 10437 (190) | 1 | $-17490.61 | -5.3% |
| **+15¢** | 43888 | 32648 | 11240 (246) | 0 | $-15574.02 | -5.7% |
| **+20¢** | 39074 | 27244 | 11830 (311) | 0 | $-13947.86 | -5.7% |
| **+10¢ (15¢ stop)** | 85507 | 85311 | 196 (118) | 0 | $-31478.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 22:29 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 22:29 | +10 stop | BTC | DOWN | 0.57 | 0.98 | 3.86 |
| 11-23 22:29 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 11-23 22:28 | +10 stop | ZEC | UP | 0.55 | 0.35 | -2.34 |
| 11-23 22:28 | +10 stop | NEAR | UP | 0.54 | 0.09 | -4.72 |
| 11-23 22:28 | +10 | NEAR | UP | 0.55 | open |  |
| 11-23 22:28 | +5 | NEAR | UP | 0.56 | open |  |
| 11-23 22:27 | +10 stop | BNB | UP | 0.67 | 0.35 | -3.56 |
| 11-23 22:27 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 11-23 22:27 | +10 stop | ZEC | DOWN | 0.60 | 0.37 | -2.63 |
| 11-23 22:27 | +15 | ZEC | DOWN | 0.59 | 0.76 | 1.40 |
| 11-23 22:27 | +10 | ZEC | DOWN | 0.60 | 0.76 | 1.32 |
| 11-23 22:27 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.28 |
| 11-23 22:27 | +10 stop | BNB | DOWN | 0.63 | 0.41 | -2.54 |
| 11-23 22:27 | +10 stop | SOL | DOWN | 0.56 | 0.28 | -3.13 |
| 11-23 22:27 | +20 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 11-23 22:27 | +15 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 11-23 22:27 | +10 | SOL | DOWN | 0.56 | 0.81 | 2.21 |
| 11-23 22:27 | +5 | SOL | DOWN | 0.55 | 0.81 | 2.31 |
| 11-23 22:27 | +10 stop | BTC | DOWN | 0.68 | 0.43 | -2.84 |
| 11-23 22:27 | +10 | BTC | DOWN | 0.68 | 0.98 | 2.78 |
| 11-23 22:27 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-23 22:24 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-23 22:24 | +20 | HYPE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-23 22:24 | +15 | HYPE | DOWN | 0.66 | 0.91 | 2.33 |
| 11-23 22:24 | +10 | HYPE | DOWN | 0.66 | 0.79 | 1.07 |
| 11-23 22:24 | +5 | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-23 22:23 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-23 22:21 | +10 stop | NEAR | UP | 0.64 | 0.46 | -2.15 |
| 11-23 22:21 | +10 stop | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-23 22:20 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 11-23 22:19 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 11-23 22:19 | +10 stop | ETH | UP | 0.69 | 0.35 | -3.71 |
| 11-23 22:19 | +5 | ETH | UP | 0.69 | 0.75 | 0.31 |
| 11-23 22:19 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 11-23 22:19 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-23 22:19 | +10 stop | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 11-23 22:19 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.90 |
| 11-23 22:18 | +10 stop | NEAR | DOWN | 0.41 | 0.54 | 0.95 |
| 11-23 22:18 | +10 stop | SOL | UP | 0.52 | 0.64 | 0.85 |
