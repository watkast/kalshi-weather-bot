# Range-Scalp Bot

*Updated Sat Oct 31 11:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42186 | 36805 | 5381 (55) | 6 | $-11852.71 | -4.5% |
| **+10¢** | 31454 | 25226 | 6228 (79) | 7 | $-10592.18 | -5.4% |
| **+15¢** | 26304 | 19588 | 6716 (107) | 7 | $-9687.36 | -5.9% |
| **+20¢** | 23362 | 16328 | 7034 (138) | 7 | $-8524.80 | -5.8% |
| **+10¢ (15¢ stop)** | 51469 | 51394 | 75 (41) | 0 | $-19438.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 11:40 | +10 stop | SOL | DOWN | 0.61 | 0.19 | -4.48 |
| 10-31 11:40 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-31 11:40 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 10-31 11:38 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-31 11:36 | +10 stop | XRP | UP | 0.66 | 0.85 | 1.62 |
| 10-31 11:36 | +10 stop | SOL | DOWN | 0.59 | 0.36 | -2.64 |
| 10-31 11:36 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-31 11:36 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-31 11:36 | +10 | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 10-31 11:36 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 10-31 11:36 | +10 stop | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-31 11:35 | +10 stop | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 10-31 11:35 | +20 | ZEC | UP | 0.68 | 0.91 | 2.08 |
| 10-31 11:35 | +15 | ZEC | UP | 0.68 | 0.87 | 1.63 |
| 10-31 11:35 | +10 | ZEC | UP | 0.68 | 0.82 | 1.10 |
| 10-31 11:35 | +5 | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 10-31 11:35 | +10 stop | BNB | UP | 0.55 | 0.76 | 1.79 |
| 10-31 11:34 | +10 stop | SOL | UP | 0.52 | 0.37 | -1.85 |
| 10-31 11:34 | +10 stop | DOGE | UP | 0.52 | 0.37 | -1.85 |
| 10-31 11:33 | +10 stop | HYPE | UP | 0.66 | 0.41 | -2.87 |
| 10-31 11:32 | +10 stop | XRP | UP | 0.71 | 0.87 | 1.41 |
| 10-31 11:32 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-31 11:32 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-31 11:32 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-31 11:32 | +10 stop | ZEC | UP | 0.57 | 0.69 | 0.91 |
| 10-31 11:32 | +20 | ZEC | UP | 0.57 | 0.78 | 1.83 |
| 10-31 11:32 | +15 | ZEC | UP | 0.57 | 0.74 | 1.42 |
| 10-31 11:32 | +10 | ZEC | UP | 0.56 | 0.69 | 0.97 |
| 10-31 11:32 | +5 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 10-31 11:32 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.25 |
| 10-31 11:31 | +10 stop | SOL | DOWN | 0.57 | 0.35 | -2.54 |
| 10-31 11:31 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 11:31 | +15 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 11:31 | +10 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-31 11:31 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-31 11:31 | +10 stop | HYPE | DOWN | 0.53 | 0.38 | -1.88 |
| 10-31 11:31 | +20 | HYPE | DOWN | 0.54 | 0.80 | 2.30 |
| 10-31 11:31 | +15 | HYPE | DOWN | 0.56 | 0.73 | 1.38 |
| 10-31 11:31 | +10 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-31 11:31 | +5 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
