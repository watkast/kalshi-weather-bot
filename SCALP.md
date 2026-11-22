# Range-Scalp Bot

*Updated Sun Nov 22 22:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69151 | 60336 | 8815 (145) | 0 | $-18633.19 | -4.3% |
| **+10¢** | 51606 | 41314 | 10292 (188) | 0 | $-17279.16 | -5.3% |
| **+15¢** | 43251 | 32158 | 11093 (241) | 0 | $-15486.79 | -5.7% |
| **+20¢** | 38517 | 26859 | 11658 (300) | 0 | $-13774.94 | -5.7% |
| **+10¢ (15¢ stop)** | 84219 | 84030 | 189 (117) | 0 | $-31042.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 21:58 | +10 stop | SOL | DOWN | 0.44 | 0.54 | 0.64 |
| 11-22 21:56 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-22 21:55 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-22 21:55 | +5 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-22 21:54 | +10 stop | SOL | DOWN | 0.71 | 0.32 | -4.21 |
| 11-22 21:53 | +10 stop | XRP | DOWN | 0.62 | 0.79 | 1.41 |
| 11-22 21:52 | +10 stop | XRP | UP | 0.67 | 0.42 | -2.84 |
| 11-22 21:52 | +5 | XRP | UP | 0.67 | no | -6.86 |
| 11-22 21:50 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.11 |
| 11-22 21:49 | +10 stop | XRP | UP | 0.54 | 0.70 | 1.27 |
| 11-22 21:49 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-22 21:48 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.95 |
| 11-22 21:48 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-22 21:48 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-22 21:48 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-22 21:48 | +10 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-22 21:48 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-22 21:47 | +10 stop | BNB | DOWN | 0.59 | 0.86 | 2.44 |
| 11-22 21:47 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-22 21:47 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 11-22 21:47 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-22 21:47 | +20 | DOGE | DOWN | 0.57 | 0.82 | 2.21 |
| 11-22 21:47 | +15 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 11-22 21:47 | +10 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-22 21:47 | +5 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-22 21:46 | +10 stop | ZEC | UP | 0.61 | 0.75 | 1.09 |
| 11-22 21:46 | +10 stop | SOL | DOWN | 0.62 | 0.44 | -2.15 |
| 11-22 21:46 | +20 | SOL | DOWN | 0.62 | no | 3.63 |
| 11-22 21:46 | +15 | SOL | DOWN | 0.62 | no | 3.63 |
| 11-22 21:46 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-22 21:46 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 11-22 21:46 | +10 stop | NEAR | DOWN | 0.70 | 0.48 | -2.53 |
| 11-22 21:46 | +20 | NEAR | DOWN | 0.70 | 0.92 | 1.94 |
| 11-22 21:46 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-22 21:46 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 21:46 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 11-22 21:46 | +10 stop | BTC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-22 21:46 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.93 |
| 11-22 21:46 | +15 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
| 11-22 21:46 | +10 | BTC | DOWN | 0.71 | 0.89 | 1.58 |
