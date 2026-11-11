# Range-Scalp Bot

*Updated Wed Nov 11 20:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56188 | 49003 | 7185 (94) | 2 | $-15342.15 | -4.3% |
| **+10¢** | 41979 | 33593 | 8386 (124) | 4 | $-14321.40 | -5.4% |
| **+15¢** | 35202 | 26164 | 9038 (158) | 5 | $-13012.16 | -5.9% |
| **+20¢** | 31356 | 21874 | 9482 (208) | 7 | $-11371.63 | -5.8% |
| **+10¢ (15¢ stop)** | 68464 | 68343 | 121 (73) | 2 | $-25231.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 20:38 | +10 stop | BTC | UP | 0.56 | open |  |
| 11-11 20:38 | +10 stop | SOL | UP | 0.48 | 0.29 | -2.23 |
| 11-11 20:38 | +10 stop | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-11 20:38 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-11 20:38 | +10 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-11 20:38 | +5 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-11 20:38 | +10 stop | ZEC | UP | 0.63 | 0.38 | -2.84 |
| 11-11 20:37 | +10 stop | BNB | UP | 0.61 | open |  |
| 11-11 20:37 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 11-11 20:37 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 11-11 20:37 | +10 stop | SOL | DOWN | 0.62 | 0.38 | -2.74 |
| 11-11 20:36 | +10 stop | ZEC | DOWN | 0.68 | 0.45 | -2.64 |
| 11-11 20:36 | +10 stop | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-11 20:36 | +10 stop | BTC | UP | 0.56 | 0.67 | 0.76 |
| 11-11 20:36 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.47 |
| 11-11 20:36 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.02 |
| 11-11 20:36 | +10 stop | SOL | UP | 0.57 | 0.42 | -1.86 |
| 11-11 20:35 | +10 stop | SOL | DOWN | 0.43 | 0.54 | 0.74 |
| 11-11 20:35 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-11 20:35 | +10 stop | XRP | UP | 0.54 | 0.35 | -2.24 |
| 11-11 20:33 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-11 20:33 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 11-11 20:32 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 11-11 20:32 | +10 stop | XRP | DOWN | 0.60 | 0.44 | -1.95 |
| 11-11 20:32 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-11 20:32 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-11 20:32 | +10 | XRP | DOWN | 0.60 | open |  |
| 11-11 20:32 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-11 20:32 | +10 stop | BTC | DOWN | 0.63 | 0.42 | -2.45 |
| 11-11 20:32 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-11 20:32 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-11 20:32 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-11 20:32 | +5 | BTC | DOWN | 0.63 | open |  |
| 11-11 20:31 | +10 stop | BNB | DOWN | 0.63 | 0.48 | -1.85 |
| 11-11 20:31 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-11 20:31 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-11 20:31 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-11 20:31 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-11 20:31 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 20:31 | +20 | HYPE | DOWN | 0.68 | 0.91 | 2.12 |
