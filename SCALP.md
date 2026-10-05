# Range-Scalp Bot

*Updated Mon Oct 05 23:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4308 | 3710 | 598 (6) | 0 | $-1484.69 | -5.5% |
| **+10¢** | 3324 | 2631 | 693 (9) | 0 | $-1360.58 | -6.5% |
| **+15¢** | 2788 | 2056 | 732 (12) | 0 | $-1183.24 | -6.8% |
| **+20¢** | 2493 | 1730 | 763 (17) | 0 | $-1013.00 | -6.5% |
| **+10¢ (15¢ stop)** | 5293 | 5282 | 11 (6) | 0 | $-1891.91 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 23:09 | +10 stop | HYPE | DOWN | 0.52 | 0.85 | 3.03 |
| 10-05 23:07 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-05 23:07 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 10-05 23:07 | +15 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 10-05 23:07 | +10 | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-05 23:07 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-05 23:07 | +5 | HYPE | DOWN | 0.62 | 0.85 | 2.04 |
| 10-05 23:07 | +10 stop | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-05 23:07 | +15 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-05 23:07 | +10 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-05 23:07 | +5 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-05 23:07 | +10 stop | HYPE | DOWN | 0.69 | 0.52 | -2.03 |
| 10-05 23:07 | +10 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-05 23:06 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.19 |
| 10-05 23:05 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.83 |
| 10-05 23:03 | +10 stop | SOL | DOWN | 0.50 | 0.71 | 1.77 |
| 10-05 23:03 | +20 | SOL | DOWN | 0.50 | 0.71 | 1.77 |
| 10-05 23:03 | +15 | SOL | DOWN | 0.50 | 0.71 | 1.77 |
| 10-05 23:03 | +10 | SOL | DOWN | 0.50 | 0.71 | 1.77 |
| 10-05 23:03 | +5 | SOL | DOWN | 0.50 | 0.55 | 0.14 |
| 10-05 23:03 | +10 stop | ZEC | DOWN | 0.55 | 0.31 | -2.73 |
| 10-05 23:03 | +5 | ZEC | DOWN | 0.55 | 0.95 | 3.79 |
| 10-05 23:03 | +10 stop | DOGE | UP | 0.66 | 0.78 | 0.87 |
| 10-05 23:03 | +20 | DOGE | UP | 0.66 | 0.94 | 2.52 |
| 10-05 23:03 | +15 | DOGE | UP | 0.66 | 0.82 | 1.29 |
| 10-05 23:03 | +10 | DOGE | UP | 0.66 | 0.78 | 0.87 |
| 10-05 23:03 | +5 | DOGE | UP | 0.66 | 0.72 | 0.25 |
| 10-05 23:03 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.68 |
| 10-05 23:03 | +10 | HYPE | DOWN | 0.55 | 0.65 | 0.68 |
| 10-05 23:03 | +5 | HYPE | DOWN | 0.55 | 0.61 | 0.27 |
| 10-05 23:03 | +10 stop | XRP | UP | 0.64 | 0.77 | 1.00 |
| 10-05 23:03 | +15 | XRP | UP | 0.64 | 0.86 | 1.94 |
| 10-05 23:03 | +10 | XRP | UP | 0.64 | 0.77 | 1.00 |
| 10-05 23:03 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 10-05 23:03 | +5 | BNB | UP | 0.64 | 0.72 | 0.48 |
| 10-05 23:02 | +10 stop | HYPE | UP | 0.44 | 0.55 | 0.74 |
| 10-05 23:02 | +20 | HYPE | UP | 0.44 | no | -4.58 |
| 10-05 23:02 | +15 | HYPE | UP | 0.44 | no | -4.58 |
| 10-05 23:02 | +10 | HYPE | UP | 0.44 | 0.55 | 0.74 |
| 10-05 23:02 | +5 | HYPE | UP | 0.44 | 0.55 | 0.74 |
