# Range-Scalp Bot

*Updated Sat Oct 03 13:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 814 | 711 | 103 (1) | 0 | $-217.62 | -4.2% |
| **+10¢** | 623 | 511 | 112 (2) | 1 | $-122.39 | -3.1% |
| **+15¢** | 528 | 408 | 120 (3) | 2 | $-98.59 | -3.0% |
| **+20¢** | 461 | 335 | 126 (3) | 2 | $-86.11 | -3.0% |
| **+10¢ (15¢ stop)** | 1040 | 1039 | 1 (1) | 0 | $-520.25 | -8.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 13:27 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-03 13:27 | +20 | HYPE | UP | 0.64 | open |  |
| 10-03 13:27 | +15 | HYPE | UP | 0.64 | open |  |
| 10-03 13:27 | +10 | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-03 13:21 | +10 stop | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 10-03 13:19 | +10 stop | NEAR | DOWN | 0.65 | 0.48 | -2.04 |
| 10-03 13:19 | +5 | NEAR | DOWN | 0.65 | 0.79 | 1.13 |
| 10-03 13:18 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.96 |
| 10-03 13:18 | +15 | HYPE | DOWN | 0.70 | 0.91 | 1.92 |
| 10-03 13:18 | +10 | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-03 13:18 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.79 |
| 10-03 13:18 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.79 |
| 10-03 13:18 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.27 |
| 10-03 13:18 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 10-03 13:17 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-03 13:17 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-03 13:17 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 10-03 13:17 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.82 |
| 10-03 13:17 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.82 |
| 10-03 13:17 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.30 |
| 10-03 13:17 | +10 stop | NEAR | UP | 0.48 | 0.32 | -1.94 |
| 10-03 13:17 | +20 | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +15 | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +10 | NEAR | UP | 0.48 | open |  |
| 10-03 13:17 | +5 | NEAR | UP | 0.48 | 0.53 | 0.14 |
| 10-03 13:17 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-03 13:17 | +20 | ETH | DOWN | 0.59 | 0.84 | 2.23 |
| 10-03 13:17 | +15 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 13:17 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-03 13:17 | +5 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-03 13:16 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-03 13:16 | +20 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-03 13:16 | +15 | BTC | DOWN | 0.64 | 0.83 | 1.63 |
| 10-03 13:16 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-03 13:16 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-03 13:16 | +5 | HYPE | UP | 0.57 | 0.64 | 0.35 |
| 10-03 13:15 | +10 stop | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 13:15 | +20 | DOGE | DOWN | 0.59 | 0.80 | 1.81 |
| 10-03 13:15 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-03 13:15 | +10 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
