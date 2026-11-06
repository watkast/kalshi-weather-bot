# Range-Scalp Bot

*Updated Fri Nov 06 20:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49887 | 43484 | 6403 (76) | 2 | $-14023.04 | -4.5% |
| **+10¢** | 37237 | 29788 | 7449 (102) | 3 | $-12913.30 | -5.5% |
| **+15¢** | 31187 | 23160 | 8027 (131) | 4 | $-11826.18 | -6.0% |
| **+20¢** | 27724 | 19309 | 8415 (172) | 5 | $-10459.60 | -6.0% |
| **+10¢ (15¢ stop)** | 60800 | 60701 | 99 (58) | 0 | $-22564.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 20:12 | +10 stop | BNB | UP | 0.55 | 0.69 | 1.07 |
| 11-06 20:12 | +20 | BNB | UP | 0.56 | open |  |
| 11-06 20:12 | +15 | BNB | UP | 0.56 | open |  |
| 11-06 20:12 | +10 | BNB | UP | 0.58 | 0.69 | 0.77 |
| 11-06 20:12 | +5 | BNB | UP | 0.58 | 0.69 | 0.77 |
| 11-06 20:11 | +10 stop | ETH | UP | 0.54 | 0.32 | -2.54 |
| 11-06 20:11 | +10 | ETH | UP | 0.54 | open |  |
| 11-06 20:11 | +5 | ETH | UP | 0.54 | open |  |
| 11-06 20:11 | +5 | NEAR | UP | 0.51 | 0.59 | 0.45 |
| 11-06 20:11 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 11-06 20:11 | +20 | ETH | UP | 0.56 | open |  |
| 11-06 20:11 | +15 | ETH | UP | 0.56 | open |  |
| 11-06 20:11 | +10 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-06 20:11 | +5 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-06 20:09 | +10 stop | NEAR | UP | 0.68 | 0.49 | -2.24 |
| 11-06 20:09 | +10 | NEAR | UP | 0.68 | open |  |
| 11-06 20:09 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 11-06 20:09 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-06 20:08 | +10 stop | XRP | DOWN | 0.68 | 0.46 | -2.54 |
| 11-06 20:07 | +10 stop | ETH | UP | 0.57 | 0.67 | 0.66 |
| 11-06 20:07 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-06 20:06 | +10 stop | ZEC | DOWN | 0.55 | 0.31 | -2.73 |
| 11-06 20:06 | +10 stop | ETH | DOWN | 0.66 | 0.42 | -2.74 |
| 11-06 20:05 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-06 20:05 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-06 20:05 | +5 | BTC | UP | 0.67 | 0.75 | 0.50 |
| 11-06 20:05 | +10 stop | NEAR | DOWN | 0.64 | 0.48 | -1.95 |
| 11-06 20:04 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 11-06 20:04 | +5 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-06 20:03 | +10 stop | NEAR | DOWN | 0.45 | 0.61 | 1.25 |
| 11-06 20:03 | +10 stop | ZEC | UP | 0.71 | 0.52 | -2.23 |
| 11-06 20:03 | +20 | ZEC | UP | 0.71 | open |  |
| 11-06 20:03 | +15 | ZEC | UP | 0.71 | 0.89 | 1.58 |
| 11-06 20:03 | +10 | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-06 20:03 | +5 | ZEC | UP | 0.69 | 0.78 | 0.62 |
| 11-06 20:03 | +10 stop | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 20:03 | +5 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-06 20:03 | +5 | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-06 20:03 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.09 |
| 11-06 20:03 | +20 | BNB | UP | 0.59 | 0.84 | 2.23 |
