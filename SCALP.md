# Range-Scalp Bot

*Updated Wed Nov 04 00:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46539 | 40527 | 6012 (72) | 1 | $-13364.14 | -4.6% |
| **+10¢** | 34753 | 27785 | 6968 (96) | 3 | $-12200.83 | -5.6% |
| **+15¢** | 29097 | 21602 | 7495 (124) | 3 | $-11146.63 | -6.1% |
| **+20¢** | 25850 | 17997 | 7853 (164) | 3 | $-9832.41 | -6.1% |
| **+10¢ (15¢ stop)** | 56751 | 56658 | 93 (56) | 0 | $-21244.50 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 00:17 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-04 00:17 | +10 stop | ETH | UP | 0.42 | 0.56 | 1.04 |
| 11-04 00:17 | +10 stop | NEAR | UP | 0.50 | 0.18 | -3.49 |
| 11-04 00:17 | +20 | NEAR | UP | 0.50 | open |  |
| 11-04 00:17 | +15 | NEAR | UP | 0.50 | open |  |
| 11-04 00:17 | +10 | NEAR | UP | 0.50 | open |  |
| 11-04 00:17 | +5 | NEAR | UP | 0.50 | 0.59 | 0.55 |
| 11-04 00:17 | +10 stop | BTC | UP | 0.45 | 0.26 | -2.22 |
| 11-04 00:17 | +15 | BTC | UP | 0.46 | open |  |
| 11-04 00:17 | +10 | BTC | UP | 0.46 | open |  |
| 11-04 00:17 | +5 | BTC | UP | 0.46 | 0.54 | 0.44 |
| 11-04 00:17 | +5 | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-04 00:17 | +10 | ETH | UP | 0.57 | open |  |
| 11-04 00:17 | +5 | ETH | UP | 0.59 | open |  |
| 11-04 00:16 | +10 stop | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 11-04 00:16 | +20 | BNB | DOWN | 0.61 | 0.89 | 2.56 |
| 11-04 00:16 | +15 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 11-04 00:16 | +10 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 11-04 00:16 | +5 | BNB | DOWN | 0.59 | 0.66 | 0.37 |
| 11-04 00:16 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 00:16 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-04 00:16 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.63 |
| 11-04 00:16 | +10 stop | XRP | DOWN | 0.62 | 0.84 | 1.93 |
| 11-04 00:16 | +20 | XRP | DOWN | 0.62 | 0.84 | 1.93 |
| 11-04 00:16 | +15 | XRP | DOWN | 0.62 | 0.84 | 1.93 |
| 11-04 00:16 | +10 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-04 00:16 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 00:16 | +10 stop | ETH | UP | 0.46 | 0.56 | 0.64 |
| 11-04 00:16 | +20 | ETH | UP | 0.46 | open |  |
| 11-04 00:16 | +15 | ETH | UP | 0.45 | open |  |
| 11-04 00:16 | +10 | ETH | UP | 0.45 | 0.55 | 0.64 |
| 11-04 00:16 | +5 | ETH | UP | 0.45 | 0.54 | 0.54 |
| 11-04 00:16 | +10 stop | BTC | UP | 0.43 | 0.57 | 1.04 |
| 11-04 00:16 | +20 | BTC | UP | 0.42 | open |  |
| 11-04 00:16 | +15 | BTC | UP | 0.42 | 0.57 | 1.14 |
| 11-04 00:16 | +10 | BTC | UP | 0.42 | 0.57 | 1.14 |
| 11-04 00:16 | +5 | BTC | UP | 0.42 | 0.57 | 1.14 |
| 11-04 00:16 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 00:16 | +20 | HYPE | DOWN | 0.63 | 0.92 | 2.67 |
| 11-04 00:16 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
