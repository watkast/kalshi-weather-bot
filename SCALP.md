# Range-Scalp Bot

*Updated Tue Oct 06 16:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5197 | 4506 | 691 (7) | 6 | $-1593.47 | -4.9% |
| **+10¢** | 3973 | 3164 | 809 (12) | 6 | $-1475.55 | -5.9% |
| **+15¢** | 3336 | 2480 | 856 (15) | 7 | $-1266.07 | -6.0% |
| **+20¢** | 2984 | 2094 | 890 (22) | 7 | $-999.32 | -5.3% |
| **+10¢ (15¢ stop)** | 6356 | 6341 | 15 (9) | 0 | $-2322.37 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 16:56 | +10 stop | ZEC | UP | 0.66 | 0.50 | -1.94 |
| 10-06 16:56 | +10 | ZEC | UP | 0.66 | open |  |
| 10-06 16:56 | +5 | ZEC | UP | 0.66 | open |  |
| 10-06 16:56 | +10 stop | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 10-06 16:56 | +10 stop | HYPE | UP | 0.56 | 0.36 | -2.35 |
| 10-06 16:55 | +5 | SOL | UP | 0.54 | open |  |
| 10-06 16:55 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 10-06 16:54 | +5 | SOL | UP | 0.54 | 0.62 | 0.45 |
| 10-06 16:54 | +20 | HYPE | UP | 0.67 | open |  |
| 10-06 16:54 | +5 | HYPE | UP | 0.67 | open |  |
| 10-06 16:54 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 10-06 16:54 | +10 | BNB | UP | 0.62 | open |  |
| 10-06 16:54 | +5 | BNB | UP | 0.62 | open |  |
| 10-06 16:53 | +10 stop | NEAR | UP | 0.65 | 0.49 | -1.94 |
| 10-06 16:53 | +20 | NEAR | UP | 0.65 | open |  |
| 10-06 16:53 | +15 | NEAR | UP | 0.65 | open |  |
| 10-06 16:53 | +10 | NEAR | UP | 0.65 | open |  |
| 10-06 16:53 | +5 | NEAR | UP | 0.65 | open |  |
| 10-06 16:53 | +10 stop | ETH | DOWN | 0.55 | 0.33 | -2.54 |
| 10-06 16:53 | +10 stop | ZEC | UP | 0.60 | 0.70 | 0.68 |
| 10-06 16:53 | +5 | ZEC | UP | 0.60 | 0.67 | 0.37 |
| 10-06 16:53 | +5 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-06 16:53 | +10 stop | SOL | UP | 0.67 | 0.47 | -2.34 |
| 10-06 16:53 | +15 | SOL | UP | 0.67 | open |  |
| 10-06 16:53 | +10 | SOL | UP | 0.67 | open |  |
| 10-06 16:53 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-06 16:53 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 10-06 16:53 | +15 | HYPE | UP | 0.71 | open |  |
| 10-06 16:53 | +10 | HYPE | UP | 0.71 | open |  |
| 10-06 16:52 | +5 | ETH | UP | 0.46 | 0.61 | 1.15 |
| 10-06 16:52 | +10 stop | BTC | UP | 0.54 | 0.35 | -2.24 |
| 10-06 16:52 | +10 stop | ETH | UP | 0.58 | 0.39 | -2.25 |
| 10-06 16:52 | +10 stop | BNB | UP | 0.59 | 0.72 | 0.98 |
| 10-06 16:52 | +5 | HYPE | UP | 0.69 | 0.78 | 0.58 |
| 10-06 16:51 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 10-06 16:50 | +10 stop | SOL | UP | 0.55 | 0.68 | 0.96 |
| 10-06 16:50 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-06 16:50 | +10 stop | ETH | DOWN | 0.49 | 0.61 | 0.85 |
| 10-06 16:50 | +10 stop | SOL | DOWN | 0.40 | 0.57 | 1.35 |
| 10-06 16:48 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.24 |
