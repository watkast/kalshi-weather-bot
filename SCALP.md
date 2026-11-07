# Range-Scalp Bot

*Updated Sat Nov 07 05:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50500 | 44016 | 6484 (76) | 3 | $-14231.78 | -4.5% |
| **+10¢** | 37687 | 30137 | 7550 (102) | 4 | $-13170.52 | -5.6% |
| **+15¢** | 31554 | 23419 | 8135 (131) | 4 | $-12087.47 | -6.1% |
| **+20¢** | 28056 | 19528 | 8528 (173) | 5 | $-10686.93 | -6.1% |
| **+10¢ (15¢ stop)** | 61496 | 61397 | 99 (58) | 1 | $-22778.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 05:11 | +10 stop | XRP | UP | 0.56 | open |  |
| 11-07 05:09 | +10 stop | XRP | DOWN | 0.55 | 0.37 | -2.15 |
| 11-07 05:09 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 11-07 05:09 | +10 stop | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 11-07 05:09 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-07 05:09 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 11-07 05:08 | +10 stop | SOL | UP | 0.49 | 0.59 | 0.65 |
| 11-07 05:07 | +20 | XRP | UP | 0.66 | open |  |
| 11-07 05:07 | +15 | XRP | UP | 0.66 | open |  |
| 11-07 05:07 | +10 | XRP | UP | 0.66 | open |  |
| 11-07 05:07 | +5 | XRP | UP | 0.66 | open |  |
| 11-07 05:07 | +10 stop | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 11-07 05:06 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 11-07 05:05 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-07 05:05 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-07 05:05 | +5 | BTC | UP | 0.60 | 0.68 | 0.47 |
| 11-07 05:04 | +10 stop | XRP | UP | 0.69 | 0.34 | -3.81 |
| 11-07 05:04 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-07 05:04 | +10 stop | HYPE | UP | 0.61 | 0.73 | 0.88 |
| 11-07 05:03 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.44 |
| 11-07 05:03 | +10 | BNB | UP | 0.66 | 0.83 | 1.44 |
| 11-07 05:03 | +5 | BNB | UP | 0.66 | 0.83 | 1.44 |
| 11-07 05:03 | +10 stop | DOGE | UP | 0.52 | 0.66 | 1.06 |
| 11-07 05:03 | +5 | ETH | UP | 0.71 | 0.80 | 0.63 |
| 11-07 05:03 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 11-07 05:03 | +5 | BTC | UP | 0.59 | 0.68 | 0.57 |
| 11-07 05:03 | +10 stop | SOL | DOWN | 0.58 | 0.29 | -3.23 |
| 11-07 05:03 | +10 | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 11-07 05:03 | +5 | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 11-07 05:03 | +10 stop | ETH | UP | 0.64 | 0.75 | 0.79 |
| 11-07 05:02 | +10 stop | XRP | DOWN | 0.48 | 0.62 | 1.05 |
| 11-07 05:02 | +10 stop | DOGE | DOWN | 0.63 | 0.43 | -2.35 |
| 11-07 05:02 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-07 05:02 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-07 05:02 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-07 05:02 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-07 05:02 | +10 stop | BTC | DOWN | 0.59 | 0.40 | -2.24 |
| 11-07 05:02 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-07 05:02 | +15 | BTC | DOWN | 0.58 | open |  |
| 11-07 05:02 | +10 | BTC | DOWN | 0.58 | open |  |
