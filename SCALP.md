# Range-Scalp Bot

*Updated Thu Oct 22 19:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29157 | 25398 | 3759 (39) | 6 | $-8461.15 | -4.6% |
| **+10¢** | 21868 | 17516 | 4352 (55) | 6 | $-7580.78 | -5.5% |
| **+15¢** | 18306 | 13629 | 4677 (78) | 6 | $-6774.03 | -5.9% |
| **+20¢** | 16204 | 11301 | 4903 (100) | 6 | $-6104.92 | -6.0% |
| **+10¢ (15¢ stop)** | 35790 | 35731 | 59 (32) | 0 | $-13482.12 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 19:08 | +10 stop | BTC | DOWN | 0.62 | 0.80 | 1.51 |
| 10-22 19:08 | +10 stop | BNB | DOWN | 0.56 | 0.73 | 1.38 |
| 10-22 19:07 | +10 stop | XRP | DOWN | 0.57 | 0.79 | 1.90 |
| 10-22 19:06 | +10 stop | NEAR | UP | 0.55 | 0.34 | -2.44 |
| 10-22 19:05 | +10 stop | BTC | UP | 0.56 | 0.35 | -2.44 |
| 10-22 19:05 | +10 stop | XRP | UP | 0.56 | 0.33 | -2.64 |
| 10-22 19:05 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 10-22 19:05 | +5 | HYPE | DOWN | 0.67 | 0.75 | 0.49 |
| 10-22 19:05 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-22 19:05 | +10 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-22 19:05 | +5 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-22 19:05 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-22 19:04 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-22 19:04 | +10 stop | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-22 19:04 | +10 stop | BNB | DOWN | 0.51 | 0.64 | 0.95 |
| 10-22 19:02 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 19:02 | +10 stop | NEAR | DOWN | 0.65 | 0.43 | -2.54 |
| 10-22 19:02 | +10 stop | BTC | DOWN | 0.61 | 0.45 | -1.95 |
| 10-22 19:02 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 19:02 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-22 19:02 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 19:02 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-22 19:02 | +15 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-22 19:02 | +10 | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 19:02 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-22 19:01 | +10 stop | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-22 19:01 | +20 | HYPE | DOWN | 0.71 | 0.97 | 2.48 |
| 10-22 19:01 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-22 19:01 | +10 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-22 19:01 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-22 19:01 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-22 19:01 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 10-22 19:01 | +15 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 10-22 19:01 | +10 | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-22 19:01 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 10-22 19:01 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.85 |
| 10-22 19:01 | +20 | BNB | UP | 0.60 | open |  |
| 10-22 19:01 | +15 | BNB | UP | 0.60 | open |  |
| 10-22 19:01 | +10 | BNB | UP | 0.59 | open |  |
| 10-22 19:01 | +5 | BNB | UP | 0.59 | open |  |
