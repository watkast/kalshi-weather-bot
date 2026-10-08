# Range-Scalp Bot

*Updated Thu Oct 08 23:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8178 | 7072 | 1106 (13) | 2 | $-2687.48 | -5.2% |
| **+10¢** | 6187 | 4880 | 1307 (25) | 4 | $-2651.72 | -6.8% |
| **+15¢** | 5211 | 3836 | 1375 (37) | 4 | $-2165.59 | -6.6% |
| **+20¢** | 4647 | 3220 | 1427 (45) | 6 | $-1768.14 | -6.1% |
| **+10¢ (15¢ stop)** | 9934 | 9904 | 30 (19) | 2 | $-3693.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 23:40 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-08 23:40 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-08 23:40 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-08 23:40 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-08 23:40 | +5 | BTC | UP | 0.65 | open |  |
| 10-08 23:39 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-08 23:38 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-08 23:37 | +5 | DOGE | UP | 0.59 | 0.66 | 0.33 |
| 10-08 23:37 | +10 stop | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-08 23:37 | +15 | ETH | DOWN | 0.57 | 0.85 | 2.53 |
| 10-08 23:37 | +10 | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-08 23:37 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 10-08 23:37 | +10 stop | HYPE | DOWN | 0.65 | 0.45 | -2.38 |
| 10-08 23:37 | +10 stop | DOGE | UP | 0.59 | 0.83 | 2.13 |
| 10-08 23:37 | +20 | DOGE | UP | 0.59 | 0.83 | 2.13 |
| 10-08 23:37 | +15 | DOGE | UP | 0.58 | 0.83 | 2.22 |
| 10-08 23:37 | +10 | DOGE | UP | 0.58 | 0.83 | 2.22 |
| 10-08 23:37 | +5 | DOGE | UP | 0.57 | 0.66 | 0.56 |
| 10-08 23:36 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-08 23:36 | +10 stop | XRP | DOWN | 0.69 | 0.86 | 1.46 |
| 10-08 23:36 | +5 | HYPE | UP | 0.53 | 0.65 | 0.86 |
| 10-08 23:35 | +5 | SOL | UP | 0.44 | 0.65 | 1.76 |
| 10-08 23:34 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 10-08 23:34 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-08 23:33 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-08 23:33 | +15 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 10-08 23:33 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-08 23:33 | +5 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-08 23:33 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.80 |
| 10-08 23:33 | +10 | BNB | UP | 0.63 | 0.74 | 0.80 |
| 10-08 23:33 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.11 |
| 10-08 23:33 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-08 23:33 | +5 | ZEC | UP | 0.70 | 0.79 | 0.63 |
| 10-08 23:32 | +5 | BNB | UP | 0.63 | 0.72 | 0.59 |
| 10-08 23:32 | +10 stop | HYPE | UP | 0.67 | 0.50 | -2.01 |
| 10-08 23:32 | +20 | HYPE | UP | 0.67 | open |  |
| 10-08 23:32 | +15 | HYPE | UP | 0.67 | 0.83 | 1.37 |
| 10-08 23:32 | +10 | HYPE | UP | 0.67 | 0.83 | 1.37 |
| 10-08 23:32 | +5 | HYPE | UP | 0.67 | 0.73 | 0.33 |
| 10-08 23:31 | +10 stop | BNB | UP | 0.56 | 0.66 | 0.71 |
