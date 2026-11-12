# Range-Scalp Bot

*Updated Thu Nov 12 04:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56609 | 49349 | 7260 (98) | 5 | $-15594.55 | -4.4% |
| **+10¢** | 42302 | 33833 | 8469 (128) | 5 | $-14544.35 | -5.5% |
| **+15¢** | 35467 | 26349 | 9118 (162) | 5 | $-13182.80 | -5.9% |
| **+20¢** | 31599 | 22030 | 9569 (212) | 5 | $-11573.05 | -5.8% |
| **+10¢ (15¢ stop)** | 69020 | 68897 | 123 (73) | 0 | $-25491.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 04:13 | +10 stop | BNB | DOWN | 0.70 | 0.88 | 1.57 |
| 11-12 04:13 | +10 stop | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 11-12 04:11 | +10 stop | BNB | DOWN | 0.65 | 0.29 | -3.91 |
| 11-12 04:10 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-12 04:09 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-12 04:08 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 04:08 | +10 stop | BTC | UP | 0.66 | 0.35 | -3.42 |
| 11-12 04:08 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 11-12 04:08 | +5 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-12 04:07 | +10 stop | SOL | DOWN | 0.57 | 0.73 | 1.28 |
| 11-12 04:07 | +10 stop | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 11-12 04:07 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 11-12 04:07 | +10 stop | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
| 11-12 04:07 | +10 | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
| 11-12 04:06 | +10 stop | XRP | UP | 0.57 | 0.38 | -2.25 |
| 11-12 04:06 | +20 | XRP | UP | 0.59 | open |  |
| 11-12 04:06 | +15 | XRP | UP | 0.59 | open |  |
| 11-12 04:06 | +10 | XRP | UP | 0.59 | open |  |
| 11-12 04:06 | +5 | XRP | UP | 0.59 | open |  |
| 11-12 04:05 | +10 stop | NEAR | DOWN | 0.50 | 0.60 | 0.65 |
| 11-12 04:05 | +15 | NEAR | DOWN | 0.50 | 0.71 | 1.77 |
| 11-12 04:05 | +10 | NEAR | DOWN | 0.50 | 0.60 | 0.65 |
| 11-12 04:05 | +10 stop | BNB | UP | 0.69 | 0.48 | -2.42 |
| 11-12 04:05 | +10 | BNB | UP | 0.69 | open |  |
| 11-12 04:05 | +5 | BNB | UP | 0.69 | open |  |
| 11-12 04:05 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 11-12 04:05 | +10 stop | DOGE | UP | 0.61 | 0.46 | -1.85 |
| 11-12 04:03 | +5 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-12 04:03 | +5 | ZEC | UP | 0.59 | 0.66 | 0.37 |
| 11-12 04:03 | +10 stop | ZEC | UP | 0.57 | 0.76 | 1.59 |
| 11-12 04:03 | +20 | ZEC | UP | 0.56 | 0.76 | 1.69 |
| 11-12 04:03 | +15 | ZEC | UP | 0.56 | 0.76 | 1.69 |
| 11-12 04:03 | +10 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-12 04:03 | +5 | ZEC | UP | 0.56 | 0.61 | 0.15 |
| 11-12 04:03 | +5 | BNB | UP | 0.68 | 0.76 | 0.52 |
| 11-12 04:02 | +10 stop | SOL | UP | 0.56 | 0.36 | -2.35 |
| 11-12 04:02 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-12 04:02 | +20 | NEAR | DOWN | 0.59 | 0.84 | 2.23 |
| 11-12 04:02 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-12 04:02 | +10 | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
