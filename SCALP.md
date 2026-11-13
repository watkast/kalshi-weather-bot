# Range-Scalp Bot

*Updated Fri Nov 13 05:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57910 | 50519 | 7391 (101) | 2 | $-15706.91 | -4.3% |
| **+10¢** | 43272 | 34637 | 8635 (133) | 2 | $-14655.31 | -5.4% |
| **+15¢** | 36272 | 26978 | 9294 (167) | 4 | $-13202.40 | -5.8% |
| **+20¢** | 32310 | 22554 | 9756 (217) | 4 | $-11595.18 | -5.7% |
| **+10¢ (15¢ stop)** | 70579 | 70451 | 128 (78) | 0 | $-25973.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 05:26 | +10 stop | DOGE | UP | 0.71 | 0.55 | -1.93 |
| 11-13 05:26 | +20 | DOGE | UP | 0.71 | open |  |
| 11-13 05:26 | +15 | DOGE | UP | 0.70 | open |  |
| 11-13 05:26 | +10 | DOGE | UP | 0.70 | open |  |
| 11-13 05:26 | +5 | DOGE | UP | 0.71 | open |  |
| 11-13 05:26 | +10 stop | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-13 05:26 | +10 stop | BNB | UP | 0.58 | 0.39 | -2.25 |
| 11-13 05:26 | +20 | BNB | UP | 0.58 | open |  |
| 11-13 05:26 | +15 | BNB | UP | 0.58 | open |  |
| 11-13 05:26 | +10 | BNB | UP | 0.59 | open |  |
| 11-13 05:26 | +5 | BNB | UP | 0.59 | open |  |
| 11-13 05:24 | +10 stop | BTC | UP | 0.66 | 0.48 | -2.14 |
| 11-13 05:23 | +5 | ETH | DOWN | 0.54 | 0.61 | 0.35 |
| 11-13 05:22 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-13 05:22 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-13 05:22 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-13 05:21 | +5 | NEAR | UP | 0.65 | 0.72 | 0.39 |
| 11-13 05:21 | +10 stop | BNB | UP | 0.59 | 0.78 | 1.60 |
| 11-13 05:21 | +10 | BNB | UP | 0.59 | 0.78 | 1.60 |
| 11-13 05:21 | +5 | BNB | UP | 0.59 | 0.65 | 0.27 |
| 11-13 05:20 | +10 stop | SOL | UP | 0.57 | 0.68 | 0.76 |
| 11-13 05:20 | +10 | SOL | UP | 0.57 | 0.68 | 0.76 |
| 11-13 05:20 | +5 | SOL | UP | 0.57 | 0.68 | 0.76 |
| 11-13 05:20 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 05:20 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 05:20 | +5 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 05:19 | +10 stop | BTC | DOWN | 0.56 | 0.35 | -2.44 |
| 11-13 05:19 | +10 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-13 05:19 | +5 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-13 05:19 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 11-13 05:19 | +20 | NEAR | UP | 0.68 | 0.89 | 1.87 |
| 11-13 05:19 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-13 05:19 | +10 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-13 05:19 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 11-13 05:19 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-13 05:19 | +20 | ZEC | UP | 0.66 | 0.94 | 2.63 |
| 11-13 05:19 | +15 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 11-13 05:19 | +10 | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-13 05:19 | +5 | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-13 05:19 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
