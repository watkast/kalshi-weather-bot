# Range-Scalp Bot

*Updated Mon Oct 05 02:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3125 | 2678 | 447 (3) | 7 | $-1164.59 | -5.9% |
| **+10¢** | 2422 | 1915 | 507 (4) | 7 | $-1026.17 | -6.7% |
| **+15¢** | 2038 | 1503 | 535 (5) | 7 | $-903.28 | -7.1% |
| **+20¢** | 1819 | 1263 | 556 (10) | 7 | $-758.88 | -6.6% |
| **+10¢ (15¢ stop)** | 3907 | 3906 | 1 (1) | 3 | $-1557.78 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 02:23 | +5 | ETH | UP | 0.64 | open |  |
| 10-05 02:22 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-05 02:22 | +10 stop | ETH | UP | 0.59 | open |  |
| 10-05 02:22 | +10 | ETH | UP | 0.59 | open |  |
| 10-05 02:22 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
| 10-05 02:21 | +10 stop | ETH | UP | 0.32 | 0.53 | 1.76 |
| 10-05 02:21 | +10 | ETH | UP | 0.32 | 0.53 | 1.76 |
| 10-05 02:21 | +5 | ETH | UP | 0.32 | 0.53 | 1.76 |
| 10-05 02:21 | +10 stop | NEAR | UP | 0.66 | 0.45 | -2.44 |
| 10-05 02:21 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-05 02:19 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-05 02:19 | +10 stop | NEAR | DOWN | 0.49 | 0.30 | -2.25 |
| 10-05 02:19 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 10-05 02:18 | +10 stop | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 10-05 02:18 | +10 stop | HYPE | UP | 0.66 | 0.44 | -2.54 |
| 10-05 02:18 | +5 | HYPE | UP | 0.66 | open |  |
| 10-05 02:18 | +10 stop | NEAR | UP | 0.64 | 0.45 | -2.27 |
| 10-05 02:18 | +10 | NEAR | UP | 0.64 | open |  |
| 10-05 02:18 | +5 | NEAR | UP | 0.64 | open |  |
| 10-05 02:18 | +10 stop | XRP | UP | 0.61 | 0.29 | -3.52 |
| 10-05 02:17 | +10 stop | SOL | UP | 0.58 | 0.35 | -2.64 |
| 10-05 02:17 | +10 stop | ZEC | DOWN | 0.53 | 0.74 | 1.78 |
| 10-05 02:17 | +10 stop | DOGE | UP | 0.57 | 0.37 | -2.35 |
| 10-05 02:17 | +20 | DOGE | UP | 0.57 | open |  |
| 10-05 02:17 | +15 | DOGE | UP | 0.57 | open |  |
| 10-05 02:17 | +10 | DOGE | UP | 0.57 | open |  |
| 10-05 02:17 | +5 | DOGE | UP | 0.57 | open |  |
| 10-05 02:17 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.86 |
| 10-05 02:17 | +20 | XRP | UP | 0.63 | open |  |
| 10-05 02:17 | +15 | XRP | UP | 0.63 | open |  |
| 10-05 02:17 | +10 | XRP | UP | 0.63 | open |  |
| 10-05 02:17 | +5 | XRP | UP | 0.64 | open |  |
| 10-05 02:17 | +5 | HYPE | UP | 0.56 | 0.62 | 0.21 |
| 10-05 02:17 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-05 02:17 | +20 | NEAR | UP | 0.57 | open |  |
| 10-05 02:17 | +15 | NEAR | UP | 0.57 | open |  |
| 10-05 02:17 | +10 | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-05 02:17 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 10-05 02:16 | +10 stop | ZEC | UP | 0.67 | 0.43 | -2.74 |
| 10-05 02:16 | +20 | ZEC | UP | 0.67 | open |  |
