# Range-Scalp Bot

*Updated Thu Oct 15 02:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16932 | 14691 | 2241 (28) | 2 | $-5213.78 | -4.9% |
| **+10¢** | 12803 | 10207 | 2596 (40) | 3 | $-4730.57 | -5.9% |
| **+15¢** | 10753 | 7962 | 2791 (59) | 6 | $-4250.22 | -6.3% |
| **+20¢** | 9550 | 6626 | 2924 (76) | 8 | $-3751.60 | -6.3% |
| **+10¢ (15¢ stop)** | 20843 | 20793 | 50 (29) | 0 | $-8059.53 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 02:18 | +10 stop | BTC | UP | 0.43 | 0.63 | 1.65 |
| 10-15 02:18 | +10 stop | XRP | UP | 0.42 | 0.60 | 1.45 |
| 10-15 02:18 | +10 | XRP | UP | 0.42 | 0.60 | 1.45 |
| 10-15 02:18 | +5 | XRP | UP | 0.42 | 0.60 | 1.45 |
| 10-15 02:18 | +10 stop | ETH | UP | 0.46 | 0.62 | 1.25 |
| 10-15 02:18 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-15 02:18 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-15 02:17 | +5 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-15 02:17 | +10 stop | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 10-15 02:17 | +20 | XRP | DOWN | 0.51 | open |  |
| 10-15 02:17 | +15 | XRP | DOWN | 0.52 | open |  |
| 10-15 02:17 | +10 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 10-15 02:17 | +5 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 10-15 02:17 | +10 stop | BTC | UP | 0.48 | 0.58 | 0.64 |
| 10-15 02:17 | +20 | BTC | UP | 0.48 | open |  |
| 10-15 02:17 | +15 | BTC | UP | 0.49 | open |  |
| 10-15 02:17 | +10 | BTC | UP | 0.49 | 0.63 | 1.05 |
| 10-15 02:17 | +5 | BTC | UP | 0.47 | 0.55 | 0.44 |
| 10-15 02:17 | +10 stop | ZEC | UP | 0.53 | 0.75 | 1.88 |
| 10-15 02:17 | +5 | ZEC | UP | 0.57 | 0.75 | 1.49 |
| 10-15 02:16 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-15 02:16 | +5 | ZEC | DOWN | 0.41 | 0.55 | 1.05 |
| 10-15 02:16 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 10-15 02:16 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-15 02:16 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-15 02:16 | +10 | ETH | DOWN | 0.62 | open |  |
| 10-15 02:16 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-15 02:15 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 02:15 | +20 | NEAR | DOWN | 0.61 | open |  |
| 10-15 02:15 | +15 | NEAR | DOWN | 0.61 | 0.77 | 1.30 |
| 10-15 02:15 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 02:15 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 10-15 02:15 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.15 |
| 10-15 02:15 | +20 | ZEC | DOWN | 0.56 | 0.89 | 3.05 |
| 10-15 02:15 | +15 | ZEC | DOWN | 0.56 | 0.89 | 3.05 |
| 10-15 02:15 | +10 | ZEC | DOWN | 0.56 | 0.89 | 3.05 |
| 10-15 02:15 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 10-15 02:15 | +10 stop | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
| 10-15 02:15 | +20 | DOGE | DOWN | 0.58 | open |  |
| 10-15 02:15 | +15 | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
