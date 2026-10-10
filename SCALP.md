# Range-Scalp Bot

*Updated Sat Oct 10 10:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10318 | 8894 | 1424 (22) | 0 | $-3531.50 | -5.4% |
| **+10¢** | 7804 | 6146 | 1658 (35) | 1 | $-3376.13 | -6.9% |
| **+15¢** | 6583 | 4825 | 1758 (51) | 1 | $-2856.72 | -6.9% |
| **+20¢** | 5852 | 4022 | 1830 (65) | 1 | $-2427.12 | -6.6% |
| **+10¢ (15¢ stop)** | 12667 | 12629 | 38 (25) | 1 | $-4957.85 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 10:50 | +10 stop | NEAR | DOWN | 0.61 | open |  |
| 10-10 10:50 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 10-10 10:49 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-10 10:49 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-10 10:49 | +5 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-10 10:47 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 10-10 10:47 | +10 stop | NEAR | UP | 0.65 | 0.49 | -1.94 |
| 10-10 10:47 | +20 | NEAR | UP | 0.65 | open |  |
| 10-10 10:47 | +15 | NEAR | UP | 0.65 | open |  |
| 10-10 10:47 | +10 | NEAR | UP | 0.65 | open |  |
| 10-10 10:47 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 10-10 10:46 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.77 |
| 10-10 10:46 | +20 | BNB | UP | 0.55 | 0.76 | 1.80 |
| 10-10 10:46 | +15 | BNB | UP | 0.55 | 0.71 | 1.28 |
| 10-10 10:46 | +10 | BNB | UP | 0.55 | 0.66 | 0.77 |
| 10-10 10:46 | +5 | BNB | UP | 0.55 | 0.62 | 0.36 |
| 10-10 10:46 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.77 |
| 10-10 10:46 | +20 | DOGE | UP | 0.63 | 0.84 | 1.81 |
| 10-10 10:46 | +15 | DOGE | UP | 0.63 | 0.79 | 1.29 |
| 10-10 10:46 | +10 | DOGE | UP | 0.63 | 0.74 | 0.78 |
| 10-10 10:46 | +5 | DOGE | UP | 0.63 | 0.74 | 0.78 |
| 10-10 10:46 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-10 10:46 | +20 | BTC | UP | 0.70 | 0.91 | 1.88 |
| 10-10 10:46 | +15 | BTC | UP | 0.70 | 0.91 | 1.88 |
| 10-10 10:46 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-10 10:46 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-10 10:46 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-10 10:46 | +20 | ZEC | UP | 0.68 | 0.88 | 1.76 |
| 10-10 10:46 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-10 10:46 | +10 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-10 10:46 | +5 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-10 10:44 | +10 stop | SOL | DOWN | 0.67 | no | 3.14 |
| 10-10 10:44 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-10 10:43 | +10 stop | NEAR | UP | 0.64 | 0.46 | -2.15 |
| 10-10 10:43 | +5 | NEAR | UP | 0.63 | no | -6.47 |
| 10-10 10:42 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 10:41 | +10 stop | BTC | UP | 0.57 | 0.12 | -4.76 |
| 10-10 10:41 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 10:41 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 10-10 10:41 | +10 stop | SOL | UP | 0.66 | 0.41 | -2.83 |
