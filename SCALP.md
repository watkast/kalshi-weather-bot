# Range-Scalp Bot

*Updated Sun Oct 04 07:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1944 | 1677 | 267 (3) | 1 | $-645.34 | -5.2% |
| **+10¢** | 1509 | 1213 | 296 (4) | 1 | $-467.39 | -4.9% |
| **+15¢** | 1272 | 958 | 314 (5) | 1 | $-395.33 | -4.9% |
| **+20¢** | 1125 | 793 | 332 (7) | 1 | $-370.00 | -5.2% |
| **+10¢ (15¢ stop)** | 2432 | 2431 | 1 (1) | 0 | $-963.69 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 07:26 | +10 stop | XRP | UP | 0.32 | 0.56 | 2.06 |
| 10-04 07:25 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 07:25 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 07:25 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 07:25 | +20 | SOL | DOWN | 0.68 | 0.90 | 2.01 |
| 10-04 07:25 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-04 07:24 | +5 | XRP | UP | 0.59 | open |  |
| 10-04 07:24 | +10 stop | XRP | UP | 0.56 | 0.34 | -2.54 |
| 10-04 07:24 | +10 | XRP | UP | 0.56 | open |  |
| 10-04 07:24 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 10-04 07:24 | +10 stop | BTC | DOWN | 0.66 | 0.36 | -3.33 |
| 10-04 07:24 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-04 07:24 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 07:24 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-04 07:24 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-04 07:23 | +10 stop | XRP | UP | 0.55 | 0.65 | 0.66 |
| 10-04 07:23 | +10 | XRP | UP | 0.55 | 0.65 | 0.66 |
| 10-04 07:23 | +5 | XRP | UP | 0.56 | 0.65 | 0.56 |
| 10-04 07:22 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 10-04 07:22 | +20 | XRP | UP | 0.58 | open |  |
| 10-04 07:22 | +15 | XRP | UP | 0.58 | open |  |
| 10-04 07:22 | +10 | XRP | UP | 0.58 | 0.69 | 0.74 |
| 10-04 07:22 | +5 | XRP | UP | 0.58 | 0.69 | 0.77 |
| 10-04 07:21 | +10 stop | NEAR | UP | 0.55 | 0.31 | -2.72 |
| 10-04 07:21 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-04 07:21 | +20 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-04 07:21 | +15 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-04 07:21 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-04 07:21 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 10-04 07:20 | +10 stop | NEAR | DOWN | 0.63 | 0.47 | -1.96 |
| 10-04 07:20 | +20 | NEAR | DOWN | 0.63 | 0.86 | 2.03 |
| 10-04 07:20 | +15 | NEAR | DOWN | 0.63 | 0.82 | 1.61 |
| 10-04 07:20 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.78 |
| 10-04 07:20 | +5 | NEAR | DOWN | 0.63 | 0.74 | 0.78 |
| 10-04 07:19 | +5 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-04 07:19 | +10 stop | HYPE | UP | 0.62 | 0.75 | 0.99 |
| 10-04 07:17 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-04 07:17 | +10 stop | HYPE | UP | 0.68 | 0.53 | -1.88 |
| 10-04 07:17 | +20 | HYPE | UP | 0.68 | 0.89 | 1.83 |
| 10-04 07:17 | +15 | HYPE | UP | 0.68 | 0.84 | 1.30 |
