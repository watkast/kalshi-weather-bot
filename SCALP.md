# Range-Scalp Bot

*Updated Fri Nov 20 03:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65812 | 57446 | 8366 (124) | 2 | $-17645.54 | -4.3% |
| **+10¢** | 49154 | 39370 | 9784 (165) | 1 | $-16423.01 | -5.3% |
| **+15¢** | 41222 | 30668 | 10554 (211) | 2 | $-14791.48 | -5.7% |
| **+20¢** | 36699 | 25613 | 11086 (267) | 3 | $-13091.52 | -5.7% |
| **+10¢ (15¢ stop)** | 80117 | 79953 | 164 (98) | 0 | $-29494.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 03:55 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 11-20 03:55 | +10 stop | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 11-20 03:55 | +10 | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 11-20 03:55 | +5 | DOGE | UP | 0.66 | 0.73 | 0.40 |
| 11-20 03:54 | +10 stop | DOGE | UP | 0.46 | 0.57 | 0.74 |
| 11-20 03:54 | +10 | DOGE | UP | 0.45 | 0.57 | 0.84 |
| 11-20 03:54 | +5 | DOGE | UP | 0.46 | 0.57 | 0.74 |
| 11-20 03:54 | +10 stop | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-20 03:53 | +10 stop | ZEC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-20 03:53 | +10 stop | ETH | UP | 0.65 | 0.43 | -2.54 |
| 11-20 03:53 | +10 | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-20 03:53 | +5 | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-20 03:52 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-20 03:51 | +10 stop | HYPE | DOWN | 0.65 | 0.47 | -2.11 |
| 11-20 03:51 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-20 03:51 | +20 | BNB | UP | 0.63 | 0.83 | 1.73 |
| 11-20 03:51 | +15 | BNB | UP | 0.63 | 0.83 | 1.73 |
| 11-20 03:50 | +10 stop | DOGE | UP | 0.67 | 0.52 | -1.84 |
| 11-20 03:50 | +20 | DOGE | UP | 0.67 | open |  |
| 11-20 03:50 | +15 | DOGE | UP | 0.67 | open |  |
| 11-20 03:50 | +10 | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-20 03:50 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 11-20 03:50 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 11-20 03:50 | +10 | ETH | UP | 0.62 | 0.75 | 0.99 |
| 11-20 03:50 | +10 stop | NEAR | UP | 0.51 | 0.36 | -1.85 |
| 11-20 03:49 | +5 | ETH | UP | 0.67 | 0.75 | 0.50 |
| 11-20 03:49 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 11-20 03:48 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.15 |
| 11-20 03:48 | +10 | BNB | UP | 0.69 | 0.83 | 1.15 |
| 11-20 03:48 | +5 | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 11-20 03:48 | +10 stop | HYPE | UP | 0.61 | 0.46 | -1.85 |
| 11-20 03:48 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-20 03:48 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-20 03:48 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 11-20 03:48 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-20 03:48 | +20 | ETH | UP | 0.58 | open |  |
| 11-20 03:48 | +15 | ETH | UP | 0.57 | 0.75 | 1.48 |
| 11-20 03:48 | +10 | ETH | UP | 0.57 | 0.67 | 0.66 |
| 11-20 03:48 | +5 | ETH | UP | 0.57 | 0.66 | 0.56 |
| 11-20 03:47 | +10 stop | NEAR | DOWN | 0.57 | 0.42 | -1.86 |
