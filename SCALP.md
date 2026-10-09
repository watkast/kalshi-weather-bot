# Range-Scalp Bot

*Updated Fri Oct 09 19:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9368 | 8082 | 1286 (17) | 2 | $-3194.73 | -5.4% |
| **+10¢** | 7073 | 5566 | 1507 (29) | 5 | $-3117.05 | -7.0% |
| **+15¢** | 5960 | 4374 | 1586 (42) | 6 | $-2576.57 | -6.9% |
| **+20¢** | 5308 | 3660 | 1648 (53) | 6 | $-2160.27 | -6.5% |
| **+10¢ (15¢ stop)** | 11473 | 11441 | 32 (20) | 5 | $-4427.85 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 19:16 | +10 stop | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-09 19:16 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-09 19:16 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-09 19:16 | +10 | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-09 19:16 | +5 | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-09 19:16 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:16 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:16 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-09 19:16 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-09 19:16 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-09 19:16 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 10-09 19:16 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-09 19:16 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-09 19:16 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-09 19:16 | +5 | HYPE | DOWN | 0.67 | 0.76 | 0.57 |
| 10-09 19:16 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 10-09 19:16 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-09 19:16 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-09 19:16 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-09 19:16 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 10-09 19:16 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-09 19:16 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-09 19:16 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-09 19:16 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-09 19:16 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-09 19:16 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-09 19:16 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:16 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:16 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:16 | +5 | SOL | DOWN | 0.64 | open |  |
| 10-09 19:12 | +10 stop | HYPE | UP | 0.70 | 0.34 | -3.91 |
| 10-09 19:12 | +15 | XRP | DOWN | 0.62 | 0.89 | 2.46 |
| 10-09 19:12 | +5 | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 10-09 19:12 | +20 | SOL | DOWN | 0.57 | 0.89 | 2.95 |
| 10-09 19:11 | +10 stop | HYPE | DOWN | 0.63 | 0.42 | -2.49 |
| 10-09 19:11 | +15 | SOL | DOWN | 0.64 | 0.89 | 2.24 |
| 10-09 19:11 | +10 | XRP | DOWN | 0.70 | 0.89 | 1.68 |
| 10-09 19:10 | +10 stop | XRP | DOWN | 0.70 | 0.89 | 1.68 |
| 10-09 19:10 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-09 19:10 | +10 stop | SOL | DOWN | 0.58 | 0.41 | -2.05 |
