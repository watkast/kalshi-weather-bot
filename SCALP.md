# Range-Scalp Bot

*Updated Wed Oct 14 07:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15670 | 13569 | 2101 (27) | 3 | $-4953.85 | -5.0% |
| **+10¢** | 11859 | 9420 | 2439 (39) | 3 | $-4616.62 | -6.2% |
| **+15¢** | 9956 | 7341 | 2615 (58) | 3 | $-4142.89 | -6.6% |
| **+20¢** | 8850 | 6109 | 2741 (75) | 5 | $-3685.88 | -6.6% |
| **+10¢ (15¢ stop)** | 19267 | 19217 | 50 (29) | 0 | $-7434.49 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 07:41 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 10-14 07:41 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-14 07:40 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-14 07:40 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-14 07:40 | +15 | ETH | DOWN | 0.68 | 0.85 | 1.45 |
| 10-14 07:40 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-14 07:40 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 10-14 07:39 | +10 stop | BTC | DOWN | 0.52 | 0.62 | 0.65 |
| 10-14 07:38 | +10 | DOGE | UP | 0.58 | 0.74 | 1.29 |
| 10-14 07:38 | +10 stop | HYPE | DOWN | 0.67 | 0.41 | -2.93 |
| 10-14 07:38 | +5 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-14 07:37 | +10 stop | ETH | DOWN | 0.59 | 0.34 | -2.79 |
| 10-14 07:37 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.76 |
| 10-14 07:37 | +10 stop | DOGE | UP | 0.66 | 0.26 | -4.30 |
| 10-14 07:37 | +5 | DOGE | UP | 0.66 | 0.74 | 0.50 |
| 10-14 07:36 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-14 07:36 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 10-14 07:36 | +10 stop | SOL | DOWN | 0.67 | 0.82 | 1.27 |
| 10-14 07:36 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.90 |
| 10-14 07:36 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.27 |
| 10-14 07:36 | +10 | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 10-14 07:36 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-14 07:34 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-14 07:34 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-14 07:34 | +10 | NEAR | DOWN | 0.68 | 0.81 | 1.03 |
| 10-14 07:34 | +10 stop | BNB | DOWN | 0.70 | 0.49 | -2.43 |
| 10-14 07:34 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-14 07:34 | +10 stop | ETH | DOWN | 0.71 | 0.54 | -2.03 |
| 10-14 07:34 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 10-14 07:33 | +10 stop | BTC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-14 07:33 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-14 07:33 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-14 07:33 | +10 stop | DOGE | UP | 0.53 | 0.32 | -2.44 |
| 10-14 07:33 | +10 | DOGE | UP | 0.53 | 0.65 | 0.86 |
| 10-14 07:33 | +5 | DOGE | UP | 0.57 | 0.66 | 0.56 |
| 10-14 07:32 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 10-14 07:32 | +20 | BTC | UP | 0.62 | open |  |
| 10-14 07:32 | +15 | BTC | UP | 0.62 | open |  |
| 10-14 07:32 | +10 | BTC | UP | 0.62 | open |  |
| 10-14 07:32 | +5 | BTC | UP | 0.62 | open |  |
