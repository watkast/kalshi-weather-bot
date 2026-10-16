# Range-Scalp Bot

*Updated Fri Oct 16 15:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19446 | 16901 | 2545 (29) | 6 | $-5839.22 | -4.8% |
| **+10¢** | 14662 | 11722 | 2940 (41) | 6 | $-5236.01 | -5.7% |
| **+15¢** | 12274 | 9109 | 3165 (60) | 5 | $-4747.17 | -6.2% |
| **+20¢** | 10887 | 7570 | 3317 (79) | 5 | $-4217.27 | -6.2% |
| **+10¢ (15¢ stop)** | 23911 | 23861 | 50 (29) | 0 | $-9153.50 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 15:41 | +10 stop | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 10-16 15:41 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-16 15:41 | +15 | BTC | UP | 0.64 | 0.87 | 2.05 |
| 10-16 15:41 | +10 | BTC | UP | 0.64 | 0.75 | 0.79 |
| 10-16 15:41 | +5 | BTC | UP | 0.65 | 0.72 | 0.39 |
| 10-16 15:37 | +10 stop | BTC | UP | 0.60 | 0.77 | 1.40 |
| 10-16 15:37 | +15 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 10-16 15:37 | +10 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 10-16 15:37 | +5 | BTC | UP | 0.60 | 0.68 | 0.47 |
| 10-16 15:36 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-16 15:36 | +10 stop | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 10-16 15:35 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-16 15:35 | +10 | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-16 15:35 | +10 stop | XRP | UP | 0.64 | 0.49 | -1.85 |
| 10-16 15:34 | +10 stop | HYPE | UP | 0.66 | 0.84 | 1.54 |
| 10-16 15:34 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-16 15:34 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 10-16 15:34 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 10-16 15:34 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 10-16 15:34 | +20 | NEAR | UP | 0.66 | 0.87 | 1.86 |
| 10-16 15:34 | +10 stop | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 10-16 15:34 | +15 | NEAR | UP | 0.65 | 0.80 | 1.22 |
| 10-16 15:32 | +10 stop | BNB | UP | 0.59 | 0.71 | 0.84 |
| 10-16 15:32 | +10 | BNB | UP | 0.59 | 0.71 | 0.84 |
| 10-16 15:32 | +5 | BNB | UP | 0.59 | 0.66 | 0.33 |
| 10-16 15:32 | +5 | ETH | UP | 0.63 | 0.71 | 0.48 |
| 10-16 15:32 | +10 stop | ZEC | DOWN | 0.58 | 0.43 | -1.86 |
| 10-16 15:32 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-16 15:32 | +15 | ZEC | DOWN | 0.59 | open |  |
| 10-16 15:32 | +10 | ZEC | DOWN | 0.59 | open |  |
| 10-16 15:32 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-16 15:32 | +10 stop | NEAR | DOWN | 0.59 | 0.39 | -2.34 |
| 10-16 15:32 | +10 | NEAR | DOWN | 0.61 | open |  |
| 10-16 15:32 | +5 | NEAR | DOWN | 0.61 | open |  |
| 10-16 15:32 | +10 stop | XRP | DOWN | 0.56 | 0.35 | -2.44 |
| 10-16 15:32 | +20 | XRP | DOWN | 0.56 | open |  |
| 10-16 15:32 | +15 | XRP | DOWN | 0.56 | open |  |
| 10-16 15:32 | +10 | XRP | DOWN | 0.56 | open |  |
| 10-16 15:32 | +5 | XRP | DOWN | 0.56 | open |  |
| 10-16 15:32 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.05 |
