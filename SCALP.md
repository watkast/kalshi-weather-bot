# Range-Scalp Bot

*Updated Thu Oct 08 17:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7779 | 6740 | 1039 (13) | 5 | $-2431.87 | -5.0% |
| **+10¢** | 5897 | 4667 | 1230 (24) | 6 | $-2399.01 | -6.5% |
| **+15¢** | 4956 | 3665 | 1291 (32) | 5 | $-1949.49 | -6.3% |
| **+20¢** | 4430 | 3090 | 1340 (40) | 7 | $-1537.91 | -5.5% |
| **+10¢ (15¢ stop)** | 9449 | 9420 | 29 (18) | 5 | $-3471.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 17:36 | +5 | DOGE | UP | 0.64 | open |  |
| 10-08 17:35 | +10 stop | XRP | DOWN | 0.50 | 0.32 | -2.14 |
| 10-08 17:35 | +10 stop | DOGE | UP | 0.55 | open |  |
| 10-08 17:35 | +15 | DOGE | UP | 0.55 | open |  |
| 10-08 17:35 | +10 | DOGE | UP | 0.55 | open |  |
| 10-08 17:35 | +5 | DOGE | UP | 0.55 | 0.64 | 0.56 |
| 10-08 17:34 | +10 stop | ETH | UP | 0.68 | open |  |
| 10-08 17:34 | +10 | ETH | UP | 0.68 | open |  |
| 10-08 17:34 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 10-08 17:34 | +5 | BNB | UP | 0.64 | open |  |
| 10-08 17:34 | +10 stop | NEAR | UP | 0.66 | open |  |
| 10-08 17:33 | +10 stop | XRP | UP | 0.61 | 0.35 | -2.93 |
| 10-08 17:32 | +5 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-08 17:32 | +5 | NEAR | UP | 0.64 | open |  |
| 10-08 17:32 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-08 17:32 | +10 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-08 17:32 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 10-08 17:32 | +5 | DOGE | UP | 0.60 | 0.67 | 0.37 |
| 10-08 17:32 | +5 | BNB | UP | 0.56 | 0.62 | 0.25 |
| 10-08 17:32 | +10 stop | HYPE | UP | 0.57 | open |  |
| 10-08 17:32 | +10 stop | BNB | UP | 0.57 | open |  |
| 10-08 17:32 | +10 stop | ETH | UP | 0.57 | 0.71 | 1.07 |
| 10-08 17:32 | +20 | ETH | UP | 0.57 | open |  |
| 10-08 17:32 | +15 | ETH | UP | 0.57 | 0.73 | 1.28 |
| 10-08 17:32 | +10 | ETH | UP | 0.57 | 0.71 | 1.07 |
| 10-08 17:32 | +5 | ETH | UP | 0.57 | 0.66 | 0.56 |
| 10-08 17:32 | +10 stop | DOGE | UP | 0.55 | 0.67 | 0.86 |
| 10-08 17:32 | +20 | DOGE | UP | 0.55 | open |  |
| 10-08 17:32 | +15 | DOGE | UP | 0.55 | 0.71 | 1.27 |
| 10-08 17:32 | +10 | DOGE | UP | 0.55 | 0.67 | 0.86 |
| 10-08 17:32 | +5 | DOGE | UP | 0.55 | 0.61 | 0.25 |
| 10-08 17:32 | +5 | BNB | UP | 0.60 | 0.66 | 0.28 |
| 10-08 17:32 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.84 |
| 10-08 17:32 | +20 | XRP | UP | 0.65 | open |  |
| 10-08 17:32 | +15 | XRP | UP | 0.65 | open |  |
| 10-08 17:32 | +10 | XRP | UP | 0.65 | open |  |
| 10-08 17:32 | +5 | XRP | UP | 0.65 | open |  |
| 10-08 17:31 | +10 stop | NEAR | UP | 0.69 | 0.50 | -2.23 |
| 10-08 17:31 | +20 | NEAR | UP | 0.69 | open |  |
| 10-08 17:31 | +15 | NEAR | UP | 0.69 | open |  |
