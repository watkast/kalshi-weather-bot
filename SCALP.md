# Range-Scalp Bot

*Updated Fri Oct 16 22:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19943 | 17347 | 2596 (29) | 4 | $-5899.43 | -4.7% |
| **+10¢** | 15024 | 12023 | 3001 (41) | 4 | $-5294.94 | -5.6% |
| **+15¢** | 12565 | 9338 | 3227 (60) | 5 | $-4781.36 | -6.1% |
| **+20¢** | 11145 | 7766 | 3379 (79) | 5 | $-4209.89 | -6.0% |
| **+10¢ (15¢ stop)** | 24508 | 24458 | 50 (29) | 1 | $-9317.15 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 22:26 | +5 | XRP | UP | 0.51 | 0.63 | 0.85 |
| 10-16 22:25 | +10 stop | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 10-16 22:25 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-16 22:25 | +5 | BTC | UP | 0.63 | open |  |
| 10-16 22:24 | +10 stop | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-16 22:24 | +10 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-16 22:24 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-16 22:24 | +20 | XRP | UP | 0.66 | open |  |
| 10-16 22:24 | +15 | XRP | UP | 0.66 | open |  |
| 10-16 22:24 | +10 | XRP | UP | 0.66 | open |  |
| 10-16 22:24 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 10-16 22:23 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 10-16 22:23 | +20 | SOL | UP | 0.66 | open |  |
| 10-16 22:23 | +10 | SOL | UP | 0.66 | open |  |
| 10-16 22:23 | +5 | SOL | UP | 0.66 | open |  |
| 10-16 22:23 | +10 stop | BTC | UP | 0.63 | 0.42 | -2.45 |
| 10-16 22:23 | +15 | BTC | UP | 0.63 | open |  |
| 10-16 22:23 | +10 | BTC | UP | 0.63 | open |  |
| 10-16 22:23 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-16 22:23 | +10 stop | ETH | UP | 0.61 | 0.42 | -2.25 |
| 10-16 22:21 | +10 stop | BNB | UP | 0.70 | 0.53 | -2.00 |
| 10-16 22:21 | +5 | BNB | UP | 0.70 | open |  |
| 10-16 22:21 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-16 22:21 | +10 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-16 22:21 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-16 22:20 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-16 22:20 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.77 |
| 10-16 22:19 | +15 | SOL | UP | 0.68 | open |  |
| 10-16 22:19 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-16 22:19 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-16 22:19 | +10 stop | DOGE | UP | 0.63 | 0.41 | -2.54 |
| 10-16 22:19 | +10 | DOGE | UP | 0.63 | open |  |
| 10-16 22:19 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-16 22:19 | +5 | DOGE | UP | 0.64 | open |  |
| 10-16 22:19 | +15 | NEAR | UP | 0.63 | 0.93 | 2.73 |
| 10-16 22:19 | +5 | NEAR | UP | 0.63 | 0.71 | 0.48 |
| 10-16 22:19 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-16 22:18 | +5 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-16 22:18 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 10-16 22:18 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
