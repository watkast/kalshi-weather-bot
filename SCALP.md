# Range-Scalp Bot

*Updated Fri Nov 06 15:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49670 | 43293 | 6377 (76) | 1 | $-13976.69 | -4.5% |
| **+10¢** | 37076 | 29658 | 7418 (101) | 1 | $-12874.37 | -5.5% |
| **+15¢** | 31056 | 23064 | 7992 (130) | 1 | $-11770.14 | -6.0% |
| **+20¢** | 27608 | 19229 | 8379 (171) | 2 | $-10414.57 | -6.0% |
| **+10¢ (15¢ stop)** | 60513 | 60416 | 97 (57) | 0 | $-22370.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 15:43 | +10 stop | BTC | DOWN | 0.55 | 0.73 | 1.48 |
| 11-06 15:43 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-06 15:43 | +15 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-06 15:43 | +10 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 11-06 15:43 | +5 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-06 15:42 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-06 15:41 | +10 stop | ETH | DOWN | 0.59 | 0.38 | -2.44 |
| 11-06 15:41 | +10 | ETH | DOWN | 0.59 | open |  |
| 11-06 15:41 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-06 15:38 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 15:38 | +15 | ETH | DOWN | 0.69 | open |  |
| 11-06 15:38 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 15:38 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 15:35 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-06 15:33 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-06 15:33 | +20 | NEAR | DOWN | 0.63 | 0.86 | 2.04 |
| 11-06 15:33 | +15 | NEAR | DOWN | 0.63 | 0.82 | 1.62 |
| 11-06 15:33 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-06 15:33 | +5 | NEAR | DOWN | 0.63 | 0.71 | 0.48 |
| 11-06 15:33 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-06 15:33 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-06 15:33 | +15 | SOL | DOWN | 0.68 | 0.85 | 1.45 |
| 11-06 15:33 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-06 15:33 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-06 15:32 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 11-06 15:32 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 15:32 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-06 15:32 | +10 stop | ETH | DOWN | 0.68 | 0.44 | -2.74 |
| 11-06 15:32 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-06 15:32 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 15:32 | +10 | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 11-06 15:32 | +5 | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 11-06 15:32 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-06 15:32 | +20 | DOGE | DOWN | 0.71 | 0.93 | 2.00 |
| 11-06 15:32 | +10 stop | XRP | DOWN | 0.68 | 0.47 | -2.44 |
| 11-06 15:32 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 11-06 15:32 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 15:32 | +10 | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 11-06 15:32 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 11-06 15:27 | +10 stop | BTC | UP | 0.35 | 0.62 | 2.37 |
