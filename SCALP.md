# Range-Scalp Bot

*Updated Wed Oct 14 03:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15379 | 13317 | 2062 (27) | 4 | $-4870.85 | -5.0% |
| **+10¢** | 11631 | 9237 | 2394 (39) | 5 | $-4546.83 | -6.2% |
| **+15¢** | 9771 | 7206 | 2565 (58) | 8 | $-4047.58 | -6.6% |
| **+20¢** | 8684 | 6000 | 2684 (75) | 8 | $-3560.12 | -6.5% |
| **+10¢ (15¢ stop)** | 18856 | 18806 | 50 (29) | 1 | $-7250.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 03:22 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-14 03:22 | +10 stop | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 03:22 | +5 | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 03:21 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-14 03:21 | +5 | HYPE | UP | 0.59 | 0.69 | 0.64 |
| 10-14 03:21 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 10-14 03:21 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-14 03:21 | +10 stop | BNB | DOWN | 0.50 | 0.69 | 1.57 |
| 10-14 03:21 | +10 stop | SOL | DOWN | 0.55 | 0.73 | 1.48 |
| 10-14 03:21 | +20 | SOL | DOWN | 0.55 | open |  |
| 10-14 03:21 | +10 | SOL | DOWN | 0.55 | 0.73 | 1.48 |
| 10-14 03:21 | +5 | SOL | DOWN | 0.55 | 0.61 | 0.25 |
| 10-14 03:21 | +10 stop | XRP | DOWN | 0.63 | 0.79 | 1.31 |
| 10-14 03:21 | +5 | XRP | DOWN | 0.63 | 0.79 | 1.31 |
| 10-14 03:20 | +10 stop | HYPE | DOWN | 0.60 | 0.38 | -2.54 |
| 10-14 03:20 | +10 stop | ETH | DOWN | 0.65 | 0.49 | -1.94 |
| 10-14 03:19 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.97 |
| 10-14 03:19 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-14 03:19 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 10-14 03:19 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-14 03:19 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.53 |
| 10-14 03:19 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 03:19 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-14 03:19 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-14 03:19 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-14 03:19 | +10 stop | BTC | UP | 0.67 | 0.49 | -2.14 |
| 10-14 03:18 | +10 stop | BNB | DOWN | 0.70 | 0.53 | -2.03 |
| 10-14 03:18 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 10-14 03:18 | +10 stop | DOGE | DOWN | 0.69 | 0.53 | -1.92 |
| 10-14 03:17 | +5 | BNB | UP | 0.60 | open |  |
| 10-14 03:17 | +10 stop | NEAR | DOWN | 0.55 | 0.70 | 1.17 |
| 10-14 03:17 | +5 | DOGE | UP | 0.59 | open |  |
| 10-14 03:17 | +10 stop | BTC | UP | 0.68 | 0.47 | -2.44 |
| 10-14 03:17 | +20 | BTC | UP | 0.68 | open |  |
| 10-14 03:17 | +15 | BTC | UP | 0.68 | open |  |
| 10-14 03:17 | +10 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-14 03:17 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-14 03:17 | +10 stop | ETH | UP | 0.65 | 0.45 | -2.34 |
| 10-14 03:17 | +15 | ETH | UP | 0.65 | open |  |
| 10-14 03:17 | +10 | ETH | UP | 0.65 | open |  |
