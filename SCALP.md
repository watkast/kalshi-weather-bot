# Range-Scalp Bot

*Updated Mon Oct 12 06:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13191 | 11400 | 1791 (25) | 2 | $-4289.63 | -5.2% |
| **+10¢** | 9999 | 7926 | 2073 (37) | 3 | $-3994.18 | -6.3% |
| **+15¢** | 8407 | 6191 | 2216 (55) | 4 | $-3523.08 | -6.7% |
| **+20¢** | 7487 | 5176 | 2311 (70) | 4 | $-2998.11 | -6.4% |
| **+10¢ (15¢ stop)** | 16253 | 16212 | 41 (25) | 0 | $-6382.49 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 06:57 | +10 | NEAR | UP | 0.53 | open |  |
| 10-12 06:57 | +5 | NEAR | UP | 0.53 | 0.60 | 0.35 |
| 10-12 06:57 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-12 06:57 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-12 06:57 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-12 06:56 | +10 stop | NEAR | UP | 0.67 | 0.49 | -2.14 |
| 10-12 06:55 | +10 stop | HYPE | DOWN | 0.39 | 0.54 | 1.15 |
| 10-12 06:55 | +10 | HYPE | DOWN | 0.40 | 0.54 | 1.05 |
| 10-12 06:55 | +5 | HYPE | DOWN | 0.36 | 0.54 | 1.45 |
| 10-12 06:53 | +10 stop | SOL | UP | 0.56 | 0.79 | 2.00 |
| 10-12 06:53 | +10 stop | DOGE | UP | 0.59 | 0.85 | 2.34 |
| 10-12 06:53 | +10 stop | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-12 06:52 | +10 stop | BNB | UP | 0.56 | 0.74 | 1.48 |
| 10-12 06:51 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-12 06:50 | +10 stop | SOL | DOWN | 0.71 | 0.51 | -2.33 |
| 10-12 06:50 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-12 06:50 | +10 stop | DOGE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-12 06:50 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.80 |
| 10-12 06:50 | +10 stop | ETH | UP | 0.61 | 0.46 | -1.85 |
| 10-12 06:50 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 10-12 06:50 | +15 | BNB | DOWN | 0.51 | open |  |
| 10-12 06:50 | +10 | BNB | DOWN | 0.51 | open |  |
| 10-12 06:50 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 10-12 06:49 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-12 06:49 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-12 06:49 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-12 06:49 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-12 06:47 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.90 |
| 10-12 06:47 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-12 06:47 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-12 06:47 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-12 06:47 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-12 06:47 | +10 stop | BNB | UP | 0.70 | 0.50 | -2.37 |
| 10-12 06:47 | +5 | BNB | UP | 0.70 | 0.81 | 0.80 |
| 10-12 06:47 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-12 06:47 | +10 stop | XRP | UP | 0.67 | 0.45 | -2.54 |
| 10-12 06:47 | +20 | XRP | UP | 0.67 | 0.87 | 1.76 |
| 10-12 06:47 | +15 | XRP | UP | 0.67 | 0.82 | 1.23 |
| 10-12 06:47 | +10 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 10-12 06:47 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
