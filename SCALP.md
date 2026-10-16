# Range-Scalp Bot

*Updated Fri Oct 16 00:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18438 | 16015 | 2423 (28) | 2 | $-5597.57 | -4.8% |
| **+10¢** | 13907 | 11104 | 2803 (40) | 3 | $-5050.81 | -5.8% |
| **+15¢** | 11666 | 8652 | 3014 (59) | 3 | $-4534.29 | -6.2% |
| **+20¢** | 10362 | 7209 | 3153 (78) | 3 | $-3940.42 | -6.1% |
| **+10¢ (15¢ stop)** | 22695 | 22645 | 50 (29) | 0 | $-8755.17 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 00:56 | +10 stop | ZEC | DOWN | 0.26 | 0.52 | 2.28 |
| 10-16 00:56 | +5 | ZEC | DOWN | 0.26 | 0.52 | 2.28 |
| 10-16 00:55 | +10 stop | HYPE | DOWN | 0.65 | 0.46 | -2.24 |
| 10-16 00:55 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-16 00:55 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-16 00:55 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-16 00:51 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 00:51 | +20 | DOGE | DOWN | 0.64 | 0.92 | 2.58 |
| 10-16 00:51 | +15 | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 10-16 00:51 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 00:51 | +5 | DOGE | DOWN | 0.65 | 0.74 | 0.60 |
| 10-16 00:51 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-16 00:51 | +10 stop | NEAR | UP | 0.65 | 0.49 | -1.94 |
| 10-16 00:49 | +10 stop | NEAR | UP | 0.67 | 0.45 | -2.54 |
| 10-16 00:49 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 00:49 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 00:49 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-16 00:48 | +10 stop | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-16 00:48 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-16 00:47 | +10 stop | ZEC | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 00:47 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 00:47 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-16 00:47 | +15 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-16 00:47 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 00:47 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-16 00:47 | +5 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 00:47 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 00:47 | +20 | ETH | DOWN | 0.66 | 0.87 | 1.86 |
| 10-16 00:47 | +15 | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 10-16 00:47 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 00:47 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 10-16 00:46 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 00:46 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
| 10-16 00:46 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.40 |
| 10-16 00:46 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-16 00:46 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-16 00:46 | +10 stop | DOGE | DOWN | 0.56 | 0.69 | 0.97 |
| 10-16 00:46 | +20 | DOGE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-16 00:46 | +15 | DOGE | DOWN | 0.56 | 0.73 | 1.38 |
| 10-16 00:46 | +10 | DOGE | DOWN | 0.56 | 0.69 | 0.97 |
