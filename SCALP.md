# Range-Scalp Bot

*Updated Fri Nov 06 07:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49372 | 43025 | 6347 (75) | 6 | $-13977.21 | -4.5% |
| **+10¢** | 36855 | 29476 | 7379 (101) | 7 | $-12841.37 | -5.5% |
| **+15¢** | 30871 | 22926 | 7945 (130) | 6 | $-11711.87 | -6.0% |
| **+20¢** | 27441 | 19115 | 8326 (170) | 7 | $-10344.80 | -6.0% |
| **+10¢ (15¢ stop)** | 60187 | 60092 | 95 (57) | 2 | $-22291.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 07:26 | +5 | BTC | DOWN | 0.69 | open |  |
| 11-06 07:25 | +10 stop | BTC | DOWN | 0.53 | open |  |
| 11-06 07:25 | +10 | BTC | DOWN | 0.53 | open |  |
| 11-06 07:25 | +5 | BTC | DOWN | 0.53 | 0.58 | 0.14 |
| 11-06 07:25 | +10 stop | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 07:25 | +10 stop | DOGE | UP | 0.57 | open |  |
| 11-06 07:25 | +10 stop | ZEC | UP | 0.41 | 0.58 | 1.35 |
| 11-06 07:25 | +20 | ZEC | UP | 0.41 | open |  |
| 11-06 07:25 | +15 | ZEC | UP | 0.41 | 0.58 | 1.35 |
| 11-06 07:25 | +10 | ZEC | UP | 0.41 | 0.58 | 1.35 |
| 11-06 07:25 | +5 | ZEC | UP | 0.41 | 0.58 | 1.35 |
| 11-06 07:25 | +10 stop | BNB | UP | 0.47 | 0.57 | 0.64 |
| 11-06 07:25 | +5 | BNB | UP | 0.47 | 0.57 | 0.64 |
| 11-06 07:23 | +10 stop | BTC | UP | 0.60 | 0.72 | 0.88 |
| 11-06 07:23 | +5 | XRP | DOWN | 0.59 | open |  |
| 11-06 07:23 | +10 stop | ETH | DOWN | 0.67 | 0.52 | -1.85 |
| 11-06 07:22 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.13 |
| 11-06 07:22 | +20 | NEAR | UP | 0.69 | open |  |
| 11-06 07:22 | +15 | NEAR | UP | 0.70 | open |  |
| 11-06 07:22 | +10 | NEAR | UP | 0.70 | open |  |
| 11-06 07:22 | +5 | NEAR | UP | 0.69 | open |  |
| 11-06 07:22 | +10 stop | SOL | UP | 0.61 | 0.75 | 1.09 |
| 11-06 07:22 | +20 | SOL | UP | 0.61 | 0.89 | 2.56 |
| 11-06 07:22 | +15 | SOL | UP | 0.61 | 0.78 | 1.40 |
| 11-06 07:22 | +10 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 11-06 07:22 | +5 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 11-06 07:21 | +10 stop | XRP | DOWN | 0.59 | 0.32 | -3.03 |
| 11-06 07:21 | +10 | XRP | DOWN | 0.59 | open |  |
| 11-06 07:21 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 11-06 07:21 | +10 stop | BNB | UP | 0.66 | 0.46 | -2.36 |
| 11-06 07:21 | +20 | BNB | UP | 0.66 | open |  |
| 11-06 07:21 | +15 | BNB | UP | 0.66 | open |  |
| 11-06 07:21 | +10 | BNB | UP | 0.66 | open |  |
| 11-06 07:21 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 11-06 07:21 | +10 stop | DOGE | UP | 0.70 | 0.43 | -3.03 |
| 11-06 07:21 | +15 | DOGE | UP | 0.70 | open |  |
| 11-06 07:21 | +10 | DOGE | UP | 0.70 | open |  |
| 11-06 07:21 | +5 | DOGE | UP | 0.70 | open |  |
| 11-06 07:21 | +10 stop | ETH | UP | 0.57 | 0.32 | -2.84 |
| 11-06 07:21 | +15 | ETH | UP | 0.57 | open |  |
