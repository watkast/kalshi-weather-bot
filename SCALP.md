# Range-Scalp Bot

*Updated Sun Oct 11 14:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12051 | 10402 | 1649 (24) | 1 | $-3987.16 | -5.2% |
| **+10¢** | 9149 | 7233 | 1916 (37) | 2 | $-3772.29 | -6.5% |
| **+15¢** | 7708 | 5674 | 2034 (54) | 2 | $-3213.95 | -6.6% |
| **+20¢** | 6869 | 4750 | 2119 (68) | 3 | $-2708.92 | -6.3% |
| **+10¢ (15¢ stop)** | 14839 | 14798 | 41 (25) | 2 | $-5876.57 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 14:32 | +5 | NEAR | UP | 0.62 | open |  |
| 10-11 14:31 | +10 stop | NEAR | DOWN | 0.46 | open |  |
| 10-11 14:31 | +20 | NEAR | DOWN | 0.46 | open |  |
| 10-11 14:31 | +15 | NEAR | DOWN | 0.46 | open |  |
| 10-11 14:31 | +10 | NEAR | DOWN | 0.46 | open |  |
| 10-11 14:31 | +5 | NEAR | DOWN | 0.46 | 0.54 | 0.44 |
| 10-11 14:31 | +10 stop | HYPE | UP | 0.65 | open |  |
| 10-11 14:31 | +20 | HYPE | UP | 0.65 | open |  |
| 10-11 14:31 | +15 | HYPE | UP | 0.65 | open |  |
| 10-11 14:31 | +10 | HYPE | UP | 0.65 | open |  |
| 10-11 14:31 | +5 | HYPE | UP | 0.65 | 0.70 | 0.19 |
| 10-11 14:31 | +10 stop | BTC | UP | 0.68 | 0.84 | 1.34 |
| 10-11 14:31 | +20 | BTC | UP | 0.68 | open |  |
| 10-11 14:31 | +15 | BTC | UP | 0.68 | 0.84 | 1.39 |
| 10-11 14:31 | +10 | BTC | UP | 0.67 | 0.84 | 1.44 |
| 10-11 14:31 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 10-11 14:28 | +10 stop | BNB | DOWN | 0.30 | 0.54 | 2.08 |
| 10-11 14:28 | +10 | BNB | DOWN | 0.30 | 0.54 | 2.08 |
| 10-11 14:28 | +5 | BNB | DOWN | 0.30 | 0.54 | 2.08 |
| 10-11 14:27 | +10 stop | BNB | UP | 0.49 | 0.63 | 1.05 |
| 10-11 14:27 | +15 | BNB | UP | 0.49 | 0.75 | 2.28 |
| 10-11 14:27 | +10 | BNB | UP | 0.49 | 0.63 | 1.05 |
| 10-11 14:27 | +5 | BNB | UP | 0.52 | 0.63 | 0.75 |
| 10-11 14:27 | +10 stop | SOL | UP | 0.63 | 0.42 | -2.45 |
| 10-11 14:26 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-11 14:25 | +10 stop | ZEC | DOWN | 0.57 | 0.34 | -2.64 |
| 10-11 14:25 | +10 stop | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-11 14:25 | +20 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-11 14:25 | +15 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-11 14:25 | +10 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-11 14:25 | +5 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 10-11 14:25 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-11 14:25 | +20 | HYPE | UP | 0.64 | 0.87 | 2.05 |
| 10-11 14:25 | +15 | HYPE | UP | 0.64 | 0.81 | 1.42 |
| 10-11 14:25 | +10 | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-11 14:25 | +5 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-11 14:24 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-11 14:23 | +10 stop | ZEC | UP | 0.66 | 0.44 | -2.53 |
| 10-11 14:23 | +15 | ZEC | UP | 0.66 | 0.81 | 1.24 |
| 10-11 14:23 | +10 | ZEC | UP | 0.66 | 0.81 | 1.24 |
