# Range-Scalp Bot

*Updated Tue Oct 27 03:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35939 | 31371 | 4568 (43) | 0 | $-10018.10 | -4.4% |
| **+10¢** | 26870 | 21584 | 5286 (65) | 1 | $-8866.96 | -5.2% |
| **+15¢** | 22482 | 16800 | 5682 (89) | 2 | $-7898.30 | -5.6% |
| **+20¢** | 19926 | 13973 | 5953 (112) | 5 | $-6948.35 | -5.6% |
| **+10¢ (15¢ stop)** | 44056 | 43993 | 63 (33) | 1 | $-16755.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 03:32 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 10-27 03:32 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-27 03:31 | +10 stop | SOL | UP | 0.67 | 0.81 | 1.13 |
| 10-27 03:31 | +20 | SOL | UP | 0.67 | open |  |
| 10-27 03:31 | +15 | SOL | UP | 0.67 | 0.85 | 1.55 |
| 10-27 03:31 | +10 | SOL | UP | 0.67 | 0.81 | 1.13 |
| 10-27 03:31 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 10-27 03:31 | +10 stop | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 10-27 03:31 | +20 | NEAR | UP | 0.57 | 0.81 | 2.11 |
| 10-27 03:31 | +15 | NEAR | UP | 0.57 | 0.81 | 2.11 |
| 10-27 03:31 | +10 | NEAR | UP | 0.57 | 0.70 | 0.97 |
| 10-27 03:31 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-27 03:31 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-27 03:31 | +20 | DOGE | UP | 0.65 | 0.85 | 1.75 |
| 10-27 03:31 | +15 | DOGE | UP | 0.65 | 0.85 | 1.75 |
| 10-27 03:31 | +10 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-27 03:31 | +5 | DOGE | UP | 0.65 | 0.75 | 0.74 |
| 10-27 03:31 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-27 03:31 | +20 | BTC | UP | 0.55 | 0.75 | 1.68 |
| 10-27 03:31 | +15 | BTC | UP | 0.55 | 0.74 | 1.58 |
| 10-27 03:31 | +10 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-27 03:31 | +5 | BTC | UP | 0.55 | 0.62 | 0.35 |
| 10-27 03:31 | +5 | HYPE | UP | 0.63 | 0.73 | 0.65 |
| 10-27 03:31 | +10 stop | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-27 03:31 | +20 | ZEC | UP | 0.66 | open |  |
| 10-27 03:31 | +15 | ZEC | UP | 0.67 | 0.85 | 1.55 |
| 10-27 03:31 | +10 | ZEC | UP | 0.68 | 0.81 | 1.03 |
| 10-27 03:31 | +5 | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 10-27 03:31 | +10 stop | HYPE | UP | 0.65 | open |  |
| 10-27 03:31 | +20 | HYPE | UP | 0.69 | open |  |
| 10-27 03:31 | +15 | HYPE | UP | 0.69 | open |  |
| 10-27 03:31 | +10 | HYPE | UP | 0.71 | open |  |
| 10-27 03:31 | +10 stop | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-27 03:31 | +20 | BNB | UP | 0.71 | open |  |
| 10-27 03:31 | +15 | BNB | UP | 0.71 | open |  |
| 10-27 03:31 | +10 | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-27 03:31 | +5 | BNB | UP | 0.71 | 0.76 | 0.22 |
| 10-27 03:31 | +10 stop | XRP | UP | 0.62 | 0.79 | 1.41 |
| 10-27 03:31 | +20 | XRP | UP | 0.62 | 0.85 | 2.04 |
| 10-27 03:31 | +15 | XRP | UP | 0.62 | 0.79 | 1.41 |
