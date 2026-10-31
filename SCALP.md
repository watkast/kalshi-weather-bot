# Range-Scalp Bot

*Updated Sat Oct 31 05:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41815 | 36487 | 5328 (54) | 4 | $-11730.52 | -4.5% |
| **+10¢** | 31168 | 25000 | 6168 (78) | 4 | $-10489.39 | -5.3% |
| **+15¢** | 26053 | 19403 | 6650 (106) | 4 | $-9580.56 | -5.9% |
| **+20¢** | 23132 | 16169 | 6963 (137) | 6 | $-8429.30 | -5.8% |
| **+10¢ (15¢ stop)** | 50971 | 50896 | 75 (41) | 4 | $-19233.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 05:20 | +5 | ETH | UP | 0.68 | open |  |
| 10-31 05:20 | +10 stop | ETH | UP | 0.60 | open |  |
| 10-31 05:20 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-31 05:20 | +10 | XRP | UP | 0.65 | open |  |
| 10-31 05:20 | +5 | XRP | UP | 0.65 | open |  |
| 10-31 05:20 | +10 stop | DOGE | UP | 0.49 | 0.34 | -1.84 |
| 10-31 05:19 | +10 stop | BTC | UP | 0.60 | open |  |
| 10-31 05:19 | +10 stop | HYPE | UP | 0.64 | 0.43 | -2.49 |
| 10-31 05:19 | +10 stop | BNB | UP | 0.56 | open |  |
| 10-31 05:18 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 10-31 05:18 | +10 stop | HYPE | UP | 0.58 | 0.69 | 0.73 |
| 10-31 05:18 | +10 stop | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-31 05:18 | +10 | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 10-31 05:18 | +5 | ZEC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-31 05:17 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-31 05:17 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-31 05:16 | +10 stop | ZEC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-31 05:16 | +20 | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-31 05:16 | +15 | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-31 05:16 | +10 | ZEC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-31 05:16 | +5 | ZEC | DOWN | 0.56 | 0.65 | 0.56 |
| 10-31 05:16 | +10 stop | XRP | UP | 0.68 | open |  |
| 10-31 05:16 | +20 | XRP | UP | 0.66 | open |  |
| 10-31 05:16 | +15 | XRP | UP | 0.66 | open |  |
| 10-31 05:16 | +10 | XRP | UP | 0.66 | 0.77 | 0.81 |
| 10-31 05:16 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 10-31 05:16 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.42 |
| 10-31 05:16 | +10 stop | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-31 05:16 | +20 | NEAR | UP | 0.66 | 0.86 | 1.75 |
| 10-31 05:16 | +15 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 10-31 05:16 | +10 | NEAR | UP | 0.66 | 0.79 | 1.02 |
| 10-31 05:16 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-31 05:16 | +10 stop | BTC | DOWN | 0.58 | 0.36 | -2.55 |
| 10-31 05:16 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-31 05:16 | +15 | BTC | DOWN | 0.58 | open |  |
| 10-31 05:16 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-31 05:16 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-31 05:16 | +10 stop | SOL | UP | 0.59 | 0.74 | 1.19 |
| 10-31 05:16 | +20 | SOL | UP | 0.59 | 0.80 | 1.81 |
| 10-31 05:16 | +15 | SOL | UP | 0.59 | 0.74 | 1.19 |
