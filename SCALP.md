# Range-Scalp Bot

*Updated Sun Oct 04 21:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2807 | 2415 | 392 (3) | 4 | $-954.52 | -5.4% |
| **+10¢** | 2197 | 1755 | 442 (4) | 4 | $-791.27 | -5.7% |
| **+15¢** | 1846 | 1378 | 468 (5) | 4 | $-679.28 | -5.8% |
| **+20¢** | 1645 | 1155 | 490 (9) | 4 | $-583.65 | -5.6% |
| **+10¢ (15¢ stop)** | 3509 | 3508 | 1 (1) | 0 | $-1372.47 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 21:11 | +5 | HYPE | UP | 0.62 | 0.71 | 0.58 |
| 10-04 21:11 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 10-04 21:09 | +10 stop | HYPE | DOWN | 0.51 | 0.63 | 0.85 |
| 10-04 21:08 | +10 stop | ZEC | DOWN | 0.59 | 0.39 | -2.39 |
| 10-04 21:07 | +10 stop | SOL | DOWN | 0.69 | 0.44 | -2.87 |
| 10-04 21:07 | +10 stop | ZEC | DOWN | 0.68 | 0.53 | -1.84 |
| 10-04 21:07 | +10 | ZEC | DOWN | 0.68 | open |  |
| 10-04 21:06 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.69 |
| 10-04 21:06 | +20 | BNB | UP | 0.60 | 0.81 | 1.83 |
| 10-04 21:06 | +15 | BNB | UP | 0.60 | 0.81 | 1.83 |
| 10-04 21:06 | +10 | BNB | UP | 0.60 | 0.70 | 0.69 |
| 10-04 21:06 | +5 | BNB | UP | 0.60 | 0.69 | 0.59 |
| 10-04 21:05 | +10 stop | BTC | UP | 0.65 | 0.82 | 1.43 |
| 10-04 21:05 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 10-04 21:05 | +10 stop | SOL | DOWN | 0.54 | 0.67 | 0.96 |
| 10-04 21:03 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-04 21:03 | +10 stop | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-04 21:03 | +20 | ZEC | DOWN | 0.57 | open |  |
| 10-04 21:03 | +15 | ZEC | DOWN | 0.57 | open |  |
| 10-04 21:03 | +10 | ZEC | DOWN | 0.57 | 0.67 | 0.67 |
| 10-04 21:03 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 10-04 21:03 | +10 stop | XRP | UP | 0.56 | 0.70 | 1.07 |
| 10-04 21:03 | +10 stop | HYPE | UP | 0.52 | 0.31 | -2.43 |
| 10-04 21:03 | +20 | HYPE | UP | 0.52 | 0.73 | 1.78 |
| 10-04 21:03 | +15 | HYPE | UP | 0.52 | 0.71 | 1.57 |
| 10-04 21:03 | +10 | HYPE | UP | 0.52 | 0.71 | 1.57 |
| 10-04 21:03 | +5 | HYPE | UP | 0.52 | 0.58 | 0.24 |
| 10-04 21:02 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 10-04 21:02 | +20 | BTC | UP | 0.70 | 0.92 | 1.94 |
| 10-04 21:02 | +15 | BTC | UP | 0.70 | 0.85 | 1.26 |
| 10-04 21:02 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-04 21:02 | +5 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-04 21:02 | +10 stop | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-04 21:01 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.28 |
| 10-04 21:01 | +20 | NEAR | DOWN | 0.66 | 0.88 | 2.01 |
| 10-04 21:01 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.28 |
| 10-04 21:01 | +10 | NEAR | DOWN | 0.66 | 0.81 | 1.28 |
| 10-04 21:01 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.55 |
| 10-04 21:01 | +10 stop | ETH | DOWN | 0.59 | 0.40 | -2.24 |
| 10-04 21:01 | +20 | ETH | DOWN | 0.59 | open |  |
