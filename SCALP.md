# Range-Scalp Bot

*Updated Thu Oct 22 18:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29133 | 25377 | 3756 (39) | 3 | $-8453.63 | -4.6% |
| **+10¢** | 21850 | 17502 | 4348 (55) | 3 | $-7574.90 | -5.5% |
| **+15¢** | 18290 | 13616 | 4674 (78) | 3 | $-6776.75 | -5.9% |
| **+20¢** | 16190 | 11291 | 4899 (100) | 3 | $-6102.59 | -6.0% |
| **+10¢ (15¢ stop)** | 35749 | 35690 | 59 (32) | 1 | $-13463.09 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 18:40 | +5 | ETH | UP | 0.56 | open |  |
| 10-22 18:39 | +10 stop | HYPE | DOWN | 0.55 | 0.82 | 2.41 |
| 10-22 18:39 | +10 stop | BNB | UP | 0.68 | 0.84 | 1.34 |
| 10-22 18:39 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-22 18:38 | +10 stop | ETH | UP | 0.50 | open |  |
| 10-22 18:38 | +5 | ETH | UP | 0.49 | 0.55 | 0.24 |
| 10-22 18:38 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.14 |
| 10-22 18:37 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 10-22 18:37 | +10 stop | ETH | UP | 0.67 | 0.46 | -2.44 |
| 10-22 18:35 | +10 stop | HYPE | UP | 0.64 | 0.47 | -2.09 |
| 10-22 18:34 | +10 stop | ETH | UP | 0.60 | 0.72 | 0.88 |
| 10-22 18:34 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-22 18:34 | +10 stop | BNB | UP | 0.69 | 0.53 | -1.93 |
| 10-22 18:33 | +10 stop | DOGE | UP | 0.66 | 0.81 | 1.23 |
| 10-22 18:33 | +10 | DOGE | UP | 0.66 | 0.81 | 1.23 |
| 10-22 18:33 | +5 | DOGE | UP | 0.66 | 0.74 | 0.50 |
| 10-22 18:33 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-22 18:33 | +10 stop | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-22 18:33 | +20 | XRP | UP | 0.63 | 0.86 | 2.04 |
| 10-22 18:33 | +15 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-22 18:33 | +10 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-22 18:33 | +5 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-22 18:32 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-22 18:32 | +20 | BTC | UP | 0.68 | 0.88 | 1.76 |
| 10-22 18:32 | +15 | BTC | UP | 0.68 | 0.85 | 1.45 |
| 10-22 18:32 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-22 18:32 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-22 18:32 | +5 | ZEC | DOWN | 0.55 | 0.64 | 0.55 |
| 10-22 18:32 | +5 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-22 18:32 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 10-22 18:32 | +20 | DOGE | UP | 0.58 | 0.81 | 2.01 |
| 10-22 18:32 | +15 | DOGE | UP | 0.59 | 0.74 | 1.19 |
| 10-22 18:32 | +10 | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-22 18:32 | +5 | DOGE | UP | 0.62 | 0.71 | 0.58 |
| 10-22 18:31 | +10 stop | ETH | DOWN | 0.53 | 0.36 | -2.05 |
| 10-22 18:31 | +20 | ETH | DOWN | 0.53 | open |  |
| 10-22 18:31 | +15 | ETH | DOWN | 0.53 | open |  |
| 10-22 18:31 | +10 | ETH | DOWN | 0.53 | open |  |
| 10-22 18:31 | +5 | ETH | DOWN | 0.52 | 0.59 | 0.35 |
| 10-22 18:31 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
