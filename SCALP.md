# Range-Scalp Bot

*Updated Wed Oct 14 22:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16617 | 14406 | 2211 (28) | 5 | $-5189.72 | -5.0% |
| **+10¢** | 12572 | 10010 | 2562 (40) | 6 | $-4738.75 | -6.0% |
| **+15¢** | 10562 | 7810 | 2752 (59) | 6 | $-4255.09 | -6.4% |
| **+20¢** | 9384 | 6500 | 2884 (76) | 6 | $-3761.25 | -6.4% |
| **+10¢ (15¢ stop)** | 20468 | 20418 | 50 (29) | 3 | $-7875.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 22:27 | +10 stop | NEAR | UP | 0.52 | open |  |
| 10-14 22:27 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-14 22:27 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-14 22:27 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-14 22:27 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 10-14 22:27 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-14 22:27 | +15 | ETH | DOWN | 0.66 | open |  |
| 10-14 22:27 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-14 22:27 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-14 22:26 | +10 stop | NEAR | UP | 0.53 | 0.66 | 0.96 |
| 10-14 22:25 | +10 stop | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 10-14 22:23 | +10 stop | DOGE | UP | 0.54 | 0.68 | 1.06 |
| 10-14 22:23 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-14 22:22 | +10 stop | DOGE | UP | 0.68 | 0.49 | -2.24 |
| 10-14 22:21 | +10 stop | NEAR | DOWN | 0.68 | 0.32 | -3.92 |
| 10-14 22:21 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-14 22:21 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-14 22:21 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-14 22:21 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-14 22:21 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-14 22:21 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-14 22:21 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-14 22:21 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 10-14 22:21 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 10-14 22:21 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-14 22:21 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-14 22:21 | +10 | DOGE | DOWN | 0.67 | open |  |
| 10-14 22:21 | +5 | DOGE | DOWN | 0.67 | open |  |
| 10-14 22:21 | +10 stop | XRP | DOWN | 0.60 | 0.45 | -1.85 |
| 10-14 22:21 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-14 22:21 | +10 | XRP | DOWN | 0.62 | open |  |
| 10-14 22:21 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-14 22:17 | +10 stop | ZEC | DOWN | 0.62 | 0.44 | -2.18 |
| 10-14 22:17 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-14 22:17 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-14 22:16 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 22:16 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-14 22:16 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 10-14 22:16 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 22:16 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
