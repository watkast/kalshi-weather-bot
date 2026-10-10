# Range-Scalp Bot

*Updated Sat Oct 10 05:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10005 | 8630 | 1375 (18) | 1 | $-3409.98 | -5.4% |
| **+10¢** | 7558 | 5956 | 1602 (30) | 4 | $-3283.47 | -6.9% |
| **+15¢** | 6383 | 4694 | 1689 (43) | 3 | $-2713.21 | -6.8% |
| **+20¢** | 5670 | 3916 | 1754 (55) | 4 | $-2277.15 | -6.4% |
| **+10¢ (15¢ stop)** | 12286 | 12251 | 35 (22) | 0 | $-4831.19 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 05:18 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-10 05:18 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-10 05:18 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-10 05:18 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 05:18 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-10 05:17 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-10 05:17 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-10 05:17 | +5 | HYPE | DOWN | 0.64 | 0.71 | 0.34 |
| 10-10 05:17 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-10 05:17 | +20 | SOL | DOWN | 0.59 | 0.82 | 2.02 |
| 10-10 05:17 | +15 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-10 05:17 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-10 05:17 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 10-10 05:17 | +5 | NEAR | UP | 0.59 | 0.79 | 1.68 |
| 10-10 05:16 | +10 stop | ZEC | UP | 0.58 | 0.37 | -2.49 |
| 10-10 05:16 | +20 | ZEC | UP | 0.58 | open |  |
| 10-10 05:16 | +15 | ZEC | UP | 0.58 | open |  |
| 10-10 05:16 | +10 | ZEC | UP | 0.59 | open |  |
| 10-10 05:16 | +5 | ZEC | UP | 0.59 | open |  |
| 10-10 05:16 | +10 stop | NEAR | DOWN | 0.46 | 0.19 | -3.01 |
| 10-10 05:16 | +20 | NEAR | DOWN | 0.46 | open |  |
| 10-10 05:16 | +15 | NEAR | DOWN | 0.46 | open |  |
| 10-10 05:16 | +10 | NEAR | DOWN | 0.46 | open |  |
| 10-10 05:16 | +5 | NEAR | DOWN | 0.46 | 0.53 | 0.32 |
| 10-10 05:16 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.17 |
| 10-10 05:16 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-10 05:16 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-10 05:16 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 10-10 05:16 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.63 |
| 10-10 05:16 | +10 stop | DOGE | DOWN | 0.51 | 0.63 | 0.82 |
| 10-10 05:16 | +20 | DOGE | DOWN | 0.51 | 0.72 | 1.79 |
| 10-10 05:16 | +15 | DOGE | DOWN | 0.49 | 0.72 | 1.96 |
| 10-10 05:16 | +10 | DOGE | DOWN | 0.49 | 0.60 | 0.75 |
| 10-10 05:16 | +5 | DOGE | DOWN | 0.49 | 0.60 | 0.73 |
| 10-10 05:15 | +10 stop | HYPE | DOWN | 0.51 | 0.66 | 1.15 |
| 10-10 05:15 | +20 | HYPE | DOWN | 0.51 | 0.73 | 1.87 |
| 10-10 05:15 | +15 | HYPE | DOWN | 0.51 | 0.68 | 1.35 |
| 10-10 05:15 | +10 | HYPE | DOWN | 0.51 | 0.66 | 1.15 |
| 10-10 05:15 | +5 | HYPE | DOWN | 0.51 | 0.58 | 0.33 |
| 10-10 05:15 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
