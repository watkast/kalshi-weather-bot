# Range-Scalp Bot

*Updated Sat Oct 17 07:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20562 | 17883 | 2679 (29) | 1 | $-6094.88 | -4.7% |
| **+10¢** | 15493 | 12408 | 3085 (41) | 1 | $-5387.03 | -5.5% |
| **+15¢** | 12956 | 9639 | 3317 (60) | 1 | $-4848.93 | -6.0% |
| **+20¢** | 11484 | 8009 | 3475 (79) | 1 | $-4294.24 | -6.0% |
| **+10¢ (15¢ stop)** | 25279 | 25229 | 50 (29) | 1 | $-9555.07 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 07:00 | +10 stop | BNB | UP | 0.58 | open |  |
| 10-17 07:00 | +20 | BNB | UP | 0.58 | open |  |
| 10-17 07:00 | +15 | BNB | UP | 0.58 | open |  |
| 10-17 07:00 | +10 | BNB | UP | 0.58 | open |  |
| 10-17 07:00 | +5 | BNB | UP | 0.58 | open |  |
| 10-17 06:59 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-17 06:58 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-17 06:57 | +10 stop | ETH | DOWN | 0.31 | 0.61 | 2.68 |
| 10-17 06:56 | +10 stop | ETH | UP | 0.62 | 0.43 | -2.25 |
| 10-17 06:56 | +10 stop | BTC | UP | 0.63 | 0.43 | -2.35 |
| 10-17 06:56 | +10 stop | BNB | DOWN | 0.63 | 0.39 | -2.74 |
| 10-17 06:56 | +15 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-17 06:56 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-17 06:56 | +5 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-17 06:55 | +10 stop | BTC | DOWN | 0.66 | 0.43 | -2.64 |
| 10-17 06:55 | +10 stop | ETH | DOWN | 0.64 | 0.41 | -2.64 |
| 10-17 06:55 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-17 06:55 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-17 06:55 | +20 | XRP | UP | 0.64 | 0.87 | 2.05 |
| 10-17 06:55 | +15 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-17 06:55 | +10 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-17 06:55 | +5 | XRP | UP | 0.66 | 0.75 | 0.60 |
| 10-17 06:54 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 10-17 06:54 | +10 stop | BTC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-17 06:54 | +10 stop | HYPE | UP | 0.49 | 0.60 | 0.75 |
| 10-17 06:53 | +5 | BTC | UP | 0.62 | 0.71 | 0.58 |
| 10-17 06:53 | +10 stop | NEAR | DOWN | 0.60 | 0.82 | 1.95 |
| 10-17 06:53 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.95 |
| 10-17 06:53 | +15 | NEAR | DOWN | 0.60 | 0.82 | 1.95 |
| 10-17 06:53 | +10 | NEAR | DOWN | 0.60 | 0.82 | 1.95 |
| 10-17 06:53 | +5 | NEAR | DOWN | 0.60 | 0.82 | 1.95 |
| 10-17 06:53 | +10 stop | SOL | UP | 0.59 | 0.42 | -2.05 |
| 10-17 06:53 | +10 | SOL | UP | 0.59 | 0.76 | 1.40 |
| 10-17 06:53 | +5 | SOL | UP | 0.59 | 0.76 | 1.40 |
| 10-17 06:53 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-17 06:52 | +10 stop | BTC | UP | 0.70 | 0.35 | -3.81 |
| 10-17 06:51 | +10 stop | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 10-17 06:51 | +10 stop | HYPE | DOWN | 0.53 | 0.38 | -1.85 |
| 10-17 06:51 | +10 stop | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 10-17 06:51 | +10 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
