# Range-Scalp Bot

*Updated Fri Oct 16 07:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18822 | 16350 | 2472 (28) | 3 | $-5707.42 | -4.8% |
| **+10¢** | 14182 | 11321 | 2861 (40) | 4 | $-5183.98 | -5.8% |
| **+15¢** | 11885 | 8805 | 3080 (59) | 7 | $-4700.49 | -6.3% |
| **+20¢** | 10553 | 7330 | 3223 (78) | 9 | $-4130.17 | -6.2% |
| **+10¢ (15¢ stop)** | 23177 | 23127 | 50 (29) | 3 | $-8959.41 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 07:10 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-16 07:09 | +10 | HYPE | DOWN | 0.71 | open |  |
| 10-16 07:09 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-16 07:09 | +5 | ETH | UP | 0.60 | 0.73 | 0.99 |
| 10-16 07:09 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 07:08 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-16 07:08 | +10 stop | ETH | UP | 0.65 | open |  |
| 10-16 07:08 | +20 | ETH | UP | 0.65 | open |  |
| 10-16 07:08 | +15 | ETH | UP | 0.65 | open |  |
| 10-16 07:08 | +10 | ETH | UP | 0.64 | open |  |
| 10-16 07:08 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-16 07:08 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 10-16 07:08 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 10-16 07:08 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-16 07:08 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 10-16 07:08 | +10 stop | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-16 07:08 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-16 07:08 | +10 | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-16 07:08 | +5 | BTC | DOWN | 0.61 | 0.70 | 0.58 |
| 10-16 07:07 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-16 07:07 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-16 07:07 | +10 stop | DOGE | UP | 0.61 | 0.40 | -2.44 |
| 10-16 07:07 | +10 stop | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 10-16 07:07 | +10 stop | ZEC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-16 07:07 | +5 | BNB | DOWN | 0.47 | 0.55 | 0.44 |
| 10-16 07:07 | +10 stop | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 10-16 07:07 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-16 07:07 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-16 07:06 | +10 stop | NEAR | UP | 0.57 | 0.40 | -2.05 |
| 10-16 07:06 | +10 | NEAR | UP | 0.59 | open |  |
| 10-16 07:06 | +5 | NEAR | UP | 0.59 | open |  |
| 10-16 07:05 | +20 | ZEC | UP | 0.64 | open |  |
| 10-16 07:05 | +10 stop | NEAR | UP | 0.52 | 0.65 | 0.96 |
| 10-16 07:05 | +10 | NEAR | UP | 0.53 | 0.65 | 0.86 |
| 10-16 07:05 | +5 | NEAR | UP | 0.53 | 0.65 | 0.86 |
| 10-16 07:05 | +20 | DOGE | UP | 0.71 | open |  |
| 10-16 07:05 | +15 | DOGE | UP | 0.71 | open |  |
| 10-16 07:05 | +15 | ZEC | UP | 0.59 | open |  |
| 10-16 07:05 | +10 stop | DOGE | UP | 0.65 | 0.77 | 0.91 |
| 10-16 07:05 | +15 | BTC | UP | 0.70 | open |  |
