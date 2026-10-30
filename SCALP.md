# Range-Scalp Bot

*Updated Fri Oct 30 15:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40929 | 35730 | 5199 (52) | 5 | $-11391.88 | -4.4% |
| **+10¢** | 30493 | 24479 | 6014 (75) | 5 | $-10132.87 | -5.3% |
| **+15¢** | 25491 | 19012 | 6479 (102) | 6 | $-9184.52 | -5.7% |
| **+20¢** | 22628 | 15838 | 6790 (132) | 6 | $-8093.34 | -5.7% |
| **+10¢ (15¢ stop)** | 49910 | 49840 | 70 (37) | 0 | $-18882.28 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 15:58 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-30 15:58 | +10 stop | HYPE | UP | 0.55 | 0.37 | -2.15 |
| 10-30 15:58 | +20 | HYPE | UP | 0.55 | open |  |
| 10-30 15:58 | +15 | HYPE | UP | 0.55 | open |  |
| 10-30 15:58 | +10 | HYPE | UP | 0.55 | open |  |
| 10-30 15:58 | +5 | HYPE | UP | 0.55 | open |  |
| 10-30 15:58 | +10 stop | BNB | DOWN | 0.58 | 0.85 | 2.43 |
| 10-30 15:58 | +20 | BNB | DOWN | 0.58 | 0.85 | 2.43 |
| 10-30 15:58 | +15 | BNB | DOWN | 0.58 | 0.85 | 2.43 |
| 10-30 15:58 | +10 | BNB | DOWN | 0.58 | 0.85 | 2.43 |
| 10-30 15:58 | +5 | BNB | DOWN | 0.58 | 0.85 | 2.43 |
| 10-30 15:56 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-30 15:56 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-30 15:56 | +10 stop | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-30 15:56 | +10 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-30 15:55 | +10 stop | BTC | UP | 0.61 | 0.79 | 1.51 |
| 10-30 15:55 | +10 | DOGE | DOWN | 0.40 | 0.59 | 1.56 |
| 10-30 15:54 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-30 15:54 | +10 stop | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 10-30 15:54 | +5 | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 10-30 15:54 | +10 stop | DOGE | DOWN | 0.61 | 0.42 | -2.25 |
| 10-30 15:54 | +10 stop | BTC | UP | 0.55 | 0.66 | 0.76 |
| 10-30 15:53 | +10 stop | SOL | UP | 0.71 | 0.54 | -2.03 |
| 10-30 15:52 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-30 15:52 | +10 stop | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 10-30 15:52 | +20 | BNB | DOWN | 0.63 | 0.87 | 2.15 |
| 10-30 15:52 | +15 | BNB | DOWN | 0.63 | 0.80 | 1.41 |
| 10-30 15:52 | +10 | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 10-30 15:52 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 10-30 15:52 | +10 stop | DOGE | UP | 0.71 | 0.45 | -2.93 |
| 10-30 15:51 | +10 stop | BTC | UP | 0.54 | 0.73 | 1.58 |
| 10-30 15:51 | +5 | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 10-30 15:50 | +10 stop | SOL | UP | 0.58 | 0.75 | 1.38 |
| 10-30 15:50 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 10-30 15:50 | +5 | NEAR | UP | 0.62 | 0.68 | 0.27 |
| 10-30 15:50 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-30 15:50 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.88 |
| 10-30 15:50 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 15:50 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-30 15:50 | +5 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
