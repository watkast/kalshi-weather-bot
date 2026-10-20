# Range-Scalp Bot

*Updated Tue Oct 20 14:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25739 | 22421 | 3318 (31) | 4 | $-7486.88 | -4.6% |
| **+10¢** | 19372 | 15540 | 3832 (46) | 4 | $-6600.49 | -5.4% |
| **+15¢** | 16216 | 12088 | 4128 (70) | 6 | $-5913.88 | -5.8% |
| **+20¢** | 14344 | 10022 | 4322 (88) | 7 | $-5275.21 | -5.9% |
| **+10¢ (15¢ stop)** | 31572 | 31519 | 53 (30) | 0 | $-11651.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 14:23 | +5 | NEAR | DOWN | 0.58 | open |  |
| 10-20 14:22 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.43 |
| 10-20 14:21 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
| 10-20 14:21 | +10 stop | DOGE | DOWN | 0.66 | 0.35 | -3.42 |
| 10-20 14:21 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 10-20 14:20 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 10-20 14:20 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.85 |
| 10-20 14:20 | +20 | NEAR | UP | 0.56 | open |  |
| 10-20 14:20 | +15 | NEAR | UP | 0.56 | open |  |
| 10-20 14:20 | +10 | NEAR | UP | 0.56 | open |  |
| 10-20 14:20 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-20 14:20 | +10 stop | DOGE | UP | 0.53 | 0.35 | -2.14 |
| 10-20 14:20 | +10 | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-20 14:19 | +5 | DOGE | UP | 0.64 | open |  |
| 10-20 14:19 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 14:19 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-20 14:19 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-20 14:19 | +10 stop | SOL | UP | 0.68 | 0.43 | -2.84 |
| 10-20 14:19 | +20 | SOL | UP | 0.68 | open |  |
| 10-20 14:19 | +15 | SOL | UP | 0.69 | open |  |
| 10-20 14:19 | +10 | SOL | UP | 0.69 | open |  |
| 10-20 14:19 | +5 | SOL | UP | 0.69 | open |  |
| 10-20 14:19 | +5 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-20 14:19 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-20 14:19 | +10 stop | DOGE | UP | 0.55 | 0.66 | 0.76 |
| 10-20 14:19 | +20 | DOGE | UP | 0.55 | open |  |
| 10-20 14:19 | +15 | DOGE | UP | 0.55 | open |  |
| 10-20 14:19 | +10 | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 10-20 14:19 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 10-20 14:18 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 10-20 14:18 | +15 | ETH | UP | 0.63 | open |  |
| 10-20 14:18 | +10 | ETH | UP | 0.63 | open |  |
| 10-20 14:18 | +5 | ETH | UP | 0.63 | open |  |
| 10-20 14:18 | +10 stop | XRP | UP | 0.48 | 0.28 | -2.33 |
| 10-20 14:18 | +20 | XRP | UP | 0.48 | open |  |
| 10-20 14:18 | +15 | XRP | UP | 0.48 | open |  |
| 10-20 14:18 | +10 | NEAR | UP | 0.62 | 0.75 | 0.99 |
| 10-20 14:18 | +10 stop | BNB | UP | 0.47 | 0.30 | -2.03 |
| 10-20 14:18 | +5 | BNB | UP | 0.43 | 0.53 | 0.60 |
| 10-20 14:18 | +10 stop | BTC | UP | 0.47 | 0.57 | 0.64 |
