# Range-Scalp Bot

*Updated Sun Oct 18 05:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22086 | 19231 | 2855 (29) | 7 | $-6401.29 | -4.6% |
| **+10¢** | 16623 | 13325 | 3298 (41) | 7 | $-5695.26 | -5.4% |
| **+15¢** | 13918 | 10362 | 3556 (61) | 7 | $-5170.75 | -5.9% |
| **+20¢** | 12318 | 8594 | 3724 (80) | 7 | $-4599.81 | -6.0% |
| **+10¢ (15¢ stop)** | 27169 | 27119 | 50 (29) | 0 | $-10370.46 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 05:23 | +10 stop | BNB | UP | 0.56 | 0.21 | -3.75 |
| 10-18 05:23 | +10 | BNB | UP | 0.56 | open |  |
| 10-18 05:23 | +5 | BNB | UP | 0.56 | open |  |
| 10-18 05:21 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-18 05:21 | +10 stop | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-18 05:21 | +10 stop | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 10-18 05:21 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-18 05:21 | +20 | BNB | UP | 0.59 | open |  |
| 10-18 05:21 | +15 | BNB | UP | 0.59 | open |  |
| 10-18 05:21 | +10 | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-18 05:21 | +5 | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-18 05:21 | +10 stop | XRP | UP | 0.64 | 0.40 | -2.74 |
| 10-18 05:21 | +10 | XRP | UP | 0.64 | open |  |
| 10-18 05:21 | +5 | XRP | UP | 0.64 | open |  |
| 10-18 05:19 | +10 stop | BTC | UP | 0.64 | 0.36 | -3.14 |
| 10-18 05:19 | +10 | BTC | UP | 0.64 | open |  |
| 10-18 05:19 | +5 | BTC | UP | 0.64 | open |  |
| 10-18 05:19 | +5 | NEAR | UP | 0.60 | open |  |
| 10-18 05:18 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-18 05:18 | +15 | ZEC | DOWN | 0.70 | 0.90 | 1.79 |
| 10-18 05:18 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-18 05:18 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-18 05:18 | +5 | SOL | UP | 0.71 | open |  |
| 10-18 05:18 | +5 | DOGE | UP | 0.64 | open |  |
| 10-18 05:17 | +10 stop | NEAR | UP | 0.59 | 0.42 | -2.05 |
| 10-18 05:17 | +20 | NEAR | UP | 0.59 | open |  |
| 10-18 05:17 | +15 | NEAR | UP | 0.59 | open |  |
| 10-18 05:17 | +10 | NEAR | UP | 0.59 | open |  |
| 10-18 05:17 | +5 | NEAR | UP | 0.59 | 0.66 | 0.37 |
| 10-18 05:16 | +10 stop | BTC | UP | 0.65 | 0.76 | 0.81 |
| 10-18 05:16 | +20 | BTC | UP | 0.65 | open |  |
| 10-18 05:16 | +15 | BTC | UP | 0.65 | open |  |
| 10-18 05:16 | +10 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 10-18 05:16 | +5 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 10-18 05:16 | +10 stop | ETH | UP | 0.64 | 0.39 | -2.84 |
| 10-18 05:16 | +20 | ETH | UP | 0.65 | open |  |
| 10-18 05:16 | +15 | ETH | UP | 0.65 | open |  |
| 10-18 05:16 | +10 | ETH | UP | 0.65 | open |  |
| 10-18 05:16 | +5 | ETH | UP | 0.65 | open |  |
| 10-18 05:16 | +10 stop | DOGE | UP | 0.60 | 0.37 | -2.64 |
