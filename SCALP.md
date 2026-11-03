# Range-Scalp Bot

*Updated Tue Nov 03 23:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46501 | 40493 | 6008 (72) | 2 | $-13359.40 | -4.6% |
| **+10¢** | 34722 | 27757 | 6965 (96) | 3 | $-12214.67 | -5.6% |
| **+15¢** | 29070 | 21578 | 7492 (124) | 4 | $-11166.83 | -6.1% |
| **+20¢** | 25827 | 17977 | 7850 (164) | 5 | $-9856.22 | -6.1% |
| **+10¢ (15¢ stop)** | 56715 | 56622 | 93 (56) | 2 | $-21251.68 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 23:52 | +10 stop | XRP | UP | 0.52 | 0.25 | -3.06 |
| 11-03 23:51 | +10 | NEAR | DOWN | 0.61 | open |  |
| 11-03 23:51 | +5 | NEAR | DOWN | 0.61 | open |  |
| 11-03 23:49 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-03 23:47 | +10 stop | XRP | UP | 0.59 | 0.43 | -1.95 |
| 11-03 23:47 | +20 | XRP | UP | 0.59 | open |  |
| 11-03 23:47 | +15 | XRP | UP | 0.58 | open |  |
| 11-03 23:47 | +10 | XRP | UP | 0.58 | open |  |
| 11-03 23:47 | +5 | XRP | UP | 0.58 | open |  |
| 11-03 23:47 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-03 23:47 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-03 23:47 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-03 23:47 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-03 23:47 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-03 23:46 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 23:46 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 11-03 23:46 | +15 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 23:46 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 23:46 | +5 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 23:46 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 11-03 23:46 | +20 | NEAR | DOWN | 0.57 | open |  |
| 11-03 23:46 | +15 | NEAR | DOWN | 0.57 | open |  |
| 11-03 23:46 | +10 | NEAR | DOWN | 0.56 | 0.66 | 0.66 |
| 11-03 23:46 | +5 | NEAR | DOWN | 0.56 | 0.66 | 0.66 |
| 11-03 23:46 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 11-03 23:46 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-03 23:46 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-03 23:46 | +10 | DOGE | DOWN | 0.69 | open |  |
| 11-03 23:46 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-03 23:46 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-03 23:46 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-03 23:46 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-03 23:46 | +10 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-03 23:46 | +5 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-03 23:46 | +10 stop | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-03 23:46 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-03 23:46 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-03 23:46 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-03 23:46 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 11-03 23:46 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
