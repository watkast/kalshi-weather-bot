# Range-Scalp Bot

*Updated Thu Oct 08 09:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7373 | 6390 | 983 (13) | 0 | $-2289.32 | -4.9% |
| **+10¢** | 5597 | 4436 | 1161 (22) | 0 | $-2238.12 | -6.4% |
| **+15¢** | 4693 | 3469 | 1224 (30) | 0 | $-1868.76 | -6.3% |
| **+20¢** | 4190 | 2920 | 1270 (37) | 0 | $-1489.00 | -5.7% |
| **+10¢ (15¢ stop)** | 8922 | 8895 | 27 (17) | 0 | $-3227.78 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 09:08 | +10 stop | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 10-08 09:08 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-08 09:06 | +10 stop | NEAR | UP | 0.50 | 0.25 | -2.82 |
| 10-08 09:06 | +10 | NEAR | UP | 0.50 | 0.60 | 0.65 |
| 10-08 09:06 | +5 | NEAR | UP | 0.50 | 0.57 | 0.34 |
| 10-08 09:03 | +10 stop | NEAR | UP | 0.66 | 0.51 | -1.84 |
| 10-08 09:01 | +10 stop | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 10-08 09:01 | +20 | HYPE | UP | 0.68 | 0.89 | 1.87 |
| 10-08 09:01 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 10-08 09:01 | +10 | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 10-08 09:01 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 10-08 09:01 | +10 stop | NEAR | UP | 0.61 | 0.45 | -1.97 |
| 10-08 09:01 | +20 | NEAR | UP | 0.61 | 0.87 | 2.33 |
| 10-08 09:01 | +15 | NEAR | UP | 0.61 | 0.77 | 1.28 |
| 10-08 09:01 | +10 | NEAR | UP | 0.61 | 0.72 | 0.76 |
| 10-08 09:01 | +5 | NEAR | UP | 0.61 | 0.72 | 0.76 |
| 10-08 09:01 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-08 09:01 | +20 | BTC | UP | 0.64 | 0.84 | 1.73 |
| 10-08 09:01 | +15 | BTC | UP | 0.64 | 0.84 | 1.73 |
| 10-08 09:01 | +10 | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-08 09:01 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 10-08 09:01 | +10 stop | XRP | UP | 0.63 | 0.73 | 0.73 |
| 10-08 09:01 | +20 | XRP | UP | 0.62 | 0.83 | 1.79 |
| 10-08 09:01 | +15 | XRP | UP | 0.62 | 0.83 | 1.79 |
| 10-08 09:01 | +10 | XRP | UP | 0.62 | 0.73 | 0.75 |
| 10-08 09:01 | +5 | XRP | UP | 0.62 | 0.73 | 0.75 |
| 10-08 09:01 | +10 stop | DOGE | UP | 0.66 | 0.84 | 1.54 |
| 10-08 09:01 | +20 | DOGE | UP | 0.66 | 0.87 | 1.86 |
| 10-08 09:01 | +15 | DOGE | UP | 0.66 | 0.84 | 1.54 |
| 10-08 09:01 | +10 | DOGE | UP | 0.66 | 0.84 | 1.54 |
| 10-08 09:01 | +5 | DOGE | UP | 0.66 | 0.73 | 0.40 |
| 10-08 06:56 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-08 06:56 | +20 | HYPE | UP | 0.64 | 0.88 | 2.15 |
| 10-08 06:53 | +10 stop | HYPE | DOWN | 0.52 | 0.32 | -2.34 |
| 10-08 06:51 | +10 stop | HYPE | DOWN | 0.69 | 0.53 | -1.94 |
| 10-08 06:51 | +15 | HYPE | DOWN | 0.69 | yes | -7.06 |
| 10-08 06:51 | +10 | HYPE | DOWN | 0.69 | yes | -7.06 |
| 10-08 06:51 | +5 | HYPE | DOWN | 0.69 | yes | -7.06 |
| 10-08 06:50 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-08 06:50 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
