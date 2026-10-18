# Range-Scalp Bot

*Updated Sun Oct 18 04:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22038 | 19195 | 2843 (29) | 3 | $-6348.06 | -4.6% |
| **+10¢** | 16584 | 13299 | 3285 (41) | 3 | $-5643.10 | -5.4% |
| **+15¢** | 13886 | 10344 | 3542 (61) | 4 | $-5112.86 | -5.9% |
| **+20¢** | 12287 | 8576 | 3711 (80) | 4 | $-4556.86 | -5.9% |
| **+10¢ (15¢ stop)** | 27109 | 27059 | 50 (29) | 0 | $-10345.62 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 04:27 | +10 stop | ETH | DOWN | 0.69 | 0.90 | 1.92 |
| 10-18 04:27 | +10 | ETH | DOWN | 0.69 | 0.90 | 1.92 |
| 10-18 04:27 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-18 04:27 | +10 stop | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 04:27 | +15 | DOGE | DOWN | 0.69 | 0.89 | 1.78 |
| 10-18 04:27 | +10 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 04:27 | +5 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 04:26 | +10 stop | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-18 04:25 | +10 stop | HYPE | DOWN | 0.54 | 0.26 | -3.12 |
| 10-18 04:24 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-18 04:24 | +10 stop | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 10-18 04:22 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-18 04:22 | +10 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-18 04:22 | +10 stop | HYPE | UP | 0.65 | 0.50 | -1.84 |
| 10-18 04:22 | +10 | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-18 04:22 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 10-18 04:22 | +10 stop | NEAR | DOWN | 0.52 | 0.67 | 1.16 |
| 10-18 04:22 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-18 04:22 | +10 stop | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-18 04:21 | +5 | XRP | UP | 0.60 | open |  |
| 10-18 04:20 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-18 04:20 | +15 | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-18 04:20 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-18 04:20 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.59 |
| 10-18 04:20 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-18 04:19 | +10 stop | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-18 04:19 | +10 | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-18 04:19 | +10 stop | ETH | UP | 0.54 | 0.65 | 0.76 |
| 10-18 04:19 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 10-18 04:19 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 10-18 04:19 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-18 04:19 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.55 |
| 10-18 04:19 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-18 04:18 | +10 stop | BTC | UP | 0.54 | 0.64 | 0.65 |
| 10-18 04:18 | +20 | BTC | UP | 0.54 | 0.74 | 1.68 |
| 10-18 04:18 | +15 | BTC | UP | 0.54 | 0.69 | 1.17 |
| 10-18 04:18 | +10 | BTC | UP | 0.54 | 0.64 | 0.65 |
| 10-18 04:18 | +5 | BTC | UP | 0.54 | 0.62 | 0.45 |
| 10-18 04:18 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 10-18 04:18 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
