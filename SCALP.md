# Range-Scalp Bot

*Updated Sun Nov 15 06:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60473 | 52750 | 7723 (107) | 0 | $-16459.48 | -4.3% |
| **+10¢** | 45178 | 36128 | 9050 (143) | 0 | $-15538.76 | -5.5% |
| **+15¢** | 37843 | 28080 | 9763 (181) | 1 | $-14231.98 | -6.0% |
| **+20¢** | 33730 | 23490 | 10240 (233) | 1 | $-12521.62 | -5.9% |
| **+10¢ (15¢ stop)** | 73621 | 73478 | 143 (82) | 0 | $-27120.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 06:06 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-15 06:06 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-15 06:06 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-15 06:06 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-15 06:06 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-15 05:53 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-15 05:52 | +5 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-15 05:52 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 11-15 05:52 | +10 stop | XRP | UP | 0.58 | 0.36 | -2.55 |
| 11-15 05:52 | +10 stop | HYPE | DOWN | 0.60 | 0.82 | 1.87 |
| 11-15 05:52 | +5 | HYPE | DOWN | 0.60 | 0.65 | 0.17 |
| 11-15 05:51 | +10 stop | XRP | DOWN | 0.53 | 0.38 | -1.85 |
| 11-15 05:51 | +15 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 11-15 05:51 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 05:50 | +10 stop | ETH | DOWN | 0.66 | 0.49 | -2.04 |
| 11-15 05:50 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-15 05:50 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 11-15 05:49 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-15 05:49 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-15 05:49 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-15 05:49 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-15 05:49 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-15 05:49 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-15 05:48 | +10 stop | ETH | DOWN | 0.68 | 0.51 | -2.04 |
| 11-15 05:48 | +5 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-15 05:48 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 05:48 | +10 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 05:47 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.30 |
| 11-15 05:47 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 11-15 05:47 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-15 05:47 | +10 stop | XRP | DOWN | 0.60 | 0.44 | -1.95 |
| 11-15 05:47 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-15 05:47 | +15 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-15 05:47 | +10 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-15 05:47 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 11-15 05:46 | +10 stop | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-15 05:46 | +10 stop | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-15 05:46 | +20 | BTC | DOWN | 0.56 | 0.78 | 1.89 |
| 11-15 05:46 | +15 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-15 05:46 | +10 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
