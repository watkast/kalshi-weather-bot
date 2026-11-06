# Range-Scalp Bot

*Updated Fri Nov 06 21:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49993 | 43580 | 6413 (76) | 0 | $-14033.59 | -4.5% |
| **+10¢** | 37318 | 29859 | 7459 (102) | 0 | $-12906.71 | -5.5% |
| **+15¢** | 31254 | 23215 | 8039 (131) | 2 | $-11814.23 | -6.0% |
| **+20¢** | 27786 | 19357 | 8429 (172) | 3 | $-10447.04 | -6.0% |
| **+10¢ (15¢ stop)** | 60905 | 60806 | 99 (58) | 0 | $-22562.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 21:34 | +10 stop | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 21:34 | +20 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 11-06 21:34 | +15 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 11-06 21:34 | +10 | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 21:34 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 11-06 21:34 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-06 21:34 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-06 21:34 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-06 21:34 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-06 21:34 | +5 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-06 21:34 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-06 21:34 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-06 21:34 | +15 | BTC | DOWN | 0.59 | open |  |
| 11-06 21:34 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-06 21:34 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-06 21:34 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.82 |
| 11-06 21:34 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.82 |
| 11-06 21:34 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.51 |
| 11-06 21:33 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.50 |
| 11-06 21:31 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-06 21:31 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-06 21:31 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-06 21:31 | +15 | NEAR | DOWN | 0.63 | open |  |
| 11-06 21:31 | +10 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-06 21:31 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 11-06 21:27 | +10 stop | HYPE | DOWN | 0.71 | 0.54 | -2.03 |
| 11-06 21:27 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-06 21:27 | +20 | HYPE | DOWN | 0.71 | 0.96 | 2.34 |
| 11-06 21:27 | +15 | HYPE | DOWN | 0.71 | 0.96 | 2.34 |
| 11-06 21:27 | +10 | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-06 21:27 | +10 stop | DOGE | UP | 0.34 | 0.60 | 2.27 |
| 11-06 21:26 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-06 21:26 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-06 21:26 | +10 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-06 21:26 | +5 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-06 21:25 | +10 stop | DOGE | UP | 0.58 | 0.29 | -3.23 |
| 11-06 21:25 | +20 | DOGE | UP | 0.59 | no | -6.03 |
| 11-06 21:25 | +15 | DOGE | UP | 0.59 | no | -6.07 |
| 11-06 21:25 | +10 | DOGE | UP | 0.59 | no | -6.07 |
| 11-06 21:25 | +5 | DOGE | UP | 0.59 | no | -6.07 |
