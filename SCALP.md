# Range-Scalp Bot

*Updated Fri Oct 30 20:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41186 | 35954 | 5232 (54) | 4 | $-11446.12 | -4.4% |
| **+10¢** | 30697 | 24642 | 6055 (78) | 4 | $-10175.97 | -5.3% |
| **+15¢** | 25662 | 19138 | 6524 (106) | 5 | $-9216.76 | -5.7% |
| **+20¢** | 22779 | 15944 | 6835 (137) | 4 | $-8100.72 | -5.7% |
| **+10¢ (15¢ stop)** | 50217 | 50142 | 75 (41) | 0 | $-18969.52 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 20:12 | +5 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-30 20:12 | +10 stop | SOL | UP | 0.65 | 0.89 | 2.17 |
| 10-30 20:11 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-30 20:11 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 10-30 20:11 | +10 stop | BTC | DOWN | 0.44 | 0.55 | 0.74 |
| 10-30 20:11 | +5 | BTC | DOWN | 0.44 | 0.55 | 0.74 |
| 10-30 20:11 | +10 stop | BNB | UP | 0.66 | 0.82 | 1.33 |
| 10-30 20:11 | +20 | BNB | UP | 0.67 | 0.98 | 2.89 |
| 10-30 20:11 | +15 | BNB | UP | 0.66 | 0.82 | 1.33 |
| 10-30 20:11 | +10 | BNB | UP | 0.66 | 0.82 | 1.33 |
| 10-30 20:11 | +5 | BNB | UP | 0.66 | 0.74 | 0.50 |
| 10-30 20:11 | +10 stop | SOL | DOWN | 0.59 | 0.38 | -2.44 |
| 10-30 20:11 | +10 stop | DOGE | DOWN | 0.68 | 0.46 | -2.54 |
| 10-30 20:11 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-30 20:11 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-30 20:09 | +10 stop | SOL | DOWN | 0.46 | 0.64 | 1.45 |
| 10-30 20:08 | +10 stop | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-30 20:07 | +10 stop | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-30 20:07 | +15 | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-30 20:07 | +10 | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-30 20:07 | +5 | ETH | UP | 0.69 | 0.75 | 0.31 |
| 10-30 20:07 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.78 |
| 10-30 20:07 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.73 |
| 10-30 20:06 | +5 | SOL | UP | 0.69 | 0.89 | 1.78 |
| 10-30 20:06 | +10 stop | BTC | UP | 0.63 | 0.43 | -2.35 |
| 10-30 20:06 | +20 | BTC | UP | 0.63 | 0.93 | 2.77 |
| 10-30 20:06 | +15 | BTC | UP | 0.63 | 0.93 | 2.77 |
| 10-30 20:06 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-30 20:06 | +5 | BTC | UP | 0.63 | 0.72 | 0.58 |
| 10-30 20:06 | +20 | ZEC | UP | 0.60 | open |  |
| 10-30 20:06 | +15 | ZEC | UP | 0.60 | open |  |
| 10-30 20:06 | +10 stop | DOGE | UP | 0.66 | 0.50 | -1.94 |
| 10-30 20:06 | +10 | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-30 20:06 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 10-30 20:06 | +5 | SOL | UP | 0.61 | 0.67 | 0.27 |
| 10-30 20:05 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 10-30 20:05 | +10 | ZEC | UP | 0.62 | open |  |
| 10-30 20:05 | +5 | ZEC | UP | 0.62 | open |  |
| 10-30 20:05 | +10 stop | NEAR | UP | 0.61 | 0.38 | -2.64 |
| 10-30 20:05 | +20 | NEAR | UP | 0.61 | open |  |
