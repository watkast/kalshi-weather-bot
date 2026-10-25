# Range-Scalp Bot

*Updated Sun Oct 25 16:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33396 | 29138 | 4258 (42) | 1 | $-9383.68 | -4.5% |
| **+10¢** | 24996 | 20070 | 4926 (60) | 2 | $-8331.34 | -5.3% |
| **+15¢** | 20911 | 15607 | 5304 (83) | 2 | $-7510.08 | -5.7% |
| **+20¢** | 18530 | 12976 | 5554 (105) | 2 | $-6619.17 | -5.7% |
| **+10¢ (15¢ stop)** | 40936 | 40876 | 60 (32) | 0 | $-15603.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 16:25 | +10 stop | NEAR | UP | 0.63 | 0.44 | -2.25 |
| 10-25 16:25 | +15 | NEAR | UP | 0.65 | 1.00 | 3.32 |
| 10-25 16:25 | +5 | NEAR | UP | 0.65 | 1.00 | 3.32 |
| 10-25 16:24 | +10 stop | XRP | UP | 0.67 | 0.46 | -2.44 |
| 10-25 16:24 | +15 | XRP | UP | 0.67 | 0.92 | 2.25 |
| 10-25 16:24 | +10 | XRP | UP | 0.67 | 0.92 | 2.25 |
| 10-25 16:24 | +5 | XRP | UP | 0.67 | 0.92 | 2.25 |
| 10-25 16:22 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-25 16:22 | +5 | XRP | UP | 0.47 | 0.54 | 0.34 |
| 10-25 16:21 | +10 stop | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-25 16:20 | +5 | BTC | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 16:19 | +10 stop | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 10-25 16:19 | +10 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 10-25 16:19 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 10-25 16:19 | +10 stop | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-25 16:19 | +10 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-25 16:19 | +10 stop | NEAR | DOWN | 0.71 | 0.48 | -2.63 |
| 10-25 16:19 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 16:19 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-25 16:19 | +5 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-25 16:19 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.40 |
| 10-25 16:19 | +5 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-25 16:19 | +20 | BNB | DOWN | 0.58 | 0.92 | 3.11 |
| 10-25 16:19 | +15 | BNB | DOWN | 0.58 | 0.92 | 3.11 |
| 10-25 16:19 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 10-25 16:19 | +10 stop | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-25 16:19 | +10 stop | XRP | DOWN | 0.50 | 0.75 | 2.22 |
| 10-25 16:19 | +5 | XRP | DOWN | 0.50 | 0.55 | 0.18 |
| 10-25 16:19 | +5 | BTC | DOWN | 0.50 | 0.56 | 0.24 |
| 10-25 16:19 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-25 16:18 | +5 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-25 16:18 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-25 16:18 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-25 16:18 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-25 16:18 | +5 | XRP | UP | 0.51 | 0.60 | 0.56 |
| 10-25 16:18 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-25 16:18 | +10 stop | BTC | UP | 0.54 | 0.36 | -2.15 |
| 10-25 16:18 | +20 | BTC | UP | 0.53 | open |  |
| 10-25 16:18 | +15 | BTC | UP | 0.53 | open |  |
| 10-25 16:18 | +10 | BTC | UP | 0.53 | open |  |
