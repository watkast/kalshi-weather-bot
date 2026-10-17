# Range-Scalp Bot

*Updated Sat Oct 17 16:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21218 | 18473 | 2745 (29) | 1 | $-6155.73 | -4.6% |
| **+10¢** | 15967 | 12796 | 3171 (41) | 2 | $-5489.22 | -5.5% |
| **+15¢** | 13350 | 9934 | 3416 (61) | 2 | $-4980.80 | -5.9% |
| **+20¢** | 11832 | 8254 | 3578 (80) | 4 | $-4408.54 | -5.9% |
| **+10¢ (15¢ stop)** | 26056 | 26006 | 50 (29) | 1 | $-9912.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 16:24 | +5 | ZEC | UP | 0.64 | open |  |
| 10-17 16:23 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 10-17 16:22 | +10 stop | ZEC | UP | 0.59 | 0.44 | -1.85 |
| 10-17 16:22 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-17 16:22 | +10 | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-17 16:22 | +5 | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-17 16:22 | +5 | ZEC | UP | 0.54 | 0.61 | 0.35 |
| 10-17 16:21 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-17 16:21 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-17 16:21 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-17 16:21 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-17 16:21 | +5 | HYPE | DOWN | 0.69 | 0.79 | 0.69 |
| 10-17 16:21 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 10-17 16:19 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-17 16:19 | +10 stop | ZEC | UP | 0.52 | 0.37 | -1.85 |
| 10-17 16:19 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-17 16:19 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-17 16:19 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 16:19 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-17 16:19 | +5 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-17 16:18 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.93 |
| 10-17 16:18 | +10 stop | ZEC | DOWN | 0.64 | 0.44 | -2.35 |
| 10-17 16:17 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-17 16:17 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-17 16:17 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 16:17 | +20 | BTC | DOWN | 0.71 | 0.91 | 1.79 |
| 10-17 16:17 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 16:17 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-17 16:17 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-17 16:16 | +10 stop | ZEC | UP | 0.60 | 0.44 | -1.95 |
| 10-17 16:16 | +20 | ZEC | UP | 0.60 | open |  |
| 10-17 16:16 | +15 | ZEC | UP | 0.60 | open |  |
| 10-17 16:16 | +10 | ZEC | UP | 0.60 | open |  |
| 10-17 16:16 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-17 16:16 | +10 stop | NEAR | UP | 0.66 | 0.51 | -1.84 |
| 10-17 16:16 | +20 | NEAR | UP | 0.66 | open |  |
| 10-17 16:16 | +15 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 10-17 16:16 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-17 16:16 | +5 | NEAR | UP | 0.66 | 0.74 | 0.50 |
| 10-17 16:16 | +10 stop | ETH | DOWN | 0.56 | 0.73 | 1.38 |
