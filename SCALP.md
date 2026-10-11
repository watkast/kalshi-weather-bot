# Range-Scalp Bot

*Updated Sun Oct 11 15:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12086 | 10431 | 1655 (24) | 4 | $-4001.33 | -5.2% |
| **+10¢** | 9184 | 7262 | 1922 (37) | 2 | $-3774.77 | -6.5% |
| **+15¢** | 7738 | 5698 | 2040 (54) | 3 | $-3211.70 | -6.6% |
| **+20¢** | 6890 | 4766 | 2124 (68) | 5 | $-2704.96 | -6.3% |
| **+10¢ (15¢ stop)** | 14903 | 14862 | 41 (25) | 0 | $-5877.43 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 15:13 | +10 stop | ETH | UP | 0.39 | 0.61 | 1.86 |
| 10-11 15:13 | +15 | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-11 15:13 | +10 | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-11 15:13 | +5 | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-11 15:13 | +10 stop | NEAR | DOWN | 0.70 | 0.89 | 1.70 |
| 10-11 15:13 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.70 |
| 10-11 15:13 | +10 | NEAR | DOWN | 0.70 | 0.89 | 1.70 |
| 10-11 15:13 | +5 | NEAR | DOWN | 0.70 | 0.89 | 1.70 |
| 10-11 15:13 | +10 stop | NEAR | DOWN | 0.41 | 0.62 | 1.76 |
| 10-11 15:13 | +15 | NEAR | DOWN | 0.41 | 0.62 | 1.76 |
| 10-11 15:13 | +10 | NEAR | DOWN | 0.42 | 0.62 | 1.62 |
| 10-11 15:13 | +5 | NEAR | DOWN | 0.44 | 0.62 | 1.45 |
| 10-11 15:12 | +10 stop | XRP | UP | 0.47 | 0.68 | 1.76 |
| 10-11 15:11 | +10 stop | XRP | UP | 0.52 | 0.64 | 0.86 |
| 10-11 15:11 | +10 stop | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 15:10 | +10 | HYPE | DOWN | 0.58 | 0.72 | 1.07 |
| 10-11 15:10 | +10 stop | BTC | DOWN | 0.54 | 0.17 | -3.98 |
| 10-11 15:08 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-11 15:08 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-11 15:08 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-11 15:08 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-11 15:08 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-11 15:07 | +10 stop | BNB | UP | 0.48 | 0.59 | 0.75 |
| 10-11 15:07 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 15:07 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-11 15:07 | +20 | DOGE | DOWN | 0.55 | 0.81 | 2.29 |
| 10-11 15:07 | +15 | DOGE | DOWN | 0.55 | 0.74 | 1.56 |
| 10-11 15:07 | +10 | DOGE | DOWN | 0.55 | 0.68 | 0.94 |
| 10-11 15:07 | +10 stop | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-11 15:07 | +15 | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-11 15:07 | +10 | ETH | DOWN | 0.56 | 0.70 | 1.02 |
| 10-11 15:07 | +5 | ETH | DOWN | 0.56 | 0.65 | 0.51 |
| 10-11 15:06 | +10 stop | BTC | UP | 0.66 | 0.47 | -2.24 |
| 10-11 15:06 | +15 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-11 15:06 | +10 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-11 15:06 | +5 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 10-11 15:06 | +10 stop | BNB | UP | 0.70 | 0.54 | -1.89 |
| 10-11 15:06 | +10 stop | SOL | UP | 0.65 | 0.38 | -3.03 |
| 10-11 15:06 | +20 | SOL | UP | 0.65 | open |  |
| 10-11 15:06 | +15 | SOL | UP | 0.65 | open |  |
