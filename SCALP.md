# Range-Scalp Bot

*Updated Thu Nov 26 13:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72708 | 63462 | 9246 (158) | 1 | $-19348.01 | -4.2% |
| **+10¢** | 54221 | 43422 | 10799 (203) | 1 | $-17963.11 | -5.3% |
| **+15¢** | 45400 | 33766 | 11634 (261) | 1 | $-16072.67 | -5.6% |
| **+20¢** | 40411 | 28162 | 12249 (327) | 1 | $-14453.45 | -5.7% |
| **+10¢ (15¢ stop)** | 88546 | 88337 | 209 (128) | 0 | $-32571.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 13:13 | +10 stop | ETH | UP | 0.51 | 0.68 | 1.36 |
| 11-26 13:13 | +5 | ETH | UP | 0.45 | 0.68 | 1.96 |
| 11-26 13:12 | +10 stop | NEAR | DOWN | 0.49 | 0.28 | -2.43 |
| 11-26 13:12 | +5 | ETH | UP | 0.59 | 0.67 | 0.47 |
| 11-26 13:11 | +10 stop | ETH | UP | 0.53 | 0.67 | 1.06 |
| 11-26 13:11 | +5 | ETH | UP | 0.50 | 0.55 | 0.14 |
| 11-26 13:11 | +10 stop | BTC | DOWN | 0.70 | 0.54 | -1.93 |
| 11-26 13:11 | +5 | ETH | DOWN | 0.40 | 0.59 | 1.56 |
| 11-26 13:11 | +10 stop | ETH | DOWN | 0.60 | 0.43 | -2.05 |
| 11-26 13:11 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.95 |
| 11-26 13:09 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-26 13:09 | +10 stop | HYPE | DOWN | 0.71 | 0.47 | -2.73 |
| 11-26 13:08 | +10 stop | ETH | DOWN | 0.46 | 0.56 | 0.64 |
| 11-26 13:07 | +10 stop | SOL | UP | 0.56 | 0.74 | 1.48 |
| 11-26 13:07 | +10 stop | HYPE | UP | 0.60 | 0.41 | -2.24 |
| 11-26 13:06 | +10 stop | BTC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-26 13:06 | +10 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-26 13:06 | +5 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-26 13:06 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-26 13:05 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-26 13:04 | +10 stop | HYPE | UP | 0.63 | 0.44 | -2.25 |
| 11-26 13:04 | +5 | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 11-26 13:04 | +10 stop | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-26 13:04 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-26 13:04 | +15 | BTC | DOWN | 0.65 | 0.94 | 2.65 |
| 11-26 13:04 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-26 13:04 | +5 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-26 13:04 | +10 stop | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 11-26 13:04 | +20 | DOGE | UP | 0.64 | 0.86 | 1.94 |
| 11-26 13:04 | +15 | DOGE | UP | 0.64 | 0.80 | 1.31 |
| 11-26 13:04 | +10 | DOGE | UP | 0.64 | 0.80 | 1.31 |
| 11-26 13:04 | +5 | DOGE | UP | 0.64 | 0.70 | 0.28 |
| 11-26 13:03 | +10 stop | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-26 13:03 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-26 13:03 | +5 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 11-26 13:02 | +10 stop | SOL | UP | 0.56 | 0.41 | -1.85 |
| 11-26 13:02 | +10 stop | ETH | DOWN | 0.68 | 0.38 | -3.33 |
| 11-26 13:02 | +20 | ETH | DOWN | 0.66 | 0.95 | 2.68 |
| 11-26 13:02 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-26 13:02 | +10 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
