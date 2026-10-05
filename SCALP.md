# Range-Scalp Bot

*Updated Mon Oct 05 19:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4161 | 3576 | 585 (4) | 3 | $-1507.74 | -5.7% |
| **+10¢** | 3214 | 2544 | 670 (5) | 4 | $-1354.57 | -6.7% |
| **+15¢** | 2698 | 1993 | 705 (8) | 4 | $-1158.31 | -6.8% |
| **+20¢** | 2408 | 1674 | 734 (13) | 4 | $-984.90 | -6.5% |
| **+10¢ (15¢ stop)** | 5133 | 5128 | 5 (2) | 1 | $-1875.04 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 19:08 | +10 stop | ZEC | UP | 0.63 | open |  |
| 10-05 19:08 | +10 | ZEC | UP | 0.63 | open |  |
| 10-05 19:08 | +5 | ZEC | UP | 0.63 | open |  |
| 10-05 19:06 | +10 stop | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 10-05 19:06 | +10 | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 10-05 19:06 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-05 19:06 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-05 19:05 | +10 stop | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-05 19:05 | +10 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-05 19:05 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 10-05 19:04 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 19:04 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-05 19:04 | +10 stop | ZEC | UP | 0.57 | 0.32 | -2.81 |
| 10-05 19:04 | +10 | ZEC | UP | 0.57 | 0.74 | 1.41 |
| 10-05 19:04 | +5 | ZEC | UP | 0.57 | 0.65 | 0.49 |
| 10-05 19:04 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-05 19:04 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-05 19:04 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 10-05 19:04 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-05 19:04 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-05 19:02 | +5 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 10-05 19:02 | +10 stop | HYPE | UP | 0.56 | 0.69 | 0.97 |
| 10-05 19:01 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-05 19:01 | +10 stop | BNB | UP | 0.55 | 0.26 | -3.22 |
| 10-05 19:01 | +20 | BNB | UP | 0.55 | open |  |
| 10-05 19:01 | +15 | BNB | UP | 0.55 | open |  |
| 10-05 19:01 | +10 | BNB | UP | 0.55 | open |  |
| 10-05 19:01 | +5 | BNB | UP | 0.55 | open |  |
| 10-05 19:01 | +10 stop | NEAR | UP | 0.53 | 0.35 | -2.14 |
| 10-05 19:01 | +20 | NEAR | UP | 0.53 | open |  |
| 10-05 19:01 | +15 | NEAR | UP | 0.53 | open |  |
| 10-05 19:01 | +10 | NEAR | UP | 0.53 | open |  |
| 10-05 19:01 | +5 | NEAR | UP | 0.53 | 0.60 | 0.36 |
| 10-05 19:01 | +10 stop | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 10-05 19:01 | +20 | SOL | DOWN | 0.58 | 0.79 | 1.80 |
| 10-05 19:01 | +15 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 10-05 19:01 | +10 | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 10-05 19:01 | +5 | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 10-05 19:01 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-05 19:01 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
