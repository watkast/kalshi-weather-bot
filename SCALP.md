# Range-Scalp Bot

*Updated Thu Nov 19 17:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65253 | 56964 | 8289 (124) | 3 | $-17450.89 | -4.2% |
| **+10¢** | 48737 | 39035 | 9702 (165) | 4 | $-16267.49 | -5.3% |
| **+15¢** | 40866 | 30401 | 10465 (211) | 5 | $-14653.93 | -5.7% |
| **+20¢** | 36395 | 25401 | 10994 (266) | 6 | $-12965.36 | -5.7% |
| **+10¢ (15¢ stop)** | 79436 | 79272 | 164 (98) | 3 | $-29242.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 17:41 | +10 stop | ETH | DOWN | 0.49 | 0.59 | 0.65 |
| 11-19 17:41 | +10 | ETH | DOWN | 0.47 | 0.59 | 0.85 |
| 11-19 17:41 | +5 | ETH | DOWN | 0.48 | 0.59 | 0.75 |
| 11-19 17:41 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 11-19 17:41 | +10 stop | XRP | UP | 0.59 | open |  |
| 11-19 17:41 | +20 | XRP | UP | 0.59 | open |  |
| 11-19 17:41 | +15 | XRP | UP | 0.60 | open |  |
| 11-19 17:41 | +10 | XRP | UP | 0.60 | open |  |
| 11-19 17:41 | +5 | XRP | UP | 0.62 | open |  |
| 11-19 17:41 | +10 stop | BTC | UP | 0.61 | open |  |
| 11-19 17:41 | +20 | BTC | UP | 0.59 | open |  |
| 11-19 17:41 | +15 | BTC | UP | 0.58 | open |  |
| 11-19 17:41 | +10 | BTC | UP | 0.58 | open |  |
| 11-19 17:41 | +5 | BTC | UP | 0.58 | open |  |
| 11-19 17:40 | +10 stop | ZEC | UP | 0.53 | 0.37 | -1.95 |
| 11-19 17:39 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-19 17:39 | +20 | ETH | UP | 0.65 | open |  |
| 11-19 17:39 | +15 | ETH | UP | 0.65 | open |  |
| 11-19 17:39 | +10 | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-19 17:39 | +5 | ETH | UP | 0.67 | 0.76 | 0.61 |
| 11-19 17:39 | +10 stop | BNB | UP | 0.62 | 0.47 | -1.85 |
| 11-19 17:39 | +20 | BNB | UP | 0.62 | open |  |
| 11-19 17:39 | +15 | BNB | UP | 0.62 | open |  |
| 11-19 17:39 | +10 | BNB | UP | 0.62 | open |  |
| 11-19 17:39 | +5 | BNB | UP | 0.61 | 0.70 | 0.58 |
| 11-19 17:38 | +10 stop | ZEC | UP | 0.62 | 0.44 | -2.15 |
| 11-19 17:38 | +10 | ZEC | UP | 0.62 | open |  |
| 11-19 17:38 | +5 | ZEC | UP | 0.62 | open |  |
| 11-19 17:36 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.09 |
| 11-19 17:36 | +20 | DOGE | UP | 0.70 | open |  |
| 11-19 17:36 | +15 | DOGE | UP | 0.70 | 0.87 | 1.47 |
| 11-19 17:36 | +10 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 11-19 17:36 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 11-19 17:36 | +10 stop | BNB | UP | 0.65 | 0.75 | 0.70 |
| 11-19 17:36 | +20 | BNB | UP | 0.67 | 0.87 | 1.76 |
| 11-19 17:36 | +15 | BNB | UP | 0.68 | 0.84 | 1.34 |
| 11-19 17:36 | +10 | BNB | UP | 0.69 | 0.79 | 0.73 |
| 11-19 17:36 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-19 17:36 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-19 17:36 | +20 | ZEC | UP | 0.66 | open |  |
