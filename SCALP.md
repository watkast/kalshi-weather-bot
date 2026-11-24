# Range-Scalp Bot

*Updated Tue Nov 24 06:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70493 | 61532 | 8961 (148) | 1 | $-18822.72 | -4.2% |
| **+10¢** | 52595 | 42132 | 10463 (192) | 1 | $-17421.40 | -5.3% |
| **+15¢** | 44061 | 32791 | 11270 (248) | 1 | $-15500.69 | -5.6% |
| **+20¢** | 39237 | 27372 | 11865 (314) | 2 | $-13860.10 | -5.6% |
| **+10¢ (15¢ stop)** | 85836 | 85638 | 198 (118) | 0 | $-31551.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 06:01 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-24 06:01 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-24 06:01 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-24 06:01 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-24 06:01 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-24 06:01 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-24 06:01 | +20 | ZEC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-24 06:01 | +15 | ZEC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-24 06:01 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-24 06:01 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 11-24 06:00 | +10 stop | NEAR | UP | 0.57 | 0.31 | -2.93 |
| 11-24 06:00 | +20 | NEAR | UP | 0.57 | open |  |
| 11-24 06:00 | +15 | NEAR | UP | 0.57 | open |  |
| 11-24 06:00 | +10 | NEAR | UP | 0.57 | open |  |
| 11-24 06:00 | +5 | NEAR | UP | 0.57 | open |  |
| 11-24 05:57 | +10 stop | ZEC | DOWN | 0.67 | 0.38 | -3.23 |
| 11-24 05:55 | +10 stop | ZEC | UP | 0.53 | 0.22 | -3.41 |
| 11-24 05:54 | +10 stop | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-24 05:53 | +10 stop | DOGE | DOWN | 0.61 | 0.86 | 2.24 |
| 11-24 05:53 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 11-24 05:53 | +5 | ZEC | UP | 0.65 | 0.93 | 2.60 |
| 11-24 05:53 | +10 stop | HYPE | UP | 0.55 | 0.32 | -2.64 |
| 11-24 05:53 | +10 stop | SOL | UP | 0.54 | 0.39 | -1.85 |
| 11-24 05:53 | +5 | SOL | UP | 0.60 | no | -6.15 |
| 11-24 05:52 | +5 | SOL | DOWN | 0.50 | 0.55 | 0.14 |
| 11-24 05:52 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-24 05:51 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 11-24 05:50 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.95 |
| 11-24 05:50 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-24 05:49 | +10 stop | BNB | DOWN | 0.56 | 0.71 | 1.19 |
| 11-24 05:49 | +10 stop | ZEC | UP | 0.56 | 0.70 | 1.07 |
| 11-24 05:47 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 11-24 05:47 | +20 | NEAR | UP | 0.62 | 0.82 | 1.72 |
| 11-24 05:47 | +15 | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 11-24 05:47 | +10 | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 11-24 05:47 | +5 | NEAR | UP | 0.62 | 0.70 | 0.48 |
| 11-24 05:47 | +10 stop | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 11-24 05:47 | +20 | ETH | DOWN | 0.56 | 0.78 | 1.89 |
| 11-24 05:47 | +15 | ETH | DOWN | 0.56 | 0.78 | 1.89 |
| 11-24 05:47 | +10 | ETH | DOWN | 0.56 | 0.67 | 0.76 |
