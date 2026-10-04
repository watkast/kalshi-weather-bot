# Range-Scalp Bot

*Updated Sun Oct 04 14:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2387 | 2063 | 324 (3) | 4 | $-768.05 | -5.1% |
| **+10¢** | 1862 | 1500 | 362 (4) | 4 | $-579.20 | -4.9% |
| **+15¢** | 1561 | 1179 | 382 (5) | 6 | $-471.51 | -4.8% |
| **+20¢** | 1384 | 982 | 402 (9) | 5 | $-395.16 | -4.5% |
| **+10¢ (15¢ stop)** | 2949 | 2948 | 1 (1) | 1 | $-1097.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 14:40 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.83 |
| 10-04 14:40 | +5 | BNB | UP | 0.55 | open |  |
| 10-04 14:39 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-04 14:39 | +20 | ZEC | UP | 0.67 | 0.90 | 2.07 |
| 10-04 14:39 | +15 | ZEC | UP | 0.67 | 0.90 | 2.07 |
| 10-04 14:39 | +10 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-04 14:39 | +5 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-04 14:39 | +10 stop | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 10-04 14:39 | +10 stop | BNB | DOWN | 0.52 | open |  |
| 10-04 14:39 | +5 | BNB | DOWN | 0.52 | 0.61 | 0.55 |
| 10-04 14:38 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 10-04 14:38 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-04 14:38 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-04 14:38 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-04 14:38 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-04 14:38 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 10-04 14:37 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-04 14:37 | +10 stop | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-04 14:37 | +10 | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-04 14:37 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 10-04 14:37 | +10 stop | DOGE | DOWN | 0.58 | 0.35 | -2.64 |
| 10-04 14:37 | +15 | DOGE | DOWN | 0.58 | open |  |
| 10-04 14:37 | +10 | DOGE | DOWN | 0.58 | open |  |
| 10-04 14:37 | +5 | DOGE | DOWN | 0.58 | open |  |
| 10-04 14:37 | +10 stop | XRP | UP | 0.29 | 0.57 | 2.42 |
| 10-04 14:37 | +20 | XRP | UP | 0.29 | 0.57 | 2.42 |
| 10-04 14:37 | +15 | XRP | UP | 0.29 | 0.57 | 2.47 |
| 10-04 14:37 | +10 | XRP | UP | 0.29 | 0.57 | 2.47 |
| 10-04 14:37 | +5 | XRP | UP | 0.29 | 0.57 | 2.47 |
| 10-04 14:37 | +10 stop | SOL | UP | 0.56 | 0.40 | -1.90 |
| 10-04 14:37 | +20 | SOL | UP | 0.56 | open |  |
| 10-04 14:37 | +15 | SOL | UP | 0.56 | open |  |
| 10-04 14:37 | +10 | SOL | UP | 0.56 | open |  |
| 10-04 14:37 | +5 | SOL | UP | 0.56 | open |  |
| 10-04 14:37 | +10 stop | ETH | UP | 0.52 | 0.65 | 0.96 |
| 10-04 14:37 | +20 | ETH | UP | 0.52 | open |  |
| 10-04 14:37 | +15 | ETH | UP | 0.52 | open |  |
| 10-04 14:37 | +10 | ETH | UP | 0.52 | 0.65 | 0.96 |
| 10-04 14:37 | +5 | ETH | UP | 0.52 | 0.65 | 0.96 |
| 10-04 14:37 | +10 stop | BNB | UP | 0.50 | 0.33 | -2.02 |
