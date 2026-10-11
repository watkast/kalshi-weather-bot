# Range-Scalp Bot

*Updated Sun Oct 11 06:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11517 | 9930 | 1587 (24) | 1 | $-3905.60 | -5.4% |
| **+10¢** | 8727 | 6882 | 1845 (37) | 1 | $-3720.06 | -6.8% |
| **+15¢** | 7357 | 5405 | 1952 (53) | 1 | $-3148.12 | -6.8% |
| **+20¢** | 6557 | 4527 | 2030 (67) | 1 | $-2622.57 | -6.4% |
| **+10¢ (15¢ stop)** | 14190 | 14149 | 41 (25) | 0 | $-5664.12 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 06:50 | +10 stop | NEAR | DOWN | 0.69 | 0.38 | -3.42 |
| 10-11 06:50 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-11 06:50 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-11 06:46 | +10 stop | BNB | UP | 0.70 | 0.83 | 1.05 |
| 10-11 06:46 | +20 | BNB | UP | 0.70 | 0.90 | 1.78 |
| 10-11 06:46 | +15 | BNB | UP | 0.70 | 0.86 | 1.36 |
| 10-11 06:46 | +10 | BNB | UP | 0.70 | 0.83 | 1.05 |
| 10-11 06:46 | +5 | BNB | UP | 0.70 | 0.83 | 1.05 |
| 10-11 06:46 | +10 stop | SOL | UP | 0.71 | 0.85 | 1.16 |
| 10-11 06:46 | +20 | SOL | UP | 0.71 | 0.92 | 1.84 |
| 10-11 06:46 | +15 | SOL | UP | 0.69 | 0.85 | 1.36 |
| 10-11 06:46 | +10 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-11 06:46 | +5 | SOL | UP | 0.70 | 0.76 | 0.32 |
| 10-11 06:46 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-11 06:46 | +20 | NEAR | UP | 0.61 | open |  |
| 10-11 06:46 | +15 | NEAR | UP | 0.61 | open |  |
| 10-11 06:46 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-11 06:46 | +5 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-11 06:46 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-11 06:46 | +20 | XRP | UP | 0.69 | 0.89 | 1.78 |
| 10-11 06:46 | +15 | XRP | UP | 0.69 | 0.88 | 1.67 |
| 10-11 06:46 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-11 06:46 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 10-11 06:46 | +10 stop | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 10-11 06:46 | +20 | ZEC | UP | 0.65 | 0.93 | 2.55 |
| 10-11 06:46 | +15 | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 10-11 06:46 | +10 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 10-11 06:46 | +5 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 10-11 06:39 | +10 stop | NEAR | UP | 0.69 | 0.52 | -2.03 |
| 10-11 06:39 | +10 | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 10-11 06:39 | +5 | NEAR | UP | 0.69 | 0.75 | 0.31 |
| 10-11 06:39 | +10 stop | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-11 06:37 | +10 stop | HYPE | DOWN | 0.70 | 0.51 | -2.23 |
| 10-11 06:37 | +10 | HYPE | DOWN | 0.70 | yes | -7.15 |
| 10-11 06:37 | +5 | HYPE | DOWN | 0.70 | yes | -7.15 |
| 10-11 06:37 | +10 stop | BNB | UP | 0.59 | 0.77 | 1.50 |
| 10-11 06:37 | +15 | BNB | UP | 0.59 | 0.77 | 1.50 |
| 10-11 06:37 | +10 | BNB | UP | 0.59 | 0.77 | 1.50 |
| 10-11 06:37 | +5 | BNB | UP | 0.59 | 0.66 | 0.37 |
| 10-11 06:37 | +10 stop | ZEC | UP | 0.56 | 0.81 | 2.21 |
