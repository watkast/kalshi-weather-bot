# Range-Scalp Bot

*Updated Sat Oct 10 00:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9670 | 8348 | 1322 (18) | 2 | $-3254.34 | -5.3% |
| **+10¢** | 7302 | 5755 | 1547 (30) | 2 | $-3150.69 | -6.9% |
| **+15¢** | 6157 | 4526 | 1631 (43) | 2 | $-2610.35 | -6.8% |
| **+20¢** | 5478 | 3785 | 1693 (55) | 4 | $-2161.09 | -6.3% |
| **+10¢ (15¢ stop)** | 11842 | 11807 | 35 (22) | 0 | $-4573.23 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 00:08 | +10 stop | BTC | DOWN | 0.61 | 0.30 | -3.42 |
| 10-10 00:08 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-10 00:08 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-10 00:08 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-10 00:08 | +10 stop | ZEC | UP | 0.52 | 0.64 | 0.85 |
| 10-10 00:08 | +15 | ZEC | UP | 0.52 | 0.84 | 2.92 |
| 10-10 00:08 | +10 | ZEC | UP | 0.52 | 0.64 | 0.85 |
| 10-10 00:08 | +5 | ZEC | UP | 0.52 | 0.57 | 0.14 |
| 10-10 00:08 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-10 00:08 | +10 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-10 00:08 | +5 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-10 00:07 | +10 stop | ZEC | DOWN | 0.31 | 0.50 | 1.57 |
| 10-10 00:07 | +20 | ZEC | DOWN | 0.31 | open |  |
| 10-10 00:07 | +15 | ZEC | DOWN | 0.32 | 0.50 | 1.46 |
| 10-10 00:07 | +10 | ZEC | DOWN | 0.32 | 0.50 | 1.46 |
| 10-10 00:07 | +5 | ZEC | DOWN | 0.32 | 0.50 | 1.46 |
| 10-10 00:04 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-10 00:04 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 00:04 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-10 00:04 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 10-10 00:04 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 00:04 | +5 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 00:04 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-10 00:04 | +20 | XRP | UP | 0.55 | 0.83 | 2.52 |
| 10-10 00:04 | +15 | XRP | UP | 0.55 | 0.83 | 2.52 |
| 10-10 00:04 | +10 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-10 00:04 | +5 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-10 00:04 | +10 stop | NEAR | UP | 0.48 | 0.60 | 0.86 |
| 10-10 00:04 | +10 stop | DOGE | UP | 0.28 | 0.55 | 2.37 |
| 10-10 00:04 | +5 | DOGE | UP | 0.28 | 0.55 | 2.37 |
| 10-10 00:03 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-10 00:03 | +10 stop | NEAR | DOWN | 0.55 | 0.38 | -2.05 |
| 10-10 00:02 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 00:02 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 10-10 00:02 | +15 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 10-10 00:02 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 00:02 | +5 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 00:02 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.68 |
| 10-10 00:02 | +20 | ZEC | DOWN | 0.58 | 0.79 | 1.78 |
| 10-10 00:02 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.36 |
