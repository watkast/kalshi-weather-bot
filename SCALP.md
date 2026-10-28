# Range-Scalp Bot

*Updated Wed Oct 28 04:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37559 | 32775 | 4784 (45) | 6 | $-10558.55 | -4.5% |
| **+10¢** | 28049 | 22512 | 5537 (67) | 4 | $-9417.15 | -5.3% |
| **+15¢** | 23463 | 17519 | 5944 (91) | 5 | $-8375.48 | -5.7% |
| **+20¢** | 20799 | 14577 | 6222 (116) | 6 | $-7353.85 | -5.6% |
| **+10¢ (15¢ stop)** | 46015 | 45950 | 65 (34) | 0 | $-17508.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 04:23 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-28 04:23 | +10 stop | HYPE | DOWN | 0.56 | 0.21 | -3.80 |
| 10-28 04:23 | +10 stop | BNB | DOWN | 0.55 | 0.21 | -3.70 |
| 10-28 04:23 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.35 |
| 10-28 04:22 | +10 stop | HYPE | UP | 0.53 | 0.34 | -2.24 |
| 10-28 04:22 | +20 | HYPE | UP | 0.53 | 0.78 | 2.19 |
| 10-28 04:22 | +15 | HYPE | UP | 0.53 | 0.78 | 2.19 |
| 10-28 04:22 | +10 | HYPE | UP | 0.53 | 0.78 | 2.19 |
| 10-28 04:22 | +5 | HYPE | UP | 0.53 | 0.59 | 0.25 |
| 10-28 04:21 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 04:21 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 10-28 04:21 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-28 04:21 | +10 stop | BNB | UP | 0.67 | 0.40 | -3.03 |
| 10-28 04:21 | +10 | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-28 04:21 | +5 | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-28 04:20 | +10 stop | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 10-28 04:20 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-28 04:20 | +10 stop | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-28 04:20 | +10 stop | ETH | UP | 0.53 | 0.34 | -2.24 |
| 10-28 04:19 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 10-28 04:19 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-28 04:19 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-28 04:19 | +10 | XRP | DOWN | 0.58 | 0.74 | 1.28 |
| 10-28 04:19 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 10-28 04:18 | +10 stop | NEAR | UP | 0.71 | 0.56 | -1.83 |
| 10-28 04:18 | +10 | NEAR | UP | 0.71 | open |  |
| 10-28 04:18 | +5 | NEAR | UP | 0.71 | open |  |
| 10-28 04:18 | +10 stop | DOGE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 04:18 | +10 | DOGE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 04:18 | +10 stop | BNB | UP | 0.59 | 0.72 | 0.98 |
| 10-28 04:18 | +10 | BNB | UP | 0.59 | 0.72 | 0.98 |
| 10-28 04:18 | +5 | BNB | UP | 0.59 | 0.72 | 0.98 |
| 10-28 04:18 | +10 stop | SOL | UP | 0.55 | 0.37 | -2.15 |
| 10-28 04:18 | +10 | SOL | UP | 0.54 | open |  |
| 10-28 04:18 | +5 | SOL | UP | 0.54 | open |  |
| 10-28 04:16 | +5 | DOGE | UP | 0.64 | open |  |
| 10-28 04:16 | +10 stop | ETH | UP | 0.67 | 0.50 | -2.04 |
| 10-28 04:16 | +20 | ETH | UP | 0.67 | open |  |
| 10-28 04:16 | +15 | ETH | UP | 0.67 | open |  |
| 10-28 04:16 | +10 | ETH | UP | 0.67 | open |  |
