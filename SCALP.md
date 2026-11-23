# Range-Scalp Bot

*Updated Mon Nov 23 09:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69742 | 60855 | 8887 (146) | 1 | $-18773.61 | -4.3% |
| **+10¢** | 52047 | 41667 | 10380 (189) | 1 | $-17436.40 | -5.3% |
| **+15¢** | 43615 | 32433 | 11182 (244) | 1 | $-15580.43 | -5.7% |
| **+20¢** | 38837 | 27073 | 11764 (309) | 1 | $-13924.48 | -5.7% |
| **+10¢ (15¢ stop)** | 84936 | 84746 | 190 (118) | 0 | $-31206.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 09:24 | +10 stop | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 11-23 09:24 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.04 |
| 11-23 09:24 | +15 | DOGE | DOWN | 0.69 | 0.87 | 1.57 |
| 11-23 09:24 | +10 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-23 09:24 | +5 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-23 09:24 | +10 stop | XRP | DOWN | 0.71 | 0.87 | 1.38 |
| 11-23 09:24 | +10 stop | BTC | UP | 0.60 | 0.21 | -4.19 |
| 11-23 09:22 | +10 stop | XRP | UP | 0.61 | 0.44 | -2.05 |
| 11-23 09:21 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.77 |
| 11-23 09:20 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 11-23 09:19 | +10 stop | ETH | UP | 0.63 | 0.38 | -2.84 |
| 11-23 09:19 | +10 stop | ZEC | DOWN | 0.49 | 0.18 | -3.40 |
| 11-23 09:19 | +10 stop | XRP | DOWN | 0.43 | 0.57 | 1.04 |
| 11-23 09:18 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-23 09:18 | +10 stop | SOL | UP | 0.64 | 0.79 | 1.21 |
| 11-23 09:17 | +5 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-23 09:17 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-23 09:17 | +20 | DOGE | UP | 0.64 | 0.84 | 1.73 |
| 11-23 09:17 | +15 | DOGE | UP | 0.64 | 0.83 | 1.63 |
| 11-23 09:17 | +10 | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-23 09:17 | +5 | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-23 09:17 | +20 | HYPE | UP | 0.71 | 0.95 | 2.22 |
| 11-23 09:17 | +15 | HYPE | UP | 0.71 | 0.88 | 1.47 |
| 11-23 09:17 | +10 | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 11-23 09:17 | +10 stop | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 11-23 09:16 | +10 stop | BTC | DOWN | 0.61 | 0.39 | -2.54 |
| 11-23 09:16 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-23 09:16 | +15 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-23 09:16 | +10 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-23 09:16 | +5 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-23 09:16 | +10 stop | BNB | UP | 0.53 | 0.73 | 1.68 |
| 11-23 09:16 | +20 | BNB | UP | 0.53 | 0.73 | 1.68 |
| 11-23 09:16 | +15 | BNB | UP | 0.53 | 0.73 | 1.68 |
| 11-23 09:16 | +10 | BNB | UP | 0.53 | 0.73 | 1.68 |
| 11-23 09:16 | +5 | BNB | UP | 0.53 | 0.73 | 1.68 |
| 11-23 09:16 | +10 stop | ZEC | DOWN | 0.61 | 0.44 | -2.05 |
| 11-23 09:16 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-23 09:16 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-23 09:16 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-23 09:16 | +5 | ZEC | DOWN | 0.61 | open |  |
