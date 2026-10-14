# Range-Scalp Bot

*Updated Wed Oct 14 19:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16442 | 14245 | 2197 (28) | 4 | $-5195.34 | -5.0% |
| **+10¢** | 12440 | 9894 | 2546 (40) | 4 | $-4770.55 | -6.1% |
| **+15¢** | 10454 | 7722 | 2732 (59) | 4 | $-4267.75 | -6.5% |
| **+20¢** | 9294 | 6430 | 2864 (76) | 5 | $-3780.53 | -6.5% |
| **+10¢ (15¢ stop)** | 20262 | 20212 | 50 (29) | 1 | $-7827.91 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 19:57 | +10 stop | BNB | UP | 0.66 | open |  |
| 10-14 19:55 | +10 stop | DOGE | DOWN | 0.65 | 0.88 | 2.06 |
| 10-14 19:55 | +10 | DOGE | DOWN | 0.66 | 0.88 | 1.96 |
| 10-14 19:55 | +10 stop | DOGE | UP | 0.44 | 0.60 | 1.25 |
| 10-14 19:54 | +10 | DOGE | DOWN | 0.57 | 0.72 | 1.17 |
| 10-14 19:53 | +5 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-14 19:53 | +10 stop | DOGE | DOWN | 0.70 | 0.43 | -3.03 |
| 10-14 19:53 | +10 stop | ETH | DOWN | 0.58 | 0.43 | -1.86 |
| 10-14 19:52 | +10 stop | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 10-14 19:52 | +10 stop | DOGE | UP | 0.59 | 0.39 | -2.30 |
| 10-14 19:52 | +10 stop | ETH | UP | 0.64 | 0.48 | -1.95 |
| 10-14 19:51 | +10 stop | BNB | UP | 0.68 | 0.51 | -2.04 |
| 10-14 19:51 | +5 | DOGE | DOWN | 0.56 | 0.63 | 0.35 |
| 10-14 19:51 | +10 stop | DOGE | DOWN | 0.57 | 0.42 | -1.86 |
| 10-14 19:51 | +10 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 10-14 19:51 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-14 19:50 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-14 19:50 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-14 19:50 | +10 stop | ZEC | UP | 0.67 | 0.81 | 1.13 |
| 10-14 19:50 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-14 19:50 | +10 stop | ETH | DOWN | 0.58 | 0.30 | -3.13 |
| 10-14 19:50 | +10 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 10-14 19:50 | +5 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 10-14 19:50 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-14 19:50 | +15 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 10-14 19:50 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 19:50 | +5 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 19:50 | +10 stop | XRP | UP | 0.54 | 0.29 | -2.83 |
| 10-14 19:49 | +5 | NEAR | DOWN | 0.67 | open |  |
| 10-14 19:48 | +10 stop | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-14 19:48 | +15 | HYPE | UP | 0.57 | 0.74 | 1.38 |
| 10-14 19:48 | +10 | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-14 19:48 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 10-14 19:47 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-14 19:47 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-14 19:47 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-14 19:47 | +10 stop | BTC | DOWN | 0.66 | 0.44 | -2.54 |
