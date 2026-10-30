# Range-Scalp Bot

*Updated Fri Oct 30 14:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40845 | 35648 | 5197 (52) | 2 | $-11423.40 | -4.4% |
| **+10¢** | 30428 | 24417 | 6011 (75) | 3 | $-10190.15 | -5.3% |
| **+15¢** | 25436 | 18964 | 6472 (102) | 5 | $-9226.04 | -5.8% |
| **+20¢** | 22576 | 15794 | 6782 (132) | 7 | $-8137.16 | -5.7% |
| **+10¢ (15¢ stop)** | 49806 | 49736 | 70 (37) | 0 | $-18875.09 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 14:38 | +10 stop | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-30 14:38 | +15 | ETH | DOWN | 0.51 | open |  |
| 10-30 14:38 | +10 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-30 14:38 | +5 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-30 14:37 | +5 | HYPE | DOWN | 0.66 | open |  |
| 10-30 14:36 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-30 14:36 | +10 stop | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 10-30 14:35 | +10 stop | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 14:35 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-30 14:35 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 14:35 | +10 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 14:35 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-30 14:34 | +5 | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-30 14:34 | +10 stop | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 10-30 14:34 | +10 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 10-30 14:34 | +5 | ETH | DOWN | 0.70 | 0.79 | 0.63 |
| 10-30 14:33 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 10-30 14:32 | +5 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 14:32 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.06 |
| 10-30 14:32 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-30 14:32 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-30 14:32 | +5 | NEAR | UP | 0.46 | 0.61 | 1.15 |
| 10-30 14:32 | +5 | HYPE | UP | 0.53 | 0.66 | 0.95 |
| 10-30 14:31 | +10 stop | XRP | DOWN | 0.66 | 0.45 | -2.44 |
| 10-30 14:31 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-30 14:31 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-30 14:31 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-30 14:31 | +5 | XRP | DOWN | 0.66 | 0.75 | 0.60 |
| 10-30 14:31 | +10 stop | NEAR | UP | 0.63 | 0.38 | -2.84 |
| 10-30 14:31 | +20 | NEAR | UP | 0.63 | open |  |
| 10-30 14:31 | +15 | NEAR | UP | 0.63 | open |  |
| 10-30 14:31 | +10 | NEAR | UP | 0.63 | open |  |
| 10-30 14:31 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 10-30 14:31 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-30 14:31 | +20 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-30 14:31 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-30 14:31 | +10 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-30 14:31 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-30 14:31 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-30 14:31 | +15 | SOL | DOWN | 0.69 | 0.86 | 1.46 |
