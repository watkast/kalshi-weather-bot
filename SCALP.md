# Range-Scalp Bot

*Updated Thu Nov 19 18:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65365 | 57071 | 8294 (124) | 1 | $-17408.59 | -4.2% |
| **+10¢** | 48806 | 39098 | 9708 (165) | 1 | $-16238.65 | -5.3% |
| **+15¢** | 40924 | 30453 | 10471 (211) | 2 | $-14611.98 | -5.7% |
| **+20¢** | 36440 | 25438 | 11002 (266) | 3 | $-12937.69 | -5.7% |
| **+10¢ (15¢ stop)** | 79565 | 79401 | 164 (98) | 0 | $-29285.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 18:41 | +10 stop | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-19 18:40 | +10 stop | BNB | DOWN | 0.71 | 0.47 | -2.73 |
| 11-19 18:39 | +5 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-19 18:39 | +10 stop | ETH | UP | 0.67 | 0.49 | -2.14 |
| 11-19 18:39 | +20 | ETH | UP | 0.68 | open |  |
| 11-19 18:39 | +15 | ETH | UP | 0.67 | open |  |
| 11-19 18:39 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-19 18:39 | +10 stop | ZEC | UP | 0.65 | 0.44 | -2.44 |
| 11-19 18:39 | +10 stop | DOGE | UP | 0.67 | 0.28 | -4.21 |
| 11-19 18:39 | +5 | DOGE | UP | 0.66 | 0.71 | 0.19 |
| 11-19 18:39 | +10 stop | NEAR | UP | 0.50 | 0.60 | 0.65 |
| 11-19 18:38 | +5 | XRP | UP | 0.55 | 0.69 | 1.07 |
| 11-19 18:38 | +10 stop | BNB | UP | 0.69 | 0.47 | -2.53 |
| 11-19 18:38 | +5 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-19 18:38 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-19 18:38 | +5 | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 11-19 18:37 | +5 | ETH | UP | 0.61 | 0.70 | 0.58 |
| 11-19 18:37 | +5 | XRP | UP | 0.56 | 0.65 | 0.56 |
| 11-19 18:37 | +10 stop | SOL | DOWN | 0.57 | 0.80 | 2.00 |
| 11-19 18:37 | +10 stop | NEAR | DOWN | 0.47 | 0.57 | 0.64 |
| 11-19 18:37 | +5 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-19 18:37 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-19 18:37 | +5 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-19 18:36 | +5 | XRP | UP | 0.64 | 0.70 | 0.28 |
| 11-19 18:36 | +10 stop | XRP | UP | 0.65 | 0.42 | -2.64 |
| 11-19 18:36 | +15 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-19 18:36 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-19 18:36 | +10 stop | ETH | UP | 0.58 | 0.70 | 0.87 |
| 11-19 18:36 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 11-19 18:36 | +10 stop | BNB | UP | 0.56 | 0.69 | 0.97 |
| 11-19 18:36 | +5 | XRP | UP | 0.58 | 0.68 | 0.62 |
| 11-19 18:36 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 11-19 18:36 | +15 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-19 18:36 | +10 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-19 18:36 | +5 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-19 18:36 | +10 | NEAR | DOWN | 0.69 | 0.91 | 1.99 |
| 11-19 18:36 | +5 | NEAR | DOWN | 0.69 | 0.91 | 1.99 |
| 11-19 18:36 | +10 stop | ZEC | DOWN | 0.67 | 0.50 | -2.08 |
| 11-19 18:36 | +5 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-19 18:36 | +10 stop | ETH | DOWN | 0.43 | 0.62 | 1.55 |
