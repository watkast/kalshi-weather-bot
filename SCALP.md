# Range-Scalp Bot

*Updated Fri Oct 23 16:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30635 | 26692 | 3943 (39) | 5 | $-8885.07 | -4.6% |
| **+10¢** | 22926 | 18364 | 4562 (56) | 7 | $-7952.42 | -5.5% |
| **+15¢** | 19182 | 14274 | 4908 (79) | 9 | $-7178.43 | -6.0% |
| **+20¢** | 16990 | 11849 | 5141 (102) | 9 | $-6439.02 | -6.0% |
| **+10¢ (15¢ stop)** | 37578 | 37519 | 59 (32) | 0 | $-14264.51 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 16:58 | +10 stop | NEAR | UP | 0.48 | 0.63 | 1.15 |
| 10-23 16:56 | +10 stop | NEAR | UP | 0.67 | 0.46 | -2.44 |
| 10-23 16:56 | +15 | NEAR | UP | 0.67 | open |  |
| 10-23 16:56 | +10 | NEAR | UP | 0.67 | open |  |
| 10-23 16:56 | +5 | NEAR | UP | 0.67 | open |  |
| 10-23 16:55 | +10 stop | NEAR | DOWN | 0.43 | 0.59 | 1.25 |
| 10-23 16:55 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-23 16:55 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-23 16:55 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 10-23 16:52 | +10 | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 16:52 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-23 16:52 | +10 stop | NEAR | UP | 0.59 | 0.41 | -2.14 |
| 10-23 16:52 | +20 | NEAR | UP | 0.59 | open |  |
| 10-23 16:52 | +15 | NEAR | UP | 0.59 | 0.74 | 1.19 |
| 10-23 16:52 | +10 | NEAR | UP | 0.59 | 0.74 | 1.19 |
| 10-23 16:52 | +5 | NEAR | UP | 0.59 | 0.65 | 0.27 |
| 10-23 16:52 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-23 16:52 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 10-23 16:52 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-23 16:52 | +10 stop | DOGE | DOWN | 0.67 | 0.81 | 1.13 |
| 10-23 16:51 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-23 16:51 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-23 16:51 | +10 stop | SOL | UP | 0.54 | 0.35 | -2.24 |
| 10-23 16:51 | +10 stop | ZEC | UP | 0.67 | 0.45 | -2.54 |
| 10-23 16:51 | +5 | ZEC | UP | 0.67 | open |  |
| 10-23 16:51 | +10 stop | DOGE | UP | 0.52 | 0.36 | -1.95 |
| 10-23 16:51 | +5 | DOGE | UP | 0.52 | open |  |
| 10-23 16:50 | +10 stop | BTC | UP | 0.58 | 0.41 | -2.05 |
| 10-23 16:49 | +10 stop | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 10-23 16:49 | +20 | ZEC | UP | 0.65 | open |  |
| 10-23 16:49 | +15 | ZEC | UP | 0.66 | open |  |
| 10-23 16:49 | +10 | ZEC | UP | 0.66 | open |  |
| 10-23 16:49 | +5 | ZEC | UP | 0.66 | 0.75 | 0.60 |
| 10-23 16:49 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 10-23 16:49 | +10 stop | SOL | DOWN | 0.58 | 0.42 | -1.96 |
| 10-23 16:49 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 10-23 16:49 | +10 | BTC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-23 16:49 | +5 | BTC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-23 16:49 | +5 | SOL | DOWN | 0.56 | 0.64 | 0.45 |
| 10-23 16:49 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
