# Range-Scalp Bot

*Updated Sun Nov 01 05:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43279 | 37725 | 5554 (62) | 2 | $-12301.05 | -4.5% |
| **+10¢** | 32275 | 25859 | 6416 (84) | 3 | $-11003.97 | -5.4% |
| **+15¢** | 27008 | 20094 | 6914 (112) | 3 | $-10062.55 | -5.9% |
| **+20¢** | 23987 | 16743 | 7244 (146) | 2 | $-8880.11 | -5.9% |
| **+10¢ (15¢ stop)** | 52760 | 52677 | 83 (48) | 0 | $-19918.75 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 05:43 | +20 | DOGE | UP | 0.68 | 0.99 | 2.97 |
| 11-01 05:42 | +10 stop | DOGE | UP | 0.62 | 0.75 | 0.99 |
| 11-01 05:41 | +10 stop | DOGE | DOWN | 0.66 | 0.40 | -2.93 |
| 11-01 05:41 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-01 05:41 | +10 | DOGE | DOWN | 0.66 | open |  |
| 11-01 05:41 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-01 05:41 | +10 stop | DOGE | UP | 0.42 | 0.58 | 1.24 |
| 11-01 05:41 | +20 | DOGE | UP | 0.42 | 0.68 | 2.26 |
| 11-01 05:41 | +15 | DOGE | UP | 0.42 | 0.58 | 1.24 |
| 11-01 05:41 | +10 | DOGE | UP | 0.42 | 0.58 | 1.24 |
| 11-01 05:41 | +5 | DOGE | UP | 0.42 | 0.58 | 1.24 |
| 11-01 05:40 | +5 | SOL | UP | 0.55 | no | -5.68 |
| 11-01 05:39 | +10 stop | SOL | UP | 0.57 | 0.36 | -2.45 |
| 11-01 05:39 | +20 | SOL | UP | 0.57 | no | -5.88 |
| 11-01 05:39 | +15 | SOL | UP | 0.58 | no | -5.98 |
| 11-01 05:39 | +10 | SOL | UP | 0.57 | no | -5.88 |
| 11-01 05:39 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-01 05:38 | +10 stop | BTC | DOWN | 0.61 | 0.87 | 2.35 |
| 11-01 05:38 | +5 | BTC | DOWN | 0.64 | 0.87 | 2.05 |
| 11-01 05:38 | +10 stop | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 11-01 05:38 | +20 | XRP | UP | 0.70 | 0.97 | 2.54 |
| 11-01 05:38 | +15 | XRP | UP | 0.70 | 0.97 | 2.54 |
| 11-01 05:38 | +10 | XRP | UP | 0.71 | 0.97 | 2.44 |
| 11-01 05:38 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 11-01 05:38 | +10 stop | XRP | UP | 0.71 | 0.53 | -2.13 |
| 11-01 05:38 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 11-01 05:38 | +10 stop | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 11-01 05:36 | +5 | BTC | UP | 0.61 | 0.66 | 0.17 |
| 11-01 05:36 | +10 stop | ETH | UP | 0.57 | 0.35 | -2.54 |
| 11-01 05:36 | +15 | ETH | UP | 0.57 | no | -5.88 |
| 11-01 05:36 | +10 | ETH | UP | 0.57 | no | -5.88 |
| 11-01 05:36 | +5 | ETH | UP | 0.57 | no | -5.88 |
| 11-01 05:36 | +10 stop | BTC | UP | 0.61 | 0.44 | -2.05 |
| 11-01 05:36 | +15 | BTC | UP | 0.61 | open |  |
| 11-01 05:36 | +10 | BTC | UP | 0.61 | open |  |
| 11-01 05:36 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-01 05:35 | +10 stop | ZEC | UP | 0.66 | 0.48 | -2.14 |
| 11-01 05:35 | +20 | ZEC | UP | 0.66 | open |  |
| 11-01 05:35 | +15 | ZEC | UP | 0.66 | open |  |
| 11-01 05:35 | +10 | ZEC | UP | 0.66 | open |  |
