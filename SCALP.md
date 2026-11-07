# Range-Scalp Bot

*Updated Sat Nov 07 02:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50335 | 43877 | 6458 (76) | 1 | $-14153.94 | -4.5% |
| **+10¢** | 37560 | 30042 | 7518 (102) | 4 | $-13078.78 | -5.5% |
| **+15¢** | 31451 | 23350 | 8101 (131) | 6 | $-11989.40 | -6.1% |
| **+20¢** | 27960 | 19465 | 8495 (173) | 6 | $-10616.95 | -6.1% |
| **+10¢ (15¢ stop)** | 61290 | 61191 | 99 (58) | 4 | $-22708.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 02:18 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 11-07 02:18 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 02:18 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-07 02:18 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-07 02:18 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-07 02:18 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-07 02:17 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 11-07 02:17 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-07 02:17 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-07 02:17 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-07 02:17 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 11-07 02:17 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 11-07 02:17 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-07 02:17 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-07 02:17 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-07 02:17 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-07 02:17 | +10 stop | HYPE | UP | 0.56 | open |  |
| 11-07 02:17 | +20 | HYPE | UP | 0.56 | open |  |
| 11-07 02:17 | +15 | HYPE | UP | 0.56 | open |  |
| 11-07 02:17 | +10 | HYPE | UP | 0.56 | open |  |
| 11-07 02:17 | +5 | HYPE | UP | 0.56 | open |  |
| 11-07 02:16 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-07 02:16 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-07 02:16 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-07 02:16 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-07 02:16 | +5 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-07 02:16 | +10 stop | SOL | DOWN | 0.50 | 0.67 | 1.36 |
| 11-07 02:16 | +20 | SOL | DOWN | 0.50 | 0.73 | 1.98 |
| 11-07 02:16 | +15 | SOL | DOWN | 0.50 | 0.67 | 1.36 |
| 11-07 02:16 | +10 | SOL | DOWN | 0.50 | 0.67 | 1.36 |
| 11-07 02:16 | +5 | SOL | DOWN | 0.50 | 0.57 | 0.34 |
| 11-07 02:16 | +10 stop | NEAR | UP | 0.66 | open |  |
| 11-07 02:16 | +20 | NEAR | UP | 0.66 | open |  |
| 11-07 02:16 | +15 | NEAR | UP | 0.66 | open |  |
| 11-07 02:16 | +10 | NEAR | UP | 0.66 | open |  |
| 11-07 02:16 | +5 | NEAR | UP | 0.66 | 0.74 | 0.50 |
| 11-07 02:15 | +10 stop | BNB | DOWN | 0.60 | 0.74 | 1.09 |
| 11-07 02:15 | +20 | BNB | DOWN | 0.60 | 0.82 | 1.92 |
| 11-07 02:15 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 11-07 02:15 | +10 | BNB | DOWN | 0.60 | 0.74 | 1.09 |
