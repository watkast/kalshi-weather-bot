# Range-Scalp Bot

*Updated Fri Nov 27 00:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73107 | 63803 | 9304 (158) | 1 | $-19529.12 | -4.2% |
| **+10¢** | 54504 | 43642 | 10862 (204) | 1 | $-18116.55 | -5.3% |
| **+15¢** | 45639 | 33936 | 11703 (262) | 1 | $-16237.83 | -5.7% |
| **+20¢** | 40614 | 28292 | 12322 (328) | 1 | $-14633.78 | -5.7% |
| **+10¢ (15¢ stop)** | 89038 | 88829 | 209 (128) | 1 | $-32856.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 00:06 | +10 stop | BTC | UP | 0.64 | open |  |
| 11-27 00:06 | +20 | BTC | UP | 0.64 | open |  |
| 11-27 00:06 | +15 | BTC | UP | 0.64 | open |  |
| 11-27 00:06 | +10 | BTC | UP | 0.64 | open |  |
| 11-27 00:06 | +5 | BTC | UP | 0.64 | open |  |
| 11-27 00:00 | +10 stop | NEAR | UP | 0.55 | 0.74 | 1.56 |
| 11-27 00:00 | +20 | NEAR | UP | 0.55 | 0.77 | 1.87 |
| 11-27 00:00 | +15 | NEAR | UP | 0.55 | 0.74 | 1.56 |
| 11-27 00:00 | +10 | NEAR | UP | 0.55 | 0.74 | 1.56 |
| 11-27 00:00 | +5 | NEAR | UP | 0.55 | 0.64 | 0.53 |
| 11-26 23:58 | +10 stop | SOL | DOWN | 0.47 | 0.63 | 1.25 |
| 11-26 23:58 | +10 | SOL | DOWN | 0.47 | 0.63 | 1.27 |
| 11-26 23:58 | +5 | SOL | DOWN | 0.47 | 0.63 | 1.23 |
| 11-26 23:58 | +5 | HYPE | DOWN | 0.24 | 0.58 | 3.09 |
| 11-26 23:58 | +10 stop | HYPE | DOWN | 0.36 | 0.58 | 1.85 |
| 11-26 23:56 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 23:56 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 23:56 | +10 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 23:56 | +5 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-26 23:56 | +10 stop | HYPE | UP | 0.70 | 0.52 | -2.13 |
| 11-26 23:55 | +10 stop | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-26 23:55 | +20 | ZEC | DOWN | 0.61 | 0.92 | 2.84 |
| 11-26 23:55 | +15 | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-26 23:55 | +10 | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-26 23:55 | +5 | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-26 23:54 | +10 stop | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 11-26 23:53 | +10 stop | SOL | DOWN | 0.54 | 0.71 | 1.37 |
| 11-26 23:53 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 11-26 23:52 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.15 |
| 11-26 23:52 | +10 | HYPE | DOWN | 0.56 | yes | -5.78 |
| 11-26 23:52 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-26 23:52 | +10 stop | XRP | UP | 0.64 | 0.77 | 1.00 |
| 11-26 23:51 | +10 stop | DOGE | DOWN | 0.53 | 0.34 | -2.24 |
| 11-26 23:50 | +10 stop | ETH | UP | 0.54 | 0.69 | 1.17 |
| 11-26 23:50 | +10 stop | BTC | UP | 0.66 | 0.79 | 1.02 |
| 11-26 23:50 | +10 stop | NEAR | UP | 0.55 | 0.69 | 1.03 |
| 11-26 23:50 | +10 stop | BNB | UP | 0.58 | 0.75 | 1.38 |
| 11-26 23:49 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 11-26 23:49 | +10 stop | DOGE | DOWN | 0.66 | 0.46 | -2.34 |
| 11-26 23:49 | +10 stop | ETH | DOWN | 0.55 | 0.39 | -1.95 |
