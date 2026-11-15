# Range-Scalp Bot

*Updated Sun Nov 15 04:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60348 | 52634 | 7714 (107) | 5 | $-16471.14 | -4.3% |
| **+10¢** | 45086 | 36047 | 9039 (143) | 5 | $-15561.20 | -5.5% |
| **+15¢** | 37766 | 28019 | 9747 (181) | 6 | $-14232.06 | -6.0% |
| **+20¢** | 33661 | 23435 | 10226 (233) | 7 | $-12552.80 | -5.9% |
| **+10¢ (15¢ stop)** | 73483 | 73340 | 143 (82) | 3 | $-27082.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 04:24 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 11-15 04:24 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-15 04:24 | +10 stop | SOL | DOWN | 0.67 | open |  |
| 11-15 04:24 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-15 04:24 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-15 04:24 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 11-15 04:24 | +5 | DOGE | DOWN | 0.67 | open |  |
| 11-15 04:24 | +10 stop | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-15 04:23 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-15 04:23 | +20 | XRP | UP | 0.67 | open |  |
| 11-15 04:23 | +15 | XRP | UP | 0.67 | open |  |
| 11-15 04:23 | +10 | XRP | UP | 0.66 | 0.80 | 1.12 |
| 11-15 04:23 | +5 | XRP | UP | 0.66 | 0.75 | 0.60 |
| 11-15 04:23 | +5 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-15 04:23 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-15 04:23 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-15 04:23 | +10 stop | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-15 04:23 | +10 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-15 04:23 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 11-15 04:22 | +10 stop | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-15 04:22 | +5 | BTC | DOWN | 0.55 | 0.63 | 0.45 |
| 11-15 04:22 | +5 | BNB | UP | 0.63 | open |  |
| 11-15 04:21 | +10 stop | BNB | UP | 0.58 | 0.34 | -2.74 |
| 11-15 04:21 | +10 | BNB | UP | 0.58 | open |  |
| 11-15 04:21 | +5 | BNB | UP | 0.58 | 0.63 | 0.15 |
| 11-15 04:21 | +10 stop | BTC | UP | 0.56 | 0.40 | -1.95 |
| 11-15 04:21 | +10 | BTC | UP | 0.56 | open |  |
| 11-15 04:21 | +5 | BTC | UP | 0.56 | 0.62 | 0.25 |
| 11-15 04:21 | +10 stop | ETH | UP | 0.53 | 0.28 | -2.83 |
| 11-15 04:21 | +10 stop | DOGE | UP | 0.59 | 0.36 | -2.64 |
| 11-15 04:21 | +10 | DOGE | UP | 0.59 | open |  |
| 11-15 04:21 | +5 | ETH | UP | 0.57 | open |  |
| 11-15 04:21 | +10 stop | ZEC | UP | 0.64 | 0.39 | -2.84 |
| 11-15 04:20 | +10 stop | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 11-15 04:20 | +5 | ETH | DOWN | 0.53 | 0.60 | 0.35 |
| 11-15 04:20 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-15 04:19 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 11-15 04:19 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 11-15 04:19 | +5 | DOGE | DOWN | 0.59 | 0.64 | 0.16 |
| 11-15 04:19 | +10 stop | ETH | DOWN | 0.60 | 0.38 | -2.54 |
