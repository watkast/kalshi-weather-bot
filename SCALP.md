# Range-Scalp Bot

*Updated Sun Oct 04 22:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2888 | 2479 | 409 (3) | 4 | $-1031.83 | -5.6% |
| **+10¢** | 2255 | 1797 | 458 (4) | 6 | $-847.92 | -6.0% |
| **+15¢** | 1896 | 1411 | 485 (5) | 6 | $-735.25 | -6.2% |
| **+20¢** | 1690 | 1182 | 508 (9) | 5 | $-638.09 | -6.0% |
| **+10¢ (15¢ stop)** | 3610 | 3609 | 1 (1) | 0 | $-1444.31 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 22:41 | +10 stop | ETH | DOWN | 0.61 | 0.33 | -3.13 |
| 10-04 22:41 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-04 22:41 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-04 22:41 | +10 stop | SOL | DOWN | 0.62 | 0.27 | -3.81 |
| 10-04 22:41 | +10 | SOL | DOWN | 0.62 | open |  |
| 10-04 22:41 | +5 | SOL | DOWN | 0.63 | open |  |
| 10-04 22:40 | +10 stop | NEAR | DOWN | 0.62 | 0.39 | -2.64 |
| 10-04 22:40 | +20 | BTC | UP | 0.70 | 0.97 | 2.50 |
| 10-04 22:40 | +10 stop | SOL | DOWN | 0.55 | 0.68 | 0.96 |
| 10-04 22:40 | +5 | SOL | DOWN | 0.55 | 0.63 | 0.45 |
| 10-04 22:40 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-04 22:40 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -1.95 |
| 10-04 22:40 | +10 stop | DOGE | DOWN | 0.69 | 0.45 | -2.73 |
| 10-04 22:40 | +10 | DOGE | DOWN | 0.69 | open |  |
| 10-04 22:40 | +10 stop | XRP | UP | 0.65 | 0.88 | 2.06 |
| 10-04 22:39 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 10-04 22:39 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-04 22:39 | +10 stop | SOL | UP | 0.58 | 0.37 | -2.45 |
| 10-04 22:38 | +10 stop | DOGE | UP | 0.53 | 0.37 | -1.95 |
| 10-04 22:38 | +5 | DOGE | UP | 0.53 | 0.74 | 1.78 |
| 10-04 22:38 | +10 stop | BNB | UP | 0.60 | 0.29 | -3.47 |
| 10-04 22:38 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.91 |
| 10-04 22:38 | +10 | NEAR | UP | 0.68 | 0.81 | 1.00 |
| 10-04 22:38 | +5 | NEAR | UP | 0.68 | 0.74 | 0.27 |
| 10-04 22:36 | +10 stop | ETH | UP | 0.64 | 0.42 | -2.55 |
| 10-04 22:36 | +10 stop | ZEC | UP | 0.71 | 0.43 | -3.10 |
| 10-04 22:36 | +5 | ZEC | UP | 0.71 | 0.78 | 0.45 |
| 10-04 22:36 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.03 |
| 10-04 22:35 | +5 | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-04 22:35 | +10 stop | BNB | UP | 0.53 | 0.64 | 0.75 |
| 10-04 22:35 | +10 stop | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-04 22:35 | +5 | ZEC | DOWN | 0.52 | 0.61 | 0.55 |
| 10-04 22:34 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 10-04 22:34 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 10-04 22:34 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.57 |
| 10-04 22:33 | +10 stop | XRP | UP | 0.60 | 0.76 | 1.31 |
| 10-04 22:33 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-04 22:33 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.90 |
| 10-04 22:33 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-04 22:33 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
