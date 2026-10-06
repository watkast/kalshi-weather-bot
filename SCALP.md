# Range-Scalp Bot

*Updated Tue Oct 06 04:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4634 | 4003 | 631 (6) | 1 | $-1517.31 | -5.2% |
| **+10¢** | 3564 | 2830 | 734 (9) | 1 | $-1407.30 | -6.3% |
| **+15¢** | 2994 | 2219 | 775 (12) | 2 | $-1205.49 | -6.4% |
| **+20¢** | 2688 | 1880 | 808 (17) | 2 | $-990.86 | -5.9% |
| **+10¢ (15¢ stop)** | 5686 | 5675 | 11 (6) | 0 | $-2064.81 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 04:06 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-06 04:05 | +10 stop | ETH | UP | 0.62 | 0.77 | 1.20 |
| 10-06 04:05 | +10 stop | NEAR | UP | 0.70 | 0.55 | -1.83 |
| 10-06 04:04 | +10 stop | DOGE | UP | 0.67 | 0.84 | 1.44 |
| 10-06 04:04 | +5 | DOGE | UP | 0.67 | 0.84 | 1.44 |
| 10-06 04:04 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.75 |
| 10-06 04:04 | +10 | BNB | UP | 0.63 | 0.74 | 0.75 |
| 10-06 04:04 | +5 | BNB | UP | 0.63 | 0.69 | 0.24 |
| 10-06 04:03 | +5 | SOL | UP | 0.64 | 0.79 | 1.20 |
| 10-06 04:03 | +10 stop | DOGE | UP | 0.50 | 0.66 | 1.26 |
| 10-06 04:02 | +10 stop | ETH | DOWN | 0.59 | 0.41 | -2.14 |
| 10-06 04:02 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-06 04:02 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-06 04:02 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-06 04:02 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-06 04:02 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 10-06 04:02 | +5 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-06 04:01 | +10 stop | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-06 04:01 | +20 | SOL | UP | 0.64 | 0.86 | 1.94 |
| 10-06 04:01 | +15 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-06 04:01 | +10 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-06 04:01 | +5 | SOL | UP | 0.64 | 0.71 | 0.38 |
| 10-06 04:01 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
| 10-06 04:01 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-06 04:01 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-06 04:01 | +10 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-06 04:01 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
| 10-06 04:01 | +10 stop | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-06 04:01 | +20 | BNB | UP | 0.62 | 0.86 | 2.14 |
| 10-06 04:01 | +15 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 10-06 04:01 | +10 | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-06 04:01 | +5 | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-06 04:01 | +10 stop | DOGE | UP | 0.64 | 0.45 | -2.21 |
| 10-06 04:01 | +20 | DOGE | UP | 0.64 | 0.88 | 2.14 |
| 10-06 04:01 | +15 | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 10-06 04:01 | +10 | DOGE | UP | 0.61 | 0.84 | 2.03 |
| 10-06 04:01 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 10-06 04:01 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 10-06 04:01 | +20 | HYPE | UP | 0.59 | 0.83 | 2.13 |
| 10-06 04:01 | +15 | HYPE | UP | 0.59 | 0.74 | 1.19 |
