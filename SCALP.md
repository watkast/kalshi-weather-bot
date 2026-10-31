# Range-Scalp Bot

*Updated Sat Oct 31 01:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41515 | 36230 | 5285 (54) | 1 | $-11614.03 | -4.4% |
| **+10¢** | 30944 | 24829 | 6115 (78) | 1 | $-10348.93 | -5.3% |
| **+15¢** | 25870 | 19279 | 6591 (106) | 1 | $-9412.66 | -5.8% |
| **+20¢** | 22964 | 16063 | 6901 (137) | 2 | $-8272.47 | -5.7% |
| **+10¢ (15¢ stop)** | 50598 | 50523 | 75 (41) | 0 | $-19111.02 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 00:56 | +10 stop | ETH | UP | 0.60 | 0.87 | 2.45 |
| 10-31 00:56 | +10 stop | ZEC | DOWN | 0.58 | 0.89 | 2.85 |
| 10-31 00:55 | +10 stop | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 10-31 00:55 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 00:55 | +5 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 00:53 | +10 stop | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-31 00:53 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.86 |
| 10-31 00:53 | +15 | ZEC | DOWN | 0.61 | 0.89 | 2.55 |
| 10-31 00:53 | +10 | ZEC | DOWN | 0.61 | 0.89 | 2.55 |
| 10-31 00:53 | +5 | ZEC | DOWN | 0.61 | 0.89 | 2.55 |
| 10-31 00:52 | +10 stop | ETH | UP | 0.47 | 0.65 | 1.46 |
| 10-31 00:52 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 10-31 00:52 | +10 stop | NEAR | UP | 0.68 | 0.53 | -1.84 |
| 10-31 00:52 | +10 stop | XRP | DOWN | 0.67 | 0.82 | 1.21 |
| 10-31 00:51 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.52 |
| 10-31 00:51 | +10 stop | ETH | UP | 0.65 | 0.48 | -2.04 |
| 10-31 00:51 | +15 | ETH | UP | 0.65 | 0.87 | 1.96 |
| 10-31 00:51 | +10 | ETH | UP | 0.64 | 0.87 | 2.05 |
| 10-31 00:51 | +5 | ETH | UP | 0.64 | 0.87 | 2.05 |
| 10-31 00:49 | +10 stop | NEAR | UP | 0.67 | 0.84 | 1.44 |
| 10-31 00:49 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-31 00:48 | +10 stop | XRP | UP | 0.61 | 0.43 | -2.15 |
| 10-31 00:48 | +10 | XRP | UP | 0.61 | 0.78 | 1.40 |
| 10-31 00:48 | +10 stop | DOGE | UP | 0.67 | 0.46 | -2.44 |
| 10-31 00:48 | +5 | ZEC | UP | 0.68 | 0.76 | 0.51 |
| 10-31 00:48 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 10-31 00:48 | +20 | HYPE | DOWN | 0.61 | 0.83 | 1.93 |
| 10-31 00:48 | +15 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 10-31 00:48 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 00:48 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 00:47 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-31 00:47 | +20 | BTC | UP | 0.63 | 0.86 | 2.04 |
| 10-31 00:47 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 10-31 00:47 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-31 00:47 | +5 | BTC | UP | 0.63 | 0.72 | 0.58 |
| 10-31 00:47 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 10-31 00:47 | +10 stop | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 10-31 00:47 | +10 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 10-31 00:47 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-31 00:47 | +10 stop | DOGE | DOWN | 0.60 | 0.42 | -2.15 |
