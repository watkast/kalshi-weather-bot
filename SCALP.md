# Range-Scalp Bot

*Updated Thu Oct 08 20:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7945 | 6889 | 1056 (13) | 3 | $-2460.68 | -4.9% |
| **+10¢** | 6016 | 4761 | 1255 (25) | 3 | $-2447.10 | -6.5% |
| **+15¢** | 5059 | 3739 | 1320 (37) | 4 | $-1966.09 | -6.2% |
| **+20¢** | 4518 | 3150 | 1368 (45) | 4 | $-1535.39 | -5.4% |
| **+10¢ (15¢ stop)** | 9650 | 9620 | 30 (19) | 1 | $-3557.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 20:28 | +10 stop | ZEC | DOWN | 0.56 | open |  |
| 10-08 20:28 | +15 | ZEC | DOWN | 0.56 | open |  |
| 10-08 20:28 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-08 20:28 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-08 20:27 | +10 stop | ZEC | DOWN | 0.52 | 0.67 | 1.16 |
| 10-08 20:27 | +10 stop | NEAR | UP | 0.62 | 0.41 | -2.48 |
| 10-08 20:25 | +5 | DOGE | UP | 0.66 | 0.74 | 0.50 |
| 10-08 20:24 | +10 | BNB | UP | 0.63 | 0.84 | 1.83 |
| 10-08 20:24 | +5 | BNB | UP | 0.63 | 0.72 | 0.58 |
| 10-08 20:24 | +10 stop | BNB | UP | 0.62 | 0.39 | -2.64 |
| 10-08 20:24 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-08 20:23 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-08 20:22 | +10 stop | BNB | DOWN | 0.63 | 0.43 | -2.39 |
| 10-08 20:22 | +10 stop | NEAR | DOWN | 0.64 | 0.48 | -1.95 |
| 10-08 20:21 | +10 stop | DOGE | DOWN | 0.61 | 0.38 | -2.64 |
| 10-08 20:20 | +10 stop | NEAR | DOWN | 0.54 | 0.68 | 1.06 |
| 10-08 20:19 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-08 20:19 | +5 | BNB | UP | 0.54 | 0.62 | 0.45 |
| 10-08 20:18 | +10 stop | BNB | UP | 0.50 | 0.34 | -1.94 |
| 10-08 20:18 | +20 | BNB | UP | 0.50 | 0.72 | 1.87 |
| 10-08 20:18 | +15 | BNB | UP | 0.50 | 0.72 | 1.87 |
| 10-08 20:18 | +10 | BNB | UP | 0.50 | 0.62 | 0.85 |
| 10-08 20:18 | +5 | BNB | UP | 0.50 | 0.56 | 0.24 |
| 10-08 20:18 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-08 20:18 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-08 20:18 | +5 | SOL | UP | 0.70 | open |  |
| 10-08 20:18 | +5 | ETH | UP | 0.56 | open |  |
| 10-08 20:17 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.65 |
| 10-08 20:17 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.13 |
| 10-08 20:17 | +10 stop | ETH | UP | 0.56 | 0.40 | -1.95 |
| 10-08 20:17 | +20 | ETH | UP | 0.56 | open |  |
| 10-08 20:17 | +15 | ETH | UP | 0.56 | open |  |
| 10-08 20:17 | +10 | ETH | UP | 0.56 | open |  |
| 10-08 20:17 | +5 | ETH | UP | 0.56 | 0.63 | 0.35 |
| 10-08 20:16 | +10 stop | ZEC | UP | 0.59 | 0.42 | -2.04 |
| 10-08 20:16 | +20 | ZEC | UP | 0.59 | open |  |
| 10-08 20:16 | +15 | ZEC | UP | 0.59 | 0.77 | 1.50 |
| 10-08 20:16 | +10 | ZEC | UP | 0.59 | 0.71 | 0.88 |
| 10-08 20:16 | +5 | ZEC | UP | 0.59 | 0.64 | 0.16 |
| 10-08 20:16 | +10 stop | DOGE | UP | 0.61 | 0.44 | -2.05 |
