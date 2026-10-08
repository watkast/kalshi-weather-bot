# Range-Scalp Bot

*Updated Thu Oct 08 01:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7096 | 6161 | 935 (13) | 0 | $-2112.11 | -4.7% |
| **+10¢** | 5381 | 4281 | 1100 (20) | 0 | $-2032.49 | -6.0% |
| **+15¢** | 4515 | 3354 | 1161 (28) | 0 | $-1675.49 | -5.9% |
| **+20¢** | 4034 | 2824 | 1210 (35) | 0 | $-1336.09 | -5.3% |
| **+10¢ (15¢ stop)** | 8574 | 8552 | 22 (14) | 0 | $-3013.79 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 01:25 | +10 stop | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-08 01:20 | +5 | HYPE | UP | 0.54 | 0.63 | 0.55 |
| 10-08 01:20 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.18 |
| 10-08 01:20 | +20 | HYPE | UP | 0.59 | 0.87 | 2.51 |
| 10-08 01:20 | +15 | HYPE | UP | 0.59 | 0.87 | 2.51 |
| 10-08 01:20 | +10 | HYPE | UP | 0.59 | 0.71 | 0.84 |
| 10-08 01:20 | +5 | HYPE | UP | 0.59 | 0.65 | 0.23 |
| 10-08 01:19 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-08 01:19 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-08 01:19 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 01:19 | +10 stop | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-08 01:19 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-08 01:19 | +10 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-08 01:19 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 10-08 01:19 | +10 stop | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-08 01:19 | +5 | BNB | DOWN | 0.71 | 0.87 | 1.37 |
| 10-08 01:18 | +10 stop | XRP | UP | 0.54 | 0.39 | -1.85 |
| 10-08 01:18 | +20 | XRP | UP | 0.54 | no | -5.58 |
| 10-08 01:18 | +15 | XRP | UP | 0.54 | no | -5.58 |
| 10-08 01:18 | +10 | XRP | UP | 0.54 | no | -5.58 |
| 10-08 01:18 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 10-08 01:18 | +10 stop | SOL | UP | 0.42 | 0.53 | 0.74 |
| 10-08 01:18 | +20 | SOL | UP | 0.42 | no | -4.38 |
| 10-08 01:18 | +15 | SOL | UP | 0.42 | no | -4.38 |
| 10-08 01:18 | +10 | SOL | UP | 0.42 | 0.53 | 0.74 |
| 10-08 01:18 | +5 | SOL | UP | 0.42 | 0.53 | 0.74 |
| 10-08 01:18 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 10-08 01:18 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 10-08 01:18 | +20 | BNB | UP | 0.58 | no | -5.97 |
| 10-08 01:18 | +15 | BNB | UP | 0.58 | no | -5.97 |
| 10-08 01:18 | +10 | BNB | UP | 0.58 | no | -5.97 |
| 10-08 01:18 | +5 | BNB | UP | 0.58 | 0.66 | 0.47 |
| 10-08 01:17 | +10 stop | BTC | UP | 0.71 | 0.55 | -1.93 |
| 10-08 01:17 | +20 | BTC | UP | 0.71 | no | -7.25 |
| 10-08 01:17 | +15 | BTC | UP | 0.71 | no | -7.25 |
| 10-08 01:17 | +10 | BTC | UP | 0.71 | no | -7.25 |
| 10-08 01:17 | +5 | BTC | UP | 0.71 | no | -7.25 |
| 10-08 01:17 | +10 stop | ZEC | UP | 0.71 | 0.51 | -2.33 |
| 10-08 01:17 | +15 | ZEC | UP | 0.71 | no | -7.25 |
| 10-08 01:17 | +10 | ZEC | UP | 0.71 | no | -7.25 |
