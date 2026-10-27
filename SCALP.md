# Range-Scalp Bot

*Updated Tue Oct 27 22:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37165 | 32447 | 4718 (45) | 6 | $-10328.08 | -4.4% |
| **+10¢** | 27758 | 22293 | 5465 (67) | 6 | $-9208.82 | -5.3% |
| **+15¢** | 23222 | 17352 | 5870 (91) | 5 | $-8184.18 | -5.6% |
| **+20¢** | 20575 | 14433 | 6142 (116) | 6 | $-7153.79 | -5.5% |
| **+10¢ (15¢ stop)** | 45536 | 45471 | 65 (34) | 2 | $-17364.45 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 22:42 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-27 22:42 | +10 | ETH | UP | 0.70 | open |  |
| 10-27 22:42 | +5 | ETH | UP | 0.70 | open |  |
| 10-27 22:42 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 10-27 22:42 | +10 stop | SOL | DOWN | 0.57 | open |  |
| 10-27 22:42 | +10 | SOL | DOWN | 0.56 | open |  |
| 10-27 22:42 | +5 | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 10-27 22:41 | +10 stop | ETH | UP | 0.52 | 0.68 | 1.26 |
| 10-27 22:41 | +20 | ETH | UP | 0.46 | 0.68 | 1.86 |
| 10-27 22:41 | +15 | ETH | UP | 0.44 | 0.68 | 2.06 |
| 10-27 22:41 | +10 | ETH | UP | 0.44 | 0.58 | 1.04 |
| 10-27 22:41 | +5 | ETH | UP | 0.44 | 0.53 | 0.54 |
| 10-27 22:41 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-27 22:40 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 10-27 22:40 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-27 22:40 | +15 | SOL | DOWN | 0.61 | open |  |
| 10-27 22:40 | +10 | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 22:40 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 10-27 22:40 | +10 stop | NEAR | UP | 0.64 | 0.38 | -2.94 |
| 10-27 22:39 | +10 stop | DOGE | DOWN | 0.57 | 0.31 | -2.93 |
| 10-27 22:39 | +10 stop | ZEC | UP | 0.55 | 0.77 | 1.89 |
| 10-27 22:39 | +5 | ZEC | UP | 0.55 | 0.77 | 1.89 |
| 10-27 22:38 | +10 stop | NEAR | DOWN | 0.68 | 0.35 | -3.62 |
| 10-27 22:38 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-27 22:38 | +5 | DOGE | DOWN | 0.58 | open |  |
| 10-27 22:37 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-27 22:36 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 10-27 22:36 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-27 22:36 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-27 22:36 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-27 22:36 | +10 stop | ZEC | DOWN | 0.54 | 0.38 | -1.95 |
| 10-27 22:36 | +10 stop | XRP | DOWN | 0.54 | 0.39 | -1.85 |
| 10-27 22:35 | +10 stop | XRP | UP | 0.38 | 0.64 | 2.26 |
| 10-27 22:35 | +10 stop | ZEC | UP | 0.46 | 0.66 | 1.66 |
| 10-27 22:34 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 10-27 22:33 | +10 stop | BTC | UP | 0.60 | 0.38 | -2.54 |
| 10-27 22:33 | +10 stop | BNB | UP | 0.64 | 0.43 | -2.46 |
| 10-27 22:33 | +20 | BNB | UP | 0.64 | open |  |
| 10-27 22:33 | +15 | BNB | UP | 0.64 | open |  |
| 10-27 22:33 | +10 | BNB | UP | 0.64 | open |  |
