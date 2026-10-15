# Range-Scalp Bot

*Updated Thu Oct 15 18:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17929 | 15559 | 2370 (28) | 1 | $-5530.60 | -4.9% |
| **+10¢** | 13544 | 10799 | 2745 (40) | 1 | $-5029.94 | -5.9% |
| **+15¢** | 11359 | 8408 | 2951 (59) | 2 | $-4533.96 | -6.4% |
| **+20¢** | 10096 | 7009 | 3087 (77) | 3 | $-3953.98 | -6.2% |
| **+10¢ (15¢ stop)** | 22079 | 22029 | 50 (29) | 0 | $-8544.06 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 18:05 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 10-15 18:03 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-15 18:02 | +10 stop | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-15 18:02 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-15 18:02 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-15 18:02 | +10 stop | ZEC | UP | 0.63 | 0.47 | -1.95 |
| 10-15 18:01 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 18:01 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-15 18:01 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-15 18:01 | +10 | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 10-15 18:01 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 10-15 18:01 | +10 stop | ZEC | UP | 0.70 | 0.53 | -2.03 |
| 10-15 18:01 | +20 | ZEC | UP | 0.70 | open |  |
| 10-15 18:01 | +15 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-15 18:01 | +10 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-15 18:01 | +5 | ZEC | UP | 0.70 | 0.75 | 0.21 |
| 10-15 18:01 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 10-15 18:01 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-15 18:01 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-15 18:01 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-15 18:01 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-15 18:00 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 18:00 | +20 | BNB | DOWN | 0.56 | 0.80 | 2.10 |
| 10-15 18:00 | +15 | BNB | DOWN | 0.56 | 0.71 | 1.17 |
| 10-15 18:00 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 18:00 | +5 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 17:58 | +10 stop | HYPE | UP | 0.67 | 0.95 | 2.58 |
| 10-15 17:58 | +15 | HYPE | UP | 0.67 | 0.95 | 2.58 |
| 10-15 17:58 | +10 | HYPE | UP | 0.67 | 0.95 | 2.58 |
| 10-15 17:58 | +5 | HYPE | UP | 0.67 | 0.95 | 2.58 |
| 10-15 17:57 | +10 stop | BNB | DOWN | 0.50 | 0.31 | -2.23 |
| 10-15 17:55 | +10 stop | HYPE | UP | 0.68 | 0.85 | 1.47 |
| 10-15 17:55 | +20 | HYPE | UP | 0.68 | 0.95 | 2.50 |
| 10-15 17:55 | +15 | HYPE | UP | 0.68 | 0.85 | 1.47 |
| 10-15 17:55 | +10 | HYPE | UP | 0.68 | 0.85 | 1.47 |
| 10-15 17:55 | +5 | HYPE | UP | 0.68 | 0.74 | 0.32 |
| 10-15 17:54 | +5 | ZEC | UP | 0.56 | no | -5.78 |
| 10-15 17:53 | +5 | ZEC | UP | 0.53 | 0.66 | 0.96 |
| 10-15 17:52 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-15 17:52 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.82 |
