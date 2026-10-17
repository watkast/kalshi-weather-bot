# Range-Scalp Bot

*Updated Sat Oct 17 02:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20223 | 17583 | 2640 (29) | 0 | $-6030.01 | -4.7% |
| **+10¢** | 15240 | 12192 | 3048 (41) | 0 | $-5400.67 | -5.6% |
| **+15¢** | 12742 | 9463 | 3279 (60) | 1 | $-4893.24 | -6.1% |
| **+20¢** | 11295 | 7861 | 3434 (79) | 4 | $-4343.54 | -6.1% |
| **+10¢ (15¢ stop)** | 24872 | 24822 | 50 (29) | 0 | $-9452.50 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 02:17 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.74 |
| 10-17 02:17 | +20 | ETH | DOWN | 0.64 | open |  |
| 10-17 02:17 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.26 |
| 10-17 02:17 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.74 |
| 10-17 02:17 | +5 | ETH | DOWN | 0.64 | 0.74 | 0.74 |
| 10-17 02:17 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-17 02:17 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-17 02:17 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-17 02:17 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-17 02:17 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-17 02:17 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 02:17 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-17 02:17 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-17 02:17 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 02:17 | +5 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 02:15 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 02:15 | +20 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 10-17 02:15 | +15 | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 10-17 02:15 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-17 02:15 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-17 02:15 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 10-17 02:15 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 10-17 02:15 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.33 |
| 10-17 02:15 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 10-17 02:15 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-17 02:15 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 02:15 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-17 02:15 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-17 02:15 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 02:15 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-17 02:01 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-17 02:01 | +20 | BTC | UP | 0.67 | 0.89 | 1.97 |
| 10-17 02:01 | +15 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-17 02:01 | +10 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-17 02:01 | +5 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-17 02:01 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-17 02:01 | +20 | ZEC | UP | 0.67 | 0.90 | 2.09 |
| 10-17 02:01 | +15 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 10-17 02:01 | +10 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-17 02:01 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
