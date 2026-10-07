# Range-Scalp Bot

*Updated Wed Oct 07 11:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6379 | 5547 | 832 (9) | 3 | $-1862.54 | -4.6% |
| **+10¢** | 4845 | 3870 | 975 (16) | 5 | $-1710.60 | -5.6% |
| **+15¢** | 4069 | 3039 | 1030 (20) | 6 | $-1415.01 | -5.5% |
| **+20¢** | 3639 | 2561 | 1078 (27) | 6 | $-1130.61 | -5.0% |
| **+10¢ (15¢ stop)** | 7729 | 7714 | 15 (9) | 0 | $-2688.53 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 11:55 | +10 stop | BTC | UP | 0.41 | 0.57 | 1.25 |
| 10-07 11:54 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-07 11:54 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-07 11:54 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-07 11:54 | +10 | ZEC | DOWN | 0.71 | 0.84 | 1.06 |
| 10-07 11:54 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.23 |
| 10-07 11:54 | +10 stop | XRP | UP | 0.56 | 0.68 | 0.86 |
| 10-07 11:54 | +10 stop | ETH | UP | 0.63 | 0.79 | 1.33 |
| 10-07 11:53 | +10 stop | BTC | DOWN | 0.67 | 0.47 | -2.34 |
| 10-07 11:53 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-07 11:53 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-07 11:53 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-07 11:53 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-07 11:53 | +10 stop | XRP | DOWN | 0.70 | 0.35 | -3.81 |
| 10-07 11:53 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-07 11:52 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 10-07 11:52 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-07 11:52 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-07 11:52 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 10-07 11:52 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-07 11:52 | +10 stop | ETH | DOWN | 0.59 | 0.39 | -2.34 |
| 10-07 11:52 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-07 11:52 | +10 | ETH | DOWN | 0.58 | open |  |
| 10-07 11:52 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-07 11:51 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-07 11:51 | +5 | XRP | DOWN | 0.60 | 0.69 | 0.58 |
| 10-07 11:51 | +5 | BNB | DOWN | 0.55 | 0.60 | 0.15 |
| 10-07 11:50 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-07 11:50 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 11:50 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-07 11:50 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 11:50 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 11:50 | +10 stop | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-07 11:50 | +10 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-07 11:50 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-07 11:49 | +5 | BNB | DOWN | 0.64 | 0.70 | 0.29 |
| 10-07 11:49 | +10 stop | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-07 11:49 | +10 | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-07 11:49 | +5 | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-07 11:48 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
