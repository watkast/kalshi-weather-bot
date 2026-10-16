# Range-Scalp Bot

*Updated Fri Oct 16 14:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19411 | 16871 | 2540 (29) | 5 | $-5824.70 | -4.8% |
| **+10¢** | 14632 | 11696 | 2936 (41) | 4 | $-5237.47 | -5.7% |
| **+15¢** | 12244 | 9083 | 3161 (60) | 4 | $-4760.82 | -6.2% |
| **+20¢** | 10860 | 7547 | 3313 (79) | 4 | $-4239.47 | -6.2% |
| **+10¢ (15¢ stop)** | 23869 | 23819 | 50 (29) | 0 | $-9169.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 14:52 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-16 14:52 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-16 14:52 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.20 |
| 10-16 14:52 | +10 stop | NEAR | DOWN | 0.50 | 0.66 | 1.26 |
| 10-16 14:52 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-16 14:52 | +10 stop | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 10-16 14:51 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 10-16 14:51 | +10 stop | NEAR | UP | 0.60 | 0.42 | -2.15 |
| 10-16 14:51 | +10 | NEAR | UP | 0.60 | open |  |
| 10-16 14:51 | +5 | NEAR | UP | 0.60 | open |  |
| 10-16 14:51 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 14:49 | +5 | BTC | UP | 0.57 | open |  |
| 10-16 14:49 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-16 14:48 | +10 stop | BTC | UP | 0.57 | 0.37 | -2.35 |
| 10-16 14:48 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.25 |
| 10-16 14:48 | +5 | HYPE | UP | 0.60 | open |  |
| 10-16 14:48 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.85 |
| 10-16 14:48 | +10 stop | ETH | UP | 0.52 | 0.34 | -2.14 |
| 10-16 14:48 | +20 | ETH | UP | 0.52 | open |  |
| 10-16 14:48 | +15 | ETH | UP | 0.52 | open |  |
| 10-16 14:48 | +10 | ETH | UP | 0.52 | open |  |
| 10-16 14:48 | +5 | ETH | UP | 0.52 | open |  |
| 10-16 14:48 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-16 14:48 | +10 stop | DOGE | UP | 0.66 | 0.51 | -1.84 |
| 10-16 14:48 | +20 | DOGE | UP | 0.66 | open |  |
| 10-16 14:48 | +15 | DOGE | UP | 0.66 | open |  |
| 10-16 14:48 | +10 | DOGE | UP | 0.66 | open |  |
| 10-16 14:48 | +5 | DOGE | UP | 0.66 | open |  |
| 10-16 14:47 | +5 | ZEC | DOWN | 0.49 | 0.64 | 1.15 |
| 10-16 14:47 | +5 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-16 14:47 | +10 stop | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 10-16 14:47 | +20 | NEAR | UP | 0.60 | open |  |
| 10-16 14:47 | +15 | NEAR | UP | 0.60 | open |  |
| 10-16 14:47 | +10 | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 10-16 14:47 | +5 | NEAR | UP | 0.62 | 0.70 | 0.48 |
| 10-16 14:46 | +10 stop | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-16 14:46 | +20 | SOL | DOWN | 0.56 | 0.79 | 2.00 |
| 10-16 14:46 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-16 14:46 | +10 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-16 14:46 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.25 |
