# Range-Scalp Bot

*Updated Wed Nov 18 08:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63848 | 55687 | 8161 (119) | 0 | $-17443.79 | -4.3% |
| **+10¢** | 47707 | 38155 | 9552 (160) | 1 | $-16350.32 | -5.5% |
| **+15¢** | 40002 | 29703 | 10299 (205) | 1 | $-14814.38 | -5.9% |
| **+20¢** | 35627 | 24816 | 10811 (260) | 1 | $-13104.24 | -5.9% |
| **+10¢ (15¢ stop)** | 77676 | 77518 | 158 (93) | 1 | $-28526.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 08:30 | +10 stop | XRP | DOWN | 0.52 | open |  |
| 11-18 08:30 | +20 | XRP | DOWN | 0.52 | open |  |
| 11-18 08:30 | +15 | XRP | DOWN | 0.52 | open |  |
| 11-18 08:30 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-18 08:30 | +5 | XRP | DOWN | 0.52 | 0.59 | 0.35 |
| 11-18 08:29 | +10 stop | HYPE | DOWN | 0.37 | 0.47 | 0.65 |
| 11-18 08:29 | +15 | HYPE | DOWN | 0.38 | 1.00 | 6.02 |
| 11-18 08:29 | +10 | HYPE | DOWN | 0.38 | 1.00 | 6.01 |
| 11-18 08:29 | +5 | HYPE | DOWN | 0.38 | 0.47 | 0.55 |
| 11-18 08:27 | +10 stop | HYPE | UP | 0.48 | 0.18 | -3.29 |
| 11-18 08:25 | +10 stop | ZEC | UP | 0.71 | 0.40 | -3.42 |
| 11-18 08:25 | +20 | ZEC | UP | 0.71 | no | -7.25 |
| 11-18 08:25 | +15 | ZEC | UP | 0.71 | no | -7.25 |
| 11-18 08:25 | +10 | ZEC | UP | 0.71 | no | -7.25 |
| 11-18 08:25 | +5 | ZEC | UP | 0.71 | no | -7.25 |
| 11-18 08:23 | +10 stop | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 11-18 08:22 | +10 stop | ZEC | UP | 0.57 | 0.72 | 1.17 |
| 11-18 08:22 | +10 stop | HYPE | DOWN | 0.62 | 0.42 | -2.34 |
| 11-18 08:22 | +15 | HYPE | DOWN | 0.62 | 0.80 | 1.52 |
| 11-18 08:22 | +10 | HYPE | DOWN | 0.62 | 0.80 | 1.52 |
| 11-18 08:22 | +5 | HYPE | DOWN | 0.62 | 0.80 | 1.52 |
| 11-18 08:21 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-18 08:20 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-18 08:20 | +10 stop | SOL | DOWN | 0.66 | 0.36 | -3.33 |
| 11-18 08:20 | +10 stop | NEAR | DOWN | 0.70 | 0.55 | -1.86 |
| 11-18 08:19 | +5 | BTC | UP | 0.57 | 0.64 | 0.35 |
| 11-18 08:19 | +10 stop | BNB | UP | 0.60 | 0.76 | 1.30 |
| 11-18 08:19 | +5 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 08:19 | +10 stop | DOGE | DOWN | 0.70 | 0.50 | -2.33 |
| 11-18 08:18 | +5 | BTC | UP | 0.58 | 0.66 | 0.46 |
| 11-18 08:18 | +10 stop | ETH | UP | 0.55 | 0.67 | 0.86 |
| 11-18 08:18 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.76 |
| 11-18 08:17 | +10 stop | ZEC | DOWN | 0.55 | 0.69 | 1.07 |
| 11-18 08:17 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-18 08:17 | +5 | BTC | UP | 0.56 | 0.65 | 0.56 |
| 11-18 08:17 | +5 | SOL | UP | 0.52 | 0.61 | 0.55 |
| 11-18 08:17 | +10 stop | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 08:17 | +20 | HYPE | DOWN | 0.68 | 1.00 | 3.02 |
| 11-18 08:17 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-18 08:17 | +10 | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
