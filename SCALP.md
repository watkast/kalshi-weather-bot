# Range-Scalp Bot

*Updated Fri Oct 16 02:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18574 | 16134 | 2440 (28) | 3 | $-5627.55 | -4.8% |
| **+10¢** | 14006 | 11184 | 2822 (40) | 4 | $-5081.55 | -5.8% |
| **+15¢** | 11743 | 8705 | 3038 (59) | 4 | $-4599.65 | -6.2% |
| **+20¢** | 10426 | 7247 | 3179 (78) | 6 | $-4022.41 | -6.1% |
| **+10¢ (15¢ stop)** | 22882 | 22832 | 50 (29) | 0 | $-8846.95 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 02:32 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-16 02:32 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 10-16 02:32 | +10 stop | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 10-16 02:32 | +20 | NEAR | DOWN | 0.58 | 0.81 | 2.01 |
| 10-16 02:32 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-16 02:32 | +10 | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 10-16 02:32 | +5 | NEAR | DOWN | 0.58 | 0.65 | 0.36 |
| 10-16 02:32 | +5 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-16 02:32 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-16 02:32 | +20 | BTC | UP | 0.71 | open |  |
| 10-16 02:32 | +15 | BTC | UP | 0.71 | 0.90 | 1.71 |
| 10-16 02:32 | +10 | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-16 02:32 | +5 | BTC | UP | 0.71 | 0.80 | 0.63 |
| 10-16 02:32 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-16 02:32 | +20 | ZEC | UP | 0.70 | open |  |
| 10-16 02:32 | +15 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-16 02:32 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-16 02:32 | +5 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-16 02:31 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.73 |
| 10-16 02:31 | +20 | BNB | UP | 0.68 | 0.89 | 1.89 |
| 10-16 02:31 | +15 | BNB | UP | 0.68 | 0.85 | 1.47 |
| 10-16 02:31 | +10 | BNB | UP | 0.68 | 0.78 | 0.73 |
| 10-16 02:31 | +5 | BNB | UP | 0.68 | 0.76 | 0.53 |
| 10-16 02:31 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.05 |
| 10-16 02:31 | +20 | XRP | DOWN | 0.58 | open |  |
| 10-16 02:31 | +15 | XRP | DOWN | 0.58 | open |  |
| 10-16 02:31 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-16 02:31 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-16 02:31 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-16 02:31 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-16 02:31 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-16 02:31 | +10 | SOL | DOWN | 0.57 | open |  |
| 10-16 02:31 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-16 02:31 | +10 stop | ETH | DOWN | 0.56 | 0.35 | -2.42 |
| 10-16 02:31 | +20 | ETH | DOWN | 0.56 | open |  |
| 10-16 02:31 | +15 | ETH | DOWN | 0.56 | open |  |
| 10-16 02:31 | +10 | ETH | DOWN | 0.55 | open |  |
| 10-16 02:31 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-16 02:31 | +10 stop | DOGE | DOWN | 0.53 | 0.36 | -2.05 |
| 10-16 02:31 | +20 | DOGE | DOWN | 0.53 | open |  |
