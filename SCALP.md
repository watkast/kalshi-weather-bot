# Range-Scalp Bot

*Updated Sat Oct 10 06:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10034 | 8657 | 1377 (18) | 0 | $-3407.70 | -5.4% |
| **+10¢** | 7583 | 5978 | 1605 (30) | 0 | $-3276.86 | -6.9% |
| **+15¢** | 6402 | 4710 | 1692 (43) | 0 | $-2705.90 | -6.7% |
| **+20¢** | 5691 | 3934 | 1757 (55) | 0 | $-2259.27 | -6.3% |
| **+10¢ (15¢ stop)** | 12327 | 12292 | 35 (22) | 0 | $-4836.75 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 05:57 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.15 |
| 10-10 05:55 | +10 stop | NEAR | UP | 0.58 | 0.72 | 1.05 |
| 10-10 05:53 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-10 05:53 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-10 05:53 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-10 05:53 | +10 stop | NEAR | UP | 0.53 | 0.79 | 2.30 |
| 10-10 05:52 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.94 |
| 10-10 05:51 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-10 05:51 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 10-10 05:50 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-10 05:50 | +5 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-10 05:50 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-10 05:50 | +10 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-10 05:50 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-10 05:50 | +10 stop | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-10 05:50 | +10 | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-10 05:50 | +5 | ZEC | DOWN | 0.57 | 0.63 | 0.25 |
| 10-10 05:49 | +5 | HYPE | DOWN | 0.60 | 0.73 | 0.95 |
| 10-10 05:49 | +10 stop | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 10-10 05:48 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-10 05:48 | +10 stop | BNB | DOWN | 0.49 | 0.59 | 0.65 |
| 10-10 05:48 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-10 05:48 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-10 05:48 | +10 | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-10 05:48 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-10 05:47 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.26 |
| 10-10 05:47 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 10-10 05:47 | +10 stop | DOGE | DOWN | 0.65 | 0.35 | -3.32 |
| 10-10 05:47 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-10 05:47 | +20 | BTC | DOWN | 0.56 | 0.78 | 1.89 |
| 10-10 05:47 | +15 | BTC | DOWN | 0.55 | 0.72 | 1.37 |
| 10-10 05:47 | +10 | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 10-10 05:47 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 10-10 05:46 | +10 stop | BNB | UP | 0.55 | 0.40 | -1.85 |
| 10-10 05:46 | +20 | BNB | UP | 0.55 | 0.78 | 1.99 |
| 10-10 05:46 | +15 | BNB | UP | 0.55 | 0.78 | 1.99 |
| 10-10 05:46 | +10 | BNB | UP | 0.55 | 0.69 | 1.07 |
| 10-10 05:46 | +5 | BNB | UP | 0.55 | 0.69 | 1.07 |
| 10-10 05:46 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 05:46 | +10 stop | XRP | UP | 0.55 | 0.39 | -1.95 |
