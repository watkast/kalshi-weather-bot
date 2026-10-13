# Range-Scalp Bot

*Updated Tue Oct 13 08:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14414 | 12462 | 1952 (27) | 0 | $-4677.30 | -5.1% |
| **+10¢** | 10904 | 8636 | 2268 (39) | 0 | $-4410.48 | -6.4% |
| **+15¢** | 9159 | 6733 | 2426 (57) | 0 | $-3938.82 | -6.9% |
| **+20¢** | 8152 | 5625 | 2527 (72) | 0 | $-3398.36 | -6.6% |
| **+10¢ (15¢ stop)** | 17671 | 17622 | 49 (29) | 0 | $-6853.98 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 08:23 | +10 stop | HYPE | UP | 0.60 | 0.37 | -2.64 |
| 10-13 08:21 | +10 stop | HYPE | DOWN | 0.65 | 0.47 | -2.18 |
| 10-13 08:21 | +20 | HYPE | DOWN | 0.65 | 0.94 | 2.64 |
| 10-13 08:21 | +15 | HYPE | DOWN | 0.65 | 0.94 | 2.64 |
| 10-13 08:21 | +10 | HYPE | DOWN | 0.65 | 0.94 | 2.64 |
| 10-13 08:21 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.35 |
| 10-13 08:16 | +10 stop | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-13 08:16 | +20 | HYPE | DOWN | 0.60 | 0.80 | 1.71 |
| 10-13 08:16 | +15 | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-13 08:16 | +10 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-13 08:16 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-13 08:16 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-13 08:16 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-13 08:16 | +15 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 10-13 08:16 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-13 08:16 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-13 08:11 | +10 stop | ETH | UP | 0.71 | 0.89 | 1.58 |
| 10-13 08:11 | +5 | SOL | UP | 0.60 | 0.74 | 1.09 |
| 10-13 08:07 | +10 stop | SOL | DOWN | 0.54 | 0.25 | -3.22 |
| 10-13 08:07 | +10 | SOL | DOWN | 0.54 | yes | -5.58 |
| 10-13 08:07 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 10-13 08:07 | +10 stop | HYPE | UP | 0.64 | 0.78 | 1.06 |
| 10-13 08:07 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 10-13 08:07 | +10 stop | ETH | DOWN | 0.64 | 0.46 | -2.15 |
| 10-13 08:06 | +10 stop | HYPE | DOWN | 0.57 | 0.39 | -2.15 |
| 10-13 08:06 | +10 stop | XRP | UP | 0.48 | 0.62 | 1.05 |
| 10-13 08:06 | +10 stop | NEAR | UP | 0.50 | 0.65 | 1.16 |
| 10-13 08:06 | +10 stop | BNB | UP | 0.67 | 0.81 | 1.13 |
| 10-13 08:05 | +10 stop | HYPE | UP | 0.62 | 0.45 | -2.05 |
| 10-13 08:05 | +10 stop | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-13 08:05 | +10 stop | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 10-13 08:05 | +10 | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 10-13 08:05 | +5 | ZEC | UP | 0.69 | 0.75 | 0.31 |
| 10-13 08:04 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-13 08:04 | +10 stop | XRP | UP | 0.66 | 0.46 | -2.34 |
| 10-13 08:03 | +10 stop | NEAR | UP | 0.69 | 0.48 | -2.43 |
| 10-13 08:03 | +10 | NEAR | UP | 0.69 | 0.87 | 1.57 |
| 10-13 08:03 | +5 | NEAR | UP | 0.69 | 0.78 | 0.62 |
| 10-13 08:03 | +10 stop | DOGE | UP | 0.67 | 0.48 | -2.24 |
| 10-13 08:03 | +10 stop | HYPE | UP | 0.67 | 0.51 | -1.94 |
