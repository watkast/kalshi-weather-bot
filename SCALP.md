# Range-Scalp Bot

*Updated Thu Oct 08 23:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8195 | 7088 | 1107 (13) | 2 | $-2684.21 | -5.2% |
| **+10¢** | 6203 | 4893 | 1310 (25) | 2 | $-2657.64 | -6.8% |
| **+15¢** | 5225 | 3847 | 1378 (37) | 3 | $-2168.46 | -6.6% |
| **+20¢** | 4659 | 3228 | 1431 (45) | 4 | $-1779.14 | -6.1% |
| **+10¢ (15¢ stop)** | 9953 | 9923 | 30 (19) | 2 | $-3691.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 23:50 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 10-08 23:50 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-08 23:50 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-08 23:50 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-08 23:50 | +10 stop | NEAR | UP | 0.50 | open |  |
| 10-08 23:49 | +5 | NEAR | UP | 0.57 | open |  |
| 10-08 23:49 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-08 23:49 | +15 | ZEC | UP | 0.67 | open |  |
| 10-08 23:49 | +10 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-08 23:49 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 10-08 23:49 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.93 |
| 10-08 23:48 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 23:48 | +10 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 23:48 | +5 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 23:48 | +10 stop | NEAR | UP | 0.46 | 0.59 | 0.95 |
| 10-08 23:46 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.12 |
| 10-08 23:46 | +5 | ZEC | UP | 0.66 | 0.71 | 0.19 |
| 10-08 23:46 | +10 stop | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 10-08 23:46 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-08 23:46 | +15 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-08 23:46 | +10 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-08 23:46 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-08 23:46 | +10 stop | ETH | DOWN | 0.66 | 0.80 | 1.12 |
| 10-08 23:46 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-08 23:46 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-08 23:46 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-08 23:46 | +5 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-08 23:46 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-08 23:46 | +20 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 10-08 23:46 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-08 23:46 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-08 23:46 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-08 23:46 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-08 23:46 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-08 23:46 | +15 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-08 23:46 | +10 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-08 23:46 | +5 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-08 23:46 | +10 stop | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 10-08 23:46 | +20 | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 10-08 23:46 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
