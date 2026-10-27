# Range-Scalp Bot

*Updated Tue Oct 27 04:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35998 | 31429 | 4569 (43) | 4 | $-9989.72 | -4.4% |
| **+10¢** | 26913 | 21625 | 5288 (65) | 4 | $-8833.19 | -5.2% |
| **+15¢** | 22519 | 16835 | 5684 (89) | 4 | $-7854.31 | -5.6% |
| **+20¢** | 19960 | 14005 | 5955 (112) | 4 | $-6895.45 | -5.5% |
| **+10¢ (15¢ stop)** | 44153 | 44090 | 63 (33) | 0 | $-16820.96 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 04:41 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 10-27 04:41 | +15 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 10-27 04:41 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 10-27 04:41 | +5 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-27 04:38 | +10 stop | ZEC | DOWN | 0.54 | 0.68 | 1.06 |
| 10-27 04:37 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.15 |
| 10-27 04:37 | +10 stop | NEAR | UP | 0.48 | 0.61 | 0.95 |
| 10-27 04:36 | +10 stop | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-27 04:36 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 10-27 04:36 | +10 stop | HYPE | DOWN | 0.57 | 0.76 | 1.59 |
| 10-27 04:35 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-27 04:35 | +5 | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 10-27 04:35 | +10 stop | ZEC | UP | 0.64 | 0.35 | -3.23 |
| 10-27 04:35 | +20 | ZEC | UP | 0.64 | open |  |
| 10-27 04:35 | +15 | ZEC | UP | 0.64 | open |  |
| 10-27 04:35 | +10 | ZEC | UP | 0.64 | open |  |
| 10-27 04:35 | +5 | ZEC | UP | 0.64 | open |  |
| 10-27 04:35 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-27 04:34 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-27 04:34 | +10 stop | ETH | DOWN | 0.56 | 0.72 | 1.27 |
| 10-27 04:34 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 10-27 04:34 | +10 stop | BTC | DOWN | 0.62 | 0.79 | 1.41 |
| 10-27 04:33 | +5 | XRP | UP | 0.70 | open |  |
| 10-27 04:33 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.14 |
| 10-27 04:33 | +10 | HYPE | UP | 0.59 | open |  |
| 10-27 04:33 | +5 | HYPE | UP | 0.59 | open |  |
| 10-27 04:33 | +5 | DOGE | UP | 0.67 | open |  |
| 10-27 04:32 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-27 04:32 | +10 stop | SOL | UP | 0.57 | 0.40 | -2.05 |
| 10-27 04:32 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 10-27 04:32 | +10 stop | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 10-27 04:31 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-27 04:31 | +20 | HYPE | UP | 0.62 | open |  |
| 10-27 04:31 | +15 | HYPE | UP | 0.62 | open |  |
| 10-27 04:31 | +10 | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-27 04:31 | +5 | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-27 04:31 | +10 stop | XRP | UP | 0.66 | 0.48 | -2.14 |
| 10-27 04:31 | +20 | XRP | UP | 0.66 | open |  |
| 10-27 04:31 | +15 | XRP | UP | 0.66 | open |  |
| 10-27 04:31 | +10 | XRP | UP | 0.66 | open |  |
