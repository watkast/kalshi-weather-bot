# Range-Scalp Bot

*Updated Mon Oct 19 16:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24270 | 21109 | 3161 (31) | 1 | $-7206.92 | -4.7% |
| **+10¢** | 18250 | 14600 | 3650 (46) | 2 | $-6444.21 | -5.6% |
| **+15¢** | 15287 | 11357 | 3930 (69) | 2 | $-5832.49 | -6.1% |
| **+20¢** | 13528 | 9414 | 4114 (87) | 3 | $-5235.53 | -6.2% |
| **+10¢ (15¢ stop)** | 29865 | 29813 | 52 (30) | 1 | $-11341.59 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 16:42 | +10 stop | ETH | UP | 0.57 | open |  |
| 10-19 16:42 | +15 | ETH | UP | 0.57 | open |  |
| 10-19 16:42 | +10 | ETH | UP | 0.57 | open |  |
| 10-19 16:42 | +5 | ETH | UP | 0.57 | 0.65 | 0.46 |
| 10-19 16:39 | +10 stop | BNB | DOWN | 0.67 | 0.43 | -2.74 |
| 10-19 16:38 | +5 | DOGE | DOWN | 0.69 | 0.88 | 1.67 |
| 10-19 16:38 | +10 stop | NEAR | DOWN | 0.66 | 0.85 | 1.65 |
| 10-19 16:38 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 10-19 16:38 | +15 | NEAR | DOWN | 0.66 | 0.85 | 1.65 |
| 10-19 16:38 | +10 | NEAR | DOWN | 0.66 | 0.85 | 1.65 |
| 10-19 16:38 | +5 | NEAR | DOWN | 0.66 | 0.72 | 0.29 |
| 10-19 16:38 | +10 stop | ETH | DOWN | 0.62 | 0.46 | -1.95 |
| 10-19 16:38 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 10-19 16:38 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 10-19 16:37 | +10 stop | BNB | UP | 0.63 | 0.38 | -2.84 |
| 10-19 16:37 | +10 stop | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 10-19 16:37 | +10 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 10-19 16:37 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-19 16:37 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-19 16:37 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-19 16:36 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 16:36 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 16:36 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 10-19 16:36 | +10 stop | BNB | DOWN | 0.64 | 0.46 | -2.15 |
| 10-19 16:35 | +5 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 16:34 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-19 16:34 | +10 | XRP | DOWN | 0.67 | 0.81 | 1.13 |
| 10-19 16:34 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 10-19 16:34 | +10 stop | SOL | DOWN | 0.61 | 0.79 | 1.51 |
| 10-19 16:34 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 10-19 16:34 | +10 | ETH | DOWN | 0.55 | 0.72 | 1.38 |
| 10-19 16:34 | +5 | ETH | DOWN | 0.55 | 0.72 | 1.38 |
| 10-19 16:34 | +10 stop | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-19 16:34 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-19 16:34 | +10 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-19 16:34 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-19 16:33 | +10 stop | ETH | DOWN | 0.68 | 0.51 | -2.04 |
| 10-19 16:33 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-19 16:33 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.88 |
| 10-19 16:33 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
