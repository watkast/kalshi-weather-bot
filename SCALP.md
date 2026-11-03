# Range-Scalp Bot

*Updated Tue Nov 03 06:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45672 | 39769 | 5903 (69) | 1 | $-13166.28 | -4.6% |
| **+10¢** | 34093 | 27251 | 6842 (91) | 1 | $-12067.63 | -5.6% |
| **+15¢** | 28533 | 21172 | 7361 (119) | 1 | $-11055.93 | -6.2% |
| **+20¢** | 25342 | 17629 | 7713 (154) | 1 | $-9838.11 | -6.2% |
| **+10¢ (15¢ stop)** | 55721 | 55632 | 89 (53) | 0 | $-20973.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 06:11 | +15 | HYPE | UP | 0.70 | open |  |
| 11-03 06:11 | +10 | HYPE | UP | 0.70 | open |  |
| 11-03 06:11 | +5 | HYPE | UP | 0.71 | open |  |
| 11-03 06:11 | +10 stop | HYPE | UP | 0.70 | 0.26 | -4.73 |
| 11-03 06:11 | +5 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-03 06:10 | +10 stop | ZEC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-03 06:09 | +10 stop | ZEC | DOWN | 0.60 | 0.43 | -2.05 |
| 11-03 06:09 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-03 06:09 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-03 06:08 | +10 stop | HYPE | UP | 0.60 | 0.75 | 1.19 |
| 11-03 06:08 | +20 | HYPE | UP | 0.60 | open |  |
| 11-03 06:08 | +15 | HYPE | UP | 0.60 | 0.75 | 1.19 |
| 11-03 06:08 | +10 | HYPE | UP | 0.60 | 0.75 | 1.19 |
| 11-03 06:08 | +5 | HYPE | UP | 0.60 | 0.66 | 0.27 |
| 11-03 06:08 | +10 stop | NEAR | UP | 0.66 | 0.19 | -4.97 |
| 11-03 06:08 | +10 stop | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-03 06:08 | +10 | ZEC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 06:08 | +5 | ZEC | DOWN | 0.53 | 0.64 | 0.75 |
| 11-03 06:07 | +10 stop | NEAR | UP | 0.46 | 0.58 | 0.84 |
| 11-03 06:06 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-03 06:04 | +5 | NEAR | DOWN | 0.71 | 0.80 | 0.63 |
| 11-03 06:04 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-03 06:04 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-03 06:04 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-03 06:03 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 06:03 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 06:03 | +10 stop | ZEC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-03 06:03 | +10 stop | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-03 06:03 | +10 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-03 06:03 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 11-03 06:02 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-03 06:02 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 11-03 06:02 | +15 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-03 06:02 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 06:02 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-03 06:02 | +5 | BNB | DOWN | 0.59 | 0.68 | 0.53 |
| 11-03 06:01 | +10 stop | ZEC | DOWN | 0.63 | 0.41 | -2.54 |
| 11-03 06:01 | +20 | ZEC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-03 06:01 | +15 | ZEC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-03 06:01 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
