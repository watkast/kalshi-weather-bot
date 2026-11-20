# Range-Scalp Bot

*Updated Fri Nov 20 23:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66689 | 58202 | 8487 (128) | 5 | $-17931.85 | -4.3% |
| **+10¢** | 49805 | 39885 | 9920 (170) | 4 | $-16672.66 | -5.3% |
| **+15¢** | 41766 | 31071 | 10695 (217) | 4 | $-14973.77 | -5.7% |
| **+20¢** | 37183 | 25951 | 11232 (273) | 5 | $-13247.54 | -5.7% |
| **+10¢ (15¢ stop)** | 81221 | 81055 | 166 (100) | 0 | $-29991.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 23:42 | +10 stop | SOL | UP | 0.60 | 0.44 | -1.95 |
| 11-20 23:42 | +10 stop | NEAR | UP | 0.64 | 0.77 | 1.03 |
| 11-20 23:42 | +20 | NEAR | UP | 0.64 | open |  |
| 11-20 23:42 | +15 | NEAR | UP | 0.62 | 0.77 | 1.20 |
| 11-20 23:42 | +10 | NEAR | UP | 0.62 | 0.77 | 1.20 |
| 11-20 23:42 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 11-20 23:40 | +10 stop | SOL | UP | 0.60 | 0.79 | 1.61 |
| 11-20 23:37 | +10 stop | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 11-20 23:37 | +10 | NEAR | UP | 0.63 | 0.79 | 1.31 |
| 11-20 23:37 | +5 | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 11-20 23:36 | +10 stop | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-20 23:36 | +20 | ZEC | UP | 0.62 | 0.86 | 2.14 |
| 11-20 23:36 | +15 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-20 23:36 | +10 | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-20 23:36 | +10 stop | SOL | UP | 0.56 | 0.75 | 1.58 |
| 11-20 23:36 | +10 stop | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 11-20 23:36 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-20 23:35 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-20 23:35 | +10 stop | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-20 23:35 | +10 | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-20 23:35 | +5 | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-20 23:34 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-20 23:34 | +20 | ETH | UP | 0.62 | 0.86 | 2.14 |
| 11-20 23:34 | +15 | ETH | UP | 0.62 | 0.86 | 2.14 |
| 11-20 23:34 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-20 23:34 | +5 | ETH | UP | 0.62 | 0.73 | 0.79 |
| 11-20 23:34 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-20 23:33 | +10 stop | SOL | DOWN | 0.57 | 0.34 | -2.64 |
| 11-20 23:33 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-20 23:33 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-20 23:33 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-20 23:33 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-20 23:32 | +10 stop | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-20 23:32 | +10 stop | XRP | DOWN | 0.65 | 0.47 | -2.18 |
| 11-20 23:32 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-20 23:32 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-20 23:32 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.35 |
| 11-20 23:32 | +10 stop | ZEC | UP | 0.48 | 0.70 | 1.87 |
| 11-20 23:32 | +20 | ZEC | UP | 0.48 | 0.70 | 1.87 |
| 11-20 23:32 | +15 | ZEC | UP | 0.48 | 0.70 | 1.87 |
