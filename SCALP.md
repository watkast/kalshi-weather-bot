# Range-Scalp Bot

*Updated Wed Nov 18 02:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63460 | 55342 | 8118 (118) | 0 | $-17381.95 | -4.4% |
| **+10¢** | 47404 | 37904 | 9500 (159) | 0 | $-16302.46 | -5.5% |
| **+15¢** | 39744 | 29500 | 10244 (203) | 0 | $-14796.37 | -5.9% |
| **+20¢** | 35406 | 24656 | 10750 (258) | 0 | $-13060.57 | -5.9% |
| **+10¢ (15¢ stop)** | 77237 | 77079 | 158 (93) | 0 | $-28443.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 02:10 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-18 02:09 | +10 stop | XRP | DOWN | 0.69 | 0.45 | -2.73 |
| 11-18 02:09 | +20 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 02:09 | +15 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 02:09 | +10 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 02:09 | +5 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 02:08 | +10 stop | DOGE | DOWN | 0.59 | 0.37 | -2.54 |
| 11-18 02:08 | +15 | DOGE | DOWN | 0.60 | yes | -6.17 |
| 11-18 02:08 | +10 | DOGE | DOWN | 0.60 | yes | -6.17 |
| 11-18 02:08 | +5 | DOGE | DOWN | 0.62 | yes | -6.36 |
| 11-18 02:08 | +15 | ZEC | DOWN | 0.65 | yes | -6.66 |
| 11-18 02:07 | +10 | ZEC | DOWN | 0.71 | yes | -7.25 |
| 11-18 02:07 | +15 | BNB | DOWN | 0.71 | yes | -7.25 |
| 11-18 02:07 | +10 stop | BTC | DOWN | 0.64 | 0.36 | -3.14 |
| 11-18 02:07 | +10 | BTC | DOWN | 0.63 | yes | -6.47 |
| 11-18 02:07 | +10 stop | BNB | DOWN | 0.66 | 0.49 | -2.04 |
| 11-18 02:07 | +10 | BNB | DOWN | 0.66 | yes | -6.76 |
| 11-18 02:07 | +5 | BNB | DOWN | 0.66 | yes | -6.76 |
| 11-18 02:07 | +10 stop | ZEC | DOWN | 0.66 | 0.45 | -2.44 |
| 11-18 02:06 | +10 stop | BNB | UP | 0.41 | 0.58 | 1.35 |
| 11-18 02:06 | +10 | BNB | UP | 0.41 | 0.58 | 1.35 |
| 11-18 02:06 | +5 | BNB | UP | 0.41 | 0.58 | 1.35 |
| 11-18 02:06 | +10 | BTC | UP | 0.49 | 0.64 | 1.15 |
| 11-18 02:06 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-18 02:06 | +15 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-18 02:06 | +10 | HYPE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-18 02:06 | +5 | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-18 02:06 | +10 stop | DOGE | UP | 0.68 | 0.51 | -2.04 |
| 11-18 02:06 | +5 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-18 02:05 | +10 stop | ZEC | UP | 0.68 | 0.49 | -2.24 |
| 11-18 02:05 | +10 stop | NEAR | DOWN | 0.58 | 0.75 | 1.40 |
| 11-18 02:05 | +20 | NEAR | DOWN | 0.47 | 0.75 | 2.48 |
| 11-18 02:05 | +15 | NEAR | DOWN | 0.47 | 0.65 | 1.46 |
| 11-18 02:05 | +10 | NEAR | DOWN | 0.47 | 0.65 | 1.46 |
| 11-18 02:05 | +5 | NEAR | DOWN | 0.47 | 0.54 | 0.34 |
| 11-18 02:05 | +10 stop | BTC | UP | 0.58 | 0.38 | -2.35 |
| 11-18 02:05 | +20 | BTC | UP | 0.58 | 0.79 | 1.80 |
| 11-18 02:05 | +15 | BTC | UP | 0.57 | 0.79 | 1.90 |
| 11-18 02:05 | +10 | BTC | UP | 0.53 | 0.67 | 1.06 |
| 11-18 02:05 | +5 | BTC | UP | 0.53 | 0.61 | 0.45 |
