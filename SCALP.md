# Range-Scalp Bot

*Updated Mon Oct 05 12:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3808 | 3279 | 529 (3) | 0 | $-1314.07 | -5.5% |
| **+10¢** | 2950 | 2341 | 609 (4) | 0 | $-1182.61 | -6.4% |
| **+15¢** | 2479 | 1839 | 640 (7) | 0 | $-1005.11 | -6.5% |
| **+20¢** | 2214 | 1546 | 668 (12) | 0 | $-841.91 | -6.1% |
| **+10¢ (15¢ stop)** | 4708 | 4707 | 1 (1) | 0 | $-1739.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 12:36 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-05 12:36 | +10 stop | DOGE | DOWN | 0.58 | 0.83 | 2.22 |
| 10-05 12:36 | +10 | DOGE | DOWN | 0.58 | 0.83 | 2.22 |
| 10-05 12:36 | +5 | DOGE | DOWN | 0.58 | 0.65 | 0.36 |
| 10-05 12:35 | +10 stop | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 10-05 12:35 | +15 | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 10-05 12:35 | +10 | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 10-05 12:35 | +5 | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 10-05 12:35 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-05 12:35 | +15 | SOL | DOWN | 0.63 | 0.89 | 2.36 |
| 10-05 12:35 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-05 12:35 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-05 12:35 | +10 stop | DOGE | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 12:35 | +15 | DOGE | DOWN | 0.53 | 0.83 | 2.72 |
| 10-05 12:35 | +10 | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 10-05 12:35 | +5 | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 10-05 12:35 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-05 12:35 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 12:35 | +10 | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-05 12:35 | +5 | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-05 12:34 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-05 12:32 | +10 stop | HYPE | DOWN | 0.61 | 0.44 | -2.05 |
| 10-05 12:32 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-05 12:32 | +5 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-05 12:31 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 12:31 | +20 | DOGE | DOWN | 0.60 | 0.83 | 2.03 |
| 10-05 12:31 | +15 | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 12:31 | +10 | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 12:31 | +5 | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 12:31 | +10 stop | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 10-05 12:31 | +20 | SOL | DOWN | 0.70 | 0.94 | 2.26 |
| 10-05 12:31 | +15 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 10-05 12:31 | +10 | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 10-05 12:31 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-05 12:31 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-05 12:31 | +20 | XRP | DOWN | 0.64 | 0.88 | 2.15 |
| 10-05 12:31 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-05 12:31 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-05 12:31 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 10-05 12:31 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
