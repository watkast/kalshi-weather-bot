# Range-Scalp Bot

*Updated Tue Oct 27 00:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35721 | 31175 | 4546 (43) | 3 | $-9996.53 | -4.4% |
| **+10¢** | 26701 | 21442 | 5259 (65) | 3 | $-8847.60 | -5.3% |
| **+15¢** | 22350 | 16697 | 5653 (89) | 4 | $-7888.61 | -5.6% |
| **+20¢** | 19810 | 13886 | 5924 (112) | 4 | $-6952.33 | -5.6% |
| **+10¢ (15¢ stop)** | 43782 | 43720 | 62 (33) | 2 | $-16689.77 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 00:53 | +10 stop | NEAR | DOWN | 0.64 | open |  |
| 10-27 00:53 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-27 00:53 | +5 | ETH | UP | 0.67 | 0.76 | 0.61 |
| 10-27 00:53 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-27 00:52 | +10 stop | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 10-27 00:52 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-27 00:51 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 10-27 00:51 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-27 00:51 | +15 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-27 00:51 | +10 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-27 00:51 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
| 10-27 00:50 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-27 00:50 | +5 | XRP | UP | 0.60 | 0.68 | 0.47 |
| 10-27 00:49 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-27 00:49 | +10 stop | XRP | DOWN | 0.49 | 0.66 | 1.36 |
| 10-27 00:49 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-27 00:49 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-27 00:49 | +5 | HYPE | UP | 0.63 | 0.69 | 0.24 |
| 10-27 00:49 | +5 | XRP | DOWN | 0.47 | 0.66 | 1.56 |
| 10-27 00:48 | +10 stop | ZEC | DOWN | 0.64 | 0.47 | -2.05 |
| 10-27 00:48 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.51 |
| 10-27 00:48 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 00:48 | +10 | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-27 00:48 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 10-27 00:48 | +10 stop | HYPE | UP | 0.55 | 0.69 | 1.07 |
| 10-27 00:48 | +10 | HYPE | UP | 0.55 | 0.69 | 1.07 |
| 10-27 00:48 | +5 | HYPE | UP | 0.55 | 0.60 | 0.15 |
| 10-27 00:48 | +5 | DOGE | UP | 0.47 | 0.61 | 1.05 |
| 10-27 00:48 | +5 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 10-27 00:47 | +10 stop | ZEC | UP | 0.70 | 0.43 | -3.03 |
| 10-27 00:47 | +10 | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 10-27 00:47 | +5 | ZEC | UP | 0.69 | 0.77 | 0.52 |
| 10-27 00:47 | +5 | SOL | UP | 0.61 | 0.72 | 0.78 |
| 10-27 00:47 | +10 stop | DOGE | UP | 0.55 | 0.39 | -1.95 |
| 10-27 00:47 | +15 | DOGE | UP | 0.55 | open |  |
| 10-27 00:47 | +10 | DOGE | UP | 0.55 | open |  |
| 10-27 00:47 | +5 | DOGE | UP | 0.55 | 0.62 | 0.35 |
| 10-27 00:47 | +10 stop | SOL | UP | 0.55 | 0.72 | 1.37 |
| 10-27 00:47 | +20 | SOL | UP | 0.55 | 0.76 | 1.79 |
| 10-27 00:47 | +15 | SOL | UP | 0.55 | 0.72 | 1.37 |
