# Range-Scalp Bot

*Updated Sat Oct 24 09:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31841 | 27761 | 4080 (40) | 1 | $-9110.82 | -4.5% |
| **+10¢** | 23818 | 19102 | 4716 (58) | 1 | $-8098.35 | -5.4% |
| **+15¢** | 19936 | 14866 | 5070 (81) | 1 | $-7237.50 | -5.8% |
| **+20¢** | 17658 | 12348 | 5310 (103) | 1 | $-6443.88 | -5.8% |
| **+10¢ (15¢ stop)** | 39110 | 39051 | 59 (32) | 0 | $-14926.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 09:55 | +10 stop | NEAR | DOWN | 0.46 | 0.19 | -2.99 |
| 10-24 09:54 | +10 stop | NEAR | DOWN | 0.58 | 0.38 | -2.35 |
| 10-24 09:52 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 10-24 09:52 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-24 09:50 | +10 stop | BNB | UP | 0.65 | 0.81 | 1.33 |
| 10-24 09:50 | +5 | BNB | UP | 0.65 | 0.74 | 0.60 |
| 10-24 09:49 | +5 | BTC | UP | 0.68 | 0.76 | 0.51 |
| 10-24 09:48 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-24 09:48 | +15 | DOGE | UP | 0.62 | 0.78 | 1.30 |
| 10-24 09:48 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 10-24 09:48 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-24 09:48 | +10 | SOL | UP | 0.67 | 0.78 | 0.81 |
| 10-24 09:48 | +5 | SOL | UP | 0.67 | 0.78 | 0.81 |
| 10-24 09:48 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 10-24 09:48 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-24 09:48 | +10 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-24 09:48 | +5 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-24 09:48 | +5 | NEAR | DOWN | 0.63 | 0.70 | 0.38 |
| 10-24 09:48 | +5 | BTC | UP | 0.57 | 0.63 | 0.25 |
| 10-24 09:47 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-24 09:47 | +10 | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-24 09:47 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-24 09:47 | +10 stop | DOGE | UP | 0.67 | 0.50 | -2.04 |
| 10-24 09:47 | +10 | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 10-24 09:47 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 10-24 09:46 | +10 stop | BNB | DOWN | 0.56 | 0.41 | -1.85 |
| 10-24 09:46 | +20 | BNB | DOWN | 0.56 | open |  |
| 10-24 09:46 | +15 | BNB | DOWN | 0.56 | open |  |
| 10-24 09:46 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-24 09:46 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-24 09:46 | +10 stop | NEAR | UP | 0.64 | 0.45 | -2.25 |
| 10-24 09:46 | +20 | NEAR | UP | 0.64 | 0.94 | 2.74 |
| 10-24 09:46 | +15 | NEAR | UP | 0.64 | 0.80 | 1.31 |
| 10-24 09:46 | +10 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 10-24 09:46 | +5 | NEAR | UP | 0.64 | 0.70 | 0.28 |
| 10-24 09:46 | +10 stop | HYPE | UP | 0.64 | 0.77 | 0.96 |
| 10-24 09:46 | +20 | HYPE | UP | 0.64 | 0.85 | 1.80 |
| 10-24 09:46 | +15 | HYPE | UP | 0.64 | 0.81 | 1.38 |
| 10-24 09:46 | +10 | HYPE | UP | 0.64 | 0.77 | 0.96 |
| 10-24 09:46 | +5 | HYPE | UP | 0.64 | 0.77 | 0.96 |
