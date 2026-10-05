# Range-Scalp Bot

*Updated Mon Oct 05 03:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3203 | 2743 | 460 (3) | 4 | $-1197.91 | -5.9% |
| **+10¢** | 2487 | 1965 | 522 (4) | 3 | $-1056.88 | -6.7% |
| **+15¢** | 2099 | 1549 | 550 (5) | 3 | $-925.00 | -7.0% |
| **+20¢** | 1873 | 1296 | 577 (10) | 3 | $-821.91 | -7.0% |
| **+10¢ (15¢ stop)** | 3995 | 3994 | 1 (1) | 0 | $-1558.46 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 03:38 | +10 stop | NEAR | DOWN | 0.55 | 0.39 | -1.95 |
| 10-05 03:37 | +10 stop | DOGE | DOWN | 0.67 | 0.19 | -5.07 |
| 10-05 03:37 | +10 stop | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 10-05 03:37 | +5 | HYPE | UP | 0.64 | 0.73 | 0.59 |
| 10-05 03:35 | +10 stop | DOGE | UP | 0.65 | 0.48 | -2.04 |
| 10-05 03:35 | +10 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 10-05 03:35 | +5 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 10-05 03:35 | +10 stop | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-05 03:35 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-05 03:35 | +15 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-05 03:35 | +10 | BNB | DOWN | 0.66 | 0.87 | 1.86 |
| 10-05 03:34 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-05 03:34 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-05 03:34 | +10 stop | ETH | DOWN | 0.68 | 0.82 | 1.18 |
| 10-05 03:34 | +20 | ETH | DOWN | 0.68 | 0.95 | 2.51 |
| 10-05 03:34 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.29 |
| 10-05 03:34 | +10 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-05 03:34 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-05 03:34 | +10 stop | NEAR | DOWN | 0.70 | 0.53 | -2.00 |
| 10-05 03:33 | +10 stop | ZEC | DOWN | 0.64 | 0.79 | 1.19 |
| 10-05 03:33 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-05 03:33 | +20 | SOL | DOWN | 0.62 | 0.86 | 2.14 |
| 10-05 03:33 | +15 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 03:33 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-05 03:33 | +5 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-05 03:33 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 10-05 03:32 | +10 stop | NEAR | UP | 0.59 | 0.42 | -2.04 |
| 10-05 03:32 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-05 03:32 | +20 | DOGE | UP | 0.64 | 0.86 | 1.94 |
| 10-05 03:32 | +15 | DOGE | UP | 0.64 | 0.80 | 1.31 |
| 10-05 03:32 | +10 | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-05 03:32 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 10-05 03:32 | +10 stop | XRP | UP | 0.51 | 0.29 | -2.53 |
| 10-05 03:32 | +20 | XRP | UP | 0.52 | open |  |
| 10-05 03:32 | +15 | XRP | UP | 0.52 | open |  |
| 10-05 03:32 | +10 | XRP | UP | 0.52 | open |  |
| 10-05 03:32 | +5 | XRP | UP | 0.52 | open |  |
| 10-05 03:32 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-05 03:32 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-05 03:32 | +20 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
