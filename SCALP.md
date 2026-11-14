# Range-Scalp Bot

*Updated Sat Nov 14 17:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59654 | 52051 | 7603 (107) | 0 | $-16123.40 | -4.3% |
| **+10¢** | 44565 | 35663 | 8902 (143) | 0 | $-15140.35 | -5.4% |
| **+15¢** | 37343 | 27744 | 9599 (180) | 0 | $-13760.45 | -5.9% |
| **+20¢** | 33264 | 23190 | 10074 (232) | 0 | $-12126.13 | -5.8% |
| **+10¢ (15¢ stop)** | 72583 | 72440 | 143 (82) | 0 | $-26682.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 17:50 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 17:48 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 17:48 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-14 17:48 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-14 17:48 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 17:48 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-14 17:48 | +10 stop | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-14 17:48 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-14 17:48 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-14 17:48 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-14 17:48 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-14 17:46 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-14 17:46 | +20 | XRP | DOWN | 0.61 | 0.83 | 1.93 |
| 11-14 17:46 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-14 17:46 | +10 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 17:46 | +5 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 17:46 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 17:46 | +20 | ETH | DOWN | 0.68 | 0.90 | 2.00 |
| 11-14 17:46 | +15 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 11-14 17:46 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 17:46 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 11-14 17:46 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 17:46 | +20 | BNB | DOWN | 0.66 | 0.87 | 1.86 |
| 11-14 17:46 | +15 | BNB | DOWN | 0.66 | 0.83 | 1.44 |
| 11-14 17:46 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 17:46 | +5 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 17:46 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 17:46 | +20 | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 11-14 17:46 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 17:46 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 17:46 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 17:46 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 17:46 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-14 17:46 | +15 | NEAR | DOWN | 0.67 | 0.83 | 1.34 |
| 11-14 17:46 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 17:46 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 11-14 17:43 | +10 stop | XRP | UP | 0.44 | 0.59 | 1.15 |
| 11-14 17:43 | +10 stop | SOL | DOWN | 0.71 | 0.52 | -2.23 |
| 11-14 17:41 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 11-14 17:37 | +15 | DOGE | UP | 0.65 | 0.80 | 1.22 |
