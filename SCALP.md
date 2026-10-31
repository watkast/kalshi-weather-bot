# Range-Scalp Bot

*Updated Sat Oct 31 08:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42014 | 36653 | 5361 (55) | 3 | $-11826.95 | -4.5% |
| **+10¢** | 31316 | 25110 | 6206 (79) | 4 | $-10587.46 | -5.4% |
| **+15¢** | 26180 | 19491 | 6689 (107) | 5 | $-9670.59 | -5.9% |
| **+20¢** | 23248 | 16243 | 7005 (138) | 6 | $-8522.81 | -5.8% |
| **+10¢ (15¢ stop)** | 51217 | 51142 | 75 (41) | 3 | $-19332.60 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 08:21 | +5 | BNB | UP | 0.53 | open |  |
| 10-31 08:21 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 10-31 08:21 | +5 | BNB | UP | 0.47 | 0.54 | 0.29 |
| 10-31 08:21 | +10 stop | ZEC | UP | 0.45 | open |  |
| 10-31 08:21 | +20 | ZEC | UP | 0.44 | open |  |
| 10-31 08:21 | +15 | ZEC | UP | 0.44 | open |  |
| 10-31 08:21 | +10 | ZEC | UP | 0.44 | 0.54 | 0.64 |
| 10-31 08:21 | +5 | ZEC | UP | 0.42 | 0.54 | 0.84 |
| 10-31 08:20 | +10 stop | ETH | UP | 0.69 | 0.47 | -2.53 |
| 10-31 08:20 | +5 | ETH | UP | 0.68 | open |  |
| 10-31 08:20 | +5 | SOL | UP | 0.68 | open |  |
| 10-31 08:19 | +5 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 08:19 | +10 stop | SOL | UP | 0.65 | 0.38 | -3.03 |
| 10-31 08:19 | +5 | ZEC | UP | 0.57 | 0.62 | 0.15 |
| 10-31 08:18 | +10 stop | ZEC | UP | 0.57 | 0.72 | 1.17 |
| 10-31 08:18 | +15 | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 10-31 08:18 | +10 | ZEC | UP | 0.61 | 0.72 | 0.78 |
| 10-31 08:18 | +5 | ZEC | UP | 0.60 | 0.69 | 0.58 |
| 10-31 08:18 | +10 stop | BTC | UP | 0.64 | 0.83 | 1.63 |
| 10-31 08:18 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-31 08:18 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-31 08:18 | +15 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 08:18 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-31 08:18 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 08:17 | +10 stop | ETH | DOWN | 0.55 | 0.33 | -2.54 |
| 10-31 08:17 | +10 stop | NEAR | UP | 0.71 | open |  |
| 10-31 08:17 | +20 | NEAR | UP | 0.71 | open |  |
| 10-31 08:17 | +15 | NEAR | UP | 0.70 | open |  |
| 10-31 08:17 | +10 | NEAR | UP | 0.70 | open |  |
| 10-31 08:17 | +5 | NEAR | UP | 0.71 | 0.76 | 0.22 |
| 10-31 08:17 | +10 stop | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 08:17 | +20 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-31 08:17 | +15 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-31 08:17 | +10 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-31 08:17 | +5 | HYPE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-31 08:17 | +10 stop | ZEC | UP | 0.54 | 0.69 | 1.17 |
| 10-31 08:17 | +20 | ZEC | UP | 0.54 | 0.74 | 1.68 |
| 10-31 08:17 | +15 | ZEC | UP | 0.53 | 0.69 | 1.27 |
| 10-31 08:17 | +10 | ZEC | UP | 0.55 | 0.69 | 1.07 |
| 10-31 08:17 | +5 | ZEC | UP | 0.57 | 0.62 | 0.15 |
