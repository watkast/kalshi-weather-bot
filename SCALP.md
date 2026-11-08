# Range-Scalp Bot

*Updated Sun Nov 08 18:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52640 | 45886 | 6754 (83) | 0 | $-14639.32 | -4.4% |
| **+10¢** | 39300 | 31433 | 7867 (108) | 2 | $-13604.94 | -5.5% |
| **+15¢** | 32922 | 24444 | 8478 (139) | 3 | $-12461.11 | -6.0% |
| **+20¢** | 29286 | 20398 | 8888 (184) | 4 | $-10973.24 | -6.0% |
| **+10¢ (15¢ stop)** | 64111 | 64005 | 106 (63) | 1 | $-23744.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 18:18 | +5 | ETH | UP | 0.57 | 0.72 | 1.17 |
| 11-08 18:18 | +10 stop | DOGE | UP | 0.55 | 0.71 | 1.27 |
| 11-08 18:18 | +10 | DOGE | UP | 0.55 | 0.71 | 1.27 |
| 11-08 18:18 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-08 18:18 | +5 | BTC | UP | 0.63 | 0.76 | 1.00 |
| 11-08 18:18 | +10 stop | SOL | UP | 0.71 | 0.87 | 1.37 |
| 11-08 18:18 | +20 | SOL | UP | 0.71 | 0.94 | 2.15 |
| 11-08 18:18 | +15 | SOL | UP | 0.71 | 0.87 | 1.37 |
| 11-08 18:18 | +10 | SOL | UP | 0.71 | 0.87 | 1.37 |
| 11-08 18:18 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 11-08 18:17 | +10 stop | NEAR | UP | 0.69 | 0.97 | 2.61 |
| 11-08 18:17 | +20 | NEAR | UP | 0.69 | 0.97 | 2.61 |
| 11-08 18:17 | +15 | NEAR | UP | 0.69 | 0.97 | 2.61 |
| 11-08 18:17 | +10 | NEAR | UP | 0.69 | 0.97 | 2.61 |
| 11-08 18:17 | +5 | NEAR | UP | 0.69 | 0.97 | 2.61 |
| 11-08 18:16 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-08 18:16 | +20 | DOGE | UP | 0.65 | open |  |
| 11-08 18:16 | +15 | DOGE | UP | 0.65 | open |  |
| 11-08 18:16 | +10 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-08 18:16 | +5 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-08 18:16 | +10 stop | ETH | UP | 0.64 | 0.48 | -1.95 |
| 11-08 18:16 | +20 | ETH | UP | 0.64 | open |  |
| 11-08 18:16 | +15 | ETH | UP | 0.64 | open |  |
| 11-08 18:16 | +10 | ETH | UP | 0.64 | open |  |
| 11-08 18:16 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 11-08 18:16 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.21 |
| 11-08 18:16 | +20 | XRP | UP | 0.68 | open |  |
| 11-08 18:16 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-08 18:16 | +10 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-08 18:16 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 11-08 18:16 | +10 stop | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 11-08 18:16 | +20 | HYPE | UP | 0.68 | 0.90 | 1.97 |
| 11-08 18:16 | +15 | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 11-08 18:16 | +10 | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 11-08 18:16 | +5 | HYPE | UP | 0.68 | 0.75 | 0.40 |
| 11-08 18:16 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-08 18:16 | +20 | BTC | UP | 0.69 | open |  |
| 11-08 18:16 | +15 | BTC | UP | 0.69 | open |  |
| 11-08 18:16 | +10 | BTC | UP | 0.69 | open |  |
| 11-08 18:16 | +5 | BTC | UP | 0.69 | 0.75 | 0.31 |
