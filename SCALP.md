# Range-Scalp Bot

*Updated Sun Nov 15 07:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60510 | 52785 | 7725 (107) | 0 | $-16451.94 | -4.3% |
| **+10¢** | 45210 | 36158 | 9052 (143) | 0 | $-15520.60 | -5.5% |
| **+15¢** | 37874 | 28108 | 9766 (181) | 0 | $-14206.71 | -6.0% |
| **+20¢** | 33759 | 23516 | 10243 (233) | 0 | $-12485.08 | -5.9% |
| **+10¢ (15¢ stop)** | 73664 | 73521 | 143 (82) | 0 | $-27119.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 06:55 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 11-15 06:55 | +20 | HYPE | UP | 0.70 | 0.96 | 2.44 |
| 11-15 06:55 | +15 | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 11-15 06:55 | +10 | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 11-15 06:55 | +5 | HYPE | UP | 0.70 | 0.78 | 0.52 |
| 11-15 06:54 | +10 stop | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-15 06:52 | +10 stop | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 11-15 06:51 | +10 stop | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-15 06:50 | +10 stop | ZEC | UP | 0.69 | 0.48 | -2.43 |
| 11-15 06:50 | +10 | XRP | UP | 0.51 | no | -5.28 |
| 11-15 06:50 | +5 | XRP | UP | 0.51 | no | -5.28 |
| 11-15 06:50 | +10 stop | NEAR | DOWN | 0.56 | 0.67 | 0.72 |
| 11-15 06:50 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 1.02 |
| 11-15 06:49 | +10 stop | XRP | UP | 0.71 | 0.55 | -1.93 |
| 11-15 06:49 | +10 stop | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 06:49 | +20 | SOL | DOWN | 0.56 | 0.82 | 2.31 |
| 11-15 06:49 | +15 | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 06:49 | +10 | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 11-15 06:49 | +5 | SOL | DOWN | 0.57 | 0.65 | 0.46 |
| 11-15 06:49 | +10 stop | BNB | DOWN | 0.53 | 0.73 | 1.68 |
| 11-15 06:49 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.05 |
| 11-15 06:48 | +10 stop | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 11-15 06:48 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-15 06:47 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 06:47 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-15 06:47 | +10 stop | XRP | DOWN | 0.59 | 0.43 | -1.95 |
| 11-15 06:47 | +10 stop | ZEC | DOWN | 0.67 | 0.47 | -2.34 |
| 11-15 06:47 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-15 06:47 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-15 06:47 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 06:47 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 06:47 | +5 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 06:47 | +10 stop | BNB | DOWN | 0.67 | 0.50 | -2.03 |
| 11-15 06:47 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.87 |
| 11-15 06:47 | +15 | BNB | DOWN | 0.67 | 0.84 | 1.45 |
| 11-15 06:47 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.72 |
| 11-15 06:47 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.31 |
| 11-15 06:46 | +20 | NEAR | DOWN | 0.71 | 0.93 | 1.96 |
| 11-15 06:46 | +10 stop | NEAR | DOWN | 0.71 | 0.52 | -2.23 |
| 11-15 06:46 | +15 | NEAR | DOWN | 0.71 | 0.88 | 1.47 |
