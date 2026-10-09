# Range-Scalp Bot

*Updated Fri Oct 09 18:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9316 | 8035 | 1281 (17) | 1 | $-3191.87 | -5.4% |
| **+10¢** | 7036 | 5535 | 1501 (29) | 0 | $-3113.26 | -7.0% |
| **+15¢** | 5930 | 4350 | 1580 (42) | 0 | $-2578.62 | -6.9% |
| **+20¢** | 5278 | 3637 | 1641 (53) | 1 | $-2164.13 | -6.5% |
| **+10¢ (15¢ stop)** | 11410 | 11378 | 32 (20) | 0 | $-4401.96 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 18:25 | +10 stop | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-09 18:25 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-09 18:25 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-09 18:22 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-09 18:22 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-09 18:21 | +10 stop | XRP | UP | 0.53 | 0.35 | -2.14 |
| 10-09 18:21 | +5 | XRP | UP | 0.53 | open |  |
| 10-09 18:21 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-09 18:21 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-09 18:21 | +15 | NEAR | DOWN | 0.67 | 0.86 | 1.65 |
| 10-09 18:21 | +10 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-09 18:21 | +5 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 10-09 18:21 | +15 | SOL | DOWN | 0.63 | 0.82 | 1.63 |
| 10-09 18:21 | +5 | SOL | DOWN | 0.63 | 0.77 | 1.11 |
| 10-09 18:19 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.30 |
| 10-09 18:18 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-09 18:18 | +10 stop | ETH | DOWN | 0.62 | 0.42 | -2.35 |
| 10-09 18:18 | +10 stop | XRP | DOWN | 0.70 | 0.51 | -2.23 |
| 10-09 18:18 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.04 |
| 10-09 18:18 | +10 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-09 18:18 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 10-09 18:17 | +10 stop | BNB | DOWN | 0.51 | 0.67 | 1.26 |
| 10-09 18:17 | +10 stop | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-09 18:16 | +10 stop | SOL | DOWN | 0.52 | 0.65 | 0.96 |
| 10-09 18:16 | +20 | SOL | DOWN | 0.52 | 0.77 | 2.19 |
| 10-09 18:16 | +15 | SOL | DOWN | 0.52 | 0.67 | 1.16 |
| 10-09 18:16 | +10 | SOL | DOWN | 0.52 | 0.65 | 0.96 |
| 10-09 18:16 | +5 | SOL | DOWN | 0.52 | 0.65 | 0.96 |
| 10-09 18:16 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 18:16 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-09 18:16 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-09 18:16 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-09 18:16 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-09 18:16 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.75 |
| 10-09 18:16 | +20 | NEAR | DOWN | 0.60 | 0.83 | 1.99 |
| 10-09 18:16 | +15 | NEAR | DOWN | 0.60 | 0.80 | 1.67 |
| 10-09 18:16 | +10 | NEAR | DOWN | 0.60 | 0.71 | 0.74 |
| 10-09 18:16 | +5 | NEAR | DOWN | 0.61 | 0.71 | 0.72 |
| 10-09 18:16 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.18 |
| 10-09 18:16 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
