# Range-Scalp Bot

*Updated Thu Oct 15 00:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16762 | 14536 | 2226 (28) | 2 | $-5218.46 | -4.9% |
| **+10¢** | 12675 | 10095 | 2580 (40) | 3 | $-4766.82 | -6.0% |
| **+15¢** | 10647 | 7875 | 2772 (59) | 2 | $-4283.29 | -6.4% |
| **+20¢** | 9459 | 6555 | 2904 (76) | 2 | $-3780.94 | -6.4% |
| **+10¢ (15¢ stop)** | 20633 | 20583 | 50 (29) | 2 | $-7924.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 00:08 | +5 | NEAR | UP | 0.67 | open |  |
| 10-15 00:07 | +10 stop | NEAR | UP | 0.59 | open |  |
| 10-15 00:07 | +20 | NEAR | UP | 0.59 | open |  |
| 10-15 00:07 | +15 | NEAR | UP | 0.60 | open |  |
| 10-15 00:07 | +10 | NEAR | UP | 0.60 | open |  |
| 10-15 00:07 | +5 | NEAR | UP | 0.59 | 0.65 | 0.27 |
| 10-15 00:07 | +10 stop | BNB | UP | 0.54 | open |  |
| 10-15 00:07 | +20 | BNB | UP | 0.54 | open |  |
| 10-15 00:07 | +15 | BNB | UP | 0.54 | open |  |
| 10-15 00:07 | +10 | BNB | UP | 0.54 | open |  |
| 10-15 00:07 | +5 | BNB | UP | 0.54 | 0.59 | 0.15 |
| 10-15 00:03 | +10 | NEAR | UP | 0.65 | 0.81 | 1.33 |
| 10-15 00:03 | +10 stop | SOL | UP | 0.70 | 0.84 | 1.15 |
| 10-15 00:03 | +5 | SOL | UP | 0.70 | 0.84 | 1.15 |
| 10-15 00:03 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-15 00:03 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-15 00:03 | +15 | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 10-15 00:03 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-15 00:02 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-15 00:02 | +10 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-15 00:02 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 10-15 00:02 | +20 | XRP | UP | 0.60 | 0.84 | 2.13 |
| 10-15 00:02 | +15 | XRP | UP | 0.60 | 0.76 | 1.30 |
| 10-15 00:02 | +10 | XRP | UP | 0.60 | 0.70 | 0.68 |
| 10-15 00:02 | +5 | XRP | UP | 0.60 | 0.67 | 0.37 |
| 10-15 00:02 | +10 stop | BNB | DOWN | 0.49 | 0.30 | -2.23 |
| 10-15 00:02 | +10 stop | SOL | DOWN | 0.48 | 0.33 | -1.84 |
| 10-15 00:02 | +10 stop | DOGE | DOWN | 0.57 | 0.40 | -2.05 |
| 10-15 00:02 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-15 00:02 | +5 | DOGE | DOWN | 0.57 | open |  |
| 10-15 00:02 | +5 | ETH | UP | 0.61 | 0.66 | 0.19 |
| 10-15 00:01 | +10 stop | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 10-15 00:01 | +10 | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 10-15 00:01 | +10 | ETH | UP | 0.53 | 0.66 | 0.96 |
| 10-15 00:01 | +5 | NEAR | UP | 0.59 | 0.81 | 1.95 |
| 10-15 00:01 | +10 stop | ETH | UP | 0.63 | 0.75 | 0.89 |
| 10-15 00:01 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-15 00:01 | +5 | BTC | UP | 0.61 | 0.66 | 0.17 |
| 10-15 00:01 | +10 stop | BNB | UP | 0.61 | 0.41 | -2.34 |
| 10-15 00:01 | +10 | BNB | UP | 0.61 | 0.77 | 1.30 |
