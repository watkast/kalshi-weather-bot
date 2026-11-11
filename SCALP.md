# Range-Scalp Bot

*Updated Wed Nov 11 05:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55475 | 48383 | 7092 (94) | 2 | $-15135.47 | -4.3% |
| **+10¢** | 41444 | 33170 | 8274 (124) | 3 | $-14072.23 | -5.4% |
| **+15¢** | 34749 | 25827 | 8922 (158) | 3 | $-12835.12 | -5.9% |
| **+20¢** | 30942 | 21585 | 9357 (207) | 5 | $-11207.16 | -5.8% |
| **+10¢ (15¢ stop)** | 67554 | 67436 | 118 (73) | 1 | $-24863.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 05:38 | +10 stop | HYPE | UP | 0.65 | open |  |
| 11-11 05:38 | +5 | HYPE | UP | 0.63 | 0.72 | 0.58 |
| 11-11 05:38 | +10 stop | ZEC | UP | 0.57 | 0.72 | 1.17 |
| 11-11 05:38 | +10 | ZEC | UP | 0.57 | 0.72 | 1.17 |
| 11-11 05:38 | +10 stop | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 11-11 05:37 | +5 | ZEC | UP | 0.59 | 0.72 | 0.98 |
| 11-11 05:37 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-11 05:37 | +20 | BTC | UP | 0.61 | 0.85 | 2.14 |
| 11-11 05:37 | +15 | BTC | UP | 0.61 | 0.78 | 1.40 |
| 11-11 05:37 | +10 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-11 05:37 | +5 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-11 05:37 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-11 05:37 | +20 | XRP | UP | 0.70 | open |  |
| 11-11 05:37 | +15 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-11 05:37 | +10 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-11 05:37 | +5 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-11 05:37 | +10 stop | DOGE | UP | 0.53 | 0.67 | 1.06 |
| 11-11 05:37 | +10 stop | ZEC | UP | 0.49 | 0.60 | 0.75 |
| 11-11 05:37 | +20 | ZEC | UP | 0.49 | 0.72 | 1.97 |
| 11-11 05:37 | +15 | ZEC | UP | 0.48 | 0.72 | 2.07 |
| 11-11 05:37 | +10 | ZEC | UP | 0.48 | 0.60 | 0.85 |
| 11-11 05:37 | +5 | ZEC | UP | 0.48 | 0.54 | 0.24 |
| 11-11 05:35 | +10 | NEAR | DOWN | 0.67 | 0.86 | 1.65 |
| 11-11 05:35 | +10 stop | BNB | UP | 0.52 | 0.31 | -2.43 |
| 11-11 05:35 | +5 | BNB | UP | 0.61 | open |  |
| 11-11 05:34 | +5 | BNB | UP | 0.60 | 0.68 | 0.47 |
| 11-11 05:34 | +10 stop | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-11 05:34 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 11-11 05:34 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.94 |
| 11-11 05:33 | +10 stop | NEAR | DOWN | 0.38 | 0.51 | 0.98 |
| 11-11 05:33 | +5 | NEAR | DOWN | 0.37 | 0.51 | 1.02 |
| 11-11 05:32 | +10 stop | DOGE | UP | 0.69 | 0.86 | 1.46 |
| 11-11 05:32 | +5 | NEAR | DOWN | 0.48 | 0.56 | 0.44 |
| 11-11 05:32 | +10 stop | ETH | UP | 0.68 | 0.82 | 1.13 |
| 11-11 05:32 | +20 | ETH | UP | 0.67 | 0.87 | 1.76 |
| 11-11 05:32 | +15 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 11-11 05:32 | +10 | ETH | UP | 0.66 | 0.77 | 0.81 |
| 11-11 05:32 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 11-11 05:32 | +10 stop | BNB | UP | 0.70 | 0.54 | -1.93 |
| 11-11 05:32 | +20 | BNB | UP | 0.70 | open |  |
