# Range-Scalp Bot

*Updated Thu Oct 08 14:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7582 | 6570 | 1012 (13) | 0 | $-2362.40 | -4.9% |
| **+10¢** | 5750 | 4555 | 1195 (24) | 0 | $-2308.61 | -6.4% |
| **+15¢** | 4832 | 3573 | 1259 (32) | 0 | $-1903.15 | -6.3% |
| **+20¢** | 4317 | 3011 | 1306 (40) | 0 | $-1498.48 | -5.5% |
| **+10¢ (15¢ stop)** | 9197 | 9168 | 29 (18) | 0 | $-3358.61 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 14:36 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 10-08 14:36 | +10 stop | XRP | DOWN | 0.65 | 0.83 | 1.54 |
| 10-08 14:35 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-08 14:35 | +10 stop | XRP | UP | 0.57 | 0.40 | -2.05 |
| 10-08 14:35 | +10 stop | NEAR | UP | 0.56 | 0.37 | -2.22 |
| 10-08 14:35 | +10 stop | BNB | UP | 0.52 | 0.36 | -1.95 |
| 10-08 14:34 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 10-08 14:34 | +10 stop | DOGE | UP | 0.63 | 0.36 | -3.04 |
| 10-08 14:34 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 10-08 14:34 | +10 stop | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 10-08 14:32 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-08 14:32 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-08 14:32 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-08 14:32 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 10-08 14:32 | +10 stop | NEAR | DOWN | 0.61 | 0.44 | -2.05 |
| 10-08 14:32 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 10-08 14:32 | +15 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 10-08 14:32 | +10 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 10-08 14:32 | +5 | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 10-08 14:31 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 14:31 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.79 |
| 10-08 14:31 | +15 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-08 14:31 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 14:31 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-08 14:31 | +10 stop | BNB | DOWN | 0.64 | 0.47 | -2.09 |
| 10-08 14:31 | +20 | BNB | DOWN | 0.64 | 0.88 | 2.11 |
| 10-08 14:31 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-08 14:31 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-08 14:31 | +5 | BNB | DOWN | 0.64 | 0.72 | 0.48 |
| 10-08 14:31 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.92 |
| 10-08 14:31 | +20 | DOGE | DOWN | 0.66 | 0.86 | 1.77 |
| 10-08 14:31 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.25 |
| 10-08 14:31 | +10 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-08 14:31 | +5 | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-08 14:31 | +10 stop | SOL | DOWN | 0.63 | 0.42 | -2.45 |
| 10-08 14:31 | +20 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 10-08 14:31 | +15 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 10-08 14:31 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-08 14:31 | +5 | SOL | DOWN | 0.63 | 0.70 | 0.38 |
| 10-08 14:31 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
