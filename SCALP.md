# Range-Scalp Bot

*Updated Fri Oct 16 04:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18628 | 16178 | 2450 (28) | 0 | $-5667.24 | -4.8% |
| **+10¢** | 14051 | 11217 | 2834 (40) | 0 | $-5121.71 | -5.8% |
| **+15¢** | 11784 | 8733 | 3051 (59) | 2 | $-4636.74 | -6.3% |
| **+20¢** | 10463 | 7271 | 3192 (78) | 3 | $-4056.28 | -6.2% |
| **+10¢ (15¢ stop)** | 22943 | 22893 | 50 (29) | 0 | $-8842.50 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 04:08 | +10 stop | NEAR | UP | 0.43 | 0.56 | 0.94 |
| 10-16 04:07 | +10 stop | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 04:07 | +15 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 04:07 | +10 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 04:07 | +5 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 04:07 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-16 04:07 | +20 | BTC | DOWN | 0.65 | 0.92 | 2.52 |
| 10-16 04:07 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-16 04:07 | +10 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-16 04:07 | +5 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-16 04:07 | +10 stop | ETH | DOWN | 0.55 | 0.85 | 2.73 |
| 10-16 04:07 | +20 | ETH | DOWN | 0.55 | 0.85 | 2.73 |
| 10-16 04:07 | +15 | ETH | DOWN | 0.55 | 0.85 | 2.73 |
| 10-16 04:07 | +10 | ETH | DOWN | 0.55 | 0.85 | 2.73 |
| 10-16 04:07 | +5 | ETH | DOWN | 0.55 | 0.85 | 2.73 |
| 10-16 04:07 | +5 | SOL | DOWN | 0.63 | 0.77 | 1.10 |
| 10-16 04:07 | +10 stop | XRP | DOWN | 0.58 | 0.76 | 1.53 |
| 10-16 04:07 | +20 | XRP | DOWN | 0.58 | 0.80 | 1.93 |
| 10-16 04:07 | +15 | XRP | DOWN | 0.57 | 0.76 | 1.59 |
| 10-16 04:07 | +10 | XRP | DOWN | 0.57 | 0.76 | 1.59 |
| 10-16 04:07 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 10-16 04:06 | +10 stop | NEAR | DOWN | 0.61 | 0.46 | -1.85 |
| 10-16 04:06 | +10 stop | ZEC | DOWN | 0.71 | 0.52 | -2.23 |
| 10-16 04:06 | +10 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-16 04:06 | +5 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-16 04:06 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-16 04:06 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-16 04:06 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-16 04:01 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 10-16 04:01 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-16 04:01 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-16 04:01 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.06 |
| 10-16 04:01 | +5 | NEAR | DOWN | 0.70 | 0.83 | 1.07 |
| 10-16 04:01 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-16 04:01 | +20 | DOGE | DOWN | 0.66 | 0.89 | 2.07 |
| 10-16 04:01 | +15 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-16 04:01 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-16 04:01 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-16 04:00 | +10 stop | HYPE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-16 04:00 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.86 |
