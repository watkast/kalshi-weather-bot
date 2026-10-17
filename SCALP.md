# Range-Scalp Bot

*Updated Sat Oct 17 19:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21476 | 18717 | 2759 (29) | 2 | $-6109.98 | -4.5% |
| **+10¢** | 16144 | 12954 | 3190 (41) | 4 | $-5442.19 | -5.4% |
| **+15¢** | 13493 | 10053 | 3440 (61) | 5 | $-4946.41 | -5.8% |
| **+20¢** | 11951 | 8346 | 3605 (80) | 6 | $-4396.16 | -5.9% |
| **+10¢ (15¢ stop)** | 26352 | 26302 | 50 (29) | 1 | $-10018.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 19:26 | +10 stop | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 10-17 19:26 | +20 | DOGE | UP | 0.49 | open |  |
| 10-17 19:26 | +15 | DOGE | UP | 0.48 | 0.64 | 1.25 |
| 10-17 19:26 | +10 | DOGE | UP | 0.48 | 0.64 | 1.25 |
| 10-17 19:26 | +5 | DOGE | UP | 0.48 | 0.64 | 1.26 |
| 10-17 19:25 | +10 stop | SOL | UP | 0.70 | 0.39 | -3.42 |
| 10-17 19:25 | +20 | SOL | UP | 0.70 | open |  |
| 10-17 19:25 | +15 | SOL | UP | 0.70 | open |  |
| 10-17 19:25 | +10 | SOL | UP | 0.70 | open |  |
| 10-17 19:25 | +5 | SOL | UP | 0.70 | 0.79 | 0.63 |
| 10-17 19:25 | +10 stop | BTC | DOWN | 0.49 | open |  |
| 10-17 19:25 | +10 stop | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 10-17 19:24 | +10 stop | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-17 19:24 | +15 | ZEC | UP | 0.47 | open |  |
| 10-17 19:24 | +10 | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-17 19:24 | +5 | ZEC | UP | 0.47 | 0.59 | 0.85 |
| 10-17 19:23 | +10 stop | BTC | UP | 0.63 | 0.43 | -2.35 |
| 10-17 19:23 | +10 stop | NEAR | UP | 0.61 | 0.37 | -2.70 |
| 10-17 19:23 | +15 | NEAR | UP | 0.61 | open |  |
| 10-17 19:23 | +10 | NEAR | UP | 0.61 | open |  |
| 10-17 19:21 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-17 19:21 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 10-17 19:21 | +5 | XRP | UP | 0.65 | 0.73 | 0.50 |
| 10-17 19:21 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 19:20 | +10 stop | XRP | UP | 0.57 | 0.68 | 0.76 |
| 10-17 19:20 | +15 | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-17 19:20 | +10 | XRP | UP | 0.57 | 0.68 | 0.75 |
| 10-17 19:20 | +5 | XRP | UP | 0.57 | 0.68 | 0.73 |
| 10-17 19:20 | +10 stop | NEAR | UP | 0.51 | 0.72 | 1.77 |
| 10-17 19:20 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-17 19:20 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-17 19:20 | +5 | ZEC | UP | 0.70 | 0.79 | 0.63 |
| 10-17 19:19 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 10-17 19:19 | +5 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 10-17 19:19 | +5 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-17 19:19 | +5 | ETH | UP | 0.65 | 0.73 | 0.50 |
| 10-17 19:18 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-17 19:18 | +10 stop | BTC | UP | 0.54 | 0.65 | 0.76 |
| 10-17 19:18 | +5 | NEAR | DOWN | 0.51 | 0.60 | 0.55 |
| 10-17 19:17 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
