# Range-Scalp Bot

*Updated Sun Oct 11 15:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12103 | 10445 | 1658 (24) | 5 | $-4009.05 | -5.2% |
| **+10¢** | 9196 | 7273 | 1923 (37) | 6 | $-3766.62 | -6.5% |
| **+15¢** | 7747 | 5705 | 2042 (54) | 6 | $-3211.62 | -6.6% |
| **+20¢** | 6899 | 4772 | 2127 (68) | 6 | $-2711.22 | -6.3% |
| **+10¢ (15¢ stop)** | 14925 | 14884 | 41 (25) | 0 | $-5889.07 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 15:23 | +10 stop | HYPE | DOWN | 0.70 | 0.46 | -2.77 |
| 10-11 15:23 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-11 15:23 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-11 15:23 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-11 15:22 | +10 stop | BTC | UP | 0.63 | 0.77 | 1.10 |
| 10-11 15:22 | +10 stop | ZEC | DOWN | 0.58 | 0.43 | -1.86 |
| 10-11 15:22 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-11 15:22 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-11 15:22 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-11 15:22 | +5 | ZEC | DOWN | 0.58 | open |  |
| 10-11 15:22 | +10 stop | ZEC | UP | 0.70 | 0.23 | -4.98 |
| 10-11 15:21 | +10 stop | BTC | UP | 0.65 | 0.50 | -1.84 |
| 10-11 15:20 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
| 10-11 15:20 | +10 | SOL | UP | 0.58 | 0.68 | 0.66 |
| 10-11 15:20 | +10 stop | BTC | UP | 0.55 | 0.68 | 0.96 |
| 10-11 15:20 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-11 15:19 | +5 | ZEC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-11 15:19 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-11 15:18 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 10-11 15:18 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-11 15:18 | +20 | SOL | UP | 0.56 | 0.84 | 2.52 |
| 10-11 15:18 | +15 | SOL | UP | 0.56 | 0.73 | 1.38 |
| 10-11 15:18 | +10 | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-11 15:18 | +5 | SOL | UP | 0.56 | 0.62 | 0.25 |
| 10-11 15:18 | +10 stop | BTC | DOWN | 0.59 | 0.39 | -2.34 |
| 10-11 15:18 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-11 15:18 | +5 | BTC | DOWN | 0.59 | open |  |
| 10-11 15:18 | +10 stop | ZEC | DOWN | 0.51 | 0.30 | -2.46 |
| 10-11 15:18 | +20 | ZEC | DOWN | 0.53 | 0.73 | 1.73 |
| 10-11 15:18 | +15 | ZEC | DOWN | 0.53 | 0.73 | 1.73 |
| 10-11 15:18 | +10 | ZEC | DOWN | 0.53 | 0.73 | 1.73 |
| 10-11 15:18 | +5 | ZEC | DOWN | 0.53 | 0.60 | 0.40 |
| 10-11 15:18 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-11 15:17 | +10 stop | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 10-11 15:17 | +10 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 10-11 15:17 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 10-11 15:17 | +10 | NEAR | UP | 0.71 | 0.88 | 1.47 |
| 10-11 15:17 | +10 stop | XRP | UP | 0.56 | 0.71 | 1.17 |
| 10-11 15:17 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-11 15:17 | +20 | DOGE | UP | 0.57 | 0.77 | 1.69 |
