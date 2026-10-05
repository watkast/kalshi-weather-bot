# Range-Scalp Bot

*Updated Mon Oct 05 20:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4281 | 3689 | 592 (4) | 1 | $-1479.92 | -5.5% |
| **+10¢** | 3300 | 2616 | 684 (5) | 2 | $-1358.84 | -6.5% |
| **+15¢** | 2766 | 2044 | 722 (8) | 2 | $-1179.95 | -6.8% |
| **+20¢** | 2473 | 1720 | 753 (13) | 2 | $-1010.96 | -6.5% |
| **+10¢ (15¢ stop)** | 5267 | 5262 | 5 (2) | 0 | $-1901.85 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 20:36 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-05 20:36 | +5 | BTC | UP | 0.67 | 0.75 | 0.50 |
| 10-05 20:36 | +10 stop | BTC | DOWN | 0.56 | 0.33 | -2.64 |
| 10-05 20:36 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-05 20:36 | +15 | BTC | DOWN | 0.56 | open |  |
| 10-05 20:36 | +10 | BTC | DOWN | 0.56 | open |  |
| 10-05 20:36 | +5 | BTC | DOWN | 0.56 | 0.61 | 0.15 |
| 10-05 20:35 | +5 | ETH | UP | 0.52 | 0.60 | 0.46 |
| 10-05 20:35 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-05 20:34 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-05 20:33 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-05 20:33 | +10 | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-05 20:33 | +5 | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-05 20:33 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-05 20:33 | +20 | ETH | UP | 0.63 | 0.86 | 2.04 |
| 10-05 20:33 | +15 | ETH | UP | 0.63 | 0.86 | 2.04 |
| 10-05 20:33 | +10 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-05 20:33 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 10-05 20:33 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.90 |
| 10-05 20:33 | +10 | BNB | UP | 0.62 | 0.74 | 0.90 |
| 10-05 20:33 | +5 | BNB | UP | 0.64 | 0.71 | 0.41 |
| 10-05 20:32 | +10 stop | BTC | DOWN | 0.50 | 0.68 | 1.46 |
| 10-05 20:32 | +20 | BTC | DOWN | 0.50 | 0.77 | 2.39 |
| 10-05 20:32 | +15 | BTC | DOWN | 0.50 | 0.68 | 1.46 |
| 10-05 20:32 | +10 | BTC | DOWN | 0.50 | 0.68 | 1.46 |
| 10-05 20:32 | +5 | BTC | DOWN | 0.50 | 0.68 | 1.46 |
| 10-05 20:31 | +10 stop | HYPE | UP | 0.68 | 0.82 | 1.13 |
| 10-05 20:31 | +5 | DOGE | UP | 0.56 | 0.63 | 0.35 |
| 10-05 20:31 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-05 20:31 | +20 | BNB | UP | 0.62 | 0.86 | 2.14 |
| 10-05 20:31 | +15 | BNB | UP | 0.62 | 0.78 | 1.30 |
| 10-05 20:31 | +10 | BNB | UP | 0.62 | 0.72 | 0.68 |
| 10-05 20:31 | +5 | BNB | UP | 0.62 | 0.70 | 0.48 |
| 10-05 20:31 | +10 stop | NEAR | UP | 0.58 | 0.73 | 1.19 |
| 10-05 20:31 | +20 | NEAR | UP | 0.58 | 0.85 | 2.44 |
| 10-05 20:31 | +15 | NEAR | UP | 0.58 | 0.73 | 1.19 |
| 10-05 20:31 | +10 | NEAR | UP | 0.58 | 0.73 | 1.19 |
| 10-05 20:31 | +5 | NEAR | UP | 0.58 | 0.64 | 0.26 |
| 10-05 20:31 | +10 stop | DOGE | UP | 0.52 | 0.63 | 0.75 |
| 10-05 20:31 | +20 | DOGE | UP | 0.52 | 0.76 | 2.09 |
