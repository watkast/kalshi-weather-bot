# Range-Scalp Bot

*Updated Sat Oct 03 07:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 422 | 361 | 61 (1) | 2 | $-160.60 | -6.0% |
| **+10¢** | 338 | 272 | 66 (2) | 2 | $-105.79 | -4.9% |
| **+15¢** | 283 | 213 | 70 (2) | 2 | $-105.98 | -5.9% |
| **+20¢** | 244 | 171 | 73 (2) | 3 | $-103.79 | -6.7% |
| **+10¢ (15¢ stop)** | 570 | 569 | 1 (1) | 0 | $-274.02 | -7.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 07:55 | +10 stop | BTC | UP | 0.65 | 0.84 | 1.64 |
| 10-03 07:55 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-03 07:54 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 10-03 07:54 | +20 | NEAR | UP | 0.58 | 0.81 | 2.01 |
| 10-03 07:54 | +15 | NEAR | UP | 0.58 | 0.74 | 1.28 |
| 10-03 07:54 | +10 | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 10-03 07:54 | +5 | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 10-03 07:54 | +10 stop | ZEC | DOWN | 0.50 | 0.34 | -1.94 |
| 10-03 07:54 | +10 stop | ETH | UP | 0.62 | 0.75 | 0.99 |
| 10-03 07:54 | +20 | ETH | UP | 0.62 | 0.85 | 2.04 |
| 10-03 07:54 | +15 | ETH | UP | 0.62 | 0.85 | 2.04 |
| 10-03 07:54 | +10 | ETH | UP | 0.62 | 0.75 | 0.99 |
| 10-03 07:54 | +5 | ETH | UP | 0.62 | 0.75 | 0.99 |
| 10-03 07:54 | +10 stop | BTC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-03 07:53 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.86 |
| 10-03 07:53 | +20 | BNB | UP | 0.57 | open |  |
| 10-03 07:53 | +15 | BNB | UP | 0.57 | open |  |
| 10-03 07:53 | +10 | BNB | UP | 0.57 | open |  |
| 10-03 07:53 | +5 | BNB | UP | 0.57 | open |  |
| 10-03 07:52 | +10 stop | BTC | UP | 0.71 | 0.47 | -2.73 |
| 10-03 07:52 | +10 | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-03 07:52 | +5 | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-03 07:52 | +10 stop | ZEC | UP | 0.66 | 0.45 | -2.44 |
| 10-03 07:52 | +15 | ZEC | UP | 0.66 | 0.82 | 1.33 |
| 10-03 07:52 | +10 | ZEC | UP | 0.66 | 0.79 | 1.02 |
| 10-03 07:52 | +5 | ZEC | UP | 0.66 | 0.79 | 1.02 |
| 10-03 07:50 | +5 | BTC | UP | 0.71 | 0.80 | 0.63 |
| 10-03 07:49 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.70 |
| 10-03 07:49 | +20 | ZEC | UP | 0.64 | 0.86 | 1.95 |
| 10-03 07:49 | +15 | ZEC | UP | 0.64 | 0.81 | 1.43 |
| 10-03 07:49 | +10 | ZEC | UP | 0.64 | 0.74 | 0.70 |
| 10-03 07:49 | +5 | ZEC | UP | 0.64 | 0.74 | 0.70 |
| 10-03 07:47 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 10-03 07:47 | +20 | BTC | UP | 0.68 | open |  |
| 10-03 07:47 | +15 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 10-03 07:47 | +10 | BTC | UP | 0.68 | 0.80 | 0.92 |
| 10-03 07:47 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-03 07:47 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-03 07:47 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 10-03 07:47 | +20 | HYPE | UP | 0.67 | 0.88 | 1.82 |
