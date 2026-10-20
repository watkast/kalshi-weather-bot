# Range-Scalp Bot

*Updated Tue Oct 20 11:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25585 | 22279 | 3306 (31) | 1 | $-7483.58 | -4.6% |
| **+10¢** | 19252 | 15434 | 3818 (46) | 1 | $-6621.96 | -5.5% |
| **+15¢** | 16112 | 12000 | 4112 (70) | 1 | $-5946.63 | -5.9% |
| **+20¢** | 14250 | 9947 | 4303 (88) | 1 | $-5305.50 | -5.9% |
| **+10¢ (15¢ stop)** | 31398 | 31345 | 53 (30) | 0 | $-11597.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 11:37 | +10 stop | BTC | DOWN | 0.49 | 0.34 | -1.84 |
| 10-20 11:37 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-20 11:37 | +5 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-20 11:37 | +10 stop | HYPE | DOWN | 0.60 | 0.39 | -2.44 |
| 10-20 11:36 | +10 stop | BNB | UP | 0.60 | 0.83 | 2.03 |
| 10-20 11:36 | +5 | BNB | UP | 0.59 | 0.65 | 0.27 |
| 10-20 11:36 | +10 stop | XRP | UP | 0.49 | 0.60 | 0.75 |
| 10-20 11:36 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.95 |
| 10-20 11:34 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.28 |
| 10-20 11:34 | +10 stop | BNB | UP | 0.53 | 0.64 | 0.75 |
| 10-20 11:34 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-20 11:34 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-20 11:33 | +10 stop | BNB | DOWN | 0.45 | 0.58 | 0.94 |
| 10-20 11:33 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 11:33 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-20 11:33 | +5 | DOGE | UP | 0.47 | 0.61 | 1.02 |
| 10-20 11:32 | +5 | BNB | UP | 0.55 | 0.64 | 0.55 |
| 10-20 11:32 | +10 stop | HYPE | DOWN | 0.65 | 0.47 | -2.14 |
| 10-20 11:32 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-20 11:32 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-20 11:32 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-20 11:32 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-20 11:32 | +5 | NEAR | UP | 0.65 | 0.79 | 1.12 |
| 10-20 11:31 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 10-20 11:31 | +20 | ETH | UP | 0.69 | 0.90 | 1.89 |
| 10-20 11:31 | +15 | ETH | UP | 0.69 | 0.90 | 1.89 |
| 10-20 11:31 | +10 | ETH | UP | 0.69 | 0.90 | 1.89 |
| 10-20 11:31 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-20 11:31 | +10 stop | XRP | UP | 0.68 | 0.52 | -1.94 |
| 10-20 11:31 | +20 | XRP | UP | 0.68 | 0.94 | 2.38 |
| 10-20 11:31 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-20 11:31 | +10 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 10-20 11:31 | +5 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 10-20 11:31 | +5 | BTC | UP | 0.63 | 0.71 | 0.48 |
| 10-20 11:31 | +10 stop | BNB | UP | 0.64 | 0.46 | -2.15 |
| 10-20 11:31 | +20 | BNB | UP | 0.64 | 0.86 | 1.94 |
| 10-20 11:31 | +15 | BNB | UP | 0.64 | 0.83 | 1.63 |
| 10-20 11:31 | +10 | BNB | UP | 0.64 | 0.83 | 1.63 |
| 10-20 11:31 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 10-20 11:31 | +10 stop | DOGE | UP | 0.69 | 0.42 | -3.03 |
