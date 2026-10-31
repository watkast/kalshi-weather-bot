# Range-Scalp Bot

*Updated Sat Oct 31 01:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41565 | 36271 | 5294 (54) | 3 | $-11645.73 | -4.4% |
| **+10¢** | 30982 | 24856 | 6126 (78) | 3 | $-10388.07 | -5.3% |
| **+15¢** | 25895 | 19293 | 6602 (106) | 5 | $-9458.62 | -5.8% |
| **+20¢** | 22984 | 16071 | 6913 (137) | 7 | $-8328.50 | -5.8% |
| **+10¢ (15¢ stop)** | 50656 | 50581 | 75 (41) | 0 | $-19144.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 01:35 | +10 stop | NEAR | UP | 0.64 | 0.80 | 1.30 |
| 10-31 01:35 | +10 stop | BNB | UP | 0.69 | 0.82 | 1.04 |
| 10-31 01:35 | +10 stop | BTC | UP | 0.58 | 0.74 | 1.28 |
| 10-31 01:35 | +10 stop | XRP | UP | 0.66 | 0.80 | 1.12 |
| 10-31 01:34 | +10 stop | HYPE | UP | 0.63 | 0.83 | 1.69 |
| 10-31 01:33 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 10-31 01:33 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-31 01:33 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-31 01:33 | +5 | ZEC | UP | 0.70 | 0.79 | 0.63 |
| 10-31 01:33 | +5 | DOGE | UP | 0.71 | 0.79 | 0.53 |
| 10-31 01:33 | +10 stop | BTC | UP | 0.66 | 0.48 | -2.14 |
| 10-31 01:33 | +15 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-31 01:33 | +10 | BTC | UP | 0.66 | 0.79 | 1.02 |
| 10-31 01:33 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 10-31 01:32 | +10 stop | NEAR | DOWN | 0.65 | 0.47 | -2.14 |
| 10-31 01:32 | +10 | NEAR | DOWN | 0.65 | open |  |
| 10-31 01:32 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-31 01:32 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-31 01:32 | +10 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-31 01:32 | +5 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-31 01:32 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 10-31 01:32 | +10 stop | SOL | UP | 0.56 | 0.71 | 1.17 |
| 10-31 01:32 | +10 | SOL | UP | 0.55 | 0.71 | 1.27 |
| 10-31 01:32 | +5 | SOL | UP | 0.55 | 0.71 | 1.27 |
| 10-31 01:32 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-31 01:32 | +15 | DOGE | UP | 0.60 | 0.79 | 1.61 |
| 10-31 01:32 | +10 | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-31 01:32 | +5 | DOGE | UP | 0.60 | 0.69 | 0.58 |
| 10-31 01:32 | +10 stop | ZEC | UP | 0.57 | 0.68 | 0.76 |
| 10-31 01:32 | +20 | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 10-31 01:32 | +15 | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 10-31 01:32 | +10 | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 10-31 01:32 | +5 | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 10-31 01:31 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-31 01:31 | +5 | BNB | DOWN | 0.61 | open |  |
| 10-31 01:31 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 10-31 01:31 | +20 | HYPE | UP | 0.68 | 0.90 | 2.01 |
| 10-31 01:31 | +15 | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 10-31 01:31 | +10 | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 10-31 01:31 | +5 | HYPE | UP | 0.68 | 0.76 | 0.51 |
