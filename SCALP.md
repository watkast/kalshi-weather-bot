# Range-Scalp Bot

*Updated Tue Oct 13 03:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14272 | 12346 | 1926 (27) | 4 | $-4581.99 | -5.1% |
| **+10¢** | 10801 | 8563 | 2238 (39) | 4 | $-4301.44 | -6.3% |
| **+15¢** | 9072 | 6679 | 2393 (57) | 4 | $-3817.97 | -6.7% |
| **+20¢** | 8071 | 5580 | 2491 (72) | 7 | $-3260.59 | -6.4% |
| **+10¢ (15¢ stop)** | 17497 | 17448 | 49 (29) | 0 | $-6749.91 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 03:24 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-13 03:24 | +20 | BTC | UP | 0.71 | 0.92 | 1.84 |
| 10-13 03:24 | +15 | BTC | UP | 0.71 | 0.92 | 1.84 |
| 10-13 03:24 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-13 03:24 | +5 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-13 03:24 | +15 | BNB | UP | 0.71 | 0.89 | 1.61 |
| 10-13 03:24 | +10 | BNB | UP | 0.67 | 0.81 | 1.13 |
| 10-13 03:24 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 10-13 03:23 | +10 stop | HYPE | UP | 0.60 | 0.78 | 1.46 |
| 10-13 03:23 | +15 | HYPE | UP | 0.60 | 0.78 | 1.46 |
| 10-13 03:23 | +10 | HYPE | UP | 0.60 | 0.78 | 1.46 |
| 10-13 03:23 | +5 | HYPE | UP | 0.60 | 0.66 | 0.23 |
| 10-13 03:23 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-13 03:23 | +15 | ETH | UP | 0.68 | 0.84 | 1.34 |
| 10-13 03:23 | +10 | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-13 03:23 | +5 | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-13 03:23 | +10 stop | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 10-13 03:23 | +15 | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 10-13 03:23 | +10 | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 10-13 03:23 | +5 | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 10-13 03:23 | +10 stop | ZEC | DOWN | 0.66 | 0.46 | -2.34 |
| 10-13 03:23 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-13 03:23 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-13 03:23 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-13 03:23 | +5 | ZEC | DOWN | 0.66 | open |  |
| 10-13 03:23 | +10 stop | NEAR | UP | 0.57 | 0.77 | 1.69 |
| 10-13 03:23 | +10 stop | XRP | DOWN | 0.61 | 0.46 | -1.85 |
| 10-13 03:23 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-13 03:23 | +15 | XRP | DOWN | 0.62 | open |  |
| 10-13 03:23 | +10 | XRP | DOWN | 0.62 | open |  |
| 10-13 03:23 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-13 03:23 | +10 stop | HYPE | DOWN | 0.34 | 0.57 | 1.96 |
| 10-13 03:23 | +15 | HYPE | DOWN | 0.34 | 0.57 | 1.96 |
| 10-13 03:23 | +10 | HYPE | DOWN | 0.34 | 0.57 | 1.96 |
| 10-13 03:23 | +5 | HYPE | DOWN | 0.34 | 0.57 | 1.96 |
| 10-13 03:23 | +10 stop | DOGE | DOWN | 0.37 | 0.56 | 1.55 |
| 10-13 03:23 | +20 | DOGE | DOWN | 0.37 | open |  |
| 10-13 03:23 | +15 | DOGE | DOWN | 0.37 | 0.56 | 1.55 |
| 10-13 03:23 | +10 | DOGE | DOWN | 0.37 | 0.56 | 1.55 |
| 10-13 03:23 | +5 | DOGE | DOWN | 0.37 | 0.56 | 1.55 |
