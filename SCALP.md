# Range-Scalp Bot

*Updated Sat Nov 07 09:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50805 | 44292 | 6513 (76) | 0 | $-14226.81 | -4.4% |
| **+10¢** | 37929 | 30340 | 7589 (102) | 0 | $-13185.02 | -5.5% |
| **+15¢** | 31751 | 23575 | 8176 (131) | 1 | $-12091.18 | -6.1% |
| **+20¢** | 28232 | 19661 | 8571 (173) | 1 | $-10681.93 | -6.0% |
| **+10¢ (15¢ stop)** | 61869 | 61770 | 99 (58) | 0 | $-22862.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 09:21 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 09:21 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 09:21 | +5 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 09:18 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-07 09:18 | +10 | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-07 09:18 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-07 09:16 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 09:16 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-07 09:16 | +15 | ZEC | DOWN | 0.69 | open |  |
| 11-07 09:16 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 09:16 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-07 09:16 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 09:16 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-07 09:16 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 09:16 | +10 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-07 09:16 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-07 09:16 | +10 stop | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-07 09:16 | +20 | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
| 11-07 09:16 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-07 09:16 | +10 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-07 09:16 | +5 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-07 09:14 | +10 stop | BTC | UP | 0.44 | 0.66 | 1.86 |
| 11-07 09:14 | +20 | BTC | UP | 0.45 | 0.66 | 1.76 |
| 11-07 09:14 | +15 | BTC | UP | 0.43 | 0.66 | 1.96 |
| 11-07 09:14 | +10 | BTC | UP | 0.43 | 0.66 | 1.96 |
| 11-07 09:14 | +5 | BTC | UP | 0.44 | 0.66 | 1.86 |
| 11-07 09:12 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 11-07 09:12 | +5 | HYPE | UP | 0.57 | 0.64 | 0.35 |
| 11-07 09:11 | +10 stop | HYPE | DOWN | 0.51 | 0.34 | -2.03 |
| 11-07 09:11 | +20 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 11-07 09:11 | +15 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 11-07 09:11 | +10 | HYPE | DOWN | 0.49 | yes | -5.08 |
| 11-07 09:11 | +5 | HYPE | DOWN | 0.49 | 0.58 | 0.54 |
| 11-07 09:08 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 09:08 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 11-07 09:08 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 09:08 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 11-07 09:07 | +10 stop | DOGE | DOWN | 0.66 | 0.85 | 1.65 |
| 11-07 09:07 | +20 | DOGE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-07 09:07 | +15 | DOGE | DOWN | 0.66 | 0.85 | 1.65 |
