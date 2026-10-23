# Range-Scalp Bot

*Updated Fri Oct 23 15:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30542 | 26608 | 3934 (39) | 6 | $-8879.53 | -4.6% |
| **+10¢** | 22855 | 18304 | 4551 (56) | 7 | $-7944.79 | -5.5% |
| **+15¢** | 19126 | 14232 | 4894 (79) | 8 | $-7158.80 | -6.0% |
| **+20¢** | 16937 | 11810 | 5127 (102) | 8 | $-6432.04 | -6.0% |
| **+10¢ (15¢ stop)** | 37432 | 37373 | 59 (32) | 5 | $-14172.07 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 15:20 | +15 | SOL | UP | 0.49 | open |  |
| 10-23 15:20 | +10 stop | ZEC | DOWN | 0.55 | open |  |
| 10-23 15:19 | +10 stop | ETH | UP | 0.65 | open |  |
| 10-23 15:19 | +15 | ETH | UP | 0.65 | open |  |
| 10-23 15:19 | +10 | ETH | UP | 0.65 | open |  |
| 10-23 15:19 | +5 | ETH | UP | 0.66 | open |  |
| 10-23 15:19 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 10-23 15:19 | +10 | NEAR | UP | 0.64 | open |  |
| 10-23 15:19 | +10 stop | SOL | UP | 0.61 | open |  |
| 10-23 15:19 | +10 | SOL | UP | 0.60 | open |  |
| 10-23 15:19 | +10 stop | DOGE | UP | 0.61 | 0.46 | -1.85 |
| 10-23 15:19 | +15 | DOGE | UP | 0.61 | open |  |
| 10-23 15:19 | +10 | DOGE | UP | 0.61 | open |  |
| 10-23 15:19 | +5 | DOGE | UP | 0.61 | open |  |
| 10-23 15:19 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 10-23 15:19 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 10-23 15:19 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 10-23 15:18 | +5 | ETH | UP | 0.64 | 0.72 | 0.48 |
| 10-23 15:18 | +5 | NEAR | UP | 0.60 | open |  |
| 10-23 15:18 | +10 stop | BTC | UP | 0.60 | open |  |
| 10-23 15:18 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 10-23 15:18 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-23 15:18 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-23 15:18 | +5 | DOGE | UP | 0.61 | 0.67 | 0.27 |
| 10-23 15:18 | +5 | BNB | UP | 0.68 | 0.77 | 0.61 |
| 10-23 15:18 | +10 stop | HYPE | DOWN | 0.62 | open |  |
| 10-23 15:18 | +5 | SOL | DOWN | 0.50 | open |  |
| 10-23 15:18 | +10 stop | SOL | DOWN | 0.55 | 0.34 | -2.44 |
| 10-23 15:17 | +10 stop | ZEC | DOWN | 0.63 | 0.43 | -2.35 |
| 10-23 15:17 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-23 15:17 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-23 15:17 | +10 stop | XRP | DOWN | 0.50 | 0.31 | -2.23 |
| 10-23 15:17 | +5 | XRP | DOWN | 0.50 | 0.56 | 0.24 |
| 10-23 15:17 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 10-23 15:17 | +5 | BNB | UP | 0.49 | 0.55 | 0.24 |
| 10-23 15:17 | +10 stop | BTC | DOWN | 0.63 | 0.48 | -1.85 |
| 10-23 15:16 | +10 stop | NEAR | UP | 0.54 | 0.64 | 0.65 |
| 10-23 15:16 | +20 | NEAR | UP | 0.53 | open |  |
| 10-23 15:16 | +15 | NEAR | UP | 0.53 | open |  |
| 10-23 15:16 | +10 | NEAR | UP | 0.53 | 0.64 | 0.75 |
