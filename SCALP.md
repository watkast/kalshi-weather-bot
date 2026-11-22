# Range-Scalp Bot

*Updated Sun Nov 22 20:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69067 | 60270 | 8797 (145) | 0 | $-18554.54 | -4.3% |
| **+10¢** | 51540 | 41268 | 10272 (188) | 1 | $-17198.32 | -5.3% |
| **+15¢** | 43195 | 32123 | 11072 (240) | 0 | $-15419.78 | -5.7% |
| **+20¢** | 38464 | 26829 | 11635 (299) | 0 | $-13706.18 | -5.7% |
| **+10¢ (15¢ stop)** | 84100 | 83911 | 189 (117) | 0 | $-30941.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 20:22 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-22 20:22 | +5 | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-22 20:22 | +10 stop | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 11-22 20:22 | +10 stop | XRP | UP | 0.51 | 0.68 | 1.36 |
| 11-22 20:22 | +5 | XRP | UP | 0.51 | 0.68 | 1.36 |
| 11-22 20:21 | +10 stop | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-22 20:21 | +10 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-22 20:21 | +5 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-22 20:21 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-22 20:21 | +5 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-22 20:21 | +5 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-22 20:20 | +10 stop | XRP | UP | 0.52 | 0.68 | 1.31 |
| 11-22 20:19 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 11-22 20:19 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.58 |
| 11-22 20:19 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-22 20:19 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-22 20:19 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-22 20:19 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-22 20:19 | +20 | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 11-22 20:19 | +15 | ZEC | DOWN | 0.59 | 0.76 | 1.40 |
| 11-22 20:19 | +10 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-22 20:19 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-22 20:18 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 11-22 20:17 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 11-22 20:17 | +10 stop | HYPE | DOWN | 0.55 | 0.33 | -2.54 |
| 11-22 20:17 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 20:17 | +20 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-22 20:17 | +15 | DOGE | DOWN | 0.60 | 0.79 | 1.61 |
| 11-22 20:17 | +10 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-22 20:17 | +5 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-22 20:16 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.79 |
| 11-22 20:16 | +20 | BNB | DOWN | 0.67 | 0.89 | 1.95 |
| 11-22 20:16 | +15 | BNB | DOWN | 0.68 | 0.87 | 1.64 |
| 11-22 20:16 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.80 |
| 11-22 20:16 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.59 |
| 11-22 20:16 | +10 stop | XRP | UP | 0.65 | 0.48 | -2.04 |
| 11-22 20:16 | +10 | XRP | UP | 0.65 | open |  |
| 11-22 20:16 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 11-22 20:16 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-22 20:16 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.87 |
