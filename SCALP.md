# Range-Scalp Bot

*Updated Mon Oct 05 18:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4142 | 3561 | 581 (4) | 5 | $-1492.66 | -5.7% |
| **+10¢** | 3199 | 2533 | 666 (5) | 5 | $-1343.70 | -6.7% |
| **+15¢** | 2687 | 1986 | 701 (8) | 5 | $-1145.17 | -6.8% |
| **+20¢** | 2397 | 1667 | 730 (13) | 5 | $-975.31 | -6.5% |
| **+10¢ (15¢ stop)** | 5117 | 5112 | 5 (2) | 0 | $-1876.10 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 18:58 | +10 stop | XRP | DOWN | 0.17 | 0.61 | 4.13 |
| 10-05 18:55 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-05 18:55 | +10 stop | BTC | UP | 0.63 | 0.75 | 0.89 |
| 10-05 18:55 | +5 | XRP | DOWN | 0.44 | 0.54 | 0.64 |
| 10-05 18:53 | +10 stop | BTC | DOWN | 0.65 | 0.45 | -2.34 |
| 10-05 18:53 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-05 18:53 | +10 stop | ETH | UP | 0.62 | 0.76 | 1.10 |
| 10-05 18:53 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-05 18:53 | +10 stop | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-05 18:51 | +10 stop | XRP | DOWN | 0.66 | 0.47 | -2.23 |
| 10-05 18:51 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-05 18:51 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.20 |
| 10-05 18:51 | +5 | BNB | UP | 0.68 | 0.75 | 0.40 |
| 10-05 18:49 | +10 stop | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 10-05 18:49 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-05 18:49 | +15 | BTC | DOWN | 0.55 | open |  |
| 10-05 18:49 | +10 | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 10-05 18:49 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-05 18:49 | +5 | BNB | UP | 0.56 | 0.61 | 0.15 |
| 10-05 18:48 | +10 stop | NEAR | UP | 0.47 | 0.30 | -2.05 |
| 10-05 18:48 | +10 | NEAR | UP | 0.47 | open |  |
| 10-05 18:48 | +5 | NEAR | UP | 0.50 | open |  |
| 10-05 18:48 | +10 stop | SOL | DOWN | 0.64 | 0.49 | -1.85 |
| 10-05 18:48 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-05 18:48 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.39 |
| 10-05 18:47 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-05 18:47 | +10 stop | ETH | DOWN | 0.60 | 0.41 | -2.24 |
| 10-05 18:47 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-05 18:47 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-05 18:47 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-05 18:47 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-05 18:47 | +10 stop | SOL | DOWN | 0.55 | 0.66 | 0.75 |
| 10-05 18:47 | +20 | SOL | DOWN | 0.55 | open |  |
| 10-05 18:47 | +15 | SOL | DOWN | 0.55 | open |  |
| 10-05 18:47 | +10 | SOL | DOWN | 0.55 | 0.66 | 0.75 |
| 10-05 18:47 | +5 | SOL | DOWN | 0.55 | 0.64 | 0.54 |
| 10-05 18:46 | +10 stop | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-05 18:46 | +20 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-05 18:46 | +15 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-05 18:46 | +10 | DOGE | UP | 0.63 | 0.85 | 1.94 |
