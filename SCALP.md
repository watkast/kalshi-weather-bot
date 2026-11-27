# Range-Scalp Bot

*Updated Fri Nov 27 16:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73782 | 64392 | 9390 (171) | 0 | $-19603.20 | -4.2% |
| **+10¢** | 54981 | 44016 | 10965 (216) | 2 | $-18220.07 | -5.3% |
| **+15¢** | 46038 | 34228 | 11810 (274) | 3 | $-16306.61 | -5.6% |
| **+20¢** | 40967 | 28529 | 12438 (341) | 5 | $-14725.17 | -5.7% |
| **+10¢ (15¢ stop)** | 89831 | 89612 | 219 (135) | 0 | $-33173.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 16:56 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-27 16:56 | +10 stop | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 11-27 16:56 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 11-27 16:56 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-27 16:55 | +5 | NEAR | UP | 0.40 | 0.57 | 1.35 |
| 11-27 16:55 | +10 stop | NEAR | UP | 0.61 | 0.39 | -2.54 |
| 11-27 16:54 | +10 stop | ZEC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-27 16:54 | +5 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-27 16:54 | +5 | XRP | UP | 0.60 | 0.73 | 0.96 |
| 11-27 16:54 | +10 stop | DOGE | UP | 0.57 | 0.20 | -4.00 |
| 11-27 16:54 | +10 | DOGE | UP | 0.57 | open |  |
| 11-27 16:54 | +5 | DOGE | UP | 0.57 | 0.62 | 0.15 |
| 11-27 16:54 | +10 stop | XRP | UP | 0.60 | 0.73 | 1.02 |
| 11-27 16:54 | +10 | XRP | UP | 0.60 | 0.73 | 1.02 |
| 11-27 16:54 | +5 | XRP | UP | 0.60 | 0.69 | 0.61 |
| 11-27 16:54 | +10 stop | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 11-27 16:53 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 11-27 16:53 | +10 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-27 16:53 | +5 | DOGE | UP | 0.66 | 0.75 | 0.60 |
| 11-27 16:53 | +10 stop | XRP | UP | 0.56 | 0.69 | 0.97 |
| 11-27 16:53 | +10 | XRP | UP | 0.57 | 0.69 | 0.87 |
| 11-27 16:53 | +5 | XRP | UP | 0.57 | 0.69 | 0.85 |
| 11-27 16:52 | +10 stop | ZEC | DOWN | 0.69 | 0.53 | -1.93 |
| 11-27 16:52 | +5 | NEAR | UP | 0.63 | 0.69 | 0.28 |
| 11-27 16:52 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-27 16:52 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-27 16:51 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-27 16:51 | +15 | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 11-27 16:51 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-27 16:51 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-27 16:51 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-27 16:51 | +20 | ZEC | DOWN | 0.58 | 0.88 | 2.74 |
| 11-27 16:51 | +5 | ZEC | DOWN | 0.58 | 0.66 | 0.42 |
| 11-27 16:51 | +10 stop | NEAR | UP | 0.70 | 0.47 | -2.63 |
| 11-27 16:51 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-27 16:51 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-27 16:51 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 11-27 16:50 | +10 stop | SOL | DOWN | 0.21 | 0.56 | 3.20 |
| 11-27 16:50 | +10 stop | NEAR | DOWN | 0.39 | 0.55 | 1.25 |
| 11-27 16:49 | +10 stop | SOL | UP | 0.60 | 0.45 | -1.85 |
