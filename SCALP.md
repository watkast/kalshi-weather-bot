# Range-Scalp Bot

*Updated Mon Nov 23 23:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70295 | 61351 | 8944 (147) | 2 | $-18839.90 | -4.3% |
| **+10¢** | 52442 | 41996 | 10446 (190) | 3 | $-17481.58 | -5.3% |
| **+15¢** | 43930 | 32680 | 11250 (246) | 5 | $-15576.94 | -5.7% |
| **+20¢** | 39113 | 27272 | 11841 (311) | 5 | $-13952.95 | -5.7% |
| **+10¢ (15¢ stop)** | 85612 | 85416 | 196 (118) | 0 | $-31491.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 23:39 | +10 stop | NEAR | UP | 0.60 | 0.36 | -2.74 |
| 11-23 23:37 | +5 | NEAR | UP | 0.64 | open |  |
| 11-23 23:37 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 11-23 23:37 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-23 23:37 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-23 23:37 | +10 stop | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-23 23:35 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.90 |
| 11-23 23:35 | +10 stop | ZEC | DOWN | 0.70 | 0.91 | 1.85 |
| 11-23 23:35 | +10 | ZEC | DOWN | 0.68 | 0.91 | 2.04 |
| 11-23 23:35 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-23 23:34 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-23 23:34 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-23 23:34 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-23 23:33 | +5 | ZEC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-23 23:33 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-23 23:32 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-23 23:32 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-23 23:32 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 11-23 23:32 | +5 | DOGE | DOWN | 0.59 | 0.70 | 0.80 |
| 11-23 23:32 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-23 23:32 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-23 23:32 | +5 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-23 23:32 | +10 stop | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-23 23:32 | +20 | ZEC | DOWN | 0.59 | 0.91 | 2.93 |
| 11-23 23:32 | +15 | ZEC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-23 23:32 | +10 | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-23 23:32 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-23 23:32 | +10 stop | SOL | DOWN | 0.69 | 0.54 | -1.83 |
| 11-23 23:32 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-23 23:32 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-23 23:32 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-23 23:32 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-23 23:32 | +10 stop | DOGE | UP | 0.47 | 0.28 | -2.23 |
| 11-23 23:32 | +10 | DOGE | UP | 0.47 | open |  |
| 11-23 23:32 | +5 | DOGE | UP | 0.47 | 0.56 | 0.54 |
| 11-23 23:32 | +10 stop | NEAR | UP | 0.60 | 0.40 | -2.38 |
| 11-23 23:32 | +20 | NEAR | UP | 0.58 | open |  |
| 11-23 23:32 | +15 | NEAR | UP | 0.58 | open |  |
| 11-23 23:32 | +10 | NEAR | UP | 0.58 | open |  |
| 11-23 23:32 | +5 | NEAR | UP | 0.58 | 0.63 | 0.15 |
