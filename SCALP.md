# Range-Scalp Bot

*Updated Tue Oct 20 05:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25178 | 21917 | 3261 (31) | 2 | $-7399.96 | -4.7% |
| **+10¢** | 18945 | 15178 | 3767 (46) | 0 | $-6569.35 | -5.5% |
| **+15¢** | 15858 | 11801 | 4057 (70) | 1 | $-5915.99 | -5.9% |
| **+20¢** | 14020 | 9774 | 4246 (88) | 1 | $-5310.22 | -6.0% |
| **+10¢ (15¢ stop)** | 30894 | 30842 | 52 (30) | 0 | $-11494.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 05:35 | +5 | XRP | UP | 0.60 | open |  |
| 10-20 05:35 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 10-20 05:35 | +10 | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 10-20 05:34 | +5 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 05:34 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 05:34 | +20 | ETH | DOWN | 0.71 | 0.96 | 2.34 |
| 10-20 05:34 | +15 | ETH | DOWN | 0.71 | 0.90 | 1.72 |
| 10-20 05:34 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 05:34 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 10-20 05:34 | +10 stop | DOGE | DOWN | 0.60 | 0.78 | 1.50 |
| 10-20 05:34 | +10 | DOGE | DOWN | 0.60 | 0.78 | 1.50 |
| 10-20 05:34 | +5 | DOGE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-20 05:33 | +10 stop | SOL | DOWN | 0.58 | 0.71 | 0.99 |
| 10-20 05:33 | +20 | SOL | DOWN | 0.58 | 0.83 | 2.24 |
| 10-20 05:33 | +15 | SOL | DOWN | 0.58 | 0.83 | 2.24 |
| 10-20 05:33 | +10 | SOL | DOWN | 0.58 | 0.71 | 0.99 |
| 10-20 05:33 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.38 |
| 10-20 05:33 | +10 stop | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 10-20 05:33 | +10 stop | DOGE | UP | 0.41 | 0.54 | 0.95 |
| 10-20 05:33 | +20 | DOGE | UP | 0.41 | open |  |
| 10-20 05:33 | +15 | DOGE | UP | 0.41 | open |  |
| 10-20 05:33 | +10 | DOGE | UP | 0.41 | 0.54 | 0.95 |
| 10-20 05:33 | +5 | DOGE | UP | 0.41 | 0.54 | 0.95 |
| 10-20 05:33 | +10 stop | XRP | UP | 0.59 | 0.36 | -2.64 |
| 10-20 05:32 | +5 | NEAR | UP | 0.55 | open |  |
| 10-20 05:32 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-20 05:32 | +10 stop | ETH | DOWN | 0.51 | 0.70 | 1.62 |
| 10-20 05:32 | +20 | ETH | DOWN | 0.51 | 0.72 | 1.82 |
| 10-20 05:32 | +15 | ETH | DOWN | 0.50 | 0.70 | 1.67 |
| 10-20 05:32 | +10 | ETH | DOWN | 0.50 | 0.70 | 1.67 |
| 10-20 05:32 | +5 | ETH | DOWN | 0.50 | 0.57 | 0.34 |
| 10-20 05:32 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 10-20 05:32 | +5 | XRP | DOWN | 0.51 | 0.67 | 1.26 |
| 10-20 05:31 | +5 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 05:31 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 10-20 05:31 | +10 stop | NEAR | DOWN | 0.59 | 0.41 | -2.14 |
| 10-20 05:31 | +20 | NEAR | DOWN | 0.59 | 0.89 | 2.76 |
| 10-20 05:31 | +15 | NEAR | DOWN | 0.59 | 0.74 | 1.19 |
| 10-20 05:31 | +10 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 05:31 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
