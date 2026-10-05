# Range-Scalp Bot

*Updated Mon Oct 05 10:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3703 | 3184 | 519 (3) | 1 | $-1305.90 | -5.6% |
| **+10¢** | 2863 | 2266 | 597 (4) | 1 | $-1189.22 | -6.6% |
| **+15¢** | 2402 | 1774 | 628 (7) | 1 | $-1030.91 | -6.8% |
| **+20¢** | 2144 | 1490 | 654 (12) | 1 | $-870.92 | -6.5% |
| **+10¢ (15¢ stop)** | 4590 | 4589 | 1 (1) | 0 | $-1748.79 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 10:40 | +10 stop | BNB | UP | 0.56 | 0.70 | 1.07 |
| 10-05 10:39 | +10 stop | BNB | DOWN | 0.67 | 0.49 | -2.14 |
| 10-05 10:39 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-05 10:39 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-05 10:39 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-05 10:36 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 10-05 10:36 | +10 stop | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-05 10:36 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 10:36 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 10-05 10:36 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-05 10:36 | +10 stop | DOGE | DOWN | 0.66 | 0.43 | -2.60 |
| 10-05 10:36 | +20 | DOGE | DOWN | 0.66 | 0.89 | 2.11 |
| 10-05 10:36 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.37 |
| 10-05 10:36 | +10 | DOGE | DOWN | 0.66 | 0.82 | 1.38 |
| 10-05 10:36 | +5 | DOGE | DOWN | 0.66 | 0.82 | 1.38 |
| 10-05 10:36 | +10 stop | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 10-05 10:36 | +10 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 10-05 10:36 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-05 10:35 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-05 10:35 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 10:35 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-05 10:35 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-05 10:35 | +5 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-05 10:35 | +10 stop | ZEC | DOWN | 0.64 | 0.45 | -2.25 |
| 10-05 10:35 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-05 10:35 | +5 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-05 10:34 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 10-05 10:34 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-05 10:34 | +10 stop | NEAR | DOWN | 0.71 | 0.54 | -2.03 |
| 10-05 10:34 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 10-05 10:34 | +15 | NEAR | DOWN | 0.71 | 0.88 | 1.47 |
| 10-05 10:34 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 10-05 10:34 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-05 10:34 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 10:34 | +10 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 10-05 10:34 | +5 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 10-05 10:34 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 10:34 | +20 | XRP | DOWN | 0.70 | 0.94 | 2.15 |
| 10-05 10:34 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-05 10:34 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
