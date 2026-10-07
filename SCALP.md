# Range-Scalp Bot

*Updated Wed Oct 07 11:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6351 | 5519 | 832 (9) | 0 | $-1877.51 | -4.7% |
| **+10¢** | 4828 | 3853 | 975 (16) | 0 | $-1726.78 | -5.7% |
| **+15¢** | 4059 | 3029 | 1030 (20) | 2 | $-1429.11 | -5.6% |
| **+20¢** | 3629 | 2551 | 1078 (27) | 4 | $-1151.40 | -5.1% |
| **+10¢ (15¢ stop)** | 7701 | 7686 | 15 (9) | 1 | $-2694.31 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 11:36 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-07 11:36 | +5 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-07 11:36 | +10 stop | BNB | DOWN | 0.67 | 0.51 | -1.94 |
| 10-07 11:36 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-07 11:36 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.62 |
| 10-07 11:35 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-07 11:35 | +10 stop | HYPE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-07 11:35 | +10 stop | BNB | DOWN | 0.54 | 0.70 | 1.27 |
| 10-07 11:35 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-07 11:34 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 10-07 11:34 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 10-07 11:34 | +5 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-07 11:34 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-07 11:34 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-07 11:34 | +10 stop | HYPE | UP | 0.38 | 0.54 | 1.25 |
| 10-07 11:34 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-07 11:34 | +10 stop | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-07 11:34 | +10 stop | XRP | UP | 0.64 | 0.46 | -2.15 |
| 10-07 11:34 | +10 stop | NEAR | DOWN | 0.47 | 0.58 | 0.74 |
| 10-07 11:34 | +5 | NEAR | DOWN | 0.51 | 0.58 | 0.34 |
| 10-07 11:34 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-07 11:34 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-07 11:34 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.18 |
| 10-07 11:34 | +10 stop | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 11:34 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 11:34 | +15 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 11:34 | +10 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-07 11:34 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-07 11:33 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-07 11:33 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 10-07 11:33 | +5 | HYPE | DOWN | 0.67 | 0.75 | 0.50 |
| 10-07 11:33 | +5 | BNB | DOWN | 0.58 | 0.63 | 0.15 |
| 10-07 11:33 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.14 |
| 10-07 11:33 | +5 | BNB | DOWN | 0.59 | 0.64 | 0.16 |
| 10-07 11:33 | +5 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-07 11:32 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.16 |
| 10-07 11:32 | +10 stop | HYPE | DOWN | 0.63 | 0.45 | -2.15 |
| 10-07 11:32 | +10 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-07 11:32 | +5 | HYPE | DOWN | 0.63 | 0.72 | 0.58 |
| 10-07 11:32 | +10 stop | SOL | DOWN | 0.65 | 0.45 | -2.34 |
