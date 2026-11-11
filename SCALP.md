# Range-Scalp Bot

*Updated Wed Nov 11 21:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56255 | 49063 | 7192 (95) | 1 | $-15342.21 | -4.3% |
| **+10¢** | 42039 | 33646 | 8393 (125) | 1 | $-14301.21 | -5.4% |
| **+15¢** | 35248 | 26205 | 9043 (159) | 4 | $-12970.50 | -5.9% |
| **+20¢** | 31401 | 21913 | 9488 (209) | 4 | $-11321.63 | -5.8% |
| **+10¢ (15¢ stop)** | 68554 | 68433 | 121 (73) | 0 | $-25279.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 21:38 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 21:38 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 11-11 21:37 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 21:36 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-11 21:36 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-11 21:36 | +10 stop | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-11 21:36 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-11 21:36 | +15 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-11 21:36 | +10 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-11 21:36 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-11 21:35 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-11 21:35 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-11 21:35 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-11 21:35 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-11 21:35 | +10 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-11 21:35 | +10 stop | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-11 21:35 | +10 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-11 21:35 | +5 | ZEC | DOWN | 0.59 | 0.71 | 0.88 |
| 11-11 21:35 | +10 stop | NEAR | DOWN | 0.55 | 0.66 | 0.76 |
| 11-11 21:35 | +5 | NEAR | DOWN | 0.55 | 0.62 | 0.35 |
| 11-11 21:34 | +10 stop | BNB | DOWN | 0.67 | 0.46 | -2.44 |
| 11-11 21:34 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-11 21:34 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 21:34 | +5 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 21:34 | +10 | HYPE | UP | 0.40 | 0.59 | 1.56 |
| 11-11 21:34 | +5 | HYPE | UP | 0.40 | 0.59 | 1.56 |
| 11-11 21:33 | +10 stop | XRP | UP | 0.63 | 0.37 | -2.94 |
| 11-11 21:33 | +10 stop | HYPE | UP | 0.67 | 0.43 | -2.74 |
| 11-11 21:33 | +10 stop | BTC | UP | 0.60 | 0.32 | -3.13 |
| 11-11 21:33 | +20 | BTC | UP | 0.60 | open |  |
| 11-11 21:33 | +15 | BTC | UP | 0.60 | open |  |
| 11-11 21:33 | +10 | BTC | UP | 0.60 | open |  |
| 11-11 21:33 | +5 | BTC | UP | 0.60 | open |  |
| 11-11 21:32 | +10 stop | NEAR | DOWN | 0.46 | 0.21 | -2.80 |
| 11-11 21:32 | +20 | NEAR | DOWN | 0.46 | 0.66 | 1.66 |
| 11-11 21:32 | +15 | NEAR | DOWN | 0.46 | 0.62 | 1.25 |
| 11-11 21:32 | +10 | NEAR | DOWN | 0.46 | 0.57 | 0.74 |
| 11-11 21:32 | +5 | NEAR | DOWN | 0.46 | 0.53 | 0.34 |
| 11-11 21:32 | +5 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 11-11 21:32 | +10 stop | DOGE | DOWN | 0.64 | 0.36 | -3.14 |
