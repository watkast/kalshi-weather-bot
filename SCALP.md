# Range-Scalp Bot

*Updated Tue Nov 17 19:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63173 | 55111 | 8062 (117) | 2 | $-17164.35 | -4.3% |
| **+10¢** | 47194 | 37760 | 9434 (159) | 3 | $-16026.04 | -5.4% |
| **+15¢** | 39564 | 29392 | 10172 (201) | 3 | $-14519.61 | -5.8% |
| **+20¢** | 35248 | 24574 | 10674 (256) | 5 | $-12757.35 | -5.8% |
| **+10¢ (15¢ stop)** | 76879 | 76723 | 156 (92) | 0 | $-28287.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 18:57 | +10 stop | ZEC | DOWN | 0.69 | 0.96 | 2.50 |
| 11-17 18:57 | +20 | ZEC | DOWN | 0.69 | 0.96 | 2.50 |
| 11-17 18:57 | +10 | ZEC | DOWN | 0.69 | 0.96 | 2.50 |
| 11-17 18:57 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-17 18:56 | +10 stop | ETH | UP | 0.67 | 0.89 | 1.97 |
| 11-17 18:56 | +5 | BTC | DOWN | 0.44 | 0.63 | 1.55 |
| 11-17 18:55 | +10 stop | ETH | DOWN | 0.48 | 0.63 | 1.15 |
| 11-17 18:55 | +10 stop | NEAR | UP | 0.65 | 0.94 | 2.72 |
| 11-17 18:55 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-17 18:55 | +10 stop | DOGE | UP | 0.67 | 0.52 | -1.84 |
| 11-17 18:55 | +15 | DOGE | UP | 0.67 | 0.91 | 2.17 |
| 11-17 18:55 | +10 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 11-17 18:55 | +5 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 11-17 18:53 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 11-17 18:51 | +10 stop | BTC | DOWN | 0.58 | 0.24 | -3.71 |
| 11-17 18:51 | +10 stop | ETH | DOWN | 0.70 | 0.48 | -2.53 |
| 11-17 18:51 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-17 18:51 | +15 | ETH | DOWN | 0.70 | open |  |
| 11-17 18:51 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-17 18:51 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-17 18:51 | +10 stop | BNB | UP | 0.59 | 0.83 | 2.13 |
| 11-17 18:50 | +10 stop | SOL | UP | 0.64 | 0.78 | 1.10 |
| 11-17 18:50 | +15 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 11-17 18:50 | +10 | SOL | UP | 0.64 | 0.78 | 1.10 |
| 11-17 18:50 | +5 | SOL | UP | 0.64 | 0.78 | 1.10 |
| 11-17 18:50 | +10 stop | NEAR | UP | 0.66 | 0.80 | 1.15 |
| 11-17 18:50 | +10 stop | DOGE | UP | 0.60 | 0.80 | 1.73 |
| 11-17 18:50 | +15 | DOGE | UP | 0.60 | 0.80 | 1.73 |
| 11-17 18:50 | +10 | DOGE | UP | 0.60 | 0.80 | 1.71 |
| 11-17 18:50 | +5 | DOGE | UP | 0.60 | 0.80 | 1.71 |
| 11-17 18:50 | +5 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-17 18:50 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 11-17 18:50 | +5 | XRP | UP | 0.70 | 0.78 | 0.52 |
| 11-17 18:49 | +5 | BNB | DOWN | 0.68 | yes | -6.96 |
| 11-17 18:48 | +10 stop | XRP | DOWN | 0.57 | 0.40 | -2.05 |
| 11-17 18:48 | +15 | ZEC | DOWN | 0.71 | 0.96 | 2.32 |
| 11-17 18:48 | +5 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 18:48 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-17 18:48 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-17 18:48 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.94 |
