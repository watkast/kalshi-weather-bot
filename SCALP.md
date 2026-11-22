# Range-Scalp Bot

*Updated Sun Nov 22 05:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68289 | 59590 | 8699 (138) | 2 | $-18383.02 | -4.3% |
| **+10¢** | 50992 | 40833 | 10159 (181) | 2 | $-17043.01 | -5.3% |
| **+15¢** | 42743 | 31791 | 10952 (231) | 2 | $-15294.46 | -5.7% |
| **+20¢** | 38049 | 26538 | 11511 (289) | 2 | $-13636.51 | -5.7% |
| **+10¢ (15¢ stop)** | 83154 | 82975 | 179 (111) | 1 | $-30541.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 05:10 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 11-22 05:10 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-22 05:10 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-22 05:10 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-22 05:08 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 11-22 05:05 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 11-22 05:05 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-22 05:05 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-22 05:05 | +10 | NEAR | DOWN | 0.68 | open |  |
| 11-22 05:05 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-22 05:05 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-22 05:05 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-22 05:05 | +15 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-22 05:05 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-22 05:05 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-22 05:04 | +10 stop | ZEC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-22 05:04 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-22 05:04 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-22 05:04 | +10 | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-22 05:04 | +5 | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-22 05:01 | +10 stop | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-22 05:01 | +20 | ETH | DOWN | 0.70 | 0.92 | 2.01 |
| 11-22 05:01 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-22 05:01 | +10 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-22 05:01 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 11-22 05:01 | +10 stop | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-22 05:01 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.99 |
| 11-22 05:01 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-22 05:01 | +10 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-22 05:01 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-22 04:58 | +10 stop | ETH | UP | 0.57 | 0.83 | 2.32 |
| 11-22 04:58 | +10 stop | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-22 04:58 | +10 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-22 04:58 | +5 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-22 04:57 | +10 stop | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 11-22 04:57 | +10 stop | ETH | DOWN | 0.66 | 0.42 | -2.74 |
| 11-22 04:55 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 04:55 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 04:55 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-22 04:55 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
