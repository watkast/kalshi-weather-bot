# Range-Scalp Bot

*Updated Mon Oct 12 08:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13318 | 11516 | 1802 (25) | 0 | $-4285.59 | -5.1% |
| **+10¢** | 10091 | 8003 | 2088 (37) | 2 | $-3996.70 | -6.3% |
| **+15¢** | 8491 | 6260 | 2231 (55) | 2 | $-3507.64 | -6.6% |
| **+20¢** | 7558 | 5232 | 2326 (70) | 2 | $-2976.86 | -6.3% |
| **+10¢ (15¢ stop)** | 16406 | 16365 | 41 (25) | 0 | $-6409.78 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 08:58 | +10 stop | HYPE | UP | 0.71 | 0.52 | -2.23 |
| 10-12 08:58 | +5 | HYPE | UP | 0.67 | 0.86 | 1.65 |
| 10-12 08:57 | +10 stop | HYPE | DOWN | 0.39 | 0.57 | 1.45 |
| 10-12 08:57 | +5 | HYPE | DOWN | 0.39 | 0.57 | 1.45 |
| 10-12 08:56 | +20 | DOGE | DOWN | 0.60 | 0.81 | 1.77 |
| 10-12 08:56 | +10 stop | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-12 08:56 | +15 | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-12 08:56 | +10 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-12 08:56 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-12 08:56 | +10 stop | HYPE | DOWN | 0.71 | 0.56 | -1.83 |
| 10-12 08:55 | +10 stop | DOGE | UP | 0.43 | 0.58 | 1.14 |
| 10-12 08:55 | +15 | DOGE | UP | 0.43 | 0.58 | 1.14 |
| 10-12 08:55 | +10 | DOGE | UP | 0.43 | 0.58 | 1.11 |
| 10-12 08:55 | +5 | DOGE | UP | 0.44 | 0.58 | 1.06 |
| 10-12 08:55 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.77 |
| 10-12 08:54 | +10 stop | SOL | UP | 0.42 | 0.66 | 2.06 |
| 10-12 08:54 | +10 | SOL | UP | 0.42 | 0.66 | 2.06 |
| 10-12 08:54 | +5 | SOL | UP | 0.42 | 0.66 | 2.06 |
| 10-12 08:54 | +5 | ETH | DOWN | 0.52 | 0.78 | 2.29 |
| 10-12 08:54 | +10 stop | ZEC | UP | 0.47 | 0.64 | 1.35 |
| 10-12 08:54 | +10 stop | SOL | DOWN | 0.50 | 0.65 | 1.19 |
| 10-12 08:54 | +10 | SOL | DOWN | 0.50 | 0.65 | 1.19 |
| 10-12 08:54 | +5 | SOL | DOWN | 0.50 | 0.65 | 1.16 |
| 10-12 08:54 | +10 stop | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-12 08:54 | +15 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-12 08:54 | +10 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-12 08:54 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-12 08:54 | +5 | XRP | DOWN | 0.43 | 0.61 | 1.45 |
| 10-12 08:54 | +10 | HYPE | DOWN | 0.60 | open |  |
| 10-12 08:54 | +5 | HYPE | DOWN | 0.60 | 0.69 | 0.58 |
| 10-12 08:53 | +10 stop | XRP | DOWN | 0.59 | 0.39 | -2.34 |
| 10-12 08:53 | +15 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 10-12 08:53 | +10 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 10-12 08:53 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 10-12 08:53 | +10 stop | DOGE | DOWN | 0.41 | 0.60 | 1.56 |
| 10-12 08:53 | +20 | DOGE | DOWN | 0.41 | 0.62 | 1.76 |
| 10-12 08:53 | +15 | DOGE | DOWN | 0.41 | 0.60 | 1.56 |
| 10-12 08:53 | +10 | DOGE | DOWN | 0.41 | 0.60 | 1.56 |
| 10-12 08:53 | +5 | DOGE | DOWN | 0.41 | 0.60 | 1.56 |
| 10-12 08:53 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.95 |
