# Range-Scalp Bot

*Updated Wed Oct 28 03:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37529 | 32758 | 4771 (45) | 8 | $-10486.27 | -4.4% |
| **+10¢** | 28020 | 22496 | 5524 (67) | 8 | $-9353.17 | -5.3% |
| **+15¢** | 23440 | 17509 | 5931 (91) | 8 | $-8309.20 | -5.6% |
| **+20¢** | 20778 | 14569 | 6209 (116) | 8 | $-7287.98 | -5.6% |
| **+10¢ (15¢ stop)** | 45973 | 45908 | 65 (34) | 1 | $-17497.15 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 03:53 | +10 stop | ZEC | DOWN | 0.58 | open |  |
| 10-28 03:52 | +10 stop | NEAR | UP | 0.59 | 0.41 | -2.14 |
| 10-28 03:52 | +10 | NEAR | UP | 0.59 | open |  |
| 10-28 03:52 | +5 | NEAR | UP | 0.59 | open |  |
| 10-28 03:52 | +5 | ZEC | UP | 0.60 | open |  |
| 10-28 03:51 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.89 |
| 10-28 03:50 | +5 | ZEC | UP | 0.63 | 0.70 | 0.38 |
| 10-28 03:50 | +10 stop | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-28 03:49 | +10 stop | ZEC | UP | 0.61 | 0.44 | -2.06 |
| 10-28 03:49 | +15 | ZEC | UP | 0.61 | open |  |
| 10-28 03:49 | +10 | ZEC | UP | 0.61 | open |  |
| 10-28 03:49 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 10-28 03:49 | +10 stop | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 10-28 03:48 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-28 03:48 | +10 stop | NEAR | DOWN | 0.54 | 0.24 | -3.31 |
| 10-28 03:48 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 03:48 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 03:47 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-28 03:47 | +10 stop | ZEC | UP | 0.54 | 0.69 | 1.17 |
| 10-28 03:47 | +20 | ZEC | UP | 0.54 | open |  |
| 10-28 03:47 | +15 | ZEC | UP | 0.54 | 0.69 | 1.17 |
| 10-28 03:47 | +10 | ZEC | UP | 0.54 | 0.69 | 1.17 |
| 10-28 03:47 | +5 | ZEC | UP | 0.53 | 0.69 | 1.27 |
| 10-28 03:47 | +5 | BNB | UP | 0.67 | open |  |
| 10-28 03:46 | +10 stop | BTC | UP | 0.61 | 0.43 | -2.15 |
| 10-28 03:46 | +20 | BTC | UP | 0.61 | open |  |
| 10-28 03:46 | +15 | BTC | UP | 0.61 | open |  |
| 10-28 03:46 | +10 | BTC | UP | 0.61 | open |  |
| 10-28 03:46 | +5 | BTC | UP | 0.61 | open |  |
| 10-28 03:46 | +10 stop | ETH | UP | 0.62 | 0.44 | -2.15 |
| 10-28 03:46 | +20 | ETH | UP | 0.62 | open |  |
| 10-28 03:46 | +15 | ETH | UP | 0.62 | open |  |
| 10-28 03:46 | +10 | ETH | UP | 0.62 | open |  |
| 10-28 03:46 | +5 | ETH | UP | 0.62 | open |  |
| 10-28 03:46 | +10 stop | NEAR | UP | 0.61 | 0.46 | -1.85 |
| 10-28 03:46 | +20 | NEAR | UP | 0.61 | open |  |
| 10-28 03:46 | +15 | NEAR | UP | 0.61 | open |  |
| 10-28 03:46 | +10 | NEAR | UP | 0.61 | 0.73 | 0.89 |
| 10-28 03:46 | +5 | NEAR | UP | 0.61 | 0.73 | 0.89 |
| 10-28 03:46 | +10 stop | DOGE | UP | 0.60 | 0.45 | -1.85 |
