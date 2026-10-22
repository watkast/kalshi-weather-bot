# Range-Scalp Bot

*Updated Thu Oct 22 11:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28683 | 24995 | 3688 (39) | 2 | $-8244.73 | -4.6% |
| **+10¢** | 21530 | 17262 | 4268 (55) | 3 | $-7340.73 | -5.4% |
| **+15¢** | 18023 | 13434 | 4589 (78) | 4 | $-6551.24 | -5.8% |
| **+20¢** | 15943 | 11130 | 4813 (100) | 7 | $-5908.04 | -5.9% |
| **+10¢ (15¢ stop)** | 35182 | 35123 | 59 (32) | 1 | $-13159.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 11:49 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-22 11:48 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.87 |
| 10-22 11:48 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-22 11:48 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-22 11:48 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-22 11:48 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-22 11:48 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-22 11:48 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-22 11:48 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 10-22 11:48 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 10-22 11:48 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-22 11:48 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-22 11:48 | +10 | NEAR | DOWN | 0.65 | open |  |
| 10-22 11:48 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-22 11:47 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:47 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-22 11:47 | +15 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-22 11:47 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 11:47 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-22 11:47 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-22 11:47 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-22 11:47 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-22 11:47 | +10 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-22 11:47 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 11:47 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-22 11:47 | +15 | BNB | DOWN | 0.57 | 0.75 | 1.48 |
| 10-22 11:47 | +10 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 11:47 | +5 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-22 11:47 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-22 11:47 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-22 11:47 | +15 | XRP | DOWN | 0.64 | 0.82 | 1.52 |
| 10-22 11:47 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-22 11:47 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-22 11:47 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-22 11:47 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-22 11:47 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 11:47 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
