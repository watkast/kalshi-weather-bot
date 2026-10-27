# Range-Scalp Bot

*Updated Tue Oct 27 18:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36888 | 32211 | 4677 (44) | 1 | $-10222.72 | -4.4% |
| **+10¢** | 27554 | 22138 | 5416 (66) | 1 | $-9078.74 | -5.2% |
| **+15¢** | 23053 | 17241 | 5812 (90) | 1 | $-8001.77 | -5.5% |
| **+20¢** | 20433 | 14349 | 6084 (115) | 1 | $-6972.34 | -5.4% |
| **+10¢ (15¢ stop)** | 45187 | 45123 | 64 (33) | 0 | $-17216.25 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 18:09 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 18:09 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 18:09 | +10 stop | ZEC | DOWN | 0.61 | 0.80 | 1.61 |
| 10-27 18:09 | +20 | ZEC | DOWN | 0.61 | 0.87 | 2.35 |
| 10-27 18:09 | +15 | ZEC | DOWN | 0.61 | 0.80 | 1.61 |
| 10-27 18:09 | +10 | ZEC | DOWN | 0.61 | 0.80 | 1.61 |
| 10-27 18:09 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-27 18:08 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 10-27 18:08 | +10 stop | XRP | UP | 0.56 | 0.36 | -2.35 |
| 10-27 18:08 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.71 |
| 10-27 18:08 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-27 18:08 | +5 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-27 18:08 | +10 stop | SOL | UP | 0.63 | 0.45 | -2.15 |
| 10-27 18:08 | +5 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-27 18:08 | +10 stop | NEAR | DOWN | 0.55 | 0.70 | 1.17 |
| 10-27 18:08 | +10 | NEAR | DOWN | 0.55 | 0.70 | 1.17 |
| 10-27 18:08 | +5 | NEAR | DOWN | 0.55 | 0.62 | 0.35 |
| 10-27 18:07 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 18:06 | +5 | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-27 18:06 | +10 stop | BTC | UP | 0.66 | 0.51 | -1.84 |
| 10-27 18:06 | +5 | BTC | UP | 0.66 | open |  |
| 10-27 18:06 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 10-27 18:06 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-27 18:06 | +15 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-27 18:06 | +10 | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 10-27 18:06 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 10-27 18:05 | +10 stop | XRP | DOWN | 0.63 | 0.44 | -2.28 |
| 10-27 18:05 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.80 |
| 10-27 18:05 | +15 | XRP | DOWN | 0.63 | 0.84 | 1.80 |
| 10-27 18:05 | +10 | XRP | DOWN | 0.63 | 0.78 | 1.17 |
| 10-27 18:05 | +5 | XRP | DOWN | 0.63 | 0.78 | 1.17 |
| 10-27 18:05 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-27 18:05 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-27 18:05 | +15 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 10-27 18:05 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-27 18:05 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-27 18:05 | +5 | BTC | DOWN | 0.50 | 0.55 | 0.14 |
| 10-27 18:05 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 10-27 18:05 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-27 18:05 | +5 | BTC | DOWN | 0.56 | 0.65 | 0.56 |
