# Range-Scalp Bot

*Updated Wed Oct 14 03:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15393 | 13328 | 2065 (27) | 0 | $-4878.71 | -5.0% |
| **+10¢** | 11644 | 9247 | 2397 (39) | 1 | $-4552.11 | -6.2% |
| **+15¢** | 9781 | 7212 | 2569 (58) | 1 | $-4063.59 | -6.6% |
| **+20¢** | 8695 | 6006 | 2689 (75) | 1 | $-3579.40 | -6.6% |
| **+10¢ (15¢ stop)** | 18873 | 18823 | 50 (29) | 1 | $-7262.63 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 03:39 | +10 stop | ZEC | UP | 0.66 | open |  |
| 10-14 03:39 | +10 | ZEC | UP | 0.66 | open |  |
| 10-14 03:39 | +5 | ZEC | UP | 0.66 | 0.74 | 0.50 |
| 10-14 03:32 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-14 03:32 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-14 03:32 | +20 | ZEC | UP | 0.69 | open |  |
| 10-14 03:32 | +15 | ZEC | UP | 0.69 | open |  |
| 10-14 03:32 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-14 03:32 | +5 | ZEC | UP | 0.70 | 0.77 | 0.42 |
| 10-14 03:31 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 10-14 03:31 | +20 | NEAR | UP | 0.71 | 0.94 | 2.13 |
| 10-14 03:31 | +15 | NEAR | UP | 0.71 | 0.87 | 1.37 |
| 10-14 03:31 | +10 | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-14 03:31 | +5 | NEAR | UP | 0.71 | 0.79 | 0.53 |
| 10-14 03:27 | +10 stop | SOL | UP | 0.61 | 0.87 | 2.35 |
| 10-14 03:27 | +10 stop | HYPE | DOWN | 0.55 | 0.40 | -1.85 |
| 10-14 03:27 | +20 | HYPE | DOWN | 0.55 | yes | -5.68 |
| 10-14 03:27 | +15 | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-14 03:27 | +10 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-14 03:27 | +5 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-14 03:27 | +10 stop | ETH | UP | 0.67 | 0.94 | 2.44 |
| 10-14 03:25 | +20 | ETH | UP | 0.69 | 0.94 | 2.28 |
| 10-14 03:25 | +10 | ETH | UP | 0.68 | 0.94 | 2.35 |
| 10-14 03:25 | +5 | ETH | UP | 0.68 | 0.74 | 0.31 |
| 10-14 03:25 | +10 stop | DOGE | UP | 0.70 | 0.48 | -2.55 |
| 10-14 03:25 | +10 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-14 03:25 | +5 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-14 03:24 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 10-14 03:24 | +10 stop | SOL | UP | 0.68 | 0.42 | -2.96 |
| 10-14 03:24 | +10 stop | XRP | UP | 0.58 | 0.23 | -3.81 |
| 10-14 03:24 | +10 | XRP | UP | 0.58 | 0.95 | 3.48 |
| 10-14 03:24 | +5 | XRP | UP | 0.58 | 0.95 | 3.48 |
| 10-14 03:24 | +10 stop | XRP | DOWN | 0.41 | 0.56 | 1.15 |
| 10-14 03:24 | +10 | XRP | DOWN | 0.41 | 0.56 | 1.15 |
| 10-14 03:24 | +5 | XRP | DOWN | 0.41 | 0.56 | 1.15 |
| 10-14 03:23 | +10 stop | DOGE | UP | 0.60 | 0.71 | 0.78 |
| 10-14 03:23 | +10 stop | ETH | UP | 0.69 | 0.51 | -2.13 |
| 10-14 03:23 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.15 |
| 10-14 03:23 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-14 03:23 | +5 | HYPE | UP | 0.70 | 0.80 | 0.73 |
