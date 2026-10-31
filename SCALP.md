# Range-Scalp Bot

*Updated Sat Oct 31 13:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42255 | 36861 | 5394 (58) | 0 | $-11864.57 | -4.5% |
| **+10¢** | 31502 | 25257 | 6245 (81) | 0 | $-10648.78 | -5.4% |
| **+15¢** | 26347 | 19613 | 6734 (109) | 0 | $-9747.56 | -5.9% |
| **+20¢** | 23399 | 16344 | 7055 (141) | 0 | $-8598.91 | -5.9% |
| **+10¢ (15¢ stop)** | 51532 | 51453 | 79 (44) | 0 | $-19457.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 13:12 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-31 13:11 | +5 | ZEC | UP | 0.62 | 0.88 | 2.35 |
| 10-31 13:11 | +10 stop | ZEC | DOWN | 0.58 | 0.32 | -2.94 |
| 10-31 13:11 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-31 13:10 | +10 stop | ZEC | DOWN | 0.38 | 0.58 | 1.65 |
| 10-31 13:10 | +5 | ZEC | DOWN | 0.40 | 0.58 | 1.45 |
| 10-31 13:09 | +5 | ZEC | UP | 0.48 | 0.59 | 0.75 |
| 10-31 13:08 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.15 |
| 10-31 13:08 | +20 | ZEC | UP | 0.61 | 0.88 | 2.42 |
| 10-31 13:08 | +15 | ZEC | UP | 0.61 | 0.88 | 2.42 |
| 10-31 13:08 | +10 | ZEC | UP | 0.61 | 0.88 | 2.41 |
| 10-31 13:08 | +5 | ZEC | UP | 0.62 | 0.69 | 0.38 |
| 10-31 13:07 | +10 stop | BNB | UP | 0.66 | 0.51 | -1.84 |
| 10-31 13:07 | +20 | BNB | UP | 0.66 | no | -6.76 |
| 10-31 13:07 | +15 | BNB | UP | 0.66 | no | -6.76 |
| 10-31 13:07 | +10 | BNB | UP | 0.66 | no | -6.76 |
| 10-31 13:07 | +5 | BNB | UP | 0.66 | no | -6.76 |
| 10-31 13:07 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 10-31 13:07 | +20 | BTC | UP | 0.61 | no | -6.27 |
| 10-31 13:07 | +15 | BTC | UP | 0.62 | no | -6.37 |
| 10-31 13:07 | +10 | BTC | UP | 0.62 | no | -6.37 |
| 10-31 13:07 | +5 | BTC | UP | 0.62 | no | -6.37 |
| 10-31 12:20 | +10 stop | DOGE | UP | 0.48 | yes | 5.02 |
| 10-31 12:20 | +10 stop | XRP | UP | 0.59 | yes | 3.91 |
| 10-31 12:20 | +5 | XRP | UP | 0.59 | yes | 3.93 |
| 10-31 12:20 | +10 stop | BTC | DOWN | 0.67 | no | 3.14 |
| 10-31 12:20 | +20 | BTC | DOWN | 0.67 | no | 3.14 |
| 10-31 12:20 | +15 | BTC | DOWN | 0.67 | no | 3.14 |
| 10-31 12:20 | +10 | BTC | DOWN | 0.67 | no | 3.14 |
| 10-31 12:20 | +5 | BTC | DOWN | 0.67 | no | 3.14 |
| 10-31 12:19 | +10 stop | DOGE | DOWN | 0.67 | 0.42 | -2.83 |
| 10-31 12:19 | +10 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 10-31 12:19 | +5 | DOGE | DOWN | 0.65 | yes | -6.66 |
| 10-31 12:18 | +10 stop | XRP | DOWN | 0.59 | 0.33 | -2.93 |
| 10-31 12:18 | +15 | XRP | DOWN | 0.58 | yes | -5.98 |
| 10-31 12:18 | +10 | XRP | DOWN | 0.58 | yes | -5.98 |
| 10-31 12:17 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.05 |
| 10-31 12:17 | +20 | BNB | DOWN | 0.62 | no | 3.63 |
| 10-31 12:17 | +15 | BNB | DOWN | 0.62 | no | 3.63 |
| 10-31 12:17 | +10 | BNB | DOWN | 0.62 | no | 3.63 |
