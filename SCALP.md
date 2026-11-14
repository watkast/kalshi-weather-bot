# Range-Scalp Bot

*Updated Sat Nov 14 05:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59092 | 51560 | 7532 (106) | 4 | $-15958.15 | -4.3% |
| **+10¢** | 44147 | 35335 | 8812 (139) | 5 | $-14969.05 | -5.4% |
| **+15¢** | 36993 | 27494 | 9499 (174) | 5 | $-13586.80 | -5.9% |
| **+20¢** | 32955 | 22981 | 9974 (226) | 7 | $-11989.25 | -5.8% |
| **+10¢ (15¢ stop)** | 71936 | 71798 | 138 (82) | 5 | $-26455.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 05:21 | +10 stop | ZEC | UP | 0.55 | open |  |
| 11-14 05:20 | +10 stop | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +20 | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +15 | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +10 | NEAR | UP | 0.67 | open |  |
| 11-14 05:20 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 11-14 05:20 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 11-14 05:20 | +10 stop | XRP | UP | 0.54 | open |  |
| 11-14 05:19 | +5 | HYPE | UP | 0.67 | open |  |
| 11-14 05:19 | +10 stop | ZEC | UP | 0.70 | 0.49 | -2.43 |
| 11-14 05:18 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-14 05:18 | +10 stop | HYPE | UP | 0.65 | 0.45 | -2.34 |
| 11-14 05:17 | +10 stop | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 11-14 05:17 | +20 | NEAR | UP | 0.56 | 0.78 | 1.89 |
| 11-14 05:17 | +15 | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 11-14 05:17 | +10 | NEAR | UP | 0.56 | 0.71 | 1.17 |
| 11-14 05:17 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 11-14 05:17 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-14 05:17 | +5 | XRP | DOWN | 0.60 | open |  |
| 11-14 05:17 | +10 stop | BTC | DOWN | 0.54 | open |  |
| 11-14 05:17 | +20 | BTC | DOWN | 0.54 | open |  |
| 11-14 05:17 | +15 | BTC | DOWN | 0.54 | open |  |
| 11-14 05:17 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-14 05:17 | +5 | BTC | DOWN | 0.55 | open |  |
| 11-14 05:17 | +10 stop | ZEC | DOWN | 0.54 | 0.35 | -2.24 |
| 11-14 05:17 | +20 | ZEC | DOWN | 0.54 | open |  |
| 11-14 05:17 | +15 | ZEC | DOWN | 0.53 | open |  |
| 11-14 05:17 | +10 | ZEC | DOWN | 0.54 | open |  |
| 11-14 05:17 | +5 | ZEC | DOWN | 0.54 | 0.61 | 0.35 |
| 11-14 05:17 | +10 stop | XRP | DOWN | 0.54 | 0.37 | -2.05 |
| 11-14 05:17 | +20 | XRP | DOWN | 0.54 | open |  |
| 11-14 05:17 | +15 | XRP | DOWN | 0.55 | open |  |
| 11-14 05:17 | +10 | XRP | DOWN | 0.54 | open |  |
| 11-14 05:17 | +5 | XRP | DOWN | 0.55 | 0.61 | 0.25 |
| 11-14 05:16 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-14 05:16 | +20 | ETH | UP | 0.66 | open |  |
| 11-14 05:16 | +15 | ETH | UP | 0.66 | 0.82 | 1.33 |
| 11-14 05:16 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-14 05:16 | +5 | ETH | UP | 0.66 | 0.74 | 0.50 |
| 11-14 05:16 | +10 stop | DOGE | UP | 0.62 | 0.79 | 1.41 |
