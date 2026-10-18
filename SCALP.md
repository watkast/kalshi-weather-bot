# Range-Scalp Bot

*Updated Sun Oct 18 10:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22431 | 19532 | 2899 (29) | 0 | $-6501.52 | -4.6% |
| **+10¢** | 16875 | 13525 | 3350 (43) | 1 | $-5778.48 | -5.4% |
| **+15¢** | 14128 | 10509 | 3619 (63) | 2 | $-5314.09 | -6.0% |
| **+20¢** | 12504 | 8714 | 3790 (81) | 3 | $-4745.74 | -6.0% |
| **+10¢ (15¢ stop)** | 27582 | 27532 | 50 (29) | 1 | $-10565.01 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 10:20 | +10 stop | SOL | UP | 0.54 | open |  |
| 10-18 10:20 | +5 | SOL | UP | 0.54 | 0.59 | 0.15 |
| 10-18 10:19 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-18 10:19 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-18 10:19 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-18 10:19 | +10 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-18 10:19 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-18 10:19 | +5 | HYPE | DOWN | 0.64 | 0.73 | 0.59 |
| 10-18 10:19 | +10 stop | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-18 10:19 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.87 |
| 10-18 10:18 | +5 | SOL | UP | 0.70 | 0.75 | 0.21 |
| 10-18 10:18 | +5 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-18 10:18 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-18 10:18 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-18 10:18 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-18 10:17 | +10 stop | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-18 10:17 | +10 | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-18 10:17 | +5 | ETH | DOWN | 0.53 | 0.62 | 0.55 |
| 10-18 10:17 | +5 | ZEC | DOWN | 0.50 | 0.57 | 0.34 |
| 10-18 10:17 | +10 stop | XRP | DOWN | 0.46 | 0.57 | 0.74 |
| 10-18 10:17 | +20 | XRP | DOWN | 0.47 | 0.72 | 2.17 |
| 10-18 10:17 | +15 | XRP | DOWN | 0.47 | 0.65 | 1.46 |
| 10-18 10:17 | +10 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 10-18 10:17 | +5 | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 10-18 10:16 | +10 stop | SOL | DOWN | 0.48 | 0.29 | -2.23 |
| 10-18 10:16 | +20 | SOL | DOWN | 0.47 | open |  |
| 10-18 10:16 | +15 | SOL | DOWN | 0.47 | open |  |
| 10-18 10:16 | +10 | SOL | DOWN | 0.47 | open |  |
| 10-18 10:16 | +5 | SOL | DOWN | 0.47 | 0.54 | 0.34 |
| 10-18 10:16 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-18 10:16 | +20 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-18 10:16 | +15 | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 10-18 10:16 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-18 10:16 | +5 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-18 10:16 | +10 stop | ZEC | DOWN | 0.52 | 0.62 | 0.65 |
| 10-18 10:16 | +20 | ZEC | DOWN | 0.52 | 0.75 | 1.98 |
| 10-18 10:16 | +15 | ZEC | DOWN | 0.52 | 0.69 | 1.37 |
| 10-18 10:16 | +10 | ZEC | DOWN | 0.52 | 0.62 | 0.65 |
| 10-18 10:16 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
| 10-18 10:16 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.66 |
