# Range-Scalp Bot

*Updated Sat Oct 10 07:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10091 | 8702 | 1389 (18) | 3 | $-3453.13 | -5.4% |
| **+10¢** | 7627 | 6008 | 1619 (30) | 3 | $-3329.91 | -6.9% |
| **+15¢** | 6439 | 4731 | 1708 (43) | 5 | $-2769.82 | -6.9% |
| **+20¢** | 5725 | 3951 | 1774 (55) | 5 | $-2327.51 | -6.5% |
| **+10¢ (15¢ stop)** | 12405 | 12370 | 35 (22) | 3 | $-4885.70 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 07:01 | +10 stop | XRP | UP | 0.48 | 0.59 | 0.75 |
| 10-10 07:01 | +20 | XRP | UP | 0.48 | open |  |
| 10-10 07:01 | +15 | XRP | UP | 0.49 | open |  |
| 10-10 07:01 | +10 | XRP | UP | 0.49 | 0.59 | 0.65 |
| 10-10 07:01 | +5 | XRP | UP | 0.49 | 0.59 | 0.65 |
| 10-10 07:01 | +10 stop | DOGE | UP | 0.44 | 0.58 | 1.04 |
| 10-10 07:01 | +20 | DOGE | UP | 0.45 | open |  |
| 10-10 07:01 | +15 | DOGE | UP | 0.45 | open |  |
| 10-10 07:01 | +10 | DOGE | UP | 0.45 | 0.58 | 0.95 |
| 10-10 07:01 | +5 | DOGE | UP | 0.45 | 0.58 | 0.95 |
| 10-10 07:01 | +10 stop | NEAR | UP | 0.57 | open |  |
| 10-10 07:01 | +20 | NEAR | UP | 0.57 | open |  |
| 10-10 07:01 | +15 | NEAR | UP | 0.57 | open |  |
| 10-10 07:01 | +10 | NEAR | UP | 0.57 | open |  |
| 10-10 07:01 | +5 | NEAR | UP | 0.57 | open |  |
| 10-10 07:01 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-10 07:01 | +20 | ETH | UP | 0.66 | open |  |
| 10-10 07:01 | +15 | ETH | UP | 0.66 | open |  |
| 10-10 07:01 | +10 | ETH | UP | 0.66 | open |  |
| 10-10 07:01 | +5 | ETH | UP | 0.66 | open |  |
| 10-10 07:01 | +10 stop | BTC | UP | 0.71 | open |  |
| 10-10 07:01 | +20 | BTC | UP | 0.71 | open |  |
| 10-10 07:01 | +15 | BTC | UP | 0.71 | open |  |
| 10-10 07:01 | +10 | BTC | UP | 0.71 | open |  |
| 10-10 07:01 | +5 | BTC | UP | 0.71 | open |  |
| 10-10 06:54 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-10 06:54 | +10 | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-10 06:52 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-10 06:51 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.97 |
| 10-10 06:50 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.03 |
| 10-10 06:49 | +10 stop | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-10 06:48 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-10 06:48 | +10 stop | SOL | UP | 0.57 | 0.30 | -3.03 |
| 10-10 06:48 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 06:48 | +20 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
| 10-10 06:48 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-10 06:48 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 06:48 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-10 06:47 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 10-10 06:46 | +10 stop | BNB | DOWN | 0.66 | 0.83 | 1.40 |
