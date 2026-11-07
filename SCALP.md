# Range-Scalp Bot

*Updated Sat Nov 07 14:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51094 | 44543 | 6551 (78) | 3 | $-14282.34 | -4.4% |
| **+10¢** | 38148 | 30515 | 7633 (105) | 7 | $-13235.44 | -5.5% |
| **+15¢** | 31927 | 23698 | 8229 (134) | 7 | $-12182.82 | -6.1% |
| **+20¢** | 28395 | 19769 | 8626 (177) | 7 | $-10752.45 | -6.0% |
| **+10¢ (15¢ stop)** | 62241 | 62138 | 103 (61) | 0 | $-22998.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 14:56 | +10 stop | ETH | UP | 0.61 | 0.80 | 1.61 |
| 11-07 14:56 | +5 | ETH | UP | 0.62 | 0.80 | 1.51 |
| 11-07 14:53 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 11-07 14:53 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-07 14:53 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-07 14:53 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-07 14:53 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 11-07 14:53 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 11-07 14:53 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-07 14:53 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-07 14:53 | +10 stop | ETH | UP | 0.32 | 0.65 | 2.98 |
| 11-07 14:53 | +20 | ETH | UP | 0.32 | 0.65 | 2.98 |
| 11-07 14:53 | +15 | ETH | UP | 0.32 | 0.65 | 2.98 |
| 11-07 14:53 | +10 | ETH | UP | 0.32 | 0.65 | 2.98 |
| 11-07 14:53 | +5 | ETH | UP | 0.32 | 0.65 | 2.98 |
| 11-07 14:53 | +10 stop | BTC | UP | 0.46 | 0.60 | 1.05 |
| 11-07 14:53 | +20 | BTC | UP | 0.46 | open |  |
| 11-07 14:53 | +15 | BTC | UP | 0.46 | open |  |
| 11-07 14:53 | +10 | BTC | UP | 0.46 | 0.60 | 1.05 |
| 11-07 14:53 | +5 | BTC | UP | 0.46 | 0.60 | 1.05 |
| 11-07 14:52 | +10 stop | SOL | UP | 0.58 | 0.28 | -3.33 |
| 11-07 14:51 | +10 stop | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 11-07 14:51 | +10 stop | DOGE | UP | 0.47 | 0.58 | 0.74 |
| 11-07 14:51 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-07 14:50 | +10 stop | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-07 14:50 | +5 | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-07 14:50 | +5 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-07 14:49 | +10 stop | NEAR | DOWN | 0.61 | 0.45 | -1.95 |
| 11-07 14:49 | +5 | NEAR | DOWN | 0.57 | 0.82 | 2.21 |
| 11-07 14:49 | +10 stop | DOGE | DOWN | 0.66 | 0.38 | -3.13 |
| 11-07 14:49 | +10 stop | ETH | DOWN | 0.63 | 0.25 | -4.11 |
| 11-07 14:49 | +10 stop | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-07 14:49 | +10 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-07 14:49 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-07 14:48 | +10 stop | NEAR | UP | 0.62 | 0.44 | -2.15 |
| 11-07 14:48 | +10 | NEAR | UP | 0.62 | open |  |
| 11-07 14:48 | +5 | NEAR | UP | 0.62 | 0.68 | 0.27 |
| 11-07 14:48 | +5 | HYPE | UP | 0.53 | 0.60 | 0.35 |
| 11-07 14:48 | +10 stop | DOGE | UP | 0.68 | 0.38 | -3.33 |
| 11-07 14:48 | +20 | DOGE | UP | 0.68 | open |  |
