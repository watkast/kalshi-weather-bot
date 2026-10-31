# Range-Scalp Bot

*Updated Sat Oct 31 10:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42113 | 36740 | 5373 (55) | 1 | $-11836.09 | -4.5% |
| **+10¢** | 31396 | 25177 | 6219 (79) | 1 | $-10586.51 | -5.4% |
| **+15¢** | 26251 | 19545 | 6706 (107) | 1 | $-9691.19 | -5.9% |
| **+20¢** | 23312 | 16289 | 7023 (138) | 2 | $-8534.96 | -5.8% |
| **+10¢ (15¢ stop)** | 51353 | 51278 | 75 (41) | 1 | $-19386.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 10:12 | +10 stop | SOL | UP | 0.66 | open |  |
| 10-31 10:12 | +20 | SOL | UP | 0.66 | open |  |
| 10-31 10:12 | +15 | SOL | UP | 0.64 | open |  |
| 10-31 10:12 | +10 | SOL | UP | 0.64 | open |  |
| 10-31 10:12 | +5 | SOL | UP | 0.64 | open |  |
| 10-31 10:12 | +10 stop | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 10-31 10:12 | +15 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 10-31 10:12 | +10 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 10-31 10:12 | +5 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 10-31 10:10 | +10 stop | XRP | DOWN | 0.70 | 0.87 | 1.47 |
| 10-31 10:09 | +15 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-31 10:09 | +10 stop | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-31 10:09 | +10 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-31 10:09 | +5 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-31 10:09 | +10 stop | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 10-31 10:09 | +20 | ETH | DOWN | 0.60 | 0.86 | 2.34 |
| 10-31 10:09 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-31 10:09 | +10 | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 10-31 10:09 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-31 10:09 | +5 | NEAR | DOWN | 0.61 | 0.70 | 0.58 |
| 10-31 10:09 | +10 stop | BTC | UP | 0.52 | 0.68 | 1.26 |
| 10-31 10:09 | +20 | BTC | UP | 0.52 | open |  |
| 10-31 10:09 | +15 | BTC | UP | 0.52 | 0.68 | 1.26 |
| 10-31 10:09 | +10 | BTC | UP | 0.52 | 0.68 | 1.26 |
| 10-31 10:09 | +5 | BTC | UP | 0.51 | 0.68 | 1.36 |
| 10-31 10:08 | +10 stop | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 10-31 10:08 | +15 | DOGE | DOWN | 0.50 | 0.65 | 1.16 |
| 10-31 10:08 | +10 | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 10-31 10:08 | +5 | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 10-31 10:08 | +10 stop | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 10-31 10:08 | +10 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 10-31 10:08 | +5 | NEAR | DOWN | 0.54 | 0.60 | 0.25 |
| 10-31 10:08 | +10 stop | XRP | UP | 0.55 | 0.65 | 0.66 |
| 10-31 10:07 | +10 stop | XRP | DOWN | 0.66 | 0.34 | -3.52 |
| 10-31 10:07 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-31 10:07 | +15 | XRP | DOWN | 0.68 | 0.87 | 1.66 |
| 10-31 10:07 | +10 | XRP | DOWN | 0.68 | 0.87 | 1.66 |
| 10-31 10:07 | +5 | XRP | DOWN | 0.68 | 0.87 | 1.66 |
| 10-31 10:06 | +10 stop | SOL | DOWN | 0.53 | 0.22 | -3.41 |
| 10-31 10:06 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
