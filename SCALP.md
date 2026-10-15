# Range-Scalp Bot

*Updated Thu Oct 15 23:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18342 | 15925 | 2417 (28) | 3 | $-5610.19 | -4.9% |
| **+10¢** | 13839 | 11042 | 2797 (40) | 3 | $-5074.05 | -5.8% |
| **+15¢** | 11607 | 8599 | 3008 (59) | 3 | $-4582.28 | -6.3% |
| **+20¢** | 10310 | 7165 | 3145 (78) | 3 | $-3980.81 | -6.2% |
| **+10¢ (15¢ stop)** | 22572 | 22522 | 50 (29) | 0 | $-8732.31 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 23:41 | +10 stop | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-15 23:41 | +10 | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-15 23:41 | +5 | DOGE | UP | 0.65 | 0.71 | 0.29 |
| 10-15 23:40 | +10 stop | XRP | DOWN | 0.59 | 0.37 | -2.56 |
| 10-15 23:39 | +5 | ETH | UP | 0.64 | open |  |
| 10-15 23:39 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-15 23:39 | +10 stop | XRP | DOWN | 0.69 | 0.43 | -2.93 |
| 10-15 23:39 | +5 | DOGE | UP | 0.61 | 0.71 | 0.64 |
| 10-15 23:39 | +5 | ETH | UP | 0.54 | 0.59 | 0.15 |
| 10-15 23:39 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-15 23:38 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 10-15 23:38 | +10 | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 10-15 23:38 | +5 | DOGE | UP | 0.59 | 0.66 | 0.37 |
| 10-15 23:38 | +10 stop | ETH | UP | 0.56 | 0.37 | -2.25 |
| 10-15 23:38 | +20 | ETH | UP | 0.56 | open |  |
| 10-15 23:38 | +15 | ETH | UP | 0.56 | open |  |
| 10-15 23:38 | +10 | ETH | UP | 0.56 | open |  |
| 10-15 23:38 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 10-15 23:38 | +10 stop | BTC | UP | 0.47 | 0.65 | 1.46 |
| 10-15 23:37 | +10 stop | BTC | DOWN | 0.42 | 0.54 | 0.84 |
| 10-15 23:36 | +10 stop | XRP | DOWN | 0.52 | 0.33 | -2.24 |
| 10-15 23:36 | +10 stop | ZEC | DOWN | 0.50 | 0.61 | 0.75 |
| 10-15 23:36 | +10 stop | DOGE | UP | 0.61 | 0.75 | 1.09 |
| 10-15 23:36 | +10 | DOGE | UP | 0.61 | 0.75 | 1.08 |
| 10-15 23:36 | +5 | DOGE | UP | 0.61 | 0.75 | 1.07 |
| 10-15 23:35 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 10-15 23:35 | +10 stop | ZEC | DOWN | 0.67 | 0.49 | -2.14 |
| 10-15 23:35 | +10 stop | XRP | DOWN | 0.64 | 0.43 | -2.45 |
| 10-15 23:35 | +20 | XRP | DOWN | 0.64 | 0.93 | 2.69 |
| 10-15 23:35 | +15 | XRP | DOWN | 0.64 | 0.93 | 2.69 |
| 10-15 23:35 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 23:35 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-15 23:35 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.89 |
| 10-15 23:35 | +20 | HYPE | UP | 0.66 | 0.87 | 1.84 |
| 10-15 23:35 | +15 | HYPE | UP | 0.66 | 0.84 | 1.52 |
| 10-15 23:35 | +10 | HYPE | UP | 0.66 | 0.78 | 0.89 |
| 10-15 23:35 | +5 | HYPE | UP | 0.66 | 0.76 | 0.69 |
| 10-15 23:35 | +5 | NEAR | UP | 0.57 | open |  |
| 10-15 23:35 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 10-15 23:35 | +20 | ETH | UP | 0.61 | 0.82 | 1.82 |
