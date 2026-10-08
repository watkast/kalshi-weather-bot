# Range-Scalp Bot

*Updated Thu Oct 08 09:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7379 | 6393 | 986 (13) | 0 | $-2307.04 | -5.0% |
| **+10¢** | 5603 | 4439 | 1164 (22) | 0 | $-2255.43 | -6.4% |
| **+15¢** | 4698 | 3470 | 1228 (30) | 0 | $-1893.90 | -6.4% |
| **+20¢** | 4195 | 2921 | 1274 (37) | 0 | $-1512.81 | -5.7% |
| **+10¢ (15¢ stop)** | 8936 | 8909 | 27 (17) | 0 | $-3234.19 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 09:28 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-08 09:28 | +10 stop | BTC | UP | 0.39 | 0.56 | 1.35 |
| 10-08 09:27 | +10 stop | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-08 09:27 | +10 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-08 09:27 | +5 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-08 09:27 | +10 stop | BTC | DOWN | 0.40 | 0.62 | 1.86 |
| 10-08 09:27 | +10 stop | BTC | UP | 0.47 | 0.62 | 1.15 |
| 10-08 09:26 | +10 stop | BTC | DOWN | 0.60 | 0.41 | -2.24 |
| 10-08 09:24 | +10 stop | XRP | UP | 0.55 | 0.82 | 2.41 |
| 10-08 09:24 | +10 stop | BTC | UP | 0.64 | 0.44 | -2.35 |
| 10-08 09:24 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-08 09:24 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.98 |
| 10-08 09:24 | +20 | HYPE | UP | 0.62 | no | -6.40 |
| 10-08 09:24 | +15 | HYPE | UP | 0.62 | no | -6.40 |
| 10-08 09:24 | +10 | HYPE | UP | 0.62 | 0.73 | 0.76 |
| 10-08 09:24 | +5 | HYPE | UP | 0.62 | 0.69 | 0.35 |
| 10-08 09:23 | +10 stop | BNB | DOWN | 0.57 | 0.27 | -3.32 |
| 10-08 09:23 | +20 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:23 | +15 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:23 | +10 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:23 | +5 | BNB | DOWN | 0.57 | yes | -5.88 |
| 10-08 09:22 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 10-08 09:22 | +20 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +15 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +10 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +5 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 10-08 09:22 | +20 | BTC | DOWN | 0.66 | 0.96 | 2.77 |
| 10-08 09:22 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-08 09:22 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-08 09:22 | +5 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-08 09:22 | +10 stop | XRP | DOWN | 0.70 | 0.44 | -2.93 |
| 10-08 09:22 | +20 | XRP | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +15 | XRP | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +10 | XRP | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:22 | +5 | XRP | DOWN | 0.70 | yes | -7.15 |
| 10-08 09:08 | +10 stop | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 10-08 09:08 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-08 09:06 | +10 stop | NEAR | UP | 0.50 | 0.25 | -2.82 |
| 10-08 09:06 | +10 | NEAR | UP | 0.50 | 0.60 | 0.65 |
