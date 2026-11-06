# Range-Scalp Bot

*Updated Fri Nov 06 13:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49540 | 43174 | 6366 (76) | 1 | $-13990.96 | -4.5% |
| **+10¢** | 36985 | 29585 | 7400 (101) | 1 | $-12846.74 | -5.5% |
| **+15¢** | 30975 | 23004 | 7971 (130) | 1 | $-11742.21 | -6.0% |
| **+20¢** | 27536 | 19182 | 8354 (171) | 1 | $-10361.93 | -6.0% |
| **+10¢ (15¢ stop)** | 60377 | 60280 | 97 (57) | 1 | $-22340.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 13:41 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 11-06 13:41 | +10 | DOGE | DOWN | 0.66 | open |  |
| 11-06 13:41 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-06 13:39 | +10 stop | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-06 13:39 | +10 | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-06 13:39 | +5 | DOGE | DOWN | 0.51 | 0.69 | 1.47 |
| 11-06 13:39 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 11-06 13:37 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.46 |
| 11-06 13:37 | +5 | SOL | DOWN | 0.49 | 0.67 | 1.46 |
| 11-06 13:36 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-06 13:35 | +10 stop | DOGE | DOWN | 0.63 | 0.47 | -1.95 |
| 11-06 13:35 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-06 13:35 | +10 stop | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 11-06 13:35 | +10 | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 11-06 13:35 | +5 | NEAR | DOWN | 0.69 | 0.78 | 0.62 |
| 11-06 13:34 | +10 stop | DOGE | UP | 0.62 | 0.42 | -2.35 |
| 11-06 13:34 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-06 13:33 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 13:33 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-06 13:33 | +20 | BTC | DOWN | 0.71 | 0.91 | 1.83 |
| 11-06 13:33 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 13:33 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-06 13:33 | +5 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-06 13:33 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 13:33 | +20 | HYPE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-06 13:33 | +15 | HYPE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-06 13:33 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-06 13:33 | +5 | HYPE | DOWN | 0.66 | 0.77 | 0.82 |
| 11-06 13:33 | +5 | XRP | DOWN | 0.66 | 0.82 | 1.35 |
| 11-06 13:32 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-06 13:32 | +20 | BNB | DOWN | 0.57 | 0.77 | 1.69 |
| 11-06 13:32 | +15 | BNB | DOWN | 0.57 | 0.73 | 1.28 |
| 11-06 13:32 | +10 | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-06 13:32 | +5 | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-06 13:32 | +10 stop | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 11-06 13:32 | +20 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 11-06 13:32 | +15 | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 11-06 13:32 | +10 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-06 13:32 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 11-06 13:32 | +10 stop | ETH | DOWN | 0.60 | 0.75 | 1.19 |
