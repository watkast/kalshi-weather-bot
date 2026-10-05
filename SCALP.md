# Range-Scalp Bot

*Updated Mon Oct 05 17:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4048 | 3479 | 569 (4) | 2 | $-1456.94 | -5.7% |
| **+10¢** | 3129 | 2474 | 655 (5) | 3 | $-1336.22 | -6.8% |
| **+15¢** | 2630 | 1941 | 689 (8) | 4 | $-1141.86 | -6.9% |
| **+20¢** | 2349 | 1631 | 718 (13) | 4 | $-976.48 | -6.6% |
| **+10¢ (15¢ stop)** | 4983 | 4978 | 5 (2) | 1 | $-1826.03 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 17:37 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 10-05 17:36 | +10 stop | ZEC | UP | 0.67 | 0.48 | -2.24 |
| 10-05 17:36 | +10 stop | DOGE | DOWN | 0.62 | open |  |
| 10-05 17:36 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-05 17:35 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-05 17:35 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 10-05 17:34 | +10 stop | SOL | DOWN | 0.63 | 0.45 | -2.15 |
| 10-05 17:34 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 17:34 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-05 17:34 | +10 stop | ETH | DOWN | 0.68 | 0.44 | -2.74 |
| 10-05 17:34 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-05 17:34 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 10-05 17:34 | +10 stop | HYPE | DOWN | 0.67 | 0.50 | -2.04 |
| 10-05 17:34 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-05 17:34 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-05 17:34 | +5 | ZEC | UP | 0.58 | 0.68 | 0.62 |
| 10-05 17:34 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-05 17:34 | +15 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-05 17:34 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-05 17:34 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-05 17:33 | +5 | ZEC | DOWN | 0.58 | 0.64 | 0.25 |
| 10-05 17:33 | +10 stop | DOGE | DOWN | 0.69 | 0.53 | -1.93 |
| 10-05 17:32 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 17:32 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-05 17:32 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-05 17:32 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-05 17:32 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.68 |
| 10-05 17:32 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.15 |
| 10-05 17:32 | +20 | ZEC | DOWN | 0.55 | open |  |
| 10-05 17:32 | +15 | ZEC | DOWN | 0.55 | open |  |
| 10-05 17:32 | +10 | ZEC | DOWN | 0.55 | open |  |
| 10-05 17:32 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-05 17:31 | +10 stop | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-05 17:31 | +20 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-05 17:31 | +15 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-05 17:31 | +10 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-05 17:31 | +5 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-05 17:31 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.07 |
| 10-05 17:31 | +20 | DOGE | DOWN | 0.63 | open |  |
| 10-05 17:31 | +15 | DOGE | DOWN | 0.63 | open |  |
