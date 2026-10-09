# Range-Scalp Bot

*Updated Fri Oct 09 12:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9043 | 7817 | 1226 (14) | 3 | $-2993.98 | -5.2% |
| **+10¢** | 6847 | 5412 | 1435 (26) | 4 | $-2852.46 | -6.6% |
| **+15¢** | 5773 | 4260 | 1513 (38) | 4 | $-2335.95 | -6.4% |
| **+20¢** | 5138 | 3568 | 1570 (46) | 4 | $-1931.00 | -6.0% |
| **+10¢ (15¢ stop)** | 11045 | 11015 | 30 (19) | 0 | $-4170.97 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 12:12 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.44 |
| 10-09 12:10 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-09 12:10 | +5 | NEAR | UP | 0.45 | 0.56 | 0.74 |
| 10-09 12:09 | +10 stop | XRP | DOWN | 0.47 | 0.70 | 1.97 |
| 10-09 12:09 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.74 |
| 10-09 12:09 | +10 stop | NEAR | UP | 0.61 | 0.37 | -2.74 |
| 10-09 12:09 | +10 stop | XRP | UP | 0.65 | 0.44 | -2.44 |
| 10-09 12:09 | +10 stop | SOL | UP | 0.67 | 0.42 | -2.88 |
| 10-09 12:07 | +10 stop | SOL | DOWN | 0.70 | 0.44 | -2.93 |
| 10-09 12:07 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.68 |
| 10-09 12:07 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-09 12:07 | +5 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-09 12:07 | +10 stop | XRP | DOWN | 0.67 | 0.40 | -3.03 |
| 10-09 12:07 | +15 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-09 12:07 | +10 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-09 12:07 | +5 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-09 12:07 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-09 12:07 | +10 stop | ZEC | DOWN | 0.53 | 0.25 | -3.12 |
| 10-09 12:06 | +10 stop | ETH | UP | 0.62 | 0.78 | 1.30 |
| 10-09 12:06 | +10 stop | DOGE | DOWN | 0.50 | 0.29 | -2.43 |
| 10-09 12:06 | +10 | HYPE | DOWN | 0.66 | open |  |
| 10-09 12:06 | +5 | HYPE | DOWN | 0.66 | open |  |
| 10-09 12:06 | +10 stop | HYPE | DOWN | 0.60 | 0.45 | -1.85 |
| 10-09 12:06 | +10 stop | DOGE | DOWN | 0.52 | 0.63 | 0.75 |
| 10-09 12:05 | +10 stop | BTC | UP | 0.67 | 0.80 | 1.02 |
| 10-09 12:05 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-09 12:05 | +10 | BTC | UP | 0.67 | 0.80 | 1.02 |
| 10-09 12:05 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-09 12:05 | +10 stop | BNB | DOWN | 0.67 | 0.51 | -1.94 |
| 10-09 12:05 | +10 stop | HYPE | UP | 0.58 | 0.38 | -2.35 |
| 10-09 12:04 | +10 | BNB | DOWN | 0.55 | 0.68 | 0.93 |
| 10-09 12:04 | +10 stop | DOGE | UP | 0.56 | 0.35 | -2.45 |
| 10-09 12:04 | +10 stop | ETH | UP | 0.68 | 0.51 | -2.04 |
| 10-09 12:04 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-09 12:04 | +10 | XRP | DOWN | 0.60 | 0.73 | 0.99 |
| 10-09 12:04 | +10 stop | NEAR | UP | 0.63 | 0.36 | -3.04 |
| 10-09 12:04 | +10 stop | SOL | DOWN | 0.53 | 0.71 | 1.47 |
| 10-09 12:04 | +10 | SOL | DOWN | 0.53 | 0.71 | 1.47 |
| 10-09 12:04 | +10 stop | NEAR | DOWN | 0.42 | 0.56 | 1.04 |
| 10-09 12:03 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
