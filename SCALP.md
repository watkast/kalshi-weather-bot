# Range-Scalp Bot

*Updated Thu Nov 26 04:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72400 | 63200 | 9200 (158) | 1 | $-19224.59 | -4.2% |
| **+10¢** | 53997 | 43253 | 10744 (203) | 1 | $-17812.41 | -5.2% |
| **+15¢** | 45213 | 33641 | 11572 (260) | 0 | $-15898.23 | -5.6% |
| **+20¢** | 40249 | 28061 | 12188 (326) | 0 | $-14300.56 | -5.7% |
| **+10¢ (15¢ stop)** | 88154 | 87945 | 209 (128) | 0 | $-32359.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 04:56 | +10 stop | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 11-26 04:53 | +10 stop | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-26 04:53 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-26 04:53 | +10 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-26 04:53 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-26 04:53 | +10 | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-26 04:53 | +5 | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-26 04:53 | +10 stop | XRP | UP | 0.65 | 0.83 | 1.54 |
| 11-26 04:53 | +10 stop | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-26 04:53 | +10 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-26 04:53 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-26 04:51 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 11-26 04:51 | +15 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-26 04:51 | +10 stop | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 11-26 04:51 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-26 04:51 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-26 04:51 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-26 04:50 | +10 stop | XRP | UP | 0.68 | 0.53 | -1.84 |
| 11-26 04:50 | +10 stop | BNB | UP | 0.56 | 0.38 | -2.17 |
| 11-26 04:49 | +5 | ETH | DOWN | 0.58 | 0.67 | 0.56 |
| 11-26 04:49 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 11-26 04:49 | +20 | SOL | DOWN | 0.62 | 0.86 | 2.17 |
| 11-26 04:49 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.23 |
| 11-26 04:49 | +10 | SOL | DOWN | 0.62 | 0.75 | 1.02 |
| 11-26 04:49 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.20 |
| 11-26 04:49 | +10 stop | ZEC | UP | 0.71 | 0.52 | -2.23 |
| 11-26 04:49 | +10 | ZEC | UP | 0.69 | open |  |
| 11-26 04:49 | +5 | ZEC | UP | 0.68 | open |  |
| 11-26 04:49 | +10 stop | HYPE | DOWN | 0.65 | 0.81 | 1.33 |
| 11-26 04:49 | +10 stop | DOGE | DOWN | 0.57 | 0.70 | 0.97 |
| 11-26 04:49 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-26 04:49 | +10 stop | XRP | UP | 0.45 | 0.62 | 1.35 |
| 11-26 04:48 | +10 stop | BNB | UP | 0.60 | 0.40 | -2.34 |
| 11-26 04:48 | +10 stop | DOGE | UP | 0.60 | 0.44 | -1.95 |
| 11-26 04:48 | +10 stop | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 11-26 04:48 | +10 | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 11-26 04:48 | +5 | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 11-26 04:48 | +5 | ETH | DOWN | 0.55 | 0.61 | 0.25 |
| 11-26 04:47 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-26 04:47 | +10 | ZEC | UP | 0.56 | 0.67 | 0.76 |
