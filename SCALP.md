# Range-Scalp Bot

*Updated Fri Oct 30 14:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40868 | 35670 | 5198 (52) | 2 | $-11420.57 | -4.4% |
| **+10¢** | 30443 | 24431 | 6012 (75) | 2 | $-10180.03 | -5.3% |
| **+15¢** | 25450 | 18975 | 6475 (102) | 2 | $-9225.29 | -5.8% |
| **+20¢** | 22591 | 15805 | 6786 (132) | 2 | $-8140.02 | -5.7% |
| **+10¢ (15¢ stop)** | 49840 | 49770 | 70 (37) | 0 | $-18890.63 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 14:56 | +10 stop | ZEC | UP | 0.71 | 0.48 | -2.63 |
| 10-30 14:56 | +5 | ZEC | UP | 0.71 | open |  |
| 10-30 14:54 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-30 14:54 | +5 | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-30 14:54 | +10 stop | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-30 14:54 | +10 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-30 14:54 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 10-30 14:54 | +10 stop | BNB | UP | 0.69 | 0.86 | 1.46 |
| 10-30 14:54 | +15 | BNB | UP | 0.69 | 0.86 | 1.46 |
| 10-30 14:54 | +10 | BNB | UP | 0.69 | 0.86 | 1.46 |
| 10-30 14:54 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 10-30 14:54 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 10-30 14:53 | +10 stop | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 10-30 14:53 | +5 | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 10-30 14:53 | +10 stop | ETH | UP | 0.65 | 0.77 | 0.91 |
| 10-30 14:53 | +10 | ETH | UP | 0.65 | 0.77 | 0.91 |
| 10-30 14:53 | +5 | ETH | UP | 0.65 | 0.77 | 0.91 |
| 10-30 14:53 | +5 | NEAR | UP | 0.63 | 0.70 | 0.38 |
| 10-30 14:53 | +10 stop | XRP | UP | 0.46 | 0.68 | 1.86 |
| 10-30 14:53 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-30 14:52 | +5 | DOGE | UP | 0.71 | 0.77 | 0.32 |
| 10-30 14:51 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.30 |
| 10-30 14:51 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-30 14:51 | +10 stop | HYPE | DOWN | 0.53 | 0.34 | -2.24 |
| 10-30 14:51 | +10 stop | DOGE | UP | 0.61 | 0.77 | 1.27 |
| 10-30 14:51 | +5 | DOGE | UP | 0.61 | 0.70 | 0.55 |
| 10-30 14:51 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-30 14:51 | +10 | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-30 14:51 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-30 14:51 | +10 stop | XRP | DOWN | 0.61 | 0.43 | -2.15 |
| 10-30 14:50 | +10 stop | BNB | UP | 0.49 | 0.62 | 0.95 |
| 10-30 14:50 | +10 stop | SOL | UP | 0.57 | 0.38 | -2.25 |
| 10-30 14:50 | +10 stop | ZEC | UP | 0.53 | 0.66 | 0.96 |
| 10-30 14:49 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.95 |
| 10-30 14:49 | +10 stop | HYPE | UP | 0.59 | 0.40 | -2.24 |
| 10-30 14:49 | +10 stop | SOL | UP | 0.44 | 0.54 | 0.64 |
| 10-30 14:48 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-30 14:47 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-30 14:47 | +10 stop | XRP | UP | 0.67 | 0.51 | -1.94 |
| 10-30 14:47 | +10 stop | ZEC | DOWN | 0.51 | 0.62 | 0.75 |
