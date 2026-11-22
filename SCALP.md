# Range-Scalp Bot

*Updated Sun Nov 22 05:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68283 | 59586 | 8697 (138) | 2 | $-18372.61 | -4.3% |
| **+10¢** | 50986 | 40829 | 10157 (181) | 2 | $-17034.41 | -5.3% |
| **+15¢** | 42736 | 31787 | 10949 (231) | 3 | $-15281.12 | -5.7% |
| **+20¢** | 38043 | 26535 | 11508 (289) | 3 | $-13623.09 | -5.7% |
| **+10¢ (15¢ stop)** | 83148 | 82969 | 179 (111) | 0 | $-30539.72 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 04:58 | +10 stop | ETH | UP | 0.57 | 0.83 | 2.32 |
| 11-22 04:58 | +10 stop | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-22 04:58 | +10 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-22 04:58 | +5 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-22 04:57 | +10 stop | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 11-22 04:57 | +10 stop | ETH | DOWN | 0.66 | 0.42 | -2.74 |
| 11-22 04:55 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 04:55 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 04:55 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 04:55 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-22 04:55 | +15 | XRP | DOWN | 0.69 | 0.88 | 1.67 |
| 11-22 04:55 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-22 04:55 | +5 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-22 04:55 | +10 stop | DOGE | UP | 0.58 | 0.42 | -1.96 |
| 11-22 04:54 | +10 stop | ETH | DOWN | 0.69 | 0.47 | -2.53 |
| 11-22 04:54 | +10 | ETH | DOWN | 0.69 | open |  |
| 11-22 04:54 | +10 stop | NEAR | DOWN | 0.66 | 0.50 | -1.94 |
| 11-22 04:54 | +10 | NEAR | DOWN | 0.66 | 0.83 | 1.44 |
| 11-22 04:54 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 11-22 04:54 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-22 04:54 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-22 04:54 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-22 04:54 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-22 04:54 | +10 stop | DOGE | UP | 0.70 | 0.47 | -2.63 |
| 11-22 04:54 | +15 | DOGE | UP | 0.70 | 0.92 | 1.99 |
| 11-22 04:54 | +10 | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 11-22 04:54 | +5 | DOGE | UP | 0.68 | 0.82 | 1.13 |
| 11-22 04:54 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 11-22 04:54 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 04:54 | +15 | BNB | DOWN | 0.70 | 0.97 | 2.49 |
| 11-22 04:54 | +10 | BNB | DOWN | 0.71 | 0.84 | 1.05 |
| 11-22 04:54 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 11-22 04:53 | +5 | BTC | DOWN | 0.53 | 0.62 | 0.55 |
| 11-22 04:53 | +10 stop | ETH | DOWN | 0.49 | 0.59 | 0.65 |
| 11-22 04:53 | +10 | ETH | DOWN | 0.49 | 0.59 | 0.65 |
| 11-22 04:53 | +5 | ETH | DOWN | 0.49 | 0.54 | 0.14 |
| 11-22 04:53 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-22 04:52 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-22 04:52 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-22 04:52 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
