# Range-Scalp Bot

*Updated Fri Oct 09 17:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9219 | 7961 | 1258 (16) | 10 | $-3096.23 | -5.3% |
| **+10¢** | 6963 | 5488 | 1475 (28) | 14 | $-3003.37 | -6.8% |
| **+15¢** | 5873 | 4320 | 1553 (41) | 15 | $-2468.45 | -6.7% |
| **+20¢** | 5223 | 3610 | 1613 (52) | 16 | $-2057.05 | -6.3% |
| **+10¢ (15¢ stop)** | 11286 | 11254 | 32 (20) | 0 | $-4321.04 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 17:25 | +10 stop | HYPE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-09 17:25 | +15 | HYPE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-09 17:25 | +10 | HYPE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-09 17:25 | +5 | HYPE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-09 17:25 | +10 stop | SOL | DOWN | 0.66 | 0.50 | -1.94 |
| 10-09 17:25 | +10 stop | DOGE | DOWN | 0.62 | 0.44 | -2.15 |
| 10-09 17:25 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-09 17:25 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-09 17:25 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-09 17:25 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-09 17:24 | +10 stop | NEAR | UP | 0.64 | 0.05 | -6.11 |
| 10-09 17:23 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-09 17:23 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-09 17:23 | +10 stop | SOL | DOWN | 0.55 | 0.73 | 1.48 |
| 10-09 17:23 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-09 17:23 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-09 17:23 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-09 17:23 | +10 | XRP | DOWN | 0.71 | open |  |
| 10-09 17:23 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-09 17:23 | +10 stop | ZEC | UP | 0.60 | 0.79 | 1.58 |
| 10-09 17:23 | +20 | ZEC | UP | 0.60 | 0.83 | 2.00 |
| 10-09 17:23 | +15 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-09 17:23 | +10 | ZEC | UP | 0.63 | 0.79 | 1.31 |
| 10-09 17:23 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 10-09 17:23 | +10 stop | HYPE | DOWN | 0.70 | 0.50 | -2.35 |
| 10-09 17:22 | +10 stop | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 10-09 17:22 | +10 stop | SOL | UP | 0.52 | 0.36 | -1.95 |
| 10-09 17:22 | +15 | SOL | UP | 0.52 | open |  |
| 10-09 17:22 | +10 | SOL | UP | 0.52 | open |  |
| 10-09 17:22 | +5 | SOL | UP | 0.52 | open |  |
| 10-09 17:22 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-09 17:22 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-09 17:22 | +5 | BTC | UP | 0.46 | 0.57 | 0.74 |
| 10-09 17:21 | +5 | BNB | UP | 0.59 | open |  |
| 10-09 17:21 | +10 stop | HYPE | UP | 0.67 | 0.46 | -2.48 |
| 10-09 17:21 | +10 stop | DOGE | UP | 0.71 | 0.56 | -1.83 |
| 10-09 17:20 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 10-09 17:20 | +5 | SOL | UP | 0.63 | 0.77 | 1.10 |
| 10-09 17:20 | +10 stop | XRP | UP | 0.62 | 0.76 | 1.06 |
| 10-09 17:20 | +10 | XRP | UP | 0.62 | 0.76 | 1.06 |
