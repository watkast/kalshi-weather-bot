# Range-Scalp Bot

*Updated Mon Oct 19 19:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24494 | 21317 | 3177 (31) | 0 | $-7188.56 | -4.7% |
| **+10¢** | 18414 | 14746 | 3668 (46) | 0 | $-6409.89 | -5.5% |
| **+15¢** | 15415 | 11465 | 3950 (69) | 0 | $-5787.82 | -6.0% |
| **+20¢** | 13641 | 9504 | 4137 (87) | 0 | $-5201.62 | -6.1% |
| **+10¢ (15¢ stop)** | 30106 | 30054 | 52 (30) | 0 | $-11368.93 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 19:48 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-19 19:47 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-19 19:46 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-19 19:46 | +20 | ZEC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-19 19:46 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-19 19:46 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-19 19:46 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-19 19:46 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-19 19:46 | +20 | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 10-19 19:46 | +15 | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 10-19 19:46 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-19 19:46 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-19 19:46 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 19:46 | +20 | BNB | DOWN | 0.69 | 0.95 | 2.41 |
| 10-19 19:46 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 10-19 19:46 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 19:46 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-19 19:46 | +10 stop | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-19 19:46 | +20 | SOL | DOWN | 0.62 | 0.88 | 2.35 |
| 10-19 19:46 | +15 | SOL | DOWN | 0.61 | 0.79 | 1.49 |
| 10-19 19:46 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 10-19 19:46 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 10-19 19:42 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 10-19 19:41 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-19 19:40 | +10 stop | DOGE | UP | 0.68 | 0.48 | -2.34 |
| 10-19 19:39 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-19 19:39 | +10 stop | ETH | UP | 0.68 | 0.80 | 0.92 |
| 10-19 19:38 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-19 19:38 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-19 19:38 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-19 19:38 | +5 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-19 19:38 | +10 stop | BTC | UP | 0.60 | 0.76 | 1.30 |
| 10-19 19:38 | +5 | XRP | DOWN | 0.70 | yes | -7.15 |
| 10-19 19:38 | +10 stop | DOGE | UP | 0.41 | 0.54 | 0.95 |
| 10-19 19:37 | +5 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-19 19:37 | +10 stop | ZEC | UP | 0.67 | 0.83 | 1.34 |
| 10-19 19:37 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 10-19 19:37 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-19 19:36 | +10 stop | DOGE | DOWN | 0.69 | 0.41 | -3.12 |
| 10-19 19:36 | +10 stop | BTC | DOWN | 0.71 | 0.53 | -2.13 |
