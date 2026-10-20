# Range-Scalp Bot

*Updated Tue Oct 20 10:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25486 | 22194 | 3292 (31) | 3 | $-7440.59 | -4.6% |
| **+10¢** | 19183 | 15376 | 3807 (46) | 3 | $-6613.87 | -5.5% |
| **+15¢** | 16049 | 11949 | 4100 (70) | 3 | $-5955.72 | -5.9% |
| **+20¢** | 14190 | 9899 | 4291 (88) | 3 | $-5330.95 | -6.0% |
| **+10¢ (15¢ stop)** | 31288 | 31235 | 53 (30) | 0 | $-11564.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 10:10 | +10 stop | HYPE | UP | 0.50 | 0.63 | 0.95 |
| 10-20 10:08 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-20 10:08 | +5 | HYPE | DOWN | 0.62 | open |  |
| 10-20 10:08 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 10-20 10:06 | +10 stop | SOL | UP | 0.59 | 0.75 | 1.29 |
| 10-20 10:05 | +10 stop | HYPE | UP | 0.68 | 0.50 | -2.18 |
| 10-20 10:05 | +10 stop | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 10-20 10:04 | +10 stop | ZEC | UP | 0.64 | 0.78 | 1.10 |
| 10-20 10:04 | +20 | BTC | UP | 0.67 | 0.91 | 2.12 |
| 10-20 10:04 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 10-20 10:03 | +15 | BTC | UP | 0.69 | 0.86 | 1.46 |
| 10-20 10:03 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 10-20 10:03 | +10 stop | SOL | UP | 0.58 | 0.42 | -1.96 |
| 10-20 10:02 | +10 stop | BTC | UP | 0.66 | 0.79 | 1.02 |
| 10-20 10:02 | +10 | BTC | UP | 0.66 | 0.79 | 1.02 |
| 10-20 10:02 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 10-20 10:02 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-20 10:02 | +20 | BNB | UP | 0.70 | 0.90 | 1.79 |
| 10-20 10:02 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-20 10:02 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-20 10:02 | +5 | BNB | UP | 0.70 | 0.79 | 0.63 |
| 10-20 10:02 | +10 | ETH | UP | 0.70 | 0.83 | 1.05 |
| 10-20 10:02 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-20 10:02 | +10 stop | DOGE | DOWN | 0.51 | 0.36 | -1.85 |
| 10-20 10:02 | +10 stop | NEAR | DOWN | 0.56 | 0.38 | -2.15 |
| 10-20 10:02 | +20 | NEAR | DOWN | 0.56 | 0.82 | 2.31 |
| 10-20 10:02 | +15 | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-20 10:02 | +10 | NEAR | DOWN | 0.56 | 0.71 | 1.17 |
| 10-20 10:02 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 10-20 10:02 | +10 stop | HYPE | DOWN | 0.52 | 0.36 | -1.95 |
| 10-20 10:02 | +20 | HYPE | DOWN | 0.52 | open |  |
| 10-20 10:02 | +15 | HYPE | DOWN | 0.52 | open |  |
| 10-20 10:02 | +10 | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 10-20 10:02 | +5 | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 10-20 10:01 | +10 stop | BTC | UP | 0.49 | 0.63 | 1.05 |
| 10-20 10:01 | +20 | BTC | UP | 0.49 | 0.70 | 1.77 |
| 10-20 10:01 | +15 | BTC | UP | 0.50 | 0.67 | 1.36 |
| 10-20 10:01 | +10 | BTC | UP | 0.50 | 0.63 | 0.95 |
| 10-20 10:01 | +5 | BTC | UP | 0.50 | 0.63 | 0.95 |
| 10-20 10:01 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
