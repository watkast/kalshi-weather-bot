# Range-Scalp Bot

*Updated Sat Oct 03 22:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1385 | 1200 | 185 (2) | 3 | $-447.01 | -5.1% |
| **+10¢** | 1062 | 859 | 203 (4) | 3 | $-286.17 | -4.3% |
| **+15¢** | 896 | 679 | 217 (5) | 7 | $-239.71 | -4.3% |
| **+20¢** | 790 | 554 | 236 (7) | 7 | $-280.43 | -5.6% |
| **+10¢ (15¢ stop)** | 1727 | 1726 | 1 (1) | 3 | $-713.09 | -6.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 22:49 | +10 stop | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 10-03 22:49 | +10 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 10-03 22:49 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-03 22:49 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-03 22:48 | +10 stop | ETH | DOWN | 0.56 | open |  |
| 10-03 22:48 | +10 | ETH | DOWN | 0.56 | open |  |
| 10-03 22:48 | +5 | ETH | DOWN | 0.56 | 0.63 | 0.35 |
| 10-03 22:48 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-03 22:47 | +10 stop | BTC | UP | 0.59 | open |  |
| 10-03 22:47 | +20 | BTC | UP | 0.59 | open |  |
| 10-03 22:47 | +15 | BTC | UP | 0.59 | open |  |
| 10-03 22:47 | +10 | BTC | UP | 0.59 | open |  |
| 10-03 22:47 | +5 | BTC | UP | 0.59 | open |  |
| 10-03 22:47 | +10 stop | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 10-03 22:47 | +10 | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 10-03 22:47 | +5 | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 10-03 22:47 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 10-03 22:47 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-03 22:47 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-03 22:47 | +10 | DOGE | DOWN | 0.69 | open |  |
| 10-03 22:47 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-03 22:47 | +10 stop | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-03 22:47 | +10 | SOL | DOWN | 0.51 | 0.62 | 0.75 |
| 10-03 22:47 | +5 | SOL | DOWN | 0.50 | 0.58 | 0.44 |
| 10-03 22:47 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-03 22:47 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-03 22:47 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-03 22:47 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-03 22:47 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 10-03 22:47 | +10 stop | NEAR | DOWN | 0.61 | 0.78 | 1.40 |
| 10-03 22:47 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-03 22:47 | +15 | NEAR | DOWN | 0.61 | 0.78 | 1.40 |
| 10-03 22:47 | +10 | NEAR | DOWN | 0.61 | 0.78 | 1.40 |
| 10-03 22:47 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 10-03 22:46 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.97 |
| 10-03 22:46 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-03 22:46 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-03 22:46 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.97 |
| 10-03 22:46 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.24 |
| 10-03 22:46 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
