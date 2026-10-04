# Range-Scalp Bot

*Updated Sun Oct 04 14:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2365 | 2041 | 324 (3) | 1 | $-781.05 | -5.2% |
| **+10¢** | 1846 | 1485 | 361 (4) | 2 | $-588.68 | -5.0% |
| **+15¢** | 1549 | 1168 | 381 (5) | 3 | $-484.13 | -5.0% |
| **+20¢** | 1373 | 972 | 401 (9) | 3 | $-411.34 | -4.8% |
| **+10¢ (15¢ stop)** | 2927 | 2926 | 1 (1) | 2 | $-1104.16 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 14:20 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 10-04 14:20 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 10-04 14:19 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-04 14:19 | +10 stop | ZEC | UP | 0.55 | 0.37 | -2.15 |
| 10-04 14:18 | +10 stop | DOGE | UP | 0.66 | 0.40 | -2.93 |
| 10-04 14:18 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 10-04 14:18 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-04 14:18 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 14:18 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 14:18 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-04 14:16 | +10 stop | XRP | DOWN | 0.61 | 0.42 | -2.25 |
| 10-04 14:16 | +20 | XRP | DOWN | 0.61 | 0.88 | 2.45 |
| 10-04 14:16 | +15 | XRP | DOWN | 0.61 | 0.79 | 1.51 |
| 10-04 14:16 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-04 14:16 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-04 14:16 | +10 stop | HYPE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-04 14:16 | +20 | HYPE | DOWN | 0.54 | 0.77 | 1.99 |
| 10-04 14:16 | +15 | HYPE | DOWN | 0.54 | 0.70 | 1.27 |
| 10-04 14:16 | +10 | HYPE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-04 14:16 | +5 | HYPE | DOWN | 0.54 | 0.66 | 0.86 |
| 10-04 14:16 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.90 |
| 10-04 14:16 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-04 14:16 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-04 14:16 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-04 14:16 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.20 |
| 10-04 14:16 | +10 stop | NEAR | DOWN | 0.62 | 0.76 | 1.11 |
| 10-04 14:16 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-04 14:16 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-04 14:16 | +10 | NEAR | DOWN | 0.62 | 0.76 | 1.11 |
| 10-04 14:16 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.28 |
| 10-04 14:16 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-04 14:16 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 10-04 14:16 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 10-04 14:16 | +10 | ETH | DOWN | 0.65 | 0.77 | 0.88 |
| 10-04 14:16 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-04 14:16 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-04 14:16 | +20 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 10-04 14:16 | +15 | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-04 14:16 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-04 14:16 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
