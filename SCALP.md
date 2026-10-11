# Range-Scalp Bot

*Updated Sun Oct 11 08:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11656 | 10048 | 1608 (24) | 0 | $-3955.11 | -5.4% |
| **+10¢** | 8835 | 6969 | 1866 (37) | 0 | $-3751.80 | -6.7% |
| **+15¢** | 7436 | 5458 | 1978 (53) | 0 | $-3220.36 | -6.9% |
| **+20¢** | 6626 | 4570 | 2056 (67) | 0 | $-2688.10 | -6.5% |
| **+10¢ (15¢ stop)** | 14353 | 14312 | 41 (25) | 0 | $-5702.65 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 08:28 | +10 stop | ZEC | DOWN | 0.47 | 0.58 | 0.70 |
| 10-11 08:27 | +10 stop | HYPE | UP | 0.37 | 0.60 | 1.96 |
| 10-11 08:27 | +10 stop | HYPE | UP | 0.68 | 0.53 | -1.88 |
| 10-11 08:26 | +10 stop | ZEC | UP | 0.66 | 0.44 | -2.58 |
| 10-11 08:26 | +15 | ZEC | UP | 0.67 | 0.90 | 2.12 |
| 10-11 08:26 | +10 | ZEC | UP | 0.67 | 0.90 | 2.12 |
| 10-11 08:26 | +5 | ZEC | UP | 0.67 | 0.90 | 2.12 |
| 10-11 08:26 | +10 stop | HYPE | UP | 0.70 | 0.53 | -2.03 |
| 10-11 08:26 | +20 | HYPE | UP | 0.70 | 0.99 | 2.72 |
| 10-11 08:26 | +15 | HYPE | UP | 0.70 | 0.99 | 2.72 |
| 10-11 08:26 | +10 | HYPE | UP | 0.70 | 0.99 | 2.72 |
| 10-11 08:26 | +5 | HYPE | UP | 0.70 | 0.99 | 2.72 |
| 10-11 08:26 | +10 stop | DOGE | DOWN | 0.61 | 0.77 | 1.30 |
| 10-11 08:26 | +10 stop | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-11 08:26 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-11 08:26 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-11 08:26 | +10 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-11 08:26 | +5 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-11 08:25 | +10 stop | ETH | DOWN | 0.58 | 0.82 | 2.11 |
| 10-11 08:25 | +10 stop | BTC | DOWN | 0.59 | 0.81 | 1.92 |
| 10-11 08:25 | +10 stop | SOL | DOWN | 0.60 | 0.85 | 2.24 |
| 10-11 08:24 | +5 | SOL | DOWN | 0.59 | 0.85 | 2.31 |
| 10-11 08:24 | +10 stop | DOGE | UP | 0.60 | 0.40 | -2.34 |
| 10-11 08:24 | +15 | DOGE | UP | 0.60 | no | -6.17 |
| 10-11 08:24 | +10 | DOGE | UP | 0.60 | no | -6.17 |
| 10-11 08:24 | +5 | DOGE | UP | 0.60 | no | -6.17 |
| 10-11 08:24 | +5 | SOL | UP | 0.45 | 0.65 | 1.66 |
| 10-11 08:23 | +10 stop | BNB | DOWN | 0.67 | 0.90 | 2.08 |
| 10-11 08:21 | +10 stop | SOL | UP | 0.58 | 0.42 | -1.96 |
| 10-11 08:20 | +10 stop | NEAR | DOWN | 0.59 | 0.15 | -4.65 |
| 10-11 08:20 | +5 | XRP | UP | 0.71 | 0.77 | 0.32 |
| 10-11 08:19 | +10 stop | SOL | UP | 0.60 | 0.43 | -2.05 |
| 10-11 08:19 | +10 | SOL | UP | 0.60 | no | -6.17 |
| 10-11 08:19 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-11 08:19 | +5 | ETH | UP | 0.65 | no | -6.66 |
| 10-11 08:19 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 08:19 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 08:19 | +5 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-11 08:18 | +10 stop | BTC | UP | 0.57 | 0.36 | -2.45 |
| 10-11 08:17 | +10 stop | NEAR | UP | 0.64 | 0.41 | -2.64 |
