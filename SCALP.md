# Range-Scalp Bot

*Updated Wed Nov 11 13:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55878 | 48730 | 7148 (94) | 2 | $-15265.45 | -4.3% |
| **+10¢** | 41751 | 33415 | 8336 (124) | 3 | $-14198.35 | -5.4% |
| **+15¢** | 35011 | 26018 | 8993 (158) | 3 | $-12962.88 | -5.9% |
| **+20¢** | 31181 | 21746 | 9435 (208) | 4 | $-11347.02 | -5.8% |
| **+10¢ (15¢ stop)** | 68072 | 67951 | 121 (73) | 1 | $-25035.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 13:26 | +10 stop | NEAR | DOWN | 0.48 | 0.63 | 1.14 |
| 11-11 13:26 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-11 13:26 | +20 | BNB | UP | 0.71 | open |  |
| 11-11 13:25 | +10 stop | NEAR | UP | 0.66 | 0.42 | -2.74 |
| 11-11 13:25 | +20 | NEAR | UP | 0.67 | open |  |
| 11-11 13:25 | +15 | NEAR | UP | 0.71 | open |  |
| 11-11 13:25 | +10 | NEAR | UP | 0.71 | open |  |
| 11-11 13:25 | +5 | NEAR | UP | 0.69 | open |  |
| 11-11 13:25 | +5 | BTC | UP | 0.35 | 0.62 | 2.37 |
| 11-11 13:24 | +10 stop | BTC | UP | 0.54 | 0.33 | -2.44 |
| 11-11 13:24 | +5 | BTC | UP | 0.54 | 0.63 | 0.55 |
| 11-11 13:22 | +10 stop | ZEC | UP | 0.61 | 0.80 | 1.61 |
| 11-11 13:22 | +10 stop | NEAR | DOWN | 0.54 | 0.37 | -2.05 |
| 11-11 13:22 | +20 | HYPE | UP | 0.68 | 0.93 | 2.31 |
| 11-11 13:22 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-11 13:22 | +10 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-11 13:22 | +5 | HYPE | UP | 0.67 | 0.76 | 0.61 |
| 11-11 13:22 | +5 | BNB | UP | 0.59 | 0.67 | 0.47 |
| 11-11 13:22 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-11 13:22 | +15 | DOGE | UP | 0.62 | 0.81 | 1.62 |
| 11-11 13:22 | +10 | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 11-11 13:22 | +5 | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 11-11 13:21 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 11-11 13:21 | +10 stop | NEAR | UP | 0.43 | 0.58 | 1.14 |
| 11-11 13:21 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 11-11 13:20 | +10 stop | NEAR | DOWN | 0.61 | 0.41 | -2.34 |
| 11-11 13:20 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 11-11 13:20 | +10 stop | ETH | DOWN | 0.62 | 0.47 | -1.85 |
| 11-11 13:20 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 11-11 13:20 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
| 11-11 13:20 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-11 13:20 | +10 stop | DOGE | UP | 0.52 | 0.69 | 1.37 |
| 11-11 13:20 | +20 | DOGE | UP | 0.52 | 0.74 | 1.88 |
| 11-11 13:20 | +15 | DOGE | UP | 0.52 | 0.69 | 1.37 |
| 11-11 13:20 | +10 | DOGE | UP | 0.52 | 0.69 | 1.37 |
| 11-11 13:20 | +5 | DOGE | UP | 0.52 | 0.69 | 1.37 |
| 11-11 13:19 | +5 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-11 13:18 | +10 stop | ZEC | UP | 0.59 | 0.44 | -1.85 |
| 11-11 13:18 | +10 stop | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 11-11 13:17 | +10 stop | XRP | DOWN | 0.61 | 0.41 | -2.36 |
