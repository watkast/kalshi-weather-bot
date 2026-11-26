# Range-Scalp Bot

*Updated Thu Nov 26 12:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72676 | 63439 | 9237 (158) | 8 | $-19306.88 | -4.2% |
| **+10¢** | 54200 | 43411 | 10789 (203) | 8 | $-17912.49 | -5.3% |
| **+15¢** | 45382 | 33758 | 11624 (261) | 8 | $-16023.48 | -5.6% |
| **+20¢** | 40393 | 28154 | 12239 (327) | 9 | $-14408.67 | -5.7% |
| **+10¢ (15¢ stop)** | 88513 | 88304 | 209 (128) | 2 | $-32550.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 12:55 | +10 | BTC | UP | 0.62 | open |  |
| 11-26 12:55 | +5 | BTC | UP | 0.62 | open |  |
| 11-26 12:54 | +10 stop | BTC | UP | 0.61 | open |  |
| 11-26 12:54 | +10 stop | SOL | DOWN | 0.58 | open |  |
| 11-26 12:53 | +10 stop | ETH | DOWN | 0.70 | 0.50 | -2.33 |
| 11-26 12:51 | +10 stop | BNB | UP | 0.59 | 0.75 | 1.29 |
| 11-26 12:51 | +10 stop | BTC | DOWN | 0.68 | 0.39 | -3.23 |
| 11-26 12:50 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.14 |
| 11-26 12:49 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 11-26 12:48 | +10 stop | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 11-26 12:48 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 11-26 12:48 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-26 12:48 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-26 12:48 | +10 stop | NEAR | DOWN | 0.54 | 0.65 | 0.79 |
| 11-26 12:47 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-26 12:47 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-26 12:47 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-26 12:47 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-26 12:46 | +10 stop | NEAR | UP | 0.65 | 0.39 | -2.91 |
| 11-26 12:46 | +20 | NEAR | UP | 0.65 | open |  |
| 11-26 12:46 | +15 | NEAR | UP | 0.64 | open |  |
| 11-26 12:46 | +10 | NEAR | UP | 0.64 | open |  |
| 11-26 12:46 | +5 | NEAR | UP | 0.64 | open |  |
| 11-26 12:46 | +10 stop | XRP | UP | 0.56 | 0.37 | -2.25 |
| 11-26 12:46 | +20 | XRP | UP | 0.56 | open |  |
| 11-26 12:46 | +15 | XRP | UP | 0.56 | open |  |
| 11-26 12:46 | +10 | XRP | UP | 0.56 | open |  |
| 11-26 12:46 | +5 | XRP | UP | 0.56 | open |  |
| 11-26 12:46 | +10 stop | DOGE | UP | 0.63 | 0.45 | -2.15 |
| 11-26 12:46 | +20 | DOGE | UP | 0.63 | open |  |
| 11-26 12:46 | +15 | DOGE | UP | 0.63 | open |  |
| 11-26 12:46 | +10 | DOGE | UP | 0.63 | open |  |
| 11-26 12:46 | +5 | DOGE | UP | 0.63 | open |  |
| 11-26 12:46 | +10 stop | BTC | UP | 0.58 | 0.43 | -1.86 |
| 11-26 12:46 | +20 | BTC | UP | 0.58 | open |  |
| 11-26 12:46 | +15 | BTC | UP | 0.58 | open |  |
| 11-26 12:46 | +10 | BTC | UP | 0.58 | 0.68 | 0.66 |
| 11-26 12:46 | +5 | BTC | UP | 0.58 | 0.68 | 0.66 |
| 11-26 12:46 | +10 stop | BNB | UP | 0.65 | 0.47 | -2.14 |
| 11-26 12:46 | +20 | BNB | UP | 0.65 | open |  |
