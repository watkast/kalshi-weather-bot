# Range-Scalp Bot

*Updated Sun Nov 08 20:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52763 | 46001 | 6762 (83) | 1 | $-14612.27 | -4.4% |
| **+10¢** | 39391 | 31514 | 7877 (108) | 3 | $-13575.12 | -5.5% |
| **+15¢** | 33002 | 24515 | 8487 (139) | 2 | $-12401.05 | -6.0% |
| **+20¢** | 29354 | 20457 | 8897 (184) | 2 | $-10902.29 | -5.9% |
| **+10¢ (15¢ stop)** | 64258 | 64152 | 106 (63) | 0 | $-23779.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 20:12 | +10 stop | BNB | DOWN | 0.66 | 0.50 | -1.89 |
| 11-08 20:12 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-08 20:12 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-08 20:12 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-08 20:12 | +5 | BNB | DOWN | 0.64 | open |  |
| 11-08 20:09 | +10 stop | XRP | UP | 0.68 | 0.52 | -1.89 |
| 11-08 20:09 | +20 | XRP | UP | 0.67 | 0.88 | 1.86 |
| 11-08 20:09 | +15 | XRP | UP | 0.67 | 0.82 | 1.23 |
| 11-08 20:09 | +10 | XRP | UP | 0.68 | 0.82 | 1.18 |
| 11-08 20:09 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 11-08 20:09 | +10 stop | BNB | DOWN | 0.55 | 0.70 | 1.17 |
| 11-08 20:09 | +20 | BNB | DOWN | 0.55 | 0.77 | 1.89 |
| 11-08 20:09 | +15 | BNB | DOWN | 0.55 | 0.70 | 1.17 |
| 11-08 20:09 | +10 | BNB | DOWN | 0.55 | 0.70 | 1.17 |
| 11-08 20:09 | +5 | BNB | DOWN | 0.55 | 0.70 | 1.17 |
| 11-08 20:06 | +10 stop | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-08 20:06 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.60 |
| 11-08 20:06 | +10 stop | ZEC | DOWN | 0.66 | 0.85 | 1.65 |
| 11-08 20:06 | +5 | ZEC | DOWN | 0.66 | 0.85 | 1.65 |
| 11-08 20:06 | +10 stop | XRP | DOWN | 0.34 | 0.63 | 2.57 |
| 11-08 20:06 | +15 | XRP | DOWN | 0.34 | 0.63 | 2.57 |
| 11-08 20:06 | +10 | XRP | DOWN | 0.34 | 0.63 | 2.57 |
| 11-08 20:06 | +5 | XRP | DOWN | 0.34 | 0.63 | 2.57 |
| 11-08 20:05 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-08 20:05 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-08 20:05 | +5 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-08 20:05 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 11-08 20:04 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 11-08 20:04 | +10 stop | HYPE | UP | 0.50 | 0.17 | -3.58 |
| 11-08 20:04 | +5 | BNB | UP | 0.64 | 0.77 | 1.05 |
| 11-08 20:04 | +10 stop | DOGE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-08 20:04 | +20 | DOGE | DOWN | 0.61 | 0.87 | 2.35 |
| 11-08 20:04 | +15 | DOGE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-08 20:04 | +5 | DOGE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-08 20:04 | +10 stop | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-08 20:04 | +5 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-08 20:04 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-08 20:03 | +5 | BTC | UP | 0.52 | 0.65 | 0.96 |
| 11-08 20:02 | +10 stop | NEAR | UP | 0.61 | 0.41 | -2.34 |
| 11-08 20:02 | +10 stop | HYPE | UP | 0.57 | 0.41 | -1.95 |
