# Range-Scalp Bot

*Updated Sat Oct 10 22:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11018 | 9501 | 1517 (22) | 1 | $-3739.07 | -5.4% |
| **+10¢** | 8340 | 6572 | 1768 (36) | 1 | $-3573.96 | -6.8% |
| **+15¢** | 7032 | 5162 | 1870 (52) | 1 | $-3014.58 | -6.8% |
| **+20¢** | 6258 | 4311 | 1947 (66) | 1 | $-2549.89 | -6.5% |
| **+10¢ (15¢ stop)** | 13573 | 13532 | 41 (25) | 1 | $-5458.54 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 22:48 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-10 22:46 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 10-10 22:46 | +20 | NEAR | DOWN | 0.57 | open |  |
| 10-10 22:46 | +15 | NEAR | DOWN | 0.57 | open |  |
| 10-10 22:46 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-10 22:46 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.25 |
| 10-10 22:43 | +10 stop | ETH | DOWN | 0.51 | 0.79 | 2.50 |
| 10-10 22:43 | +10 | ETH | DOWN | 0.51 | 0.79 | 2.50 |
| 10-10 22:43 | +5 | ETH | DOWN | 0.51 | 0.60 | 0.55 |
| 10-10 22:43 | +10 stop | DOGE | UP | 0.70 | 0.09 | -6.28 |
| 10-10 22:41 | +10 stop | ETH | UP | 0.55 | 0.71 | 1.27 |
| 10-10 22:41 | +10 | ETH | UP | 0.55 | 0.71 | 1.27 |
| 10-10 22:41 | +5 | ETH | UP | 0.55 | 0.63 | 0.45 |
| 10-10 22:40 | +10 stop | XRP | DOWN | 0.52 | 0.64 | 0.81 |
| 10-10 22:40 | +5 | XRP | DOWN | 0.53 | 0.64 | 0.79 |
| 10-10 22:38 | +10 stop | XRP | UP | 0.65 | 0.39 | -2.93 |
| 10-10 22:37 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 10-10 22:37 | +10 stop | BTC | UP | 0.61 | 0.78 | 1.40 |
| 10-10 22:36 | +10 stop | BNB | UP | 0.52 | 0.78 | 2.29 |
| 10-10 22:36 | +5 | BNB | UP | 0.58 | 0.78 | 1.69 |
| 10-10 22:36 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 10-10 22:36 | +10 stop | XRP | DOWN | 0.62 | 0.44 | -2.15 |
| 10-10 22:35 | +10 stop | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-10 22:34 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 10-10 22:34 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.91 |
| 10-10 22:34 | +10 stop | DOGE | UP | 0.65 | 0.47 | -2.16 |
| 10-10 22:33 | +10 stop | NEAR | UP | 0.58 | 0.72 | 1.11 |
| 10-10 22:33 | +20 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 10-10 22:33 | +15 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-10 22:33 | +10 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-10 22:33 | +5 | NEAR | UP | 0.57 | 0.66 | 0.57 |
| 10-10 22:33 | +10 stop | HYPE | UP | 0.58 | 0.72 | 1.03 |
| 10-10 22:33 | +5 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 10-10 22:32 | +10 stop | ZEC | DOWN | 0.52 | 0.34 | -2.14 |
| 10-10 22:32 | +20 | ZEC | DOWN | 0.52 | yes | -5.38 |
| 10-10 22:32 | +15 | ZEC | DOWN | 0.52 | yes | -5.38 |
| 10-10 22:32 | +10 | ZEC | DOWN | 0.52 | yes | -5.38 |
| 10-10 22:32 | +5 | ZEC | DOWN | 0.52 | 0.57 | 0.14 |
| 10-10 22:31 | +10 stop | SOL | DOWN | 0.65 | 0.41 | -2.73 |
| 10-10 22:31 | +20 | SOL | DOWN | 0.65 | yes | -6.66 |
