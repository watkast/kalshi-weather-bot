# Range-Scalp Bot

*Updated Thu Nov 26 05:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72458 | 63254 | 9204 (158) | 1 | $-19216.37 | -4.2% |
| **+10¢** | 54041 | 43293 | 10748 (203) | 3 | $-17793.47 | -5.2% |
| **+15¢** | 45252 | 33674 | 11578 (261) | 4 | $-15875.87 | -5.6% |
| **+20¢** | 40277 | 28083 | 12194 (327) | 5 | $-14282.02 | -5.7% |
| **+10¢ (15¢ stop)** | 88228 | 88019 | 209 (128) | 2 | $-32374.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 05:40 | +5 | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-26 05:39 | +10 stop | XRP | UP | 0.49 | open |  |
| 11-26 05:39 | +10 stop | NEAR | UP | 0.70 | open |  |
| 11-26 05:39 | +20 | NEAR | UP | 0.70 | open |  |
| 11-26 05:39 | +15 | NEAR | UP | 0.69 | open |  |
| 11-26 05:39 | +10 | NEAR | UP | 0.69 | open |  |
| 11-26 05:39 | +5 | NEAR | UP | 0.69 | 0.75 | 0.30 |
| 11-26 05:38 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-26 05:38 | +10 stop | DOGE | UP | 0.44 | 0.61 | 1.35 |
| 11-26 05:37 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-26 05:36 | +10 stop | SOL | DOWN | 0.63 | 0.77 | 1.10 |
| 11-26 05:36 | +10 stop | NEAR | UP | 0.64 | 0.83 | 1.67 |
| 11-26 05:36 | +20 | NEAR | UP | 0.63 | 0.83 | 1.73 |
| 11-26 05:36 | +15 | NEAR | UP | 0.63 | 0.83 | 1.73 |
| 11-26 05:36 | +10 | NEAR | UP | 0.63 | 0.83 | 1.73 |
| 11-26 05:36 | +5 | NEAR | UP | 0.64 | 0.83 | 1.67 |
| 11-26 05:36 | +10 stop | ETH | UP | 0.56 | 0.67 | 0.76 |
| 11-26 05:35 | +10 stop | SOL | UP | 0.59 | 0.41 | -2.14 |
| 11-26 05:35 | +20 | SOL | UP | 0.59 | open |  |
| 11-26 05:35 | +15 | SOL | UP | 0.59 | open |  |
| 11-26 05:35 | +10 | SOL | UP | 0.59 | open |  |
| 11-26 05:35 | +5 | SOL | UP | 0.59 | open |  |
| 11-26 05:35 | +10 stop | HYPE | UP | 0.52 | 0.37 | -1.85 |
| 11-26 05:35 | +10 stop | DOGE | UP | 0.61 | 0.33 | -3.18 |
| 11-26 05:35 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.94 |
| 11-26 05:33 | +10 stop | HYPE | DOWN | 0.63 | 0.45 | -2.15 |
| 11-26 05:33 | +10 stop | BNB | DOWN | 0.67 | 0.50 | -2.04 |
| 11-26 05:33 | +20 | BNB | DOWN | 0.66 | 0.90 | 2.18 |
| 11-26 05:33 | +15 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-26 05:33 | +10 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-26 05:33 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-26 05:33 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-26 05:33 | +10 stop | ETH | DOWN | 0.54 | 0.27 | -3.02 |
| 11-26 05:33 | +20 | ETH | DOWN | 0.54 | 0.75 | 1.78 |
| 11-26 05:33 | +15 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 11-26 05:33 | +5 | XRP | DOWN | 0.52 | 0.57 | 0.14 |
| 11-26 05:32 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-26 05:32 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-26 05:32 | +10 stop | BTC | DOWN | 0.69 | 0.43 | -2.93 |
| 11-26 05:32 | +20 | BTC | DOWN | 0.70 | open |  |
