# Range-Scalp Bot

*Updated Wed Nov 11 14:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55931 | 48772 | 7159 (94) | 5 | $-15317.59 | -4.4% |
| **+10¢** | 41790 | 33441 | 8349 (124) | 6 | $-14257.71 | -5.4% |
| **+15¢** | 35044 | 26038 | 9006 (158) | 6 | $-13017.34 | -5.9% |
| **+20¢** | 31214 | 21766 | 9448 (208) | 6 | $-11390.66 | -5.8% |
| **+10¢ (15¢ stop)** | 68145 | 68024 | 121 (73) | 0 | $-25065.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 14:27 | +10 stop | ZEC | UP | 0.60 | 0.74 | 1.12 |
| 11-11 14:27 | +5 | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 11-11 14:26 | +10 stop | NEAR | UP | 0.61 | 0.41 | -2.34 |
| 11-11 14:26 | +10 | NEAR | UP | 0.61 | open |  |
| 11-11 14:25 | +10 stop | ZEC | UP | 0.69 | 0.50 | -2.23 |
| 11-11 14:25 | +10 stop | NEAR | DOWN | 0.67 | 0.32 | -3.82 |
| 11-11 14:25 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 11-11 14:23 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 11-11 14:23 | +10 | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 11-11 14:23 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.04 |
| 11-11 14:23 | +20 | ZEC | UP | 0.67 | 0.96 | 2.71 |
| 11-11 14:23 | +15 | ZEC | UP | 0.67 | 0.86 | 1.65 |
| 11-11 14:23 | +10 | ZEC | UP | 0.67 | 0.86 | 1.65 |
| 11-11 14:23 | +5 | ZEC | UP | 0.67 | 0.75 | 0.50 |
| 11-11 14:23 | +10 stop | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 11-11 14:23 | +5 | NEAR | UP | 0.65 | open |  |
| 11-11 14:22 | +10 stop | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-11 14:22 | +10 stop | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 11-11 14:22 | +10 | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 11-11 14:22 | +5 | NEAR | UP | 0.54 | 0.61 | 0.35 |
| 11-11 14:22 | +10 stop | HYPE | UP | 0.45 | 0.58 | 0.94 |
| 11-11 14:20 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.63 |
| 11-11 14:20 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-11 14:20 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-11 14:20 | +10 stop | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 11-11 14:20 | +10 stop | DOGE | DOWN | 0.61 | 0.79 | 1.51 |
| 11-11 14:20 | +5 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-11 14:19 | +10 stop | DOGE | DOWN | 0.44 | 0.55 | 0.74 |
| 11-11 14:18 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-11 14:18 | +10 stop | BTC | UP | 0.59 | 0.43 | -1.95 |
| 11-11 14:18 | +10 stop | SOL | DOWN | 0.51 | 0.72 | 1.77 |
| 11-11 14:17 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 11-11 14:17 | +10 stop | HYPE | DOWN | 0.58 | 0.40 | -2.11 |
| 11-11 14:17 | +20 | HYPE | DOWN | 0.58 | 0.79 | 1.84 |
| 11-11 14:17 | +15 | HYPE | DOWN | 0.58 | 0.79 | 1.84 |
| 11-11 14:17 | +10 | HYPE | DOWN | 0.58 | 0.71 | 1.01 |
| 11-11 14:17 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.19 |
| 11-11 14:17 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.82 |
| 11-11 14:17 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.86 |
| 11-11 14:17 | +15 | XRP | DOWN | 0.65 | 0.86 | 1.86 |
