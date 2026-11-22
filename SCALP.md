# Range-Scalp Bot

*Updated Sun Nov 22 22:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69156 | 60341 | 8815 (145) | 2 | $-18629.59 | -4.3% |
| **+10¢** | 51609 | 41317 | 10292 (188) | 2 | $-17276.62 | -5.3% |
| **+15¢** | 43253 | 32160 | 11093 (241) | 2 | $-15483.71 | -5.7% |
| **+20¢** | 38518 | 26860 | 11658 (300) | 3 | $-13773.23 | -5.7% |
| **+10¢ (15¢ stop)** | 84227 | 84038 | 189 (117) | 0 | $-31048.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 22:09 | +10 stop | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 11-22 22:09 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-22 22:09 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-22 22:09 | +5 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-22 22:08 | +10 stop | NEAR | DOWN | 0.60 | 0.32 | -3.13 |
| 11-22 22:07 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.15 |
| 11-22 22:05 | +5 | ZEC | DOWN | 0.66 | open |  |
| 11-22 22:05 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 22:05 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-22 22:05 | +15 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 11-22 22:05 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 22:05 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-22 22:05 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-22 22:05 | +20 | HYPE | DOWN | 0.60 | 0.80 | 1.71 |
| 11-22 22:05 | +15 | HYPE | DOWN | 0.60 | 0.78 | 1.50 |
| 11-22 22:05 | +10 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-22 22:05 | +5 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-22 22:03 | +5 | ZEC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-22 22:02 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-22 22:02 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-22 22:02 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-22 22:02 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-22 22:02 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-22 22:01 | +10 stop | NEAR | DOWN | 0.63 | 0.46 | -2.05 |
| 11-22 22:01 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-22 22:01 | +15 | NEAR | DOWN | 0.65 | open |  |
| 11-22 22:01 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-22 22:01 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-22 21:58 | +10 stop | SOL | DOWN | 0.44 | 0.54 | 0.64 |
| 11-22 21:56 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-22 21:55 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-22 21:55 | +5 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-22 21:54 | +10 stop | SOL | DOWN | 0.71 | 0.32 | -4.21 |
| 11-22 21:53 | +10 stop | XRP | DOWN | 0.62 | 0.79 | 1.41 |
| 11-22 21:52 | +10 stop | XRP | UP | 0.67 | 0.42 | -2.84 |
| 11-22 21:52 | +5 | XRP | UP | 0.67 | no | -6.86 |
| 11-22 21:50 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.11 |
| 11-22 21:49 | +10 stop | XRP | UP | 0.54 | 0.70 | 1.27 |
| 11-22 21:49 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-22 21:48 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.95 |
