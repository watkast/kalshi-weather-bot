# Range-Scalp Bot

*Updated Mon Oct 19 01:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23270 | 20233 | 3037 (30) | 4 | $-6942.72 | -4.7% |
| **+10¢** | 17501 | 13999 | 3502 (44) | 5 | $-6202.95 | -5.6% |
| **+15¢** | 14671 | 10896 | 3775 (66) | 6 | $-5642.33 | -6.1% |
| **+20¢** | 12985 | 9037 | 3948 (84) | 7 | $-5024.21 | -6.2% |
| **+10¢ (15¢ stop)** | 28645 | 28594 | 51 (30) | 2 | $-10925.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 01:26 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.40 |
| 10-19 01:26 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-19 01:26 | +10 stop | NEAR | UP | 0.43 | 0.53 | 0.64 |
| 10-19 01:26 | +10 stop | ZEC | UP | 0.59 | 0.79 | 1.74 |
| 10-19 01:26 | +15 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 10-19 01:26 | +10 | ZEC | UP | 0.59 | 0.79 | 1.71 |
| 10-19 01:25 | +10 stop | XRP | UP | 0.63 | open |  |
| 10-19 01:24 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
| 10-19 01:24 | +10 stop | DOGE | UP | 0.58 | 0.42 | -1.96 |
| 10-19 01:24 | +5 | ZEC | UP | 0.70 | 0.79 | 0.63 |
| 10-19 01:23 | +10 stop | ZEC | UP | 0.55 | 0.72 | 1.39 |
| 10-19 01:23 | +10 | ZEC | UP | 0.55 | 0.72 | 1.39 |
| 10-19 01:23 | +5 | ZEC | UP | 0.55 | 0.64 | 0.57 |
| 10-19 01:23 | +10 stop | NEAR | UP | 0.71 | 0.55 | -1.93 |
| 10-19 01:22 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-19 01:22 | +5 | SOL | UP | 0.67 | 0.77 | 0.72 |
| 10-19 01:22 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-19 01:21 | +5 | BTC | UP | 0.62 | open |  |
| 10-19 01:21 | +10 stop | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-19 01:20 | +5 | BNB | UP | 0.70 | 0.83 | 1.01 |
| 10-19 01:20 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-19 01:20 | +10 stop | BTC | UP | 0.56 | 0.39 | -2.05 |
| 10-19 01:20 | +10 stop | HYPE | UP | 0.59 | 0.38 | -2.44 |
| 10-19 01:19 | +5 | BNB | UP | 0.62 | 0.70 | 0.48 |
| 10-19 01:19 | +5 | SOL | UP | 0.62 | 0.68 | 0.22 |
| 10-19 01:19 | +10 stop | DOGE | UP | 0.53 | 0.74 | 1.78 |
| 10-19 01:18 | +10 stop | XRP | UP | 0.62 | 0.77 | 1.20 |
| 10-19 01:18 | +5 | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-19 01:18 | +10 stop | ZEC | UP | 0.53 | 0.66 | 0.96 |
| 10-19 01:18 | +20 | ZEC | UP | 0.53 | 0.79 | 2.30 |
| 10-19 01:18 | +15 | ZEC | UP | 0.53 | 0.72 | 1.57 |
| 10-19 01:18 | +10 | ZEC | UP | 0.53 | 0.66 | 0.96 |
| 10-19 01:18 | +5 | ZEC | UP | 0.53 | 0.59 | 0.25 |
| 10-19 01:18 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 10-19 01:17 | +10 stop | NEAR | UP | 0.57 | 0.71 | 1.07 |
| 10-19 01:17 | +10 stop | DOGE | UP | 0.52 | 0.65 | 0.95 |
| 10-19 01:17 | +10 stop | BTC | UP | 0.58 | 0.41 | -2.05 |
| 10-19 01:17 | +20 | BTC | UP | 0.58 | open |  |
| 10-19 01:17 | +15 | BTC | UP | 0.58 | open |  |
| 10-19 01:17 | +10 | BTC | UP | 0.58 | open |  |
