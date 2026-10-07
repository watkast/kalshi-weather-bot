# Range-Scalp Bot

*Updated Wed Oct 07 12:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6401 | 5563 | 838 (9) | 1 | $-1889.67 | -4.7% |
| **+10¢** | 4866 | 3881 | 985 (16) | 1 | $-1763.66 | -5.8% |
| **+15¢** | 4087 | 3046 | 1041 (20) | 2 | $-1476.06 | -5.8% |
| **+20¢** | 3656 | 2565 | 1091 (27) | 2 | $-1209.35 | -5.3% |
| **+10¢ (15¢ stop)** | 7764 | 7749 | 15 (9) | 1 | $-2718.51 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 12:17 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 10-07 12:17 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-07 12:17 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-07 12:17 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-07 12:17 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-07 12:16 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 12:16 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-07 12:16 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-07 12:16 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 12:16 | +5 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 12:13 | +10 stop | HYPE | DOWN | 0.51 | 0.05 | -4.82 |
| 10-07 12:11 | +5 | HYPE | UP | 0.66 | 0.95 | 2.66 |
| 10-07 12:11 | +10 stop | HYPE | UP | 0.66 | 0.38 | -3.13 |
| 10-07 12:11 | +10 stop | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 12:11 | +20 | BNB | DOWN | 0.59 | yes | -6.07 |
| 10-07 12:11 | +15 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-07 12:11 | +10 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 12:11 | +5 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 12:10 | +10 stop | HYPE | DOWN | 0.68 | 0.46 | -2.54 |
| 10-07 12:10 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-07 12:09 | +10 stop | ETH | UP | 0.63 | 0.46 | -2.05 |
| 10-07 12:09 | +5 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-07 12:09 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 10-07 12:09 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-07 12:08 | +10 stop | DOGE | UP | 0.68 | 0.87 | 1.66 |
| 10-07 12:08 | +10 stop | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-07 12:07 | +10 stop | NEAR | DOWN | 0.64 | 0.44 | -2.35 |
| 10-07 12:07 | +10 stop | DOGE | UP | 0.47 | 0.64 | 1.35 |
| 10-07 12:06 | +10 stop | HYPE | DOWN | 0.63 | 0.76 | 0.96 |
| 10-07 12:06 | +10 stop | SOL | DOWN | 0.61 | 0.36 | -2.84 |
| 10-07 12:06 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 10-07 12:06 | +10 stop | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 10-07 12:05 | +10 stop | SOL | UP | 0.52 | 0.34 | -2.14 |
| 10-07 12:05 | +10 stop | HYPE | UP | 0.56 | 0.39 | -2.05 |
| 10-07 12:05 | +15 | HYPE | UP | 0.56 | 0.95 | 3.64 |
| 10-07 12:05 | +10 | HYPE | UP | 0.56 | 0.95 | 3.64 |
| 10-07 12:05 | +5 | HYPE | UP | 0.56 | 0.65 | 0.56 |
| 10-07 12:05 | +10 stop | NEAR | UP | 0.64 | 0.44 | -2.35 |
| 10-07 12:05 | +20 | NEAR | UP | 0.64 | 0.84 | 1.73 |
| 10-07 12:05 | +15 | NEAR | UP | 0.64 | 0.84 | 1.73 |
