# Range-Scalp Bot

*Updated Thu Oct 22 17:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29033 | 25288 | 3745 (39) | 0 | $-8438.86 | -4.6% |
| **+10¢** | 21780 | 17448 | 4332 (55) | 2 | $-7539.11 | -5.5% |
| **+15¢** | 18231 | 13575 | 4656 (78) | 3 | $-6736.22 | -5.9% |
| **+20¢** | 16137 | 11256 | 4881 (100) | 2 | $-6067.43 | -6.0% |
| **+10¢ (15¢ stop)** | 35621 | 35562 | 59 (32) | 1 | $-13387.25 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 17:08 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-22 17:08 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-22 17:08 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-22 17:08 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-22 17:07 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 17:07 | +5 | SOL | DOWN | 0.71 | 0.79 | 0.53 |
| 10-22 17:06 | +5 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-22 17:06 | +10 stop | NEAR | UP | 0.63 | 0.45 | -2.15 |
| 10-22 17:06 | +10 stop | ETH | DOWN | 0.52 | 0.62 | 0.65 |
| 10-22 17:06 | +10 stop | DOGE | DOWN | 0.67 | 0.44 | -2.64 |
| 10-22 17:06 | +20 | DOGE | DOWN | 0.67 | 0.89 | 1.97 |
| 10-22 17:06 | +15 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 10-22 17:06 | +10 | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 10-22 17:06 | +5 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-22 17:06 | +10 stop | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 17:06 | +20 | ZEC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-22 17:06 | +15 | ZEC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-22 17:06 | +10 | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-22 17:05 | +10 stop | BTC | DOWN | 0.64 | 0.48 | -1.95 |
| 10-22 17:05 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-22 17:05 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-22 17:05 | +20 | SOL | DOWN | 0.67 | 0.89 | 1.97 |
| 10-22 17:05 | +15 | SOL | DOWN | 0.67 | 0.86 | 1.65 |
| 10-22 17:05 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-22 17:05 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 17:05 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 10-22 17:05 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-22 17:05 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 17:04 | +5 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-22 17:04 | +10 stop | ETH | DOWN | 0.65 | 0.48 | -2.04 |
| 10-22 17:04 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-22 17:04 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-22 17:04 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-22 17:03 | +5 | DOGE | DOWN | 0.59 | 0.71 | 0.86 |
| 10-22 17:02 | +10 stop | ETH | UP | 0.46 | 0.58 | 0.84 |
| 10-22 17:02 | +20 | ETH | UP | 0.46 | open |  |
| 10-22 17:02 | +15 | ETH | UP | 0.46 | open |  |
| 10-22 17:02 | +10 | ETH | UP | 0.46 | 0.58 | 0.84 |
| 10-22 17:02 | +5 | ETH | UP | 0.46 | 0.58 | 0.84 |
| 10-22 17:02 | +10 stop | BTC | UP | 0.46 | 0.25 | -2.42 |
