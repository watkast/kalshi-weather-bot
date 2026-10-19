# Range-Scalp Bot

*Updated Mon Oct 19 08:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23708 | 20612 | 3096 (31) | 1 | $-7082.90 | -4.7% |
| **+10¢** | 17834 | 14269 | 3565 (45) | 1 | $-6300.02 | -5.6% |
| **+15¢** | 14940 | 11101 | 3839 (67) | 1 | $-5707.15 | -6.1% |
| **+20¢** | 13223 | 9206 | 4017 (86) | 1 | $-5080.43 | -6.1% |
| **+10¢ (15¢ stop)** | 29178 | 29127 | 51 (30) | 0 | $-11025.95 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 07:47 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-19 07:47 | +10 | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-19 07:47 | +5 | BNB | DOWN | 0.64 | 0.72 | 0.48 |
| 10-19 07:47 | +10 stop | NEAR | DOWN | 0.61 | 0.85 | 2.14 |
| 10-19 07:46 | +10 stop | DOGE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-19 07:46 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-19 07:46 | +15 | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 10-19 07:46 | +10 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 10-19 07:46 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-19 07:46 | +10 stop | BNB | DOWN | 0.50 | 0.60 | 0.65 |
| 10-19 07:46 | +20 | BNB | DOWN | 0.49 | 0.72 | 1.97 |
| 10-19 07:46 | +15 | BNB | DOWN | 0.49 | 0.72 | 1.97 |
| 10-19 07:46 | +10 | BNB | DOWN | 0.49 | 0.60 | 0.70 |
| 10-19 07:46 | +5 | BNB | DOWN | 0.49 | 0.60 | 0.70 |
| 10-19 07:46 | +10 stop | NEAR | UP | 0.61 | 0.44 | -2.05 |
| 10-19 07:46 | +20 | NEAR | UP | 0.61 | open |  |
| 10-19 07:46 | +15 | NEAR | UP | 0.61 | open |  |
| 10-19 07:46 | +10 | NEAR | UP | 0.63 | open |  |
| 10-19 07:46 | +5 | NEAR | UP | 0.63 | open |  |
| 10-19 07:43 | +20 | BTC | UP | 0.61 | 0.87 | 2.35 |
| 10-19 07:43 | +15 | BTC | UP | 0.61 | 0.78 | 1.40 |
| 10-19 07:43 | +10 | BTC | UP | 0.61 | 0.78 | 1.40 |
| 10-19 07:43 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-19 07:43 | +10 stop | NEAR | UP | 0.49 | 0.64 | 1.15 |
| 10-19 07:43 | +15 | NEAR | UP | 0.49 | 0.64 | 1.15 |
| 10-19 07:43 | +10 | NEAR | UP | 0.49 | 0.64 | 1.15 |
| 10-19 07:43 | +5 | NEAR | UP | 0.49 | 0.64 | 1.15 |
| 10-19 07:43 | +10 stop | NEAR | DOWN | 0.21 | 0.60 | 3.61 |
| 10-19 07:43 | +15 | NEAR | DOWN | 0.21 | 0.60 | 3.61 |
| 10-19 07:43 | +10 | NEAR | DOWN | 0.21 | 0.60 | 3.61 |
| 10-19 07:43 | +5 | NEAR | DOWN | 0.21 | 0.60 | 3.61 |
| 10-19 07:42 | +10 stop | DOGE | DOWN | 0.60 | 0.26 | -3.71 |
| 10-19 07:42 | +5 | DOGE | DOWN | 0.60 | yes | -6.17 |
| 10-19 07:42 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 07:42 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 07:42 | +5 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 07:42 | +10 stop | DOGE | UP | 0.46 | 0.59 | 0.95 |
| 10-19 07:42 | +5 | DOGE | UP | 0.46 | 0.59 | 0.95 |
| 10-19 07:42 | +10 stop | XRP | DOWN | 0.65 | 0.28 | -4.01 |
| 10-19 07:42 | +20 | XRP | DOWN | 0.65 | yes | -6.66 |
