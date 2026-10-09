# Range-Scalp Bot

*Updated Fri Oct 09 03:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8456 | 7316 | 1140 (13) | 7 | $-2753.46 | -5.2% |
| **+10¢** | 6405 | 5059 | 1346 (25) | 8 | $-2701.13 | -6.7% |
| **+15¢** | 5407 | 3990 | 1417 (37) | 8 | $-2181.41 | -6.4% |
| **+20¢** | 4811 | 3340 | 1471 (45) | 8 | $-1804.62 | -6.0% |
| **+10¢ (15¢ stop)** | 10297 | 10267 | 30 (19) | 2 | $-3785.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 03:39 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-09 03:39 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-09 03:39 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-09 03:39 | +5 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-09 03:38 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-09 03:38 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 10-09 03:38 | +10 stop | ZEC | DOWN | 0.49 | 0.65 | 1.26 |
| 10-09 03:38 | +20 | ZEC | DOWN | 0.49 | 0.74 | 2.17 |
| 10-09 03:38 | +15 | ZEC | DOWN | 0.49 | 0.65 | 1.26 |
| 10-09 03:38 | +10 | ZEC | DOWN | 0.49 | 0.65 | 1.22 |
| 10-09 03:38 | +5 | ZEC | DOWN | 0.49 | 0.57 | 0.40 |
| 10-09 03:36 | +10 stop | SOL | UP | 0.67 | 0.40 | -3.03 |
| 10-09 03:36 | +10 stop | NEAR | UP | 0.70 | 0.85 | 1.28 |
| 10-09 03:36 | +10 stop | ETH | UP | 0.65 | 0.82 | 1.43 |
| 10-09 03:35 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.80 |
| 10-09 03:35 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 10-09 03:35 | +10 stop | NEAR | DOWN | 0.61 | 0.43 | -2.15 |
| 10-09 03:34 | +10 stop | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 10-09 03:34 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-09 03:34 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.69 |
| 10-09 03:34 | +10 stop | NEAR | UP | 0.43 | 0.56 | 0.94 |
| 10-09 03:33 | +10 stop | SOL | DOWN | 0.67 | 0.51 | -1.95 |
| 10-09 03:33 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-09 03:33 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.33 |
| 10-09 03:33 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.80 |
| 10-09 03:33 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.29 |
| 10-09 03:33 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 10-09 03:32 | +10 stop | XRP | DOWN | 0.52 | 0.37 | -1.85 |
| 10-09 03:32 | +20 | XRP | DOWN | 0.52 | open |  |
| 10-09 03:32 | +15 | XRP | DOWN | 0.52 | open |  |
| 10-09 03:32 | +10 | XRP | DOWN | 0.52 | open |  |
| 10-09 03:32 | +5 | XRP | DOWN | 0.52 | open |  |
| 10-09 03:32 | +10 stop | NEAR | DOWN | 0.63 | 0.39 | -2.74 |
| 10-09 03:32 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-09 03:32 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-09 03:32 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-09 03:32 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-09 03:31 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-09 03:31 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.24 |
| 10-09 03:31 | +20 | BNB | DOWN | 0.68 | open |  |
