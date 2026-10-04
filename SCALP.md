# Range-Scalp Bot

*Updated Sun Oct 04 13:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2331 | 2011 | 320 (3) | 0 | $-776.52 | -5.3% |
| **+10¢** | 1815 | 1461 | 354 (4) | 2 | $-571.89 | -5.0% |
| **+15¢** | 1522 | 1147 | 375 (5) | 2 | $-484.03 | -5.0% |
| **+20¢** | 1348 | 953 | 395 (9) | 2 | $-415.93 | -4.9% |
| **+10¢ (15¢ stop)** | 2883 | 2882 | 1 (1) | 0 | $-1078.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 13:39 | +10 stop | ETH | UP | 0.52 | 0.32 | -2.34 |
| 10-04 13:39 | +20 | ETH | UP | 0.52 | open |  |
| 10-04 13:39 | +15 | ETH | UP | 0.52 | open |  |
| 10-04 13:39 | +10 | ETH | UP | 0.52 | open |  |
| 10-04 13:39 | +10 stop | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-04 13:39 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 10-04 13:38 | +5 | BNB | UP | 0.53 | 0.58 | 0.14 |
| 10-04 13:38 | +10 stop | BNB | UP | 0.64 | 0.46 | -2.15 |
| 10-04 13:37 | +10 stop | ETH | UP | 0.71 | 0.84 | 1.05 |
| 10-04 13:37 | +10 stop | BNB | DOWN | 0.58 | 0.43 | -1.86 |
| 10-04 13:36 | +10 stop | NEAR | DOWN | 0.58 | 0.21 | -4.04 |
| 10-04 13:36 | +10 stop | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-04 13:36 | +20 | BTC | UP | 0.56 | 0.76 | 1.69 |
| 10-04 13:36 | +15 | BTC | UP | 0.56 | 0.76 | 1.69 |
| 10-04 13:36 | +10 | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-04 13:36 | +5 | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-04 13:36 | +10 stop | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 10-04 13:36 | +10 | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 10-04 13:36 | +5 | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 10-04 13:36 | +10 stop | ETH | DOWN | 0.64 | 0.41 | -2.64 |
| 10-04 13:36 | +5 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-04 13:35 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.97 |
| 10-04 13:35 | +10 stop | XRP | UP | 0.70 | 0.51 | -2.23 |
| 10-04 13:35 | +20 | XRP | UP | 0.70 | 0.93 | 2.09 |
| 10-04 13:35 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-04 13:35 | +10 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-04 13:35 | +5 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-04 13:35 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 10-04 13:35 | +10 stop | ZEC | UP | 0.61 | 0.77 | 1.30 |
| 10-04 13:35 | +20 | ZEC | UP | 0.61 | 0.83 | 1.93 |
| 10-04 13:35 | +15 | ZEC | UP | 0.61 | 0.77 | 1.30 |
| 10-04 13:35 | +10 | ZEC | UP | 0.61 | 0.77 | 1.30 |
| 10-04 13:35 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-04 13:33 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-04 13:33 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-04 13:33 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-04 13:33 | +10 stop | BNB | DOWN | 0.70 | 0.54 | -1.96 |
| 10-04 13:32 | +5 | NEAR | UP | 0.65 | 0.78 | 0.99 |
| 10-04 13:32 | +10 stop | ETH | UP | 0.69 | 0.40 | -3.22 |
| 10-04 13:32 | +15 | ETH | UP | 0.69 | 0.84 | 1.25 |
