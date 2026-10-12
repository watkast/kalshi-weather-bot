# Range-Scalp Bot

*Updated Mon Oct 12 17:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13670 | 11837 | 1833 (25) | 3 | $-4299.38 | -5.0% |
| **+10¢** | 10351 | 8221 | 2130 (37) | 4 | $-4017.27 | -6.2% |
| **+15¢** | 8700 | 6423 | 2277 (55) | 5 | $-3541.59 | -6.5% |
| **+20¢** | 7743 | 5367 | 2376 (70) | 4 | $-3015.64 | -6.2% |
| **+10¢ (15¢ stop)** | 16798 | 16751 | 47 (27) | 0 | $-6560.98 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 17:27 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-12 17:27 | +20 | DOGE | DOWN | 0.62 | 0.94 | 2.93 |
| 10-12 17:27 | +15 | DOGE | DOWN | 0.62 | 0.94 | 2.93 |
| 10-12 17:27 | +10 | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-12 17:27 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.65 |
| 10-12 17:27 | +10 stop | XRP | DOWN | 0.70 | 0.92 | 2.01 |
| 10-12 17:27 | +10 | XRP | DOWN | 0.70 | 0.92 | 2.01 |
| 10-12 17:27 | +5 | XRP | DOWN | 0.70 | 0.92 | 2.01 |
| 10-12 17:26 | +10 stop | XRP | UP | 0.40 | 0.54 | 1.05 |
| 10-12 17:26 | +15 | XRP | UP | 0.40 | open |  |
| 10-12 17:26 | +10 | XRP | UP | 0.40 | 0.54 | 1.05 |
| 10-12 17:26 | +5 | XRP | UP | 0.40 | 0.54 | 1.05 |
| 10-12 17:24 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.17 |
| 10-12 17:24 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.25 |
| 10-12 17:24 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.72 |
| 10-12 17:24 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-12 17:23 | +10 stop | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 10-12 17:23 | +10 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 10-12 17:23 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 10-12 17:22 | +10 stop | XRP | UP | 0.51 | 0.28 | -2.63 |
| 10-12 17:22 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 10-12 17:22 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-12 17:21 | +10 stop | NEAR | DOWN | 0.53 | 0.64 | 0.75 |
| 10-12 17:21 | +20 | NEAR | DOWN | 0.53 | 0.76 | 1.99 |
| 10-12 17:21 | +15 | NEAR | DOWN | 0.53 | 0.70 | 1.37 |
| 10-12 17:21 | +10 | NEAR | DOWN | 0.53 | 0.64 | 0.75 |
| 10-12 17:21 | +5 | NEAR | DOWN | 0.53 | 0.64 | 0.75 |
| 10-12 17:21 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 17:21 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-12 17:21 | +15 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-12 17:21 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 17:21 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-12 17:21 | +10 stop | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 10-12 17:21 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 10-12 17:21 | +10 stop | XRP | DOWN | 0.64 | 0.48 | -1.95 |
| 10-12 17:21 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 17:21 | +10 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 17:21 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-12 17:20 | +10 stop | BTC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-12 17:20 | +10 stop | BNB | DOWN | 0.54 | 0.64 | 0.65 |
