# Range-Scalp Bot

*Updated Tue Oct 13 19:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14849 | 12851 | 1998 (27) | 4 | $-4750.60 | -5.1% |
| **+10¢** | 11239 | 8919 | 2320 (39) | 3 | $-4433.43 | -6.3% |
| **+15¢** | 9446 | 6963 | 2483 (57) | 2 | $-3935.15 | -6.6% |
| **+20¢** | 8405 | 5816 | 2589 (73) | 2 | $-3388.97 | -6.4% |
| **+10¢ (15¢ stop)** | 18223 | 18173 | 50 (29) | 0 | $-7061.83 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 19:27 | +10 stop | DOGE | DOWN | 0.53 | 0.92 | 3.63 |
| 10-13 19:27 | +10 stop | HYPE | UP | 0.60 | 0.42 | -2.15 |
| 10-13 19:27 | +10 | HYPE | UP | 0.62 | open |  |
| 10-13 19:27 | +5 | HYPE | UP | 0.62 | open |  |
| 10-13 19:26 | +10 stop | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 10-13 19:26 | +10 | HYPE | UP | 0.65 | 0.81 | 1.29 |
| 10-13 19:26 | +5 | HYPE | UP | 0.65 | 0.74 | 0.56 |
| 10-13 19:25 | +5 | DOGE | UP | 0.70 | open |  |
| 10-13 19:24 | +10 stop | NEAR | UP | 0.67 | 0.36 | -3.43 |
| 10-13 19:24 | +10 stop | DOGE | UP | 0.61 | 0.40 | -2.44 |
| 10-13 19:24 | +10 stop | SOL | DOWN | 0.66 | 0.51 | -1.84 |
| 10-13 19:24 | +5 | SOL | DOWN | 0.66 | 0.74 | 0.50 |
| 10-13 19:22 | +10 stop | DOGE | UP | 0.60 | 0.45 | -1.85 |
| 10-13 19:22 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-13 19:22 | +10 stop | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 10-13 19:22 | +10 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 10-13 19:22 | +5 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 10-13 19:22 | +10 stop | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 10-13 19:22 | +10 | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 10-13 19:22 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-13 19:22 | +10 stop | BNB | UP | 0.71 | 0.90 | 1.70 |
| 10-13 19:22 | +10 stop | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 10-13 19:22 | +10 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 10-13 19:22 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-13 19:21 | +10 stop | NEAR | DOWN | 0.59 | 0.37 | -2.54 |
| 10-13 19:21 | +20 | NEAR | DOWN | 0.59 | 0.88 | 2.65 |
| 10-13 19:21 | +15 | NEAR | DOWN | 0.60 | 0.88 | 2.55 |
| 10-13 19:21 | +10 | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-13 19:21 | +5 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-13 19:21 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-13 19:21 | +20 | XRP | DOWN | 0.58 | 0.83 | 2.22 |
| 10-13 19:21 | +15 | XRP | DOWN | 0.58 | 0.73 | 1.18 |
| 10-13 19:21 | +10 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-13 19:21 | +5 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-13 19:21 | +10 stop | HYPE | DOWN | 0.52 | 0.63 | 0.77 |
| 10-13 19:21 | +15 | HYPE | DOWN | 0.52 | 0.82 | 2.73 |
| 10-13 19:21 | +10 | HYPE | DOWN | 0.49 | 0.63 | 1.05 |
| 10-13 19:21 | +5 | HYPE | DOWN | 0.49 | 0.63 | 1.05 |
| 10-13 19:19 | +10 stop | DOGE | DOWN | 0.68 | 0.40 | -3.13 |
| 10-13 19:19 | +10 | DOGE | DOWN | 0.68 | 0.92 | 2.15 |
