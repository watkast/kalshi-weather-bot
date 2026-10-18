# Range-Scalp Bot

*Updated Sun Oct 18 04:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22043 | 19197 | 2846 (29) | 0 | $-6364.32 | -4.6% |
| **+10¢** | 16589 | 13301 | 3288 (41) | 0 | $-5657.83 | -5.4% |
| **+15¢** | 13892 | 10346 | 3546 (61) | 0 | $-5133.12 | -5.9% |
| **+20¢** | 12293 | 8578 | 3715 (80) | 0 | $-4575.93 | -5.9% |
| **+10¢ (15¢ stop)** | 27111 | 27061 | 50 (29) | 0 | $-10343.51 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 04:32 | +10 stop | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-18 04:32 | +20 | HYPE | DOWN | 0.60 | 0.83 | 2.03 |
| 10-18 04:32 | +15 | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-18 04:32 | +10 | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-18 04:32 | +5 | HYPE | DOWN | 0.60 | 0.68 | 0.47 |
| 10-18 04:30 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-18 04:30 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-18 04:30 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-18 04:30 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-18 04:30 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-18 04:27 | +10 stop | ETH | DOWN | 0.69 | 0.90 | 1.92 |
| 10-18 04:27 | +10 | ETH | DOWN | 0.69 | 0.90 | 1.92 |
| 10-18 04:27 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-18 04:27 | +10 stop | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 04:27 | +15 | DOGE | DOWN | 0.69 | 0.89 | 1.78 |
| 10-18 04:27 | +10 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 04:27 | +5 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-18 04:26 | +10 stop | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-18 04:25 | +10 stop | HYPE | DOWN | 0.54 | 0.26 | -3.12 |
| 10-18 04:24 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-18 04:24 | +10 stop | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 10-18 04:22 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-18 04:22 | +10 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-18 04:22 | +10 stop | HYPE | UP | 0.65 | 0.50 | -1.84 |
| 10-18 04:22 | +10 | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-18 04:22 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 10-18 04:22 | +10 stop | NEAR | DOWN | 0.52 | 0.67 | 1.16 |
| 10-18 04:22 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 10-18 04:22 | +10 stop | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-18 04:21 | +5 | XRP | UP | 0.60 | no | -6.17 |
| 10-18 04:20 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-18 04:20 | +15 | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-18 04:20 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-18 04:20 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.59 |
| 10-18 04:20 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-18 04:19 | +10 stop | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-18 04:19 | +10 | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-18 04:19 | +10 stop | ETH | UP | 0.54 | 0.65 | 0.76 |
| 10-18 04:19 | +5 | XRP | UP | 0.54 | 0.59 | 0.15 |
| 10-18 04:19 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
