# Range-Scalp Bot

*Updated Tue Nov 10 21:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54935 | 47914 | 7021 (94) | 1 | $-14975.46 | -4.3% |
| **+10¢** | 41048 | 32859 | 8189 (124) | 1 | $-13876.99 | -5.4% |
| **+15¢** | 34412 | 25589 | 8823 (158) | 2 | $-12586.85 | -5.8% |
| **+20¢** | 30630 | 21373 | 9257 (207) | 3 | $-11012.54 | -5.7% |
| **+10¢ (15¢ stop)** | 66928 | 66810 | 118 (73) | 0 | $-24745.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 21:42 | +10 stop | ZEC | DOWN | 0.51 | 0.73 | 1.88 |
| 11-10 21:42 | +20 | ZEC | DOWN | 0.51 | 0.73 | 1.88 |
| 11-10 21:42 | +15 | ZEC | DOWN | 0.50 | 0.73 | 1.98 |
| 11-10 21:42 | +10 | ZEC | DOWN | 0.52 | 0.73 | 1.78 |
| 11-10 21:42 | +5 | ZEC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-10 21:39 | +10 stop | XRP | DOWN | 0.58 | 0.28 | -3.33 |
| 11-10 21:37 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.81 |
| 11-10 21:37 | +10 | HYPE | UP | 0.70 | 0.81 | 0.81 |
| 11-10 21:37 | +5 | HYPE | UP | 0.70 | 0.76 | 0.29 |
| 11-10 21:36 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 11-10 21:35 | +10 stop | XRP | DOWN | 0.63 | 0.48 | -1.85 |
| 11-10 21:35 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-10 21:35 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-10 21:35 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-10 21:35 | +10 stop | ZEC | UP | 0.58 | 0.73 | 1.18 |
| 11-10 21:35 | +20 | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 11-10 21:35 | +10 | ZEC | UP | 0.59 | 0.73 | 1.09 |
| 11-10 21:35 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 11-10 21:35 | +5 | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 11-10 21:35 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.75 |
| 11-10 21:35 | +15 | BNB | DOWN | 0.70 | 0.88 | 1.57 |
| 11-10 21:35 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-10 21:35 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-10 21:35 | +10 stop | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 11-10 21:35 | +20 | ETH | DOWN | 0.68 | 0.90 | 1.97 |
| 11-10 21:35 | +15 | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 11-10 21:35 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 11-10 21:35 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 11-10 21:35 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-10 21:34 | +10 stop | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-10 21:34 | +15 | HYPE | UP | 0.52 | 0.68 | 1.26 |
| 11-10 21:34 | +10 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-10 21:34 | +5 | HYPE | UP | 0.52 | 0.65 | 0.92 |
| 11-10 21:34 | +10 stop | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-10 21:34 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-10 21:34 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 11-10 21:34 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-10 21:34 | +10 stop | DOGE | UP | 0.61 | 0.78 | 1.40 |
| 11-10 21:34 | +20 | DOGE | UP | 0.61 | 0.81 | 1.72 |
| 11-10 21:34 | +15 | DOGE | UP | 0.61 | 0.78 | 1.40 |
