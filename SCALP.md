# Range-Scalp Bot

*Updated Fri Nov 06 02:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49018 | 42710 | 6308 (75) | 0 | $-13941.73 | -4.5% |
| **+10¢** | 36599 | 29264 | 7335 (101) | 0 | $-12818.59 | -5.6% |
| **+15¢** | 30658 | 22761 | 7897 (130) | 0 | $-11681.32 | -6.1% |
| **+20¢** | 27245 | 18970 | 8275 (170) | 0 | $-10326.92 | -6.0% |
| **+10¢ (15¢ stop)** | 59771 | 59676 | 95 (57) | 0 | $-22130.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 01:58 | +10 stop | DOGE | DOWN | 0.29 | 0.01 | -2.96 |
| 11-06 01:57 | +10 stop | BTC | DOWN | 0.48 | 0.68 | 1.66 |
| 11-06 01:57 | +10 stop | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-06 01:57 | +5 | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 11-06 01:57 | +10 stop | ETH | UP | 0.42 | 0.56 | 1.04 |
| 11-06 01:57 | +5 | ETH | UP | 0.39 | 0.56 | 1.35 |
| 11-06 01:56 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 11-06 01:56 | +10 | NEAR | UP | 0.71 | 0.90 | 1.69 |
| 11-06 01:56 | +10 stop | DOGE | DOWN | 0.51 | 0.29 | -2.53 |
| 11-06 01:56 | +10 stop | BTC | UP | 0.68 | 0.43 | -2.84 |
| 11-06 01:56 | +20 | BTC | UP | 0.68 | no | -6.96 |
| 11-06 01:56 | +15 | BTC | UP | 0.68 | no | -6.96 |
| 11-06 01:56 | +10 | BTC | UP | 0.66 | no | -6.76 |
| 11-06 01:56 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 11-06 01:55 | +10 stop | XRP | DOWN | 0.56 | 0.84 | 2.52 |
| 11-06 01:54 | +10 stop | ZEC | UP | 0.63 | 0.32 | -3.43 |
| 11-06 01:53 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 11-06 01:53 | +15 | BNB | UP | 0.61 | 0.79 | 1.51 |
| 11-06 01:52 | +10 stop | ETH | UP | 0.69 | 0.46 | -2.63 |
| 11-06 01:52 | +5 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-06 01:52 | +10 stop | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 11-06 01:51 | +10 stop | NEAR | UP | 0.53 | 0.65 | 0.86 |
| 11-06 01:51 | +10 | NEAR | UP | 0.53 | 0.65 | 0.86 |
| 11-06 01:51 | +5 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-06 01:51 | +10 stop | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-06 01:51 | +10 stop | DOGE | UP | 0.61 | 0.75 | 1.09 |
| 11-06 01:51 | +10 stop | XRP | UP | 0.59 | 0.41 | -2.14 |
| 11-06 01:51 | +10 | XRP | UP | 0.60 | 0.90 | 2.77 |
| 11-06 01:51 | +5 | XRP | UP | 0.60 | 0.90 | 2.77 |
| 11-06 01:51 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 11-06 01:51 | +10 stop | HYPE | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 01:50 | +10 stop | BNB | DOWN | 0.62 | 0.40 | -2.54 |
| 11-06 01:50 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-06 01:50 | +5 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-06 01:50 | +10 stop | SOL | UP | 0.46 | 0.59 | 0.95 |
| 11-06 01:48 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 11-06 01:48 | +5 | BNB | DOWN | 0.55 | 0.60 | 0.15 |
| 11-06 01:47 | +10 | BNB | UP | 0.42 | 0.54 | 0.84 |
| 11-06 01:47 | +10 stop | SOL | UP | 0.46 | 0.60 | 1.05 |
| 11-06 01:47 | +10 stop | ETH | UP | 0.49 | 0.60 | 0.75 |
