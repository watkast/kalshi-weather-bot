# Range-Scalp Bot

*Updated Sat Oct 17 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21724 | 18936 | 2788 (29) | 8 | $-6160.04 | -4.5% |
| **+10¢** | 16339 | 13115 | 3224 (41) | 9 | $-5472.52 | -5.3% |
| **+15¢** | 13663 | 10184 | 3479 (61) | 9 | $-4969.92 | -5.8% |
| **+20¢** | 12097 | 8449 | 3648 (80) | 9 | $-4438.47 | -5.8% |
| **+10¢ (15¢ stop)** | 26699 | 26649 | 50 (29) | 0 | $-10165.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 23:26 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.73 |
| 10-17 23:26 | +10 stop | SOL | DOWN | 0.71 | 0.90 | 1.70 |
| 10-17 23:25 | +10 stop | ETH | DOWN | 0.48 | 0.65 | 1.39 |
| 10-17 23:24 | +10 stop | SOL | DOWN | 0.65 | 0.48 | -2.04 |
| 10-17 23:23 | +10 stop | SOL | DOWN | 0.46 | 0.59 | 0.95 |
| 10-17 23:23 | +10 stop | NEAR | DOWN | 0.71 | 0.89 | 1.58 |
| 10-17 23:22 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 10-17 23:22 | +20 | ZEC | UP | 0.67 | open |  |
| 10-17 23:22 | +15 | ZEC | UP | 0.67 | open |  |
| 10-17 23:22 | +10 | ZEC | UP | 0.67 | open |  |
| 10-17 23:22 | +5 | ZEC | UP | 0.67 | open |  |
| 10-17 23:22 | +10 stop | SOL | UP | 0.59 | 0.44 | -1.85 |
| 10-17 23:22 | +10 stop | NEAR | UP | 0.52 | 0.37 | -1.85 |
| 10-17 23:21 | +10 stop | ETH | UP | 0.58 | 0.26 | -3.52 |
| 10-17 23:21 | +10 stop | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-17 23:21 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-17 23:20 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-17 23:20 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-17 23:19 | +10 stop | ETH | UP | 0.69 | 0.52 | -2.03 |
| 10-17 23:19 | +15 | ETH | UP | 0.68 | open |  |
| 10-17 23:19 | +10 | ETH | UP | 0.68 | open |  |
| 10-17 23:19 | +5 | ETH | UP | 0.68 | open |  |
| 10-17 23:19 | +5 | NEAR | UP | 0.65 | open |  |
| 10-17 23:19 | +10 stop | SOL | UP | 0.69 | 0.54 | -1.83 |
| 10-17 23:19 | +10 | SOL | UP | 0.69 | open |  |
| 10-17 23:19 | +5 | SOL | UP | 0.69 | open |  |
| 10-17 23:19 | +10 stop | XRP | UP | 0.60 | 0.39 | -2.44 |
| 10-17 23:19 | +10 | XRP | UP | 0.60 | open |  |
| 10-17 23:19 | +5 | XRP | UP | 0.60 | open |  |
| 10-17 23:18 | +10 stop | BTC | UP | 0.61 | 0.45 | -1.95 |
| 10-17 23:18 | +10 | BTC | UP | 0.61 | open |  |
| 10-17 23:18 | +5 | BTC | UP | 0.61 | open |  |
| 10-17 23:17 | +5 | XRP | UP | 0.66 | 0.77 | 0.81 |
| 10-17 23:17 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-17 23:16 | +10 stop | DOGE | UP | 0.67 | 0.52 | -1.84 |
| 10-17 23:16 | +20 | DOGE | UP | 0.67 | open |  |
| 10-17 23:16 | +15 | DOGE | UP | 0.67 | open |  |
| 10-17 23:16 | +10 | DOGE | UP | 0.67 | open |  |
| 10-17 23:16 | +5 | DOGE | UP | 0.67 | open |  |
| 10-17 23:16 | +10 stop | ETH | UP | 0.65 | 0.80 | 1.22 |
