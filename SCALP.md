# Range-Scalp Bot

*Updated Sat Nov 21 17:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67646 | 59036 | 8610 (134) | 4 | $-18182.27 | -4.3% |
| **+10¢** | 50516 | 40458 | 10058 (175) | 5 | $-16867.05 | -5.3% |
| **+15¢** | 42349 | 31506 | 10843 (225) | 5 | $-15122.88 | -5.7% |
| **+20¢** | 37695 | 26302 | 11393 (283) | 8 | $-13431.84 | -5.7% |
| **+10¢ (15¢ stop)** | 82350 | 82179 | 171 (105) | 4 | $-30229.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 17:18 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 11-21 17:18 | +10 | XRP | DOWN | 0.70 | open |  |
| 11-21 17:18 | +10 stop | NEAR | UP | 0.63 | open |  |
| 11-21 17:18 | +20 | NEAR | UP | 0.63 | open |  |
| 11-21 17:18 | +15 | NEAR | UP | 0.63 | open |  |
| 11-21 17:18 | +10 | NEAR | UP | 0.63 | open |  |
| 11-21 17:18 | +5 | NEAR | UP | 0.63 | open |  |
| 11-21 17:17 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 17:17 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-21 17:17 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-21 17:17 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 17:17 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-21 17:17 | +5 | XRP | UP | 0.50 | open |  |
| 11-21 17:17 | +10 stop | HYPE | UP | 0.55 | open |  |
| 11-21 17:17 | +20 | HYPE | UP | 0.55 | open |  |
| 11-21 17:17 | +15 | HYPE | UP | 0.55 | open |  |
| 11-21 17:17 | +10 | HYPE | UP | 0.56 | open |  |
| 11-21 17:17 | +5 | HYPE | UP | 0.56 | open |  |
| 11-21 17:17 | +10 stop | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-21 17:17 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-21 17:17 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-21 17:17 | +10 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-21 17:17 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-21 17:17 | +10 stop | DOGE | UP | 0.62 | open |  |
| 11-21 17:17 | +20 | DOGE | UP | 0.62 | open |  |
| 11-21 17:17 | +15 | DOGE | UP | 0.62 | open |  |
| 11-21 17:17 | +10 | DOGE | UP | 0.62 | open |  |
| 11-21 17:17 | +5 | DOGE | UP | 0.62 | open |  |
| 11-21 17:16 | +10 stop | XRP | DOWN | 0.46 | 0.60 | 1.05 |
| 11-21 17:16 | +20 | XRP | DOWN | 0.46 | 0.68 | 1.86 |
| 11-21 17:16 | +15 | XRP | DOWN | 0.46 | 0.68 | 1.86 |
| 11-21 17:16 | +10 | XRP | DOWN | 0.47 | 0.60 | 0.95 |
| 11-21 17:16 | +5 | XRP | DOWN | 0.48 | 0.54 | 0.24 |
| 11-21 17:16 | +10 stop | BNB | DOWN | 0.63 | 0.79 | 1.29 |
| 11-21 17:16 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-21 17:16 | +15 | BNB | DOWN | 0.63 | 0.79 | 1.29 |
| 11-21 17:16 | +10 | BNB | DOWN | 0.63 | 0.79 | 1.29 |
| 11-21 17:16 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.46 |
| 11-21 17:16 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-21 17:16 | +20 | ETH | DOWN | 0.61 | open |  |
