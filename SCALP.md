# Range-Scalp Bot

*Updated Thu Oct 22 00:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27958 | 24358 | 3600 (39) | 4 | $-8056.30 | -4.6% |
| **+10¢** | 21006 | 16851 | 4155 (55) | 5 | $-7076.90 | -5.4% |
| **+15¢** | 17595 | 13123 | 4472 (78) | 5 | $-6310.32 | -5.7% |
| **+20¢** | 15576 | 10890 | 4686 (98) | 5 | $-5633.50 | -5.8% |
| **+10¢ (15¢ stop)** | 34321 | 34262 | 59 (32) | 1 | $-12814.25 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 00:24 | +10 stop | BNB | DOWN | 0.69 | 0.49 | -2.33 |
| 10-22 00:24 | +10 stop | SOL | DOWN | 0.66 | 0.44 | -2.54 |
| 10-22 00:24 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 10-22 00:24 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 10-22 00:23 | +10 stop | ZEC | DOWN | 0.53 | 0.22 | -3.44 |
| 10-22 00:23 | +20 | ZEC | DOWN | 0.53 | open |  |
| 10-22 00:23 | +15 | ZEC | DOWN | 0.53 | open |  |
| 10-22 00:23 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-22 00:23 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-22 00:22 | +10 stop | NEAR | DOWN | 0.63 | 0.42 | -2.45 |
| 10-22 00:22 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 10-22 00:21 | +10 stop | SOL | DOWN | 0.63 | 0.40 | -2.64 |
| 10-22 00:20 | +5 | NEAR | UP | 0.65 | open |  |
| 10-22 00:20 | +15 | BNB | UP | 0.67 | open |  |
| 10-22 00:20 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.14 |
| 10-22 00:20 | +10 | ZEC | DOWN | 0.65 | 0.79 | 1.14 |
| 10-22 00:20 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-22 00:20 | +10 stop | SOL | UP | 0.63 | 0.48 | -1.85 |
| 10-22 00:19 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 00:19 | +10 stop | BNB | UP | 0.70 | 0.51 | -2.23 |
| 10-22 00:19 | +10 | BNB | UP | 0.70 | open |  |
| 10-22 00:19 | +5 | BNB | UP | 0.70 | open |  |
| 10-22 00:19 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 00:19 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-22 00:19 | +5 | ETH | DOWN | 0.63 | 0.70 | 0.38 |
| 10-22 00:19 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-22 00:18 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-22 00:18 | +10 stop | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-22 00:18 | +10 stop | NEAR | UP | 0.62 | 0.38 | -2.74 |
| 10-22 00:18 | +20 | NEAR | UP | 0.62 | open |  |
| 10-22 00:18 | +15 | NEAR | UP | 0.62 | open |  |
| 10-22 00:18 | +10 | NEAR | UP | 0.62 | open |  |
| 10-22 00:18 | +5 | NEAR | UP | 0.62 | 0.67 | 0.17 |
| 10-22 00:18 | +5 | BNB | UP | 0.54 | 0.63 | 0.55 |
| 10-22 00:17 | +10 stop | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-22 00:17 | +20 | BNB | UP | 0.53 | open |  |
| 10-22 00:17 | +15 | BNB | UP | 0.53 | 0.69 | 1.27 |
| 10-22 00:17 | +10 | BNB | UP | 0.53 | 0.63 | 0.65 |
| 10-22 00:17 | +5 | BNB | UP | 0.54 | 0.60 | 0.25 |
| 10-22 00:17 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
