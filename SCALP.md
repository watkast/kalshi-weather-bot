# Range-Scalp Bot

*Updated Sat Oct 17 15:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21157 | 18415 | 2742 (29) | 0 | $-6164.87 | -4.6% |
| **+10¢** | 15929 | 12764 | 3165 (41) | 0 | $-5483.49 | -5.5% |
| **+15¢** | 13317 | 9908 | 3409 (61) | 0 | $-4976.85 | -6.0% |
| **+20¢** | 11805 | 8234 | 3571 (80) | 0 | $-4403.48 | -5.9% |
| **+10¢ (15¢ stop)** | 25992 | 25942 | 50 (29) | 0 | $-9889.45 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 15:19 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 15:19 | +20 | XRP | DOWN | 0.70 | 0.95 | 2.27 |
| 10-17 15:19 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 10-17 15:19 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-17 15:19 | +5 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-17 15:18 | +10 stop | HYPE | UP | 0.56 | 0.37 | -2.29 |
| 10-17 15:18 | +10 stop | BTC | UP | 0.53 | 0.32 | -2.44 |
| 10-17 15:18 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 10-17 15:17 | +10 stop | SOL | UP | 0.63 | 0.43 | -2.35 |
| 10-17 15:17 | +10 stop | DOGE | UP | 0.69 | 0.44 | -2.83 |
| 10-17 15:17 | +5 | NEAR | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 15:16 | +5 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-17 15:16 | +10 stop | DOGE | DOWN | 0.65 | 0.39 | -2.93 |
| 10-17 15:16 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-17 15:16 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 15:16 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 15:16 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-17 15:16 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
| 10-17 15:16 | +20 | SOL | DOWN | 0.56 | 0.78 | 1.89 |
| 10-17 15:16 | +15 | SOL | DOWN | 0.56 | 0.78 | 1.89 |
| 10-17 15:16 | +10 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 10-17 15:16 | +5 | SOL | DOWN | 0.56 | 0.65 | 0.56 |
| 10-17 15:16 | +10 stop | BTC | DOWN | 0.64 | 0.44 | -2.35 |
| 10-17 15:16 | +20 | BTC | DOWN | 0.64 | 0.87 | 2.05 |
| 10-17 15:16 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-17 15:16 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-17 15:16 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-17 15:16 | +10 stop | NEAR | DOWN | 0.63 | 0.48 | -1.85 |
| 10-17 15:16 | +20 | NEAR | DOWN | 0.62 | 0.89 | 2.46 |
| 10-17 15:16 | +15 | NEAR | DOWN | 0.62 | 0.81 | 1.62 |
| 10-17 15:16 | +10 | NEAR | DOWN | 0.62 | 0.81 | 1.62 |
| 10-17 15:16 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-17 15:16 | +10 stop | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-17 15:16 | +20 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-17 15:16 | +15 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-17 15:16 | +10 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-17 15:16 | +5 | BNB | DOWN | 0.63 | 0.72 | 0.58 |
| 10-17 15:16 | +10 stop | ETH | DOWN | 0.52 | 0.30 | -2.53 |
| 10-17 15:16 | +20 | ETH | DOWN | 0.52 | 0.74 | 1.88 |
| 10-17 15:16 | +15 | ETH | DOWN | 0.52 | 0.74 | 1.88 |
