# Range-Scalp Bot

*Updated Thu Oct 15 17:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17915 | 15549 | 2366 (28) | 6 | $-5513.33 | -4.9% |
| **+10¢** | 13532 | 10792 | 2740 (40) | 6 | $-5007.93 | -5.9% |
| **+15¢** | 11349 | 8403 | 2946 (59) | 6 | $-4510.30 | -6.3% |
| **+20¢** | 10087 | 7005 | 3082 (77) | 7 | $-3931.00 | -6.2% |
| **+10¢ (15¢ stop)** | 22070 | 22020 | 50 (29) | 0 | $-8542.10 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 17:54 | +5 | ZEC | UP | 0.56 | open |  |
| 10-15 17:53 | +5 | ZEC | UP | 0.53 | 0.66 | 0.96 |
| 10-15 17:52 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-15 17:52 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.82 |
| 10-15 17:52 | +10 stop | ZEC | UP | 0.61 | 0.42 | -2.25 |
| 10-15 17:52 | +10 | ZEC | UP | 0.61 | open |  |
| 10-15 17:52 | +5 | ZEC | UP | 0.61 | 0.66 | 0.17 |
| 10-15 17:52 | +10 stop | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-15 17:52 | +15 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-15 17:52 | +10 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-15 17:52 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 10-15 17:51 | +10 stop | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-15 17:50 | +5 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-15 17:50 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-15 17:49 | +10 stop | BNB | UP | 0.68 | 0.48 | -2.34 |
| 10-15 17:49 | +15 | BNB | UP | 0.68 | open |  |
| 10-15 17:49 | +10 | BNB | UP | 0.68 | open |  |
| 10-15 17:49 | +5 | BNB | UP | 0.68 | open |  |
| 10-15 17:49 | +5 | DOGE | UP | 0.57 | open |  |
| 10-15 17:48 | +10 stop | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 10-15 17:48 | +20 | XRP | DOWN | 0.56 | 0.78 | 1.89 |
| 10-15 17:48 | +15 | XRP | DOWN | 0.56 | 0.75 | 1.58 |
| 10-15 17:48 | +10 | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 10-15 17:48 | +5 | XRP | DOWN | 0.56 | 0.64 | 0.45 |
| 10-15 17:47 | +5 | BNB | UP | 0.65 | 0.70 | 0.19 |
| 10-15 17:47 | +10 stop | SOL | UP | 0.58 | 0.43 | -1.86 |
| 10-15 17:47 | +20 | SOL | UP | 0.58 | open |  |
| 10-15 17:47 | +15 | SOL | UP | 0.58 | open |  |
| 10-15 17:47 | +10 | SOL | UP | 0.58 | open |  |
| 10-15 17:47 | +5 | SOL | UP | 0.58 | open |  |
| 10-15 17:47 | +10 stop | BTC | UP | 0.57 | 0.41 | -1.95 |
| 10-15 17:47 | +20 | BTC | UP | 0.57 | open |  |
| 10-15 17:47 | +15 | BTC | UP | 0.57 | open |  |
| 10-15 17:47 | +10 | BTC | UP | 0.57 | open |  |
| 10-15 17:47 | +5 | BTC | UP | 0.57 | open |  |
| 10-15 17:47 | +10 stop | DOGE | UP | 0.66 | 0.49 | -2.04 |
| 10-15 17:47 | +20 | DOGE | UP | 0.66 | open |  |
| 10-15 17:47 | +15 | DOGE | UP | 0.66 | open |  |
| 10-15 17:47 | +10 | DOGE | UP | 0.66 | open |  |
| 10-15 17:47 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
