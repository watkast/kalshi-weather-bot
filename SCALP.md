# Range-Scalp Bot

*Updated Thu Nov 12 13:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56936 | 49635 | 7301 (101) | 1 | $-15648.02 | -4.4% |
| **+10¢** | 42548 | 34032 | 8516 (133) | 3 | $-14571.30 | -5.4% |
| **+15¢** | 35673 | 26506 | 9167 (167) | 3 | $-13179.38 | -5.9% |
| **+20¢** | 31781 | 22163 | 9618 (217) | 3 | $-11553.48 | -5.8% |
| **+10¢ (15¢ stop)** | 69402 | 69274 | 128 (78) | 0 | $-25633.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 13:08 | +10 stop | BTC | UP | 0.50 | 0.62 | 0.85 |
| 11-12 13:07 | +10 stop | NEAR | DOWN | 0.36 | 0.66 | 2.67 |
| 11-12 13:07 | +10 | NEAR | DOWN | 0.30 | 0.66 | 3.29 |
| 11-12 13:07 | +5 | NEAR | DOWN | 0.30 | 0.66 | 3.29 |
| 11-12 13:07 | +10 stop | BNB | DOWN | 0.55 | 0.23 | -3.51 |
| 11-12 13:07 | +5 | BNB | DOWN | 0.55 | 0.92 | 3.47 |
| 11-12 13:05 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 11-12 13:05 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-12 13:05 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 11-12 13:04 | +5 | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-12 13:04 | +5 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-12 13:04 | +10 stop | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-12 13:04 | +10 stop | NEAR | DOWN | 0.49 | 0.65 | 1.26 |
| 11-12 13:04 | +5 | NEAR | DOWN | 0.49 | 0.57 | 0.44 |
| 11-12 13:03 | +10 stop | BNB | UP | 0.61 | 0.42 | -2.25 |
| 11-12 13:03 | +10 | BNB | UP | 0.61 | 0.76 | 1.20 |
| 11-12 13:03 | +5 | BNB | UP | 0.61 | 0.69 | 0.48 |
| 11-12 13:03 | +10 stop | NEAR | UP | 0.42 | 0.57 | 1.14 |
| 11-12 13:03 | +5 | NEAR | UP | 0.46 | 0.57 | 0.74 |
| 11-12 13:03 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 13:03 | +20 | ZEC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-12 13:03 | +15 | ZEC | DOWN | 0.62 | 0.81 | 1.62 |
| 11-12 13:03 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 13:03 | +5 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 13:03 | +10 stop | BTC | UP | 0.58 | 0.37 | -2.45 |
| 11-12 13:03 | +20 | BTC | UP | 0.58 | open |  |
| 11-12 13:03 | +15 | BTC | UP | 0.59 | open |  |
| 11-12 13:03 | +10 | BTC | UP | 0.59 | open |  |
| 11-12 13:03 | +5 | BTC | UP | 0.59 | open |  |
| 11-12 13:03 | +10 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-12 13:02 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 13:02 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-12 13:02 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-12 13:02 | +10 stop | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-12 13:02 | +20 | BNB | UP | 0.55 | 0.76 | 1.79 |
| 11-12 13:02 | +15 | BNB | UP | 0.55 | 0.76 | 1.79 |
| 11-12 13:02 | +10 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-12 13:02 | +5 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 11-12 13:01 | +10 stop | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-12 13:01 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
