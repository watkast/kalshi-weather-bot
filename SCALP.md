# Range-Scalp Bot

*Updated Fri Nov 06 17:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49849 | 43450 | 6399 (76) | 3 | $-14014.72 | -4.5% |
| **+10¢** | 37210 | 29768 | 7442 (101) | 4 | $-12899.90 | -5.5% |
| **+15¢** | 31165 | 23146 | 8019 (130) | 4 | $-11807.30 | -6.0% |
| **+20¢** | 27703 | 19296 | 8407 (171) | 4 | $-10442.63 | -6.0% |
| **+10¢ (15¢ stop)** | 60743 | 60646 | 97 (57) | 1 | $-22494.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 17:56 | +10 stop | BTC | UP | 0.50 | 0.64 | 1.05 |
| 11-06 17:56 | +10 stop | BNB | DOWN | 0.59 | open |  |
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
| 11-06 17:49 | +10 stop | BTC | DOWN | 0.70 | 0.51 | -2.23 |
| 11-06 17:49 | +10 stop | NEAR | DOWN | 0.54 | 0.33 | -2.44 |
| 11-06 17:49 | +10 stop | ETH | DOWN | 0.63 | 0.48 | -1.85 |
| 11-06 17:49 | +10 stop | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-06 17:49 | +20 | ZEC | UP | 0.67 | 0.88 | 1.86 |
| 11-06 17:49 | +15 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-06 17:49 | +10 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-06 17:49 | +5 | ZEC | UP | 0.67 | 0.76 | 0.61 |
| 11-06 17:49 | +10 stop | SOL | DOWN | 0.71 | 0.47 | -2.73 |
| 11-06 17:48 | +10 stop | DOGE | DOWN | 0.65 | 0.38 | -3.03 |
