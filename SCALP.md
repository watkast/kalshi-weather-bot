# Range-Scalp Bot

*Updated Mon Oct 12 04:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13054 | 11272 | 1782 (25) | 1 | $-4299.67 | -5.2% |
| **+10¢** | 9895 | 7836 | 2059 (37) | 2 | $-4001.49 | -6.4% |
| **+15¢** | 8320 | 6121 | 2199 (55) | 2 | $-3520.79 | -6.7% |
| **+20¢** | 7410 | 5118 | 2292 (69) | 2 | $-3010.68 | -6.5% |
| **+10¢ (15¢ stop)** | 16087 | 16046 | 41 (25) | 0 | $-6351.39 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 04:24 | +10 stop | HYPE | DOWN | 0.61 | 0.13 | -5.05 |
| 10-12 04:24 | +10 stop | NEAR | DOWN | 0.66 | 0.83 | 1.46 |
| 10-12 04:22 | +5 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-12 04:22 | +10 stop | NEAR | UP | 0.60 | 0.38 | -2.54 |
| 10-12 04:21 | +10 stop | BTC | UP | 0.62 | 0.81 | 1.62 |
| 10-12 04:21 | +20 | BTC | UP | 0.62 | 0.82 | 1.72 |
| 10-12 04:21 | +15 | BTC | UP | 0.62 | 0.81 | 1.62 |
| 10-12 04:21 | +10 | BTC | UP | 0.62 | 0.81 | 1.62 |
| 10-12 04:21 | +5 | BTC | UP | 0.62 | 0.68 | 0.27 |
| 10-12 04:21 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 10-12 04:21 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-12 04:21 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-12 04:21 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-12 04:21 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-12 04:21 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-12 04:21 | +20 | ETH | UP | 0.71 | 0.94 | 2.10 |
| 10-12 04:21 | +15 | ETH | UP | 0.71 | 0.94 | 2.07 |
| 10-12 04:21 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 10-12 04:21 | +5 | ETH | UP | 0.70 | 0.76 | 0.32 |
| 10-12 04:20 | +10 stop | XRP | DOWN | 0.28 | 0.61 | 2.98 |
| 10-12 04:20 | +10 stop | ZEC | DOWN | 0.44 | 0.61 | 1.35 |
| 10-12 04:20 | +10 stop | NEAR | DOWN | 0.70 | 0.49 | -2.47 |
| 10-12 04:20 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.01 |
| 10-12 04:20 | +5 | NEAR | DOWN | 0.70 | 0.83 | 1.01 |
| 10-12 04:20 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-12 04:19 | +5 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-12 04:18 | +5 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-12 04:18 | +5 | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 10-12 04:18 | +10 stop | ZEC | UP | 0.66 | 0.43 | -2.64 |
| 10-12 04:18 | +10 stop | XRP | UP | 0.59 | 0.42 | -2.05 |
| 10-12 04:18 | +20 | XRP | UP | 0.59 | 0.83 | 2.13 |
| 10-12 04:18 | +15 | XRP | UP | 0.59 | 0.78 | 1.60 |
| 10-12 04:18 | +10 | XRP | UP | 0.59 | 0.69 | 0.68 |
| 10-12 04:18 | +5 | XRP | UP | 0.59 | 0.69 | 0.68 |
| 10-12 04:17 | +10 stop | DOGE | UP | 0.54 | 0.36 | -2.15 |
| 10-12 04:17 | +20 | DOGE | UP | 0.54 | 0.76 | 1.89 |
| 10-12 04:17 | +15 | DOGE | UP | 0.54 | 0.73 | 1.58 |
| 10-12 04:17 | +10 | DOGE | UP | 0.54 | 0.73 | 1.56 |
| 10-12 04:17 | +5 | DOGE | UP | 0.54 | 0.59 | 0.15 |
| 10-12 04:17 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
