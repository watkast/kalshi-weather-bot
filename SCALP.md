# Range-Scalp Bot

*Updated Thu Oct 22 22:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29330 | 25525 | 3805 (39) | 1 | $-8682.73 | -4.7% |
| **+10¢** | 21997 | 17594 | 4403 (55) | 5 | $-7820.24 | -5.7% |
| **+15¢** | 18419 | 13690 | 4729 (78) | 5 | $-7010.76 | -6.1% |
| **+20¢** | 16302 | 11343 | 4959 (100) | 8 | $-6361.26 | -6.2% |
| **+10¢ (15¢ stop)** | 35991 | 35932 | 59 (32) | 2 | $-13574.01 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 22:03 | +10 stop | NEAR | UP | 0.68 | open |  |
| 10-22 22:03 | +20 | NEAR | UP | 0.68 | open |  |
| 10-22 22:03 | +15 | NEAR | UP | 0.70 | open |  |
| 10-22 22:03 | +10 | NEAR | UP | 0.69 | open |  |
| 10-22 22:03 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-22 22:03 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-22 22:03 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-22 22:03 | +5 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-22 22:01 | +10 stop | SOL | UP | 0.70 | open |  |
| 10-22 22:01 | +20 | SOL | UP | 0.70 | open |  |
| 10-22 22:01 | +15 | SOL | UP | 0.69 | open |  |
| 10-22 22:01 | +10 | SOL | UP | 0.70 | open |  |
| 10-22 22:01 | +5 | SOL | UP | 0.68 | 0.75 | 0.40 |
| 10-22 22:01 | +10 stop | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-22 22:01 | +20 | ZEC | UP | 0.67 | open |  |
| 10-22 22:01 | +15 | ZEC | UP | 0.67 | 0.84 | 1.44 |
| 10-22 22:01 | +10 | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-22 22:01 | +5 | ZEC | UP | 0.67 | 0.76 | 0.61 |
| 10-22 22:01 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-22 22:01 | +20 | DOGE | UP | 0.63 | open |  |
| 10-22 22:01 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-22 22:01 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-22 22:01 | +5 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-22 22:01 | +5 | HYPE | UP | 0.64 | 0.70 | 0.31 |
| 10-22 22:01 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 10-22 22:01 | +20 | XRP | UP | 0.68 | open |  |
| 10-22 22:01 | +15 | XRP | UP | 0.66 | 0.81 | 1.23 |
| 10-22 22:01 | +10 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-22 22:01 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 10-22 22:01 | +10 stop | ETH | DOWN | 0.50 | 0.27 | -2.62 |
| 10-22 22:01 | +20 | ETH | DOWN | 0.50 | open |  |
| 10-22 22:01 | +15 | ETH | DOWN | 0.50 | open |  |
| 10-22 22:01 | +10 | ETH | DOWN | 0.50 | open |  |
| 10-22 22:01 | +5 | ETH | DOWN | 0.50 | 0.55 | 0.14 |
| 10-22 22:01 | +10 stop | HYPE | DOWN | 0.45 | 0.29 | -1.93 |
| 10-22 22:01 | +20 | HYPE | DOWN | 0.45 | open |  |
| 10-22 22:01 | +15 | HYPE | DOWN | 0.45 | open |  |
| 10-22 22:01 | +10 | HYPE | DOWN | 0.45 | open |  |
| 10-22 22:01 | +5 | HYPE | DOWN | 0.45 | 0.54 | 0.54 |
| 10-22 22:01 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
