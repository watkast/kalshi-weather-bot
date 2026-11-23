# Range-Scalp Bot

*Updated Mon Nov 23 23:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70301 | 61355 | 8946 (147) | 2 | $-18850.10 | -4.3% |
| **+10¢** | 52448 | 41999 | 10449 (190) | 3 | $-17495.77 | -5.3% |
| **+15¢** | 43936 | 32681 | 11255 (246) | 3 | $-15600.99 | -5.7% |
| **+20¢** | 39120 | 27274 | 11846 (311) | 3 | $-13975.30 | -5.7% |
| **+10¢ (15¢ stop)** | 85618 | 85422 | 196 (118) | 2 | $-31494.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 23:50 | +10 stop | ZEC | UP | 0.69 | 0.54 | -1.83 |
| 11-23 23:50 | +10 | ZEC | UP | 0.69 | open |  |
| 11-23 23:50 | +5 | ZEC | UP | 0.69 | open |  |
| 11-23 23:49 | +10 stop | BTC | UP | 0.70 | open |  |
| 11-23 23:49 | +10 | BTC | UP | 0.70 | open |  |
| 11-23 23:49 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 11-23 23:48 | +10 stop | ZEC | DOWN | 0.52 | 0.27 | -2.82 |
| 11-23 23:47 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 11-23 23:47 | +20 | BTC | UP | 0.66 | open |  |
| 11-23 23:47 | +15 | BTC | UP | 0.67 | open |  |
| 11-23 23:47 | +10 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-23 23:47 | +5 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-23 23:47 | +10 stop | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-23 23:47 | +20 | HYPE | UP | 0.71 | 0.91 | 1.80 |
| 11-23 23:46 | +10 stop | NEAR | UP | 0.68 | 0.86 | 1.54 |
| 11-23 23:46 | +20 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 11-23 23:46 | +15 | NEAR | UP | 0.65 | 0.86 | 1.85 |
| 11-23 23:46 | +10 | NEAR | UP | 0.64 | 0.76 | 0.86 |
| 11-23 23:46 | +5 | NEAR | UP | 0.64 | 0.72 | 0.44 |
| 11-23 23:46 | +10 stop | ZEC | UP | 0.60 | 0.44 | -1.95 |
| 11-23 23:46 | +20 | ZEC | UP | 0.60 | open |  |
| 11-23 23:46 | +15 | ZEC | UP | 0.60 | open |  |
| 11-23 23:46 | +10 | ZEC | UP | 0.60 | 0.72 | 0.88 |
| 11-23 23:46 | +5 | ZEC | UP | 0.59 | 0.72 | 0.98 |
| 11-23 23:46 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-23 23:46 | +20 | XRP | UP | 0.67 | open |  |
| 11-23 23:46 | +15 | XRP | UP | 0.67 | open |  |
| 11-23 23:46 | +10 | XRP | UP | 0.67 | open |  |
| 11-23 23:46 | +5 | XRP | UP | 0.67 | open |  |
| 11-23 23:39 | +10 stop | NEAR | UP | 0.60 | 0.36 | -2.74 |
| 11-23 23:37 | +5 | NEAR | UP | 0.64 | no | -6.57 |
| 11-23 23:37 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 11-23 23:37 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-23 23:37 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-23 23:37 | +10 stop | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-23 23:35 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.90 |
| 11-23 23:35 | +10 stop | ZEC | DOWN | 0.70 | 0.91 | 1.85 |
| 11-23 23:35 | +10 | ZEC | DOWN | 0.68 | 0.91 | 2.04 |
| 11-23 23:35 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-23 23:34 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
