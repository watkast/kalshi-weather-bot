# Range-Scalp Bot

*Updated Wed Oct 21 01:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26496 | 23078 | 3418 (33) | 7 | $-7721.07 | -4.6% |
| **+10¢** | 19931 | 15986 | 3945 (48) | 8 | $-6796.69 | -5.4% |
| **+15¢** | 16681 | 12436 | 4245 (72) | 8 | $-6057.70 | -5.8% |
| **+20¢** | 14764 | 10312 | 4452 (91) | 8 | $-5450.95 | -5.9% |
| **+10¢ (15¢ stop)** | 32462 | 32409 | 53 (30) | 0 | $-11870.09 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 01:26 | +10 stop | DOGE | UP | 0.65 | 0.86 | 1.85 |
| 10-21 01:26 | +10 stop | ZEC | DOWN | 0.67 | 0.50 | -2.04 |
| 10-21 01:24 | +10 stop | DOGE | UP | 0.55 | 0.70 | 1.17 |
| 10-21 01:23 | +10 stop | DOGE | DOWN | 0.58 | 0.38 | -2.35 |
| 10-21 01:23 | +20 | DOGE | DOWN | 0.58 | open |  |
| 10-21 01:23 | +15 | DOGE | DOWN | 0.58 | open |  |
| 10-21 01:23 | +10 | DOGE | DOWN | 0.58 | open |  |
| 10-21 01:23 | +5 | DOGE | DOWN | 0.58 | open |  |
| 10-21 01:23 | +10 stop | NEAR | UP | 0.62 | 0.85 | 2.04 |
| 10-21 01:22 | +10 stop | ZEC | UP | 0.50 | 0.65 | 1.14 |
| 10-21 01:22 | +10 stop | ETH | UP | 0.54 | 0.76 | 1.89 |
| 10-21 01:22 | +20 | ETH | UP | 0.54 | 0.76 | 1.89 |
| 10-21 01:22 | +15 | ETH | UP | 0.54 | 0.76 | 1.89 |
| 10-21 01:22 | +10 | ETH | UP | 0.54 | 0.76 | 1.89 |
| 10-21 01:22 | +5 | ETH | UP | 0.54 | 0.61 | 0.35 |
| 10-21 01:21 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-21 01:21 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 10-21 01:21 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-21 01:21 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-21 01:21 | +10 stop | BTC | DOWN | 0.53 | 0.38 | -1.85 |
| 10-21 01:21 | +5 | XRP | UP | 0.69 | 0.78 | 0.62 |
| 10-21 01:21 | +10 stop | NEAR | DOWN | 0.70 | 0.51 | -2.23 |
| 10-21 01:21 | +10 stop | BNB | DOWN | 0.71 | 0.49 | -2.53 |
| 10-21 01:20 | +10 stop | HYPE | UP | 0.66 | 0.79 | 1.02 |
| 10-21 01:20 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-21 01:20 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-21 01:20 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.94 |
| 10-21 01:20 | +10 stop | DOGE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-21 01:20 | +15 | DOGE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-21 01:20 | +10 | DOGE | DOWN | 0.61 | 0.82 | 1.82 |
| 10-21 01:20 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-21 01:20 | +10 stop | NEAR | UP | 0.61 | 0.46 | -1.85 |
| 10-21 01:19 | +10 stop | NEAR | DOWN | 0.46 | 0.57 | 0.74 |
| 10-21 01:19 | +10 stop | XRP | UP | 0.53 | 0.66 | 0.96 |
| 10-21 01:19 | +5 | XRP | UP | 0.53 | 0.60 | 0.35 |
| 10-21 01:18 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-21 01:18 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-21 01:18 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
| 10-21 01:18 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-21 01:17 | +5 | HYPE | UP | 0.44 | 0.54 | 0.60 |
