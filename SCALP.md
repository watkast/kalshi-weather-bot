# Range-Scalp Bot

*Updated Fri Nov 06 18:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49854 | 43455 | 6399 (76) | 0 | $-14012.07 | -4.5% |
| **+10¢** | 37214 | 29772 | 7442 (101) | 2 | $-12893.14 | -5.5% |
| **+15¢** | 31169 | 23150 | 8019 (130) | 2 | $-11797.94 | -6.0% |
| **+20¢** | 27707 | 19300 | 8407 (171) | 2 | $-10433.17 | -6.0% |
| **+10¢ (15¢ stop)** | 60744 | 60647 | 97 (57) | 2 | $-22498.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 18:00 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 11-06 18:00 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-06 18:00 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-06 18:00 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-06 18:00 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-06 18:00 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 11-06 18:00 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-06 18:00 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-06 18:00 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-06 18:00 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-06 17:56 | +10 stop | BTC | UP | 0.50 | 0.64 | 1.05 |
| 11-06 17:56 | +10 stop | BNB | DOWN | 0.59 | 0.26 | -3.61 |
| 11-06 17:55 | +10 stop | NEAR | UP | 0.67 | 0.84 | 1.44 |
| 11-06 17:55 | +5 | NEAR | UP | 0.67 | 0.84 | 1.44 |
| 11-06 17:55 | +10 stop | BTC | DOWN | 0.67 | 0.45 | -2.54 |
| 11-06 17:55 | +10 stop | SOL | DOWN | 0.62 | 0.46 | -1.95 |
| 11-06 17:54 | +5 | HYPE | UP | 0.57 | 0.65 | 0.46 |
| 11-06 17:53 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-06 17:53 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 11-06 17:53 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-06 17:53 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 11-06 17:53 | +10 stop | ETH | DOWN | 0.71 | 0.50 | -2.43 |
| 11-06 17:53 | +10 stop | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 11-06 17:53 | +15 | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 11-06 17:53 | +10 | DOGE | UP | 0.48 | 0.66 | 1.46 |
| 11-06 17:53 | +5 | DOGE | UP | 0.48 | 0.57 | 0.54 |
| 11-06 17:53 | +10 stop | NEAR | UP | 0.55 | 0.40 | -1.85 |
| 11-06 17:53 | +15 | NEAR | UP | 0.55 | 0.70 | 1.17 |
| 11-06 17:53 | +10 | NEAR | UP | 0.55 | 0.65 | 0.66 |
| 11-06 17:53 | +5 | NEAR | UP | 0.55 | 0.62 | 0.35 |
| 11-06 17:53 | +10 stop | HYPE | UP | 0.56 | 0.74 | 1.43 |
| 11-06 17:53 | +15 | HYPE | UP | 0.56 | 0.74 | 1.43 |
| 11-06 17:53 | +10 | HYPE | UP | 0.56 | 0.74 | 1.46 |
| 11-06 17:53 | +5 | HYPE | UP | 0.55 | 0.60 | 0.15 |
| 11-06 17:52 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 17:52 | +10 stop | ETH | UP | 0.71 | 0.49 | -2.53 |
| 11-06 17:52 | +10 | ETH | UP | 0.71 | 0.87 | 1.37 |
| 11-06 17:52 | +5 | ETH | UP | 0.71 | 0.76 | 0.22 |
| 11-06 17:52 | +10 stop | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 11-06 17:52 | +10 stop | XRP | DOWN | 0.64 | 0.82 | 1.52 |
