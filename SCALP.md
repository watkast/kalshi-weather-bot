# Range-Scalp Bot

*Updated Sat Oct 31 17:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42527 | 37091 | 5436 (59) | 5 | $-11982.98 | -4.5% |
| **+10¢** | 31709 | 25418 | 6291 (81) | 6 | $-10764.58 | -5.4% |
| **+15¢** | 26522 | 19739 | 6783 (109) | 7 | $-9854.41 | -5.9% |
| **+20¢** | 23554 | 16442 | 7112 (141) | 7 | $-8747.48 | -5.9% |
| **+10¢ (15¢ stop)** | 51877 | 51798 | 79 (44) | 0 | $-19634.95 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 17:19 | +10 stop | NEAR | UP | 0.61 | 0.41 | -2.34 |
| 10-31 17:18 | +5 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-31 17:17 | +10 stop | BTC | UP | 0.63 | 0.82 | 1.62 |
| 10-31 17:17 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 10-31 17:17 | +10 stop | ZEC | DOWN | 0.51 | 0.26 | -2.82 |
| 10-31 17:17 | +20 | ZEC | DOWN | 0.51 | open |  |
| 10-31 17:17 | +15 | ZEC | DOWN | 0.51 | open |  |
| 10-31 17:17 | +10 | ZEC | DOWN | 0.51 | open |  |
| 10-31 17:17 | +5 | ZEC | DOWN | 0.51 | open |  |
| 10-31 17:17 | +10 stop | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-31 17:17 | +10 stop | DOGE | DOWN | 0.58 | 0.22 | -3.91 |
| 10-31 17:17 | +10 | DOGE | DOWN | 0.58 | open |  |
| 10-31 17:17 | +5 | DOGE | DOWN | 0.58 | open |  |
| 10-31 17:17 | +10 stop | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-31 17:17 | +20 | XRP | UP | 0.71 | open |  |
| 10-31 17:17 | +15 | XRP | UP | 0.71 | open |  |
| 10-31 17:17 | +10 | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-31 17:17 | +5 | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-31 17:16 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-31 17:16 | +10 stop | ETH | DOWN | 0.54 | 0.38 | -1.95 |
| 10-31 17:16 | +20 | ETH | DOWN | 0.54 | open |  |
| 10-31 17:16 | +15 | ETH | DOWN | 0.54 | open |  |
| 10-31 17:16 | +10 | ETH | DOWN | 0.54 | open |  |
| 10-31 17:16 | +5 | ETH | DOWN | 0.54 | open |  |
| 10-31 17:16 | +10 stop | BNB | DOWN | 0.59 | 0.38 | -2.46 |
| 10-31 17:16 | +20 | BNB | DOWN | 0.59 | open |  |
| 10-31 17:16 | +15 | BNB | DOWN | 0.59 | open |  |
| 10-31 17:16 | +10 | BNB | DOWN | 0.59 | open |  |
| 10-31 17:16 | +5 | BNB | DOWN | 0.59 | open |  |
| 10-31 17:16 | +10 stop | DOGE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-31 17:16 | +20 | DOGE | DOWN | 0.60 | open |  |
| 10-31 17:16 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-31 17:16 | +10 | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-31 17:16 | +5 | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-31 17:16 | +10 stop | BTC | DOWN | 0.53 | 0.37 | -1.95 |
| 10-31 17:16 | +20 | BTC | DOWN | 0.53 | open |  |
| 10-31 17:16 | +15 | BTC | DOWN | 0.53 | open |  |
| 10-31 17:16 | +10 | BTC | DOWN | 0.53 | open |  |
| 10-31 17:16 | +5 | BTC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-31 17:16 | +10 stop | NEAR | DOWN | 0.55 | 0.38 | -2.05 |
