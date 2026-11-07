# Range-Scalp Bot

*Updated Sat Nov 07 10:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50845 | 44328 | 6517 (76) | 1 | $-14228.68 | -4.4% |
| **+10¢** | 37957 | 30363 | 7594 (102) | 3 | $-13188.74 | -5.5% |
| **+15¢** | 31772 | 23590 | 8182 (131) | 5 | $-12102.39 | -6.1% |
| **+20¢** | 28251 | 19674 | 8577 (173) | 5 | $-10689.54 | -6.0% |
| **+10¢ (15¢ stop)** | 61922 | 61823 | 99 (58) | 0 | $-22879.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 10:13 | +10 stop | SOL | UP | 0.20 | 0.55 | 3.20 |
| 11-07 10:13 | +20 | SOL | UP | 0.20 | 0.55 | 3.20 |
| 11-07 10:13 | +15 | SOL | UP | 0.20 | 0.55 | 3.20 |
| 11-07 10:13 | +10 | SOL | UP | 0.20 | 0.55 | 3.20 |
| 11-07 10:13 | +5 | SOL | UP | 0.20 | 0.55 | 3.20 |
| 11-07 10:11 | +5 | XRP | UP | 0.36 | 0.62 | 2.26 |
| 11-07 10:11 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-07 10:11 | +10 | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-07 10:11 | +5 | NEAR | UP | 0.68 | 0.75 | 0.40 |
| 11-07 10:11 | +10 stop | XRP | UP | 0.57 | 0.25 | -3.52 |
| 11-07 10:11 | +10 | XRP | UP | 0.57 | open |  |
| 11-07 10:11 | +5 | XRP | UP | 0.57 | 0.65 | 0.46 |
| 11-07 10:10 | +5 | ZEC | DOWN | 0.53 | 0.59 | 0.25 |
| 11-07 10:09 | +10 stop | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-07 10:09 | +10 stop | HYPE | UP | 0.68 | 0.32 | -3.92 |
| 11-07 10:09 | +20 | HYPE | UP | 0.67 | open |  |
| 11-07 10:09 | +15 | HYPE | UP | 0.67 | open |  |
| 11-07 10:09 | +10 | HYPE | UP | 0.67 | open |  |
| 11-07 10:09 | +5 | HYPE | UP | 0.67 | open |  |
| 11-07 10:08 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-07 10:08 | +15 | XRP | UP | 0.67 | open |  |
| 11-07 10:08 | +10 | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-07 10:08 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 11-07 10:08 | +10 stop | ZEC | UP | 0.61 | 0.45 | -1.95 |
| 11-07 10:08 | +10 stop | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-07 10:07 | +5 | ZEC | DOWN | 0.52 | 0.57 | 0.14 |
| 11-07 10:06 | +10 stop | NEAR | DOWN | 0.62 | 0.45 | -2.05 |
| 11-07 10:05 | +10 stop | ZEC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-07 10:05 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-07 10:05 | +10 stop | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-07 10:05 | +10 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-07 10:05 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 11-07 10:05 | +5 | XRP | UP | 0.64 | 0.73 | 0.59 |
| 11-07 10:04 | +20 | BNB | UP | 0.66 | 0.88 | 1.96 |
| 11-07 10:04 | +10 stop | BTC | UP | 0.57 | 0.68 | 0.76 |
| 11-07 10:04 | +20 | BTC | UP | 0.57 | 0.78 | 1.79 |
| 11-07 10:04 | +15 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 11-07 10:04 | +10 | BTC | UP | 0.57 | 0.68 | 0.76 |
| 11-07 10:04 | +5 | BTC | UP | 0.57 | 0.68 | 0.76 |
| 11-07 10:04 | +10 stop | XRP | UP | 0.59 | 0.73 | 1.09 |
