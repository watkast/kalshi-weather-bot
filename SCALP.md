# Range-Scalp Bot

*Updated Tue Nov 17 17:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63088 | 55033 | 8055 (117) | 1 | $-17163.33 | -4.3% |
| **+10¢** | 47127 | 37705 | 9422 (159) | 1 | $-16012.16 | -5.4% |
| **+15¢** | 39501 | 29341 | 10160 (201) | 4 | $-14525.67 | -5.9% |
| **+20¢** | 35198 | 24539 | 10659 (256) | 5 | $-12737.25 | -5.8% |
| **+10¢ (15¢ stop)** | 76768 | 76612 | 156 (92) | 0 | $-28287.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 17:38 | +10 stop | NEAR | UP | 0.45 | 0.59 | 1.05 |
| 11-17 17:38 | +10 stop | ZEC | UP | 0.47 | 0.32 | -1.84 |
| 11-17 17:37 | +10 stop | BNB | UP | 0.59 | 0.32 | -3.03 |
| 11-17 17:37 | +5 | BNB | UP | 0.59 | open |  |
| 11-17 17:37 | +5 | BTC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-17 17:37 | +10 stop | XRP | UP | 0.55 | 0.34 | -2.44 |
| 11-17 17:37 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
| 11-17 17:37 | +10 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 11-17 17:37 | +5 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 11-17 17:36 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 11-17 17:36 | +5 | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 11-17 17:36 | +5 | HYPE | DOWN | 0.55 | 0.62 | 0.35 |
| 11-17 17:36 | +10 | DOGE | UP | 0.56 | 0.69 | 0.97 |
| 11-17 17:36 | +5 | DOGE | UP | 0.56 | 0.63 | 0.35 |
| 11-17 17:36 | +10 stop | DOGE | UP | 0.53 | 0.65 | 0.84 |
| 11-17 17:36 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-17 17:36 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 11-17 17:36 | +15 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 11-17 17:36 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-17 17:36 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 11-17 17:36 | +10 stop | XRP | DOWN | 0.65 | 0.48 | -2.04 |
| 11-17 17:36 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-17 17:36 | +15 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 17:36 | +10 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 17:36 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-17 17:35 | +10 stop | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-17 17:35 | +5 | HYPE | DOWN | 0.52 | 0.59 | 0.35 |
| 11-17 17:34 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 11-17 17:34 | +10 stop | SOL | DOWN | 0.63 | 0.79 | 1.32 |
| 11-17 17:34 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-17 17:34 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 11-17 17:34 | +10 stop | ZEC | DOWN | 0.67 | 0.49 | -2.14 |
| 11-17 17:34 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-17 17:34 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-17 17:33 | +10 stop | DOGE | DOWN | 0.66 | 0.48 | -2.14 |
| 11-17 17:33 | +10 stop | NEAR | DOWN | 0.64 | 0.39 | -2.84 |
| 11-17 17:33 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-17 17:33 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-17 17:33 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-17 17:33 | +5 | NEAR | DOWN | 0.62 | 0.71 | 0.58 |
