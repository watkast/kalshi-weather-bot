# Range-Scalp Bot

*Updated Thu Oct 08 03:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7227 | 6268 | 959 (13) | 4 | $-2206.14 | -4.8% |
| **+10¢** | 5479 | 4350 | 1129 (20) | 4 | $-2150.57 | -6.2% |
| **+15¢** | 4593 | 3402 | 1191 (28) | 6 | $-1790.22 | -6.2% |
| **+20¢** | 4101 | 2864 | 1237 (35) | 7 | $-1421.06 | -5.5% |
| **+10¢ (15¢ stop)** | 8746 | 8724 | 22 (14) | 4 | $-3148.16 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 03:21 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 10-08 03:21 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-08 03:21 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-08 03:21 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-08 03:21 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-08 03:21 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 10-08 03:21 | +10 | DOGE | DOWN | 0.64 | open |  |
| 10-08 03:21 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.43 |
| 10-08 03:21 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-08 03:21 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-08 03:21 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-08 03:21 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-08 03:20 | +10 | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-08 03:20 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-08 03:20 | +10 stop | SOL | DOWN | 0.68 | 0.51 | -2.04 |
| 10-08 03:19 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 10-08 03:19 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-08 03:19 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-08 03:19 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-08 03:19 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-08 03:19 | +5 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 03:19 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 03:19 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 03:18 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-08 03:18 | +10 stop | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 10-08 03:18 | +5 | NEAR | DOWN | 0.66 | 0.80 | 1.13 |
| 10-08 03:18 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 03:17 | +10 stop | SOL | UP | 0.62 | 0.46 | -1.95 |
| 10-08 03:17 | +10 stop | BTC | UP | 0.60 | 0.41 | -2.24 |
| 10-08 03:17 | +5 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-08 03:17 | +5 | XRP | UP | 0.49 | 0.54 | 0.14 |
| 10-08 03:16 | +10 stop | XRP | DOWN | 0.47 | 0.65 | 1.46 |
| 10-08 03:16 | +20 | XRP | DOWN | 0.47 | 0.74 | 2.38 |
| 10-08 03:16 | +15 | XRP | DOWN | 0.47 | 0.65 | 1.46 |
| 10-08 03:16 | +10 | XRP | DOWN | 0.47 | 0.65 | 1.46 |
| 10-08 03:16 | +5 | XRP | DOWN | 0.47 | 0.56 | 0.54 |
| 10-08 03:16 | +10 stop | NEAR | DOWN | 0.56 | 0.66 | 0.66 |
| 10-08 03:16 | +20 | NEAR | DOWN | 0.56 | 0.80 | 2.10 |
| 10-08 03:16 | +15 | NEAR | DOWN | 0.56 | 0.80 | 2.10 |
| 10-08 03:16 | +10 | NEAR | DOWN | 0.56 | 0.66 | 0.66 |
