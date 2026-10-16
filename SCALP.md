# Range-Scalp Bot

*Updated Fri Oct 16 16:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19529 | 16968 | 2561 (29) | 4 | $-5902.07 | -4.8% |
| **+10¢** | 14722 | 11764 | 2958 (41) | 5 | $-5307.19 | -5.7% |
| **+15¢** | 12319 | 9139 | 3180 (60) | 6 | $-4791.52 | -6.2% |
| **+20¢** | 10931 | 7599 | 3332 (79) | 6 | $-4252.20 | -6.2% |
| **+10¢ (15¢ stop)** | 24025 | 23975 | 50 (29) | 0 | $-9207.95 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 16:48 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 10-16 16:48 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-16 16:48 | +5 | ZEC | DOWN | 0.69 | 0.89 | 1.75 |
| 10-16 16:48 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.24 |
| 10-16 16:48 | +20 | SOL | DOWN | 0.65 | 0.88 | 2.08 |
| 10-16 16:48 | +15 | SOL | DOWN | 0.65 | 0.80 | 1.24 |
| 10-16 16:48 | +10 | SOL | DOWN | 0.65 | 0.80 | 1.24 |
| 10-16 16:48 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.21 |
| 10-16 16:47 | +10 stop | XRP | DOWN | 0.55 | 0.71 | 1.27 |
| 10-16 16:47 | +10 | XRP | DOWN | 0.55 | 0.71 | 1.27 |
| 10-16 16:47 | +5 | XRP | DOWN | 0.55 | 0.60 | 0.15 |
| 10-16 16:47 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-16 16:47 | +20 | DOGE | DOWN | 0.58 | 0.85 | 2.43 |
| 10-16 16:47 | +15 | DOGE | DOWN | 0.58 | 0.85 | 2.43 |
| 10-16 16:47 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-16 16:47 | +5 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-16 16:47 | +5 | BNB | UP | 0.54 | open |  |
| 10-16 16:47 | +5 | ZEC | UP | 0.52 | 0.60 | 0.45 |
| 10-16 16:46 | +10 stop | NEAR | UP | 0.51 | 0.19 | -3.49 |
| 10-16 16:46 | +20 | NEAR | UP | 0.51 | open |  |
| 10-16 16:46 | +15 | NEAR | UP | 0.51 | open |  |
| 10-16 16:46 | +10 | NEAR | UP | 0.51 | open |  |
| 10-16 16:46 | +5 | NEAR | UP | 0.51 | open |  |
| 10-16 16:46 | +10 stop | BTC | UP | 0.58 | 0.41 | -2.05 |
| 10-16 16:46 | +20 | BTC | UP | 0.58 | open |  |
| 10-16 16:46 | +15 | BTC | UP | 0.58 | open |  |
| 10-16 16:46 | +10 | BTC | UP | 0.58 | open |  |
| 10-16 16:46 | +5 | BTC | UP | 0.58 | open |  |
| 10-16 16:46 | +10 stop | HYPE | UP | 0.61 | 0.44 | -2.02 |
| 10-16 16:46 | +20 | HYPE | UP | 0.60 | open |  |
| 10-16 16:46 | +15 | HYPE | UP | 0.60 | open |  |
| 10-16 16:46 | +10 | HYPE | UP | 0.60 | open |  |
| 10-16 16:46 | +5 | HYPE | UP | 0.60 | open |  |
| 10-16 16:46 | +10 stop | BNB | UP | 0.61 | 0.35 | -2.93 |
| 10-16 16:46 | +20 | BNB | UP | 0.61 | open |  |
| 10-16 16:46 | +15 | BNB | UP | 0.61 | open |  |
| 10-16 16:46 | +10 | BNB | UP | 0.61 | open |  |
| 10-16 16:46 | +5 | BNB | UP | 0.61 | 0.66 | 0.17 |
| 10-16 16:46 | +10 stop | ZEC | UP | 0.60 | 0.42 | -2.15 |
| 10-16 16:46 | +20 | ZEC | UP | 0.60 | open |  |
