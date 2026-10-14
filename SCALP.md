# Range-Scalp Bot

*Updated Wed Oct 14 02:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15305 | 13244 | 2061 (27) | 7 | $-4919.93 | -5.1% |
| **+10¢** | 11577 | 9187 | 2390 (39) | 7 | $-4581.44 | -6.3% |
| **+15¢** | 9729 | 7169 | 2560 (58) | 8 | $-4075.56 | -6.7% |
| **+20¢** | 8649 | 5972 | 2677 (75) | 8 | $-3578.91 | -6.6% |
| **+10¢ (15¢ stop)** | 18748 | 18698 | 50 (29) | 3 | $-7216.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 02:22 | +10 stop | HYPE | DOWN | 0.66 | open |  |
| 10-14 02:21 | +10 stop | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-14 02:21 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-14 02:21 | +10 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-14 02:21 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-14 02:21 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 10-14 02:21 | +10 stop | SOL | UP | 0.62 | 0.41 | -2.44 |
| 10-14 02:20 | +10 stop | BNB | UP | 0.65 | open |  |
| 10-14 02:20 | +10 stop | XRP | UP | 0.69 | 0.44 | -2.83 |
| 10-14 02:20 | +10 stop | ZEC | DOWN | 0.70 | 0.53 | -2.06 |
| 10-14 02:19 | +5 | SOL | DOWN | 0.56 | open |  |
| 10-14 02:19 | +10 stop | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-14 02:19 | +20 | NEAR | DOWN | 0.57 | 0.87 | 2.74 |
| 10-14 02:19 | +15 | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-14 02:19 | +10 | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 10-14 02:19 | +5 | NEAR | DOWN | 0.57 | 0.64 | 0.35 |
| 10-14 02:19 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-14 02:19 | +20 | DOGE | UP | 0.67 | open |  |
| 10-14 02:19 | +15 | DOGE | UP | 0.67 | open |  |
| 10-14 02:19 | +10 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 10-14 02:19 | +5 | DOGE | UP | 0.67 | 0.76 | 0.61 |
| 10-14 02:19 | +10 stop | ZEC | UP | 0.56 | 0.38 | -2.15 |
| 10-14 02:18 | +10 stop | BTC | DOWN | 0.48 | open |  |
| 10-14 02:18 | +10 stop | HYPE | DOWN | 0.69 | 0.50 | -2.20 |
| 10-14 02:18 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-14 02:18 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-14 02:18 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-14 02:18 | +5 | HYPE | DOWN | 0.69 | open |  |
| 10-14 02:17 | +10 stop | ETH | DOWN | 0.59 | 0.41 | -2.14 |
| 10-14 02:17 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-14 02:17 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-14 02:17 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-14 02:17 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-14 02:17 | +10 stop | BNB | DOWN | 0.59 | 0.40 | -2.24 |
| 10-14 02:17 | +20 | BNB | DOWN | 0.59 | open |  |
| 10-14 02:17 | +15 | BNB | DOWN | 0.59 | open |  |
| 10-14 02:17 | +10 | BNB | DOWN | 0.59 | open |  |
| 10-14 02:17 | +5 | BNB | DOWN | 0.59 | open |  |
| 10-14 02:17 | +10 stop | SOL | DOWN | 0.65 | 0.45 | -2.34 |
| 10-14 02:17 | +20 | SOL | DOWN | 0.65 | open |  |
