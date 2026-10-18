# Range-Scalp Bot

*Updated Sun Oct 18 03:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21982 | 19148 | 2834 (29) | 2 | $-6313.00 | -4.6% |
| **+10¢** | 16540 | 13264 | 3276 (41) | 1 | $-5622.76 | -5.4% |
| **+15¢** | 13849 | 10316 | 3533 (61) | 1 | $-5098.68 | -5.9% |
| **+20¢** | 12254 | 8552 | 3702 (80) | 2 | $-4551.50 | -5.9% |
| **+10¢ (15¢ stop)** | 27046 | 26996 | 50 (29) | 0 | $-10343.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 03:05 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-18 03:05 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-18 03:05 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-18 03:05 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 10-18 03:04 | +10 stop | DOGE | UP | 0.60 | 0.79 | 1.61 |
| 10-18 03:04 | +10 stop | HYPE | UP | 0.54 | 0.72 | 1.47 |
| 10-18 03:03 | +5 | ZEC | DOWN | 0.57 | open |  |
| 10-18 03:03 | +10 stop | ETH | DOWN | 0.63 | 0.45 | -2.15 |
| 10-18 03:03 | +10 stop | BTC | DOWN | 0.57 | 0.42 | -1.86 |
| 10-18 03:03 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-18 03:03 | +10 stop | NEAR | DOWN | 0.57 | 0.34 | -2.64 |
| 10-18 03:03 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-18 03:03 | +15 | NEAR | DOWN | 0.57 | open |  |
| 10-18 03:03 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-18 03:03 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-18 03:03 | +10 stop | SOL | DOWN | 0.66 | 0.45 | -2.44 |
| 10-18 03:02 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 10-18 03:02 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-18 03:02 | +20 | XRP | UP | 0.67 | 0.88 | 1.86 |
| 10-18 03:02 | +15 | XRP | UP | 0.67 | 0.82 | 1.23 |
| 10-18 03:02 | +10 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-18 03:02 | +5 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 10-18 03:02 | +10 stop | ZEC | UP | 0.52 | 0.74 | 1.86 |
| 10-18 03:02 | +20 | ZEC | UP | 0.52 | 0.74 | 1.84 |
| 10-18 03:02 | +15 | ZEC | UP | 0.52 | 0.74 | 1.84 |
| 10-18 03:02 | +10 | ZEC | UP | 0.52 | 0.74 | 1.84 |
| 10-18 03:02 | +5 | ZEC | UP | 0.52 | 0.60 | 0.43 |
| 10-18 03:01 | +10 stop | BNB | UP | 0.66 | 0.88 | 1.96 |
| 10-18 03:01 | +20 | BNB | UP | 0.66 | 0.88 | 1.96 |
| 10-18 03:01 | +15 | BNB | UP | 0.66 | 0.88 | 1.96 |
| 10-18 03:01 | +10 | BNB | UP | 0.66 | 0.88 | 1.96 |
| 10-18 03:01 | +5 | BNB | UP | 0.66 | 0.73 | 0.40 |
| 10-18 03:01 | +10 stop | DOGE | UP | 0.70 | 0.51 | -2.25 |
| 10-18 03:01 | +20 | DOGE | UP | 0.70 | 0.90 | 1.78 |
| 10-18 03:01 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-18 03:01 | +10 | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 10-18 03:01 | +5 | DOGE | UP | 0.71 | 0.79 | 0.53 |
| 10-18 03:01 | +10 stop | SOL | UP | 0.63 | 0.46 | -2.05 |
| 10-18 03:01 | +20 | SOL | UP | 0.65 | open |  |
| 10-18 03:01 | +15 | SOL | UP | 0.65 | 0.80 | 1.22 |
