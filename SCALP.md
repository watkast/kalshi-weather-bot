# Range-Scalp Bot

*Updated Sat Nov 07 01:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50270 | 43825 | 6445 (76) | 5 | $-14099.22 | -4.5% |
| **+10¢** | 37512 | 30009 | 7503 (102) | 6 | $-13016.74 | -5.5% |
| **+15¢** | 31414 | 23328 | 8086 (131) | 6 | $-11930.86 | -6.1% |
| **+20¢** | 27923 | 19445 | 8478 (173) | 8 | $-10558.17 | -6.0% |
| **+10¢ (15¢ stop)** | 61208 | 61109 | 99 (58) | 0 | $-22680.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 01:27 | +10 | NEAR | DOWN | 0.50 | open |  |
| 11-07 01:27 | +5 | NEAR | DOWN | 0.50 | open |  |
| 11-07 01:27 | +10 | NEAR | DOWN | 0.43 | 0.67 | 2.06 |
| 11-07 01:27 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-07 01:26 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 11-07 01:26 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-07 01:25 | +10 stop | HYPE | DOWN | 0.63 | 0.84 | 1.82 |
| 11-07 01:25 | +10 stop | NEAR | DOWN | 0.63 | 0.45 | -2.15 |
| 11-07 01:25 | +10 stop | SOL | UP | 0.70 | 0.51 | -2.23 |
| 11-07 01:25 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 11-07 01:24 | +10 stop | BTC | UP | 0.66 | 0.39 | -3.03 |
| 11-07 01:24 | +10 stop | HYPE | UP | 0.62 | 0.37 | -2.84 |
| 11-07 01:23 | +10 stop | NEAR | UP | 0.67 | 0.43 | -2.74 |
| 11-07 01:23 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-07 01:23 | +15 | DOGE | UP | 0.69 | 0.84 | 1.25 |
| 11-07 01:23 | +10 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-07 01:23 | +5 | DOGE | UP | 0.69 | 0.75 | 0.31 |
| 11-07 01:23 | +10 stop | SOL | UP | 0.69 | 0.83 | 1.15 |
| 11-07 01:23 | +10 stop | HYPE | DOWN | 0.62 | 0.42 | -2.31 |
| 11-07 01:23 | +20 | HYPE | DOWN | 0.62 | 0.84 | 1.97 |
| 11-07 01:23 | +15 | HYPE | DOWN | 0.62 | 0.84 | 1.97 |
| 11-07 01:23 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.83 |
| 11-07 01:23 | +5 | HYPE | DOWN | 0.61 | 0.70 | 0.58 |
| 11-07 01:23 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 11-07 01:23 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 11-07 01:23 | +15 | ETH | UP | 0.55 | 0.82 | 2.41 |
| 11-07 01:23 | +10 | ETH | UP | 0.55 | 0.66 | 0.76 |
| 11-07 01:23 | +5 | ETH | UP | 0.55 | 0.63 | 0.45 |
| 11-07 01:23 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 11-07 01:23 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-07 01:23 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-07 01:23 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-07 01:23 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-07 01:22 | +10 stop | DOGE | DOWN | 0.36 | 0.54 | 1.45 |
| 11-07 01:22 | +20 | DOGE | DOWN | 0.36 | open |  |
| 11-07 01:22 | +15 | DOGE | DOWN | 0.36 | 0.54 | 1.45 |
| 11-07 01:22 | +10 | DOGE | DOWN | 0.36 | 0.54 | 1.45 |
| 11-07 01:22 | +5 | DOGE | DOWN | 0.36 | 0.54 | 1.45 |
| 11-07 01:22 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 11-07 01:22 | +5 | BTC | DOWN | 0.57 | open |  |
