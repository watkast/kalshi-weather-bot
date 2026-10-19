# Range-Scalp Bot

*Updated Mon Oct 19 10:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23849 | 20738 | 3111 (31) | 0 | $-7100.99 | -4.7% |
| **+10¢** | 17943 | 14357 | 3586 (45) | 0 | $-6331.77 | -5.6% |
| **+15¢** | 15029 | 11167 | 3862 (68) | 0 | $-5726.59 | -6.1% |
| **+20¢** | 13303 | 9264 | 4039 (86) | 2 | $-5090.77 | -6.1% |
| **+10¢ (15¢ stop)** | 29358 | 29307 | 51 (30) | 0 | $-11089.24 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 10:10 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-19 10:09 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 10:08 | +10 stop | SOL | UP | 0.49 | 0.31 | -2.13 |
| 10-19 10:07 | +10 stop | ETH | UP | 0.53 | 0.37 | -1.95 |
| 10-19 10:07 | +10 stop | XRP | DOWN | 0.56 | 0.80 | 2.08 |
| 10-19 10:07 | +10 stop | NEAR | UP | 0.60 | 0.31 | -3.22 |
| 10-19 10:07 | +10 stop | ETH | UP | 0.50 | 0.67 | 1.36 |
| 10-19 10:07 | +10 stop | XRP | UP | 0.45 | 0.64 | 1.55 |
| 10-19 10:06 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-19 10:06 | +10 stop | ETH | UP | 0.46 | 0.66 | 1.66 |
| 10-19 10:05 | +10 stop | DOGE | UP | 0.58 | 0.30 | -3.12 |
| 10-19 10:05 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-19 10:05 | +10 stop | XRP | UP | 0.56 | 0.39 | -2.02 |
| 10-19 10:05 | +10 stop | SOL | UP | 0.50 | 0.73 | 1.98 |
| 10-19 10:05 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.16 |
| 10-19 10:05 | +20 | ZEC | DOWN | 0.66 | 0.93 | 2.44 |
| 10-19 10:05 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.31 |
| 10-19 10:05 | +10 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-19 10:05 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-19 10:04 | +10 stop | DOGE | UP | 0.67 | 0.52 | -1.84 |
| 10-19 10:04 | +10 stop | NEAR | UP | 0.69 | 0.46 | -2.63 |
| 10-19 10:03 | +10 stop | BTC | UP | 0.59 | 0.76 | 1.40 |
| 10-19 10:03 | +10 stop | HYPE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-19 10:03 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 10-19 10:03 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-19 10:03 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-19 10:03 | +5 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-19 10:03 | +10 stop | ETH | DOWN | 0.62 | 0.46 | -1.95 |
| 10-19 10:03 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-19 10:03 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 10:03 | +10 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 10:03 | +5 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 10:02 | +10 stop | DOGE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-19 10:02 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-19 10:01 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 10-19 10:01 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-19 10:01 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 10-19 10:01 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 10:01 | +5 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-19 10:01 | +10 stop | XRP | DOWN | 0.64 | 0.48 | -1.95 |
