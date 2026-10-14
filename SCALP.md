# Range-Scalp Bot

*Updated Wed Oct 14 05:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15516 | 13435 | 2081 (27) | 4 | $-4912.39 | -5.0% |
| **+10¢** | 11744 | 9330 | 2414 (39) | 5 | $-4562.51 | -6.2% |
| **+15¢** | 9860 | 7271 | 2589 (58) | 6 | $-4086.94 | -6.6% |
| **+20¢** | 8762 | 6052 | 2710 (75) | 8 | $-3610.61 | -6.6% |
| **+10¢ (15¢ stop)** | 19059 | 19009 | 50 (29) | 1 | $-7332.13 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 05:41 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 10-14 05:36 | +10 stop | SOL | DOWN | 0.71 | 0.90 | 1.69 |
| 10-14 05:36 | +10 stop | BTC | UP | 0.52 | 0.27 | -2.82 |
| 10-14 05:36 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-14 05:36 | +5 | ETH | DOWN | 0.64 | 0.73 | 0.59 |
| 10-14 05:36 | +10 stop | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 10-14 05:36 | +15 | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 10-14 05:36 | +10 | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 10-14 05:36 | +5 | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 10-14 05:34 | +10 stop | DOGE | DOWN | 0.70 | 0.53 | -2.04 |
| 10-14 05:34 | +10 stop | XRP | DOWN | 0.71 | 0.54 | -2.03 |
| 10-14 05:34 | +10 stop | BTC | DOWN | 0.70 | 0.50 | -2.33 |
| 10-14 05:34 | +10 stop | HYPE | UP | 0.56 | 0.36 | -2.39 |
| 10-14 05:34 | +20 | HYPE | UP | 0.56 | open |  |
| 10-14 05:33 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 10-14 05:33 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-14 05:33 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-14 05:33 | +5 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-14 05:33 | +10 stop | BNB | DOWN | 0.57 | 0.83 | 2.32 |
| 10-14 05:33 | +15 | BNB | DOWN | 0.57 | 0.83 | 2.32 |
| 10-14 05:33 | +10 | BNB | DOWN | 0.57 | 0.83 | 2.32 |
| 10-14 05:33 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-14 05:32 | +10 stop | SOL | DOWN | 0.63 | 0.46 | -2.05 |
| 10-14 05:32 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-14 05:32 | +10 stop | DOGE | DOWN | 0.64 | 0.48 | -1.95 |
| 10-14 05:32 | +10 stop | XRP | DOWN | 0.68 | 0.48 | -2.34 |
| 10-14 05:32 | +10 stop | HYPE | DOWN | 0.63 | 0.31 | -3.52 |
| 10-14 05:32 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-14 05:32 | +10 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-14 05:32 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-14 05:32 | +10 stop | HYPE | UP | 0.47 | 0.66 | 1.56 |
| 10-14 05:32 | +20 | HYPE | UP | 0.47 | 0.68 | 1.76 |
| 10-14 05:32 | +15 | HYPE | UP | 0.47 | 0.66 | 1.56 |
| 10-14 05:32 | +10 | HYPE | UP | 0.47 | 0.66 | 1.56 |
| 10-14 05:32 | +5 | HYPE | UP | 0.47 | 0.66 | 1.56 |
| 10-14 05:32 | +10 stop | ZEC | DOWN | 0.66 | 0.84 | 1.51 |
| 10-14 05:32 | +20 | ZEC | DOWN | 0.66 | 0.89 | 2.04 |
| 10-14 05:32 | +15 | ZEC | DOWN | 0.66 | 0.84 | 1.51 |
| 10-14 05:32 | +10 | ZEC | DOWN | 0.66 | 0.84 | 1.51 |
| 10-14 05:32 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.57 |
