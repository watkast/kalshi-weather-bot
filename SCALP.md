# Range-Scalp Bot

*Updated Thu Oct 08 02:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7125 | 6188 | 937 (13) | 0 | $-2106.04 | -4.7% |
| **+10¢** | 5403 | 4301 | 1102 (20) | 0 | $-2021.82 | -5.9% |
| **+15¢** | 4533 | 3371 | 1162 (28) | 0 | $-1653.13 | -5.8% |
| **+20¢** | 4051 | 2840 | 1211 (35) | 0 | $-1306.90 | -5.1% |
| **+10¢ (15¢ stop)** | 8619 | 8597 | 22 (14) | 0 | $-3069.95 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 01:54 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-08 01:54 | +10 | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-08 01:54 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 10-08 01:53 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-08 01:52 | +10 stop | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-08 01:52 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-08 01:51 | +10 stop | NEAR | UP | 0.52 | 0.29 | -2.65 |
| 10-08 01:51 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-08 01:51 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-08 01:50 | +10 stop | SOL | UP | 0.48 | 0.61 | 0.96 |
| 10-08 01:50 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.95 |
| 10-08 01:50 | +10 stop | DOGE | UP | 0.69 | 0.51 | -2.13 |
| 10-08 01:50 | +10 stop | NEAR | UP | 0.68 | 0.51 | -2.04 |
| 10-08 01:49 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-08 01:49 | +10 stop | XRP | UP | 0.62 | 0.75 | 0.99 |
| 10-08 01:49 | +5 | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 10-08 01:48 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 10-08 01:47 | +10 stop | SOL | DOWN | 0.59 | 0.35 | -2.70 |
| 10-08 01:47 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.74 |
| 10-08 01:47 | +15 | SOL | DOWN | 0.59 | 0.74 | 1.22 |
| 10-08 01:47 | +10 | SOL | DOWN | 0.59 | 0.74 | 1.22 |
| 10-08 01:47 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.19 |
| 10-08 01:47 | +10 stop | ZEC | DOWN | 0.69 | 0.46 | -2.63 |
| 10-08 01:47 | +20 | ZEC | DOWN | 0.69 | 0.91 | 1.97 |
| 10-08 01:47 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-08 01:47 | +10 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-08 01:47 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-08 01:46 | +10 stop | DOGE | DOWN | 0.68 | 0.53 | -1.84 |
| 10-08 01:46 | +20 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-08 01:46 | +15 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 01:46 | +10 | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-08 01:46 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-08 01:46 | +10 stop | ETH | DOWN | 0.68 | 0.46 | -2.54 |
| 10-08 01:46 | +20 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 01:46 | +15 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 10-08 01:46 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 01:46 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-08 01:46 | +10 stop | XRP | DOWN | 0.61 | 0.46 | -1.85 |
| 10-08 01:46 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 10-08 01:46 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
