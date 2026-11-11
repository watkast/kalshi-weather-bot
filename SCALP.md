# Range-Scalp Bot

*Updated Wed Nov 11 20:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56170 | 48988 | 7182 (94) | 3 | $-15329.57 | -4.3% |
| **+10¢** | 41968 | 33587 | 8381 (124) | 5 | $-14297.54 | -5.4% |
| **+15¢** | 35192 | 26159 | 9033 (158) | 5 | $-12988.67 | -5.9% |
| **+20¢** | 31349 | 21872 | 9477 (208) | 5 | $-11345.41 | -5.8% |
| **+10¢ (15¢ stop)** | 68444 | 68323 | 121 (73) | 0 | $-25209.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 20:28 | +5 | SOL | UP | 0.53 | 0.61 | 0.45 |
| 11-11 20:27 | +10 stop | ETH | UP | 0.71 | 0.42 | -3.23 |
| 11-11 20:27 | +20 | ETH | UP | 0.71 | open |  |
| 11-11 20:27 | +15 | ETH | UP | 0.71 | open |  |
| 11-11 20:27 | +10 | ETH | UP | 0.71 | open |  |
| 11-11 20:27 | +5 | ETH | UP | 0.71 | open |  |
| 11-11 20:27 | +10 stop | HYPE | UP | 0.43 | 0.64 | 1.72 |
| 11-11 20:27 | +10 stop | SOL | UP | 0.63 | 0.13 | -5.25 |
| 11-11 20:26 | +10 stop | XRP | UP | 0.70 | 0.89 | 1.68 |
| 11-11 20:26 | +5 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 11-11 20:24 | +10 stop | DOGE | DOWN | 0.66 | 0.44 | -2.54 |
| 11-11 20:22 | +10 stop | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-11 20:21 | +10 stop | DOGE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-11 20:20 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-11 20:19 | +10 stop | XRP | DOWN | 0.67 | 0.52 | -1.84 |
| 11-11 20:19 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-11 20:18 | +10 stop | BNB | DOWN | 0.68 | 0.82 | 1.13 |
| 11-11 20:18 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 11-11 20:18 | +5 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 11-11 20:18 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-11 20:18 | +10 stop | DOGE | UP | 0.56 | 0.37 | -2.25 |
| 11-11 20:17 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-11 20:17 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-11 20:17 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-11 20:17 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 20:17 | +20 | BTC | DOWN | 0.54 | 0.77 | 1.99 |
| 11-11 20:17 | +15 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 20:17 | +10 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 20:17 | +5 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 20:17 | +5 | XRP | UP | 0.50 | 0.56 | 0.24 |
| 11-11 20:16 | +10 stop | XRP | UP | 0.61 | 0.44 | -2.05 |
| 11-11 20:16 | +10 | XRP | UP | 0.61 | 0.89 | 2.56 |
| 11-11 20:16 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 11-11 20:16 | +10 stop | BNB | UP | 0.51 | 0.31 | -2.33 |
| 11-11 20:16 | +20 | BNB | UP | 0.52 | open |  |
| 11-11 20:16 | +15 | BNB | UP | 0.52 | open |  |
| 11-11 20:16 | +10 | BNB | UP | 0.52 | open |  |
| 11-11 20:16 | +5 | BNB | UP | 0.52 | 0.57 | 0.14 |
| 11-11 20:16 | +10 stop | ETH | UP | 0.58 | 0.34 | -2.74 |
| 11-11 20:16 | +20 | ETH | UP | 0.59 | 0.81 | 1.92 |
