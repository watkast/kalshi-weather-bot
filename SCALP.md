# Range-Scalp Bot

*Updated Mon Oct 19 22:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24648 | 21457 | 3191 (31) | 2 | $-7203.71 | -4.6% |
| **+10¢** | 18529 | 14843 | 3686 (46) | 5 | $-6414.98 | -5.5% |
| **+15¢** | 15517 | 11548 | 3969 (70) | 6 | $-5768.23 | -5.9% |
| **+20¢** | 13722 | 9565 | 4157 (88) | 7 | $-5189.57 | -6.0% |
| **+10¢ (15¢ stop)** | 30284 | 30232 | 52 (30) | 0 | $-11387.58 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 22:25 | +10 stop | BTC | DOWN | 0.50 | 0.64 | 1.05 |
| 10-19 22:25 | +15 | BTC | DOWN | 0.49 | 0.64 | 1.15 |
| 10-19 22:25 | +10 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-19 22:25 | +5 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-19 22:25 | +10 stop | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 10-19 22:25 | +15 | ETH | DOWN | 0.41 | open |  |
| 10-19 22:25 | +10 | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 10-19 22:25 | +5 | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 10-19 22:24 | +10 stop | BTC | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +20 | BTC | UP | 0.44 | open |  |
| 10-19 22:24 | +15 | BTC | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +10 | BTC | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +5 | BTC | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +10 stop | ETH | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +20 | ETH | UP | 0.44 | 0.67 | 1.96 |
| 10-19 22:24 | +15 | ETH | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +10 | ETH | UP | 0.44 | 0.59 | 1.15 |
| 10-19 22:24 | +5 | ETH | UP | 0.46 | 0.59 | 0.95 |
| 10-19 22:24 | +10 stop | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 10-19 22:24 | +15 | NEAR | UP | 0.57 | 0.73 | 1.28 |
| 10-19 22:24 | +10 | NEAR | UP | 0.57 | 0.71 | 1.07 |
| 10-19 22:24 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-19 22:23 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-19 22:23 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 10-19 22:22 | +10 stop | XRP | UP | 0.50 | 0.31 | -2.23 |
| 10-19 22:22 | +20 | XRP | UP | 0.50 | open |  |
| 10-19 22:22 | +15 | XRP | UP | 0.50 | open |  |
| 10-19 22:22 | +10 | XRP | UP | 0.50 | open |  |
| 10-19 22:22 | +5 | XRP | UP | 0.51 | 0.58 | 0.39 |
| 10-19 22:22 | +10 stop | DOGE | UP | 0.59 | 0.39 | -2.34 |
| 10-19 22:22 | +10 | DOGE | UP | 0.62 | open |  |
| 10-19 22:22 | +5 | DOGE | UP | 0.62 | open |  |
| 10-19 22:22 | +5 | ZEC | UP | 0.55 | 0.64 | 0.55 |
| 10-19 22:20 | +15 | SOL | UP | 0.71 | open |  |
| 10-19 22:20 | +10 | SOL | UP | 0.71 | open |  |
| 10-19 22:20 | +5 | SOL | UP | 0.71 | open |  |
| 10-19 22:20 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 10-19 22:20 | +20 | ZEC | UP | 0.62 | open |  |
| 10-19 22:20 | +15 | ZEC | UP | 0.62 | open |  |
| 10-19 22:20 | +10 | ZEC | UP | 0.62 | open |  |
