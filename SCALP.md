# Range-Scalp Bot

*Updated Fri Oct 16 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18611 | 16166 | 2445 (28) | 5 | $-5645.63 | -4.8% |
| **+10¢** | 14034 | 11206 | 2828 (40) | 7 | $-5097.41 | -5.8% |
| **+15¢** | 11768 | 8724 | 3044 (59) | 8 | $-4607.24 | -6.2% |
| **+20¢** | 10448 | 7264 | 3184 (78) | 9 | $-4018.40 | -6.1% |
| **+10¢ (15¢ stop)** | 22929 | 22879 | 50 (29) | 0 | $-8852.77 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 03:27 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 10-16 03:27 | +10 stop | ZEC | DOWN | 0.63 | 0.36 | -3.04 |
| 10-16 03:26 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-16 03:24 | +5 | ZEC | UP | 0.29 | 0.37 | 0.49 |
| 10-16 03:24 | +10 stop | ZEC | UP | 0.57 | 0.28 | -3.23 |
| 10-16 03:24 | +20 | ZEC | UP | 0.57 | open |  |
| 10-16 03:24 | +15 | ZEC | UP | 0.57 | open |  |
| 10-16 03:24 | +10 | ZEC | UP | 0.57 | open |  |
| 10-16 03:24 | +5 | ZEC | UP | 0.57 | 0.62 | 0.15 |
| 10-16 03:23 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-16 03:23 | +10 stop | DOGE | UP | 0.55 | 0.36 | -2.25 |
| 10-16 03:23 | +5 | DOGE | UP | 0.55 | open |  |
| 10-16 03:23 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-16 03:23 | +10 stop | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 10-16 03:22 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-16 03:22 | +10 stop | DOGE | UP | 0.59 | 0.71 | 0.88 |
| 10-16 03:22 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 10-16 03:21 | +10 stop | BNB | UP | 0.63 | 0.44 | -2.25 |
| 10-16 03:21 | +15 | BNB | UP | 0.63 | open |  |
| 10-16 03:21 | +10 | BNB | UP | 0.63 | open |  |
| 10-16 03:21 | +5 | BNB | UP | 0.63 | open |  |
| 10-16 03:21 | +5 | ETH | UP | 0.65 | open |  |
| 10-16 03:21 | +10 stop | HYPE | UP | 0.65 | 0.43 | -2.52 |
| 10-16 03:21 | +20 | HYPE | UP | 0.65 | open |  |
| 10-16 03:21 | +15 | HYPE | UP | 0.65 | open |  |
| 10-16 03:21 | +10 | HYPE | UP | 0.65 | open |  |
| 10-16 03:21 | +5 | HYPE | UP | 0.65 | open |  |
| 10-16 03:20 | +10 stop | SOL | DOWN | 0.63 | 0.76 | 1.00 |
| 10-16 03:20 | +10 stop | ETH | UP | 0.64 | 0.48 | -1.95 |
| 10-16 03:20 | +10 | ETH | UP | 0.64 | open |  |
| 10-16 03:20 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-16 03:20 | +10 stop | BTC | DOWN | 0.58 | 0.75 | 1.38 |
| 10-16 03:20 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-16 03:20 | +10 stop | XRP | UP | 0.51 | 0.64 | 0.94 |
| 10-16 03:20 | +15 | XRP | UP | 0.51 | open |  |
| 10-16 03:20 | +10 | XRP | UP | 0.51 | 0.64 | 0.95 |
| 10-16 03:20 | +5 | XRP | UP | 0.51 | 0.64 | 0.95 |
| 10-16 03:20 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-16 03:20 | +15 | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 10-16 03:20 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
